import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=61.241780&lon=73.393028&units=metric&appid=e72f8bd76b8e708a662698694ba0ee24")
print(response.text)