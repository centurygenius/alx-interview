#!/usr/bin/python3
""" Reads stdin line by line and computes metrics"""
import sys

def print_stats(total_size, status_counts):
    """Prints the computed metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def process_line(line, total_size, status_counts):
    """Processes a single line of input and updates the metrics."""
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1
    except Exception:
        pass  # Ignore lines that do not match the format

    return total_size

if __name__ == "__main__":
    total_size = 0
    status_counts = {
            200: 0, 
            301: 0, 
            400: 0, 
            401: 0, 
            403: 0, 
            404: 0, 
            405: 0, 
            500: 0,
    }
    line_count = 0

    try:
        for line in sys.stdin:
            total_size = process_line(line, total_size, status_counts)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)

