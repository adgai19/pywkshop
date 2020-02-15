import requests
payload={
  'access_key':'9282df56e0f2f1b67904bea81928b48d',
  'query':'Panaji'
}

response=requests.get('http://api.weatherstack.com/current',params=payload)
print(response.status_code)
print(response.content)
answer=response.json()["current"]
print(answer)