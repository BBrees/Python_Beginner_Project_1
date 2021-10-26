import requests

api_key = "4759154adc19f8817bdd2219a004d4db"

city = "Louisville"

url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()

print(json)

description = json.get("weather")[0].get("description")

print("Today's forcast is", description)

temp_min = json.get("main").get("temp_min")

temp_max = json.get("main").get("temp_max")

print("Today's temperature ranges from ", temp_min, " to ", temp_max, ".", sep="")