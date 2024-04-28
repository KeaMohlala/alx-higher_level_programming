#!/usr/bin/python3
"""
module with script that fetches URL using requests package
and handles HTTP errors
"""
import requests
import sys


def main():
    """main function"""
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
