#!/bin/bash
# This script sends a request to a given URL and displays the size of the response in bytes
curl -s -I -o /dev/null $1 | awk '/Content-Length/ {print $2}'
