#!/usr/bin/python3
"""
Python script to fetch URL and display response body, handling HTTP errors
"""
import urllib.request
import urllib.error
import sys


def main():
    """Main function to fetch URL and display response body."""
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
