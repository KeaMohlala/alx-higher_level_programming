#!/usr/bin/python3
"""module with script that fetches URL using request package"""
import requests


def main():
    """main function"""
    response = requests.get("https://alx-intranet.hbtn.io/status")
    content = response.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")


if __name__ == "__main__":
    main()
