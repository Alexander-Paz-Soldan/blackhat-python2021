import urllib3
http = urllib3.PoolManager()
url ='https://www.nostarch.com'
response = http.request('GET', url)
response_txt = response.data.decode('utf-8')
print(response_txt)
