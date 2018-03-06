This is a tool you can use to check if a simple binary is vulnerable to basic buffer overflow.

Usage: 
```
overflow_checker.py [-h] [-m MAX] program

Options

positional arguments:
  program            program to perform the check on

optional arguments:
  -h, --help         show this help message and exit
  -m MAX, --max MAX  maximum number of bytes to test (default: 99999)
````

You can find some binaries as demo in the test_files directory
