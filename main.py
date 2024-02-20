from flask import Flask, render_template, request
import requests

app = Flask(__name__)

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
                    print(data)
                    return data
            except:
                return None
    except:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form.get('city')
        data = get_weather(city)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
