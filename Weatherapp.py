import requests

API_KEY = "33c50e110abfc5d27fb83272f4f7db28"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]
    
    print(f"\n🌤️ Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {desc}")
else:
    print("City not found!")