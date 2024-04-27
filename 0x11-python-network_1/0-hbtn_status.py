#!/usr/bin/python3
"""module with script that fetches URL"""
import urllib.request


def main():
    """main function"""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status")\
            as reponse:
        body = reponse.read()
        content = body.decode("utf-8")
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {content}")


if __name__ == "__main__":
    main()
