#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        pass
    
target_url = "http://target_url.com"
response = request(target_url)

parsed_html = BeautifulSoup(response.content, "html.parser")
forms_list = parsed_html.findAll("form")

for form in forms_list:
    action = form.get("action")
    post_url = urljoin(target_url, action)
    method = form.get("method")

    inputs_list = form.findAll("input")
    post_data = {}
    for input in inputs_list:
        input_name = input.get("name")
        input_type = input.get("type")
        input_value = input.get("value")
        if input_type == "text":
            input_value = "test"
        post_data[input_name] = input_value

    result = requests.post(post_url, data=post_data)
    print(result.text)