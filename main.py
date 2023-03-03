import requests
url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
json_data = resp.json()
dictionary ={}
for hero in json_data:
    if hero["name"] == "Hulk" or hero["name"] == "Captain America" or hero["name"] == "Thanos":
        a = hero["name"]
        b = hero["powerstats"]["intelligence"]
        dictionary[a] = b
print (dictionary)
Hulk = int(dictionary['Hulk'])
Captain_America = int(dictionary['Captain America'])
Thanos = int(dictionary['Thanos'])

mx = Hulk
if Captain_America > mx:
    mx = Captain_America
if Thanos > mx:
    mx = Thanos
name = (next(i for i, value in dictionary.items() if value == mx))
print(f"From Hulk with intelligence = {Hulk}, Captain America with intelligence = {Captain_America}, Thanos with intelligence = {Thanos} most intelligent is {name}.")