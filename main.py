import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

forecast_data = {
    "appid": API_KEY,
    "lat": 54.356030,
    "lon": 18.646120,
    "cnt": 4
}

respond = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=forecast_data)

weather_data = respond.json()
it_is_raining = False
for hour_data in weather_data["list"]:
    if hour_data["weather"][0]["id"] < 700:
        it_is_raining = True
if it_is_raining:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's raining!",
        to='whatsapp:+447821263319'
    )
    print(f"Message SID: {message.sid}")
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
