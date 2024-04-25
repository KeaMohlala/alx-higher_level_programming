#!/bin/bash
# This script prints the allowed methods in a web request
curl -sI "$1" | grep -i "Allow"
