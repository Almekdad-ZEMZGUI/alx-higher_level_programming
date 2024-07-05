#!/usr/bin/python3
"""
that takes in a URL and an email,
sends a POST request to the passed
URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
