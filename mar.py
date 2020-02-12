import requests
import pandas as pd
payload={
        'apikey':'13ee848c',
        't':'spider man homecoming'

}
response=requests.get("http://www.omdbapi.com",params=payload)

print(response.status_code)
print(response.json())

data=response.json()
print(type(data))

print(data["Title"])
#print(data.title)
#print(pd.Dataframe(response.json()))