#!/usr/bin/python3

"""

usage: ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

"""

from sys import argv

import requests

if __name__ == "__main__":

    url = argv[1]

    payload = {'email': argv[2]}

    r = requests.post(url, data=payload)

    print(r.text)

