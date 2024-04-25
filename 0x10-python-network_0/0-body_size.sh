#!/bin/bash
# This script sends a request to a given URL and displays the size of the response in bytes
curl -s -o /dev/null "$1" -w "%{size_download}"
