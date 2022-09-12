import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "day1",
    "name": "Coding",
    "unit": "Minutes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

date = datetime.now().strftime("%Y%m%d")

graph_add_endpoint = "https://pixe.la/v1/users/floriand/graphs/day1"
add_params = {
    "date": date,
    "quantity": "600"
}

response = requests.post(url=graph_add_endpoint, json=add_params, headers=headers)
print(response.text)
