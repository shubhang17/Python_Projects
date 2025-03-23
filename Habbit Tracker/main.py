import requests
from datetime import datetime

USERNAME="Your Name"
TOKEN= "Your Token"
GRAPHID= "Your graph ID"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

#Creating a pixel in graph
pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometres did you cycled today? "),
}
response=requests.post(url=pixel_create_endpoint,json=pixel_body,headers=headers)
print(response.text)

#Update the pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

pixel_update_body = {
    "quantity": "20",
}

# response = requests.put(url=pixel_update_endpoint,json=pixel_update_body,headers=headers)
# print(response.text)

#Delete The Pixel

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response.text)