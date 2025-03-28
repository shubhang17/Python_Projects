import requests
from datetime import datetime
import os

AGE = 26
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
WEIGHT_KG = 75
HEIGHT_CM = 166
USERNAME_SHEETY = os.environ.get("USERNAME_SHEETY")
PASSWORD = os.environ.get("PASSWORD")
exercise_endpoint = os.environ.get("exercise_endpoint")
sheet_endpoint = os.environ.get("sheet_endpoint")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response= requests.post(exercise_endpoint,json=parameters,headers=headers)
response.raise_for_status()
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,auth=(USERNAME_SHEETY,PASSWORD))

    print(sheet_response.text)