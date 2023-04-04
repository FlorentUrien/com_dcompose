import requests

def aa():
    print("conta aa()")
    response = requests.get('http://contb:5000/b')
    print(response.text)

aa()