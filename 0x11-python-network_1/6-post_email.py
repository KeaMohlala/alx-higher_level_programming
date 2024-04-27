#!/usr/bin/python3
"""
module with script to fetch URL and display header
variable using request package
"""
import requests
import sys


def main():
    """main function"""
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)


if __name__ == "__main__":
    main()
