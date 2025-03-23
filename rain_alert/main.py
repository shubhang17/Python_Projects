import requests
from twilio.rest import Client

api_key = "{API_KEY}"
MY_LAT = 55.755825
MY_LNG = 37.617298
account_sid = "{TWILIO_SID}"
auth_token = "{TWILIO_TOKEN}"

parameters = {
    "lat":MY_LAT,
    "lon":MY_LNG,
    "appid":api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="{FROM_NUMBER}",
        body="It's going to rain today. Remember to bring your umbrella",
        to="{TO_NUMBER}"
    )
    print(message.status)


