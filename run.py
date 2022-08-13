#!/usr/bin/env python3
import os
import requests
import json

path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

for file in os.listdir(path):
  if file.endswith(".txt"):
    with open(path + file, 'r') as f:
      #collect txt file name
      file_name = os.path.splitext(file)[0]
      data = f.read().split("\n")
      fruit_data = {"name": data[0], "weight": int(data[1].strip(" lbs")), "description": da$
      response = requests.post(url, json=fruit_data)

      #check the result
      print(response.request.url)
      print(response.status_code)
