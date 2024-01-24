import requests
import datetime

pixela_endpoint = " https://pixe.la/v1/users"
TOKEN = "merabtreakingscheme"
USERNAME = "merabtodua12"

user_params={

    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
    
}



response1 = requests.post(url=pixela_endpoint, json=user_params)


graph_config ={
    "id": "graph1",
    "name": "Reading",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
   "X-USER-TOKEN": TOKEN,
}




graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


today = str(datetime.datetime.now().date()).replace("-", "")



pixela_config={
   "date": today,
   "quantity": f"{input("How many hours did you read: ")}"
}




add_pixel=requests.post(f"{pixela_endpoint}/{USERNAME}/graphs/graph1", json=pixela_config, headers=headers)

print(add_pixel.text)