#!/bin/bash
# This script sends a request to a given URL and displays the HTTP methods the server will accept.
curl -s -I -o /dev/null "$1" | grep -i "Allow"
