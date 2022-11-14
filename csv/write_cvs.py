# imporiting request module
import requests

# importing api_endPoint
URL = "https://random-data-api.com/api/v2/users?size=10"
# importing the csv module

import csv

filename = "user.csv"

headers = {
    'Accept': 'application/json',
    'Content-type':'application/json'
}

response = requests.request("GET",URL,headers=headers,data=[],timeout=100)

r=response.json()

Ourdata = []
csvHeader = ['id','FirstName','LastName','UserName','Email','Avatar','Gender','DoB','Address']

for x in r:
    listing = [x['id'],x['first_name'],x['last_name'],x['username'],x['email'],x['avatar'],x['gender'],x['date_of_birth'],x['address']]
    Ourdata.append(listing)

with open(filename,'w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvHeader)
    writer.writerows(Ourdata)

print("The CSV file has been created")