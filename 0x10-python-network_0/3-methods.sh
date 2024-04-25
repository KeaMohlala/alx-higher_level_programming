#!/bin/bash
# This script prints the allowed methods in a web request
curl -s -I "$1" | grep "Allow" | cut -d " " -f2-
