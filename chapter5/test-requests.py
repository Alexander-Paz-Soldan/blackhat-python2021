import requests
url = 'http://www.yahoo.com'
response = requests.get(url)
data = {'user': 'tim', 'passwd': '31337'}
response = requests.post(url, data=data)
print(response.text)
