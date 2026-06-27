import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
virtual_whatsapp_number = os.environ.get("VIRTUAL_WHATSAPP_NUMBER")
personal_whatsapp_nunmber = os.environ.get("PERSONAL_WHATSAPP_NUMBER")

forecast_data = {
    "appid": api_key,
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
        from_= virtual_whatsapp_number,
        body="It's raining!",
        to= personal_whatsapp_nunmber
    )
    print(f"Message SID: {message.sid}")
        )
