import requests as re

response = re.get('https//www.google.com')
html = response.text

print(html)