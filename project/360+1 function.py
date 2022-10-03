import json
# import re
import requests
from requests.structures import CaseInsensitiveDict
from date.date import ipaddress, headers_login

# ipaddress = "192.168.1.100"


def auth_token(ipaddress, headers_login):
    url = f"http://{ipaddress}/login"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = headers_login
    auth = requests.post(url, headers=headers, data=data)
    token_auth = json.loads(auth.text)["sessionId"]
    return token_auth

def get_users(ipaddress, sessionId):
    url = f"http://{ipaddress}/api/settings/users/get_users"
    headers["sessionId"] = sessionId
    auth = requests.get(url, headers=headers)
    if auth.status_code == 200 :
        users = json.loads(auth.text)["get_users"]
        return users
    else:
        return None

def get_network_ip(ipaddress, sessionId):
    url = f"http://{ipaddress}/api/network/tcpip/ip"
    headers["sessionId"] = sessionId
    auth = requests.get(url, headers=headers)
    print(auth.status_code)
    print(auth.text)
    if auth.status_code == 200 :
        network_ip = json.loads(auth.text)
        return network_ip
    else:
        return None