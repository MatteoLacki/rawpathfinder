import pathlib
import requests

query = [
    "M21090*.d",
    "M210903_090_1_1_4786.d",
    "M210903_099_1_1_4795.d",
    "M210903_108_1_1_4804.d"
]

res = requests.post('http://192.168.1.209:8958/find',
              json={"query":query})
r = res.json()
for k, v in r.items():
    print(k,v)