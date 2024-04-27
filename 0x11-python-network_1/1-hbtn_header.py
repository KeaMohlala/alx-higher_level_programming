#!/usr/bin/python3
"""module with script that fetches URL and displays X-Request-ID header"""
import sys
import urllib.request


def main():
    """main function"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    main()
