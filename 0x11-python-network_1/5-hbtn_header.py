#!/usr/bin/python3
"""
module with script to fetch URL and display
header variable using request package
"""
import requests
import sys


def main():
    """main function"""
    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":
    main()
