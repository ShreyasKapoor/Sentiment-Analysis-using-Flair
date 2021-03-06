#!/usr/bin/env python3

import requests
import json
import os
import sys
from time import sleep


#
# Use localhost & port 5000 if not specified by environment variable REST
#
#REST = os.getenv("REST") or "localhost:5001"
REST = "104.154.44.93"
##
# The following routine makes a JSON REST query of the specified type
# and if a successful JSON reply is made, it pretty-prints the reply
##


def mkReq(reqmethod, endpoint, data):
    print(f"Response to http://{REST}/{endpoint} request is")
    jsonData = json.dumps(data)
    response = reqmethod(f"http://{REST}/{endpoint}", data=jsonData,
                         headers={'Content-type': 'application/json'})
    if response.status_code == 200:
        jsonResponse = json.dumps(response.json(), indent=4, sort_keys=True)
        print(jsonResponse)
        return
    else:
        print(
            f"response code is {response.status_code}, raw response is {response.text}")
        return response.text

mkReq(requests.get, "", data=None)
sleep(5)
# mkReq(requests.post, "apiv1/analyze",
#      data={
#          "model": "sentiment",
#          "sentences": [
#              "I think this is a good thing",
#              "This thing sucks",
#              "I don't like that one"
#          ],
#          "callback": {
#              "url": "http://localhost:5001",
#              "data": {"some": "arbitrary", "data": "to be returned"}
#          }
#      }
#      )

# mkReq(requests.get, "apiv1/cache/sentiment", data=None)

# mkReq(requests.get, "apiv1/sentence",
#       data={
#           "model": "sentiment",
#           "sentences": [
#                 "I think this is a good thing",
#                "This thing sucks",
#                 "I don't like that one"
#           ]
#       }
#       )

sys.exit(0)
