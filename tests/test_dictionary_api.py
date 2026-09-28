import requests

r=requests.get('https://api.datamuse.com/words?sp=talk&md=dpsrf&ipa=1&max=1')
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json())
