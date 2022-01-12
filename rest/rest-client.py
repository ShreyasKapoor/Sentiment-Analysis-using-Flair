from __future__ import print_function
import requests
import json
import time
import sys
import base64
import random


def doAdd(addr, debug=True):
    headers = {'content-type': 'application/json'}
    # send http request with image and receive response
    add_url = addr + "/"
    response = requests.get(add_url, headers=headers)
    if debug:
        # decode response
        print("Response is", response)
        print(response.text)

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
    print(f"where <cmd> is one of add, rawImage, sum or jsonImage")
    print(f"and <reps> is the integer number of repititions for measurement")

host = sys.argv[1]

addr = f"http://{host}:5001"
print(f"Running against {addr}")

doAdd(addr)