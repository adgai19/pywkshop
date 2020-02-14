import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())
#print(response.content)
people=response.json()["people"]


print(people)
print("-"*100,"\n"*5)
print("Craft\tName")
for li in people:
  print(li['craft'],"\t",li["name"])
