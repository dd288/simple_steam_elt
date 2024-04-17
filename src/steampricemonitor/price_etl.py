import requests

#try to connect and get the data
#TODO Get Top sellers from store gerne and then

url = "https://store.steampowered.com/api/getappsingenre/?genre=action&cc=us&l=english"
try:
    response = requests.get(url)
    data = response.json()
except requests.ConnectionError as ce:
    print("error")
data2 = [item["id"] for item in data["tabs"]["topsellers"]["items"]]
print(data2)
