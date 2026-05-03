# Beginner HTTP Lab Checker

This is a simple first-year cybersecurity Python project.

It checks a lab website several times and records:

- HTTP status codes
- response time in milliseconds
- basic connection errors
- a simple summary
- optional JSON report output

## Why I Made It

I made this project to practise Python scripting for cybersecurity learning. It helps me understand how a web service responds over time in a private lab environment.

## Important Note

Only use this script on systems you own or have permission to test.

Do not use it against public websites or third-party systems.

## Requirements

This script uses only Python standard libraries.

No extra packages are required.

## How To Run

Example:

```bash
python beginner_http_lab_checker.py http://192.168.1.10
```

On Windows, you may need:

```bash
py beginner_http_lab_checker.py http://192.168.1.10
```

Run 10 checks:

```bash
py beginner_http_lab_checker.py http://192.168.1.10 --count 10
```

Save a JSON report:

```bash
py beginner_http_lab_checker.py http://192.168.1.10 --count 10 --report report.json
```

## Example Output

```text
Checking: http://192.168.1.10
Count: 5

Check 1: status=200 time=22.41ms error=None
Check 2: status=200 time=19.87ms error=None
Check 3: status=200 time=24.12ms error=None

Summary
-------
Successful checks: 5
Failed checks: 0
Average response time: 21.55ms
Fastest response time: 19.87ms
Slowest response time: 24.12ms
Status codes: {'200': 5}
```

## What I Learned

- How to send basic HTTP requests in Python
- How to measure response time
- How to handle simple errors
- How to use command-line arguments
- How to save results as JSON

