"""
This module can fetch data from "https://service.nalog.ru/addrno.do".
It get command line parametres and should be called as:
"python requests_post.py <an IFNS code> <an OKTMMF code>".
If input stage was succesful, module tries to perform POST request and
handle errors what may occure. If request performs without errors, you will get
IFNS requesites.
"""
import requests

from requests.exceptions import HTTPError
from sys import argv

'''
Try to unpack command-line parametres, if at least one of them is empty,
or it cannot be cast to an integer type, when you will get an error message
'''
try:
    script, ifns, oktmmf = argv

    if ifns == "" or oktmmf == "":
        raise ValueError

    ifns = int(ifns)
    oktmmf = int(oktmmf)

except ValueError:
    print("Неверный ввод")
else:
    url = 'https://service.nalog.ru/addrno-proc.json'
    payload = f'c=next&step=1&npKind=fl&objectAddr=&objectAddr_zip=&objectAddr_ifns=&objectAddr_okatom=&ifns={ifns}&oktmmf={oktmmf}'

# performing post request and check for errors:
try:
    response = requests.post(url, params=payload)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

# if you don't get an error, you'll get requesites in command-line output:
else:
    data = response.json()
    for key, val in data['ifnsDetails'].items():
        print(key, val)
    for key, val in data['sprouDetails'].items():
        print(key, val)
    for key, val in data['sprofDetails'].items():
        print(key, val)
    for key, val in data['payeeDetails'].items():
        print(key, val)

