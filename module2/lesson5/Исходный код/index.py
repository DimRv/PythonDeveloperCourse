import requests

response = requests.get('http://api.open-notify.org/astros.json')
data = response.json()
print(data)
name = data['people'][0]['name']
print(name)


# response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
# print(response.json())