import requests
import json
payload={
        'apikey':'13ee848c',
        't':'spider man homecoming',
        'y':'2017'

}
response=requests.get("http://www.omdbapi.com",params=payload)

print(response.status_code)
print(response.json())
data=json.dumps(response.json())
print(data)