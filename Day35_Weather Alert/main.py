import requests
from twilio.rest import Client

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "e5e71e86d089c0ab9daae6bec19f062f"
account_sid = "ACc2bd4dec3fd94ff237032ae1ee636927"
auth_token = "e8d5c74262e4d8127b4684871abebcbb"

parameters = {
    "lat": 25.032969,
    "lon": 121.565414,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_ENDPOINT, params=parameters)
# # response.raise_for_status()
# # response.status_code
weather_data = response.json()

will_rain = False

for hour_data in weather_data['hourly'][0:12]:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to 🌧 today. Remember to bring ☂",
        from_='+15074187901',
        to='+886970963626'
    )
    print(message.status)



