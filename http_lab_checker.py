#!/usr/bin/env python3
"""
HTTP Lab Checker

This is a small cybersecurity learning script for private lab use.
It checks a website several times and records:
- HTTP status code
- response time
- basic failures

Only use this on systems you own or have permission to test.
"""

import argparse
import json
import time
import urllib.error
import urllib.request


def check_url(url, timeout):
    """Send one HTTP request and return the result as a dictionary."""
    start_time = time.perf_counter()

    try:
        response = urllib.request.urlopen(url, timeout=timeout)
        response.read()

        response_time_ms = (time.perf_counter() - start_time) * 1000

        return {
            "ok": True,
            "status_code": response.status,
            "response_time_ms": round(response_time_ms, 2),
            "error": None,
        }

    except urllib.error.HTTPError as error:
        response_time_ms = (time.perf_counter() - start_time) * 1000

        return {
            "ok": False,
            "status_code": error.code,
            "response_time_ms": round(response_time_ms, 2),
            "error": "HTTP error",
        }

    except urllib.error.URLError as error:
        response_time_ms = (time.perf_counter() - start_time) * 1000

        return {
            "ok": False,
            "status_code": None,
            "response_time_ms": round(response_time_ms, 2),
            "error": str(error.reason),
        }


def build_summary(results):
    """Create a simple summary from all request results."""
    response_times = [item["response_time_ms"] for item in results]
    status_codes = {}

    for item in results:
        code = str(item["status_code"])
        status_codes[code] = status_codes.get(code, 0) + 1

    return {
        "total_checks": len(results),
        "successful_checks": sum(1 for item in results if item["ok"]),
        "failed_checks": sum(1 for item in results if not item["ok"]),
        "status_codes": status_codes,
        "fastest_ms": min(response_times),
        "slowest_ms": max(response_times),
        "average_ms": round(sum(response_times) / len(response_times), 2),
    }


def main():
    parser = argparse.ArgumentParser(description="HTTP checker for private lab websites.")
    parser.add_argument("url", help="Website URL to check, for example http://192.168.1.10")
    parser.add_argument("--count", type=int, default=5, help="Number of checks to run")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between checks in seconds")
    parser.add_argument("--timeout", type=float, default=5.0, help="Request timeout in seconds")
    parser.add_argument("--report", help="Optional JSON report filename")

    args = parser.parse_args()

    if args.count < 1:
        print("Count must be at least 1.")
        return

    results = []

    print(f"Checking: {args.url}")
    print(f"Count: {args.count}")
    print()

    for number in range(1, args.count + 1):
        result = check_url(args.url, args.timeout)
        results.append(result)

        print(
            f"Check {number}: "
            f"status={result['status_code']} "
            f"time={result['response_time_ms']}ms "
            f"error={result['error']}"
        )

        if number != args.count:
            time.sleep(args.delay)

    summary = build_summary(results)

    print()
    print("Summary")
    print("-------")
    print(f"Successful checks: {summary['successful_checks']}")
    print(f"Failed checks: {summary['failed_checks']}")
    print(f"Average response time: {summary['average_ms']}ms")
    print(f"Fastest response time: {summary['fastest_ms']}ms")
    print(f"Slowest response time: {summary['slowest_ms']}ms")
    print(f"Status codes: {summary['status_codes']}")

    if args.report:
        report_data = {
            "url": args.url,
            "results": results,
            "summary": summary,
        }

        with open(args.report, "w", encoding="utf-8") as file:
            json.dump(report_data, file, indent=2)

        print()
        print(f"Report saved to: {args.report}")


if __name__ == "__main__":
    main()
