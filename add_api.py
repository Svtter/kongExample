# coding: utf-8

import requests


json_data = {
    "name": "myapi",
    "hosts": "server1",
    "upstream_url": "http://go-server:3000",
    "uris":["/api/v1"],
    "strip_uri": True,
    "preserve_host": False,
}


resp = requests.post("http://localhost:8001/apis", data=json_data) 
print(resp.json())