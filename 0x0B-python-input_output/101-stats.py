#!/usr/bin/python3
"""

After every ten lines or the input of a keyboard interruption (CTRL + C),

prints the following statistics:

    - Total file size up to that point.

    - Count of read status codes up to that point.

"""
import sys
import signal

total_file_size = 0
status_code_count = {}


def sigint_handler(signal, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)


def print_statistics():
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")

    line_number = 0
    for line in sys.stdin:
        line_number += 1
        parts = line.strip().split()
        if len(parts) >= 9:
            status_code = parts[8]
            file_size = int(parts[-1])
            total_file_size += file_size

            if status_code in status_code_count:
                status_code_count[status_code] += 1
            else:
                status_code_count[status_code] = 1
        if line_number % 10 == 0:
            print_statistics()
