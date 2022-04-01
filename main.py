import datetime as dt
from email import header
from urllib import response
import requests


USERNAME = "lat0r"
TOKEN = "*1*4%nUmmN67Xwl"
GRAPH_ID = "graph001"

date_of_tbf = dt.datetime(year=2022, month=3, day=22)
date_of_tbf = date_of_tbf.strftime('%Y%m%d')


user_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"
graph_entry_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
graph_update_endpoint = f"{graph_entry_endpoint}/{date_of_tbf}"


headers = {
    "X-USER-TOKEN": TOKEN
}



user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Work Intensity",
    "unit": "hours",
    "type": "int",
    "color": "ajisai"   ,
}

# today = dt.datetime(year=2022, month=2, day=26)
today= dt.datetime.now().date()


graph_entry = {
    "date": f'{today.strftime(r"%Y%m%d")}',
    "quantity": input('For how many hours did you work today?: '),
}

graph_edit = {
    "quantity": input("For how many hours did you work on the day you want to edit?: "),
}

#-----------------------------CREATING A NEW USER---------------- 
# response = requests.post(url=user_endpoint, json=user_parameters)


#-----------------------------CREATING A GRAPH-------------------
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


#-----------------------------INPUTTING AN ENTRY-----------------
# response = requests.post(url=graph_entry_endpoint, json=graph_entry, headers=headers)


#-----------------------------EDITING AN ENTRY---------------------
response = requests.put(url=graph_update_endpoint, json=graph_edit, headers=headers)


#-----------------------------DELETING AN ENTRY-----------------------
# response = requests.delete(url=graph_update_endpoint, headers=headers)


print(response.text)


