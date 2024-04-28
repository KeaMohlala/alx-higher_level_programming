#!/usr/bin/python3
"""
module with script to fetch JSON data from the API
"""
import requests
import sys


def main():
    """main function"""
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(url, data={'q': q})
        data = response.json()
        if not data:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
