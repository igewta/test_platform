import requests
import json

payload = "(('key1', 'value1'), ('key1', 'value2'))"
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)