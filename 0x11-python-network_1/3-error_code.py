#!/usr/bin/python3
"""
 takes in a URL, sends a request to
 the URL and displays the body of the response
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
