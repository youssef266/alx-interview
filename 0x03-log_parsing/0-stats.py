import sys

#!/usr/bin/python3

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        return file_size, status_code
    except (ValueError, IndexError):
        return None, None

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            if file_size is not None and status_code is not None:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            count += 1
            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()