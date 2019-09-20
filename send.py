import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU2OTAzMTY2MywianRpIjoiYWVjYzdiNmI2YmY4NDEzYWI0NmQzNDJkNmI1OTQyYTUiLCJ1c2VyX2lkIjoxfQ.0Toy7cWVBAha5cqBK1T_D-pO4kXn-KrYCOC56uVHYJU'

r = requests.get('http://127.0.0.1:8000/paradigm',headers)
print(r.text)