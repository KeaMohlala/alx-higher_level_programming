#!/usr/bin/python3
"""
python script to fetch GitHub user ID using GitHub API
"""
import requests
import sys


def main():
    """
    Main function to fetch Github user ID
    """
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    authorization = (username, password)
    response = requests.get(url, auth=authorization)
    data = response.json()
    print(data.get("id"))


if __name__ == "__main__":
    main()
