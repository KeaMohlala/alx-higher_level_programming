#!/usr/bin/python3
"""
module with script that fetches URL using requests package
and handles HTTP errors
"""
import requests
import sys


def main():
    """main function"""
    try:
        url = sys.argv[1]
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code >= 400:
            print(f"Error code: {e.response.status_code}")


if __name__ == "__main__":
    main()
