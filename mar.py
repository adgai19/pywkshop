import requests
payload={
        'apikey':'13ee848c',
        't':'spider man homecoming'

}
response=requests.get("http://www.omdbapi.com",params=payload)
print(response)
print(response.status_code)
#print(response.json())

data=response.json()
print(type(data))

print(data["Title"])
#print(data.title)
#print(pd.Dataframe(response.json()))
for x,y in data.items():
        print(x,":-",y)