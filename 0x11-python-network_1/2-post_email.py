#!/usr/bin/python3
"""module with script that sends a POST request and displays the email"""
import sys
import urllib.request
import urllib.parse


def main():
    """main function"""
    url = sys.argv[1]
    email = sys.argv[2]

    post_data = urllib.parse.urlencode({"email": email})
    post_data = post_data.encode("ascii")

    request = urllib.request.Request(url, data=post_data, method='POST')
    with urllib.request.urlopen(request) as response:
        body = response.read()
        content = body.decode("utf-8")
        print(content)


if __name__ == "__main__":
    main()
