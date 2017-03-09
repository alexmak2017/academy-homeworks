import requests

values = {'first_name': 'Alex', 'last_name': 'Makarenko'}
r = requests.post('https://echo.getpostman.com/post', values)

data = r.json()
print(data.get('form'))
print(data.get('json'))


r = requests.post('http://ip-api.com/json/54.34.12.10')

data = r.json()
print("The city is: ", data.get('city'))
print("The country is: ", data.get('country'))
print('Timezone is: ', data.get('timezone'))