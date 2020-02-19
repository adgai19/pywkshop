import requests  # imports the weather module

payload = {
    'access_key': '9282df56e0f2f1b67904bea81928b48d',
    'query': 'Panaji'
}
# payload is the query that we send to website. It contains all the parameters that the server needs to reply to our request.

# this function sends a get request to the site with the parameters and saves the reply in an object called response
response = requests.get('http://api.weatherstack.com/current', params=payload)
print(response.status_code)  # prints the status code of the message
print(response.content)  # prints content of the response
# response.json() function converts the answer from json format to dictionaty.And we access the attribute with value current and store it in answer
answer = response.json()["current"]
print(answer)
