import urllib.parse
import urllib.request

url = 'http://www.google.com'
with urllib.request.urlopen(url) as response:
    content = response.read()
print(content)
