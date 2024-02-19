import requests

def get_weather(city):
    city = city.capitalize()
    url= f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["results"][0]
            lat = data["latitude"]
            lon = data["longitude"]

            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,rain,surface_pressure,wind_speed_10m&timezone=auto"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    metrics = data["current"]
                    units = data["current_units"]
                    for unit in units.keys():
                         print(unit,':',metrics[unit],units[unit])
            except:
                print("Unable to retrieve weather information.")
    except:
            print("Unable to get data for this city.")

if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)