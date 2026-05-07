from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Replace with your real API key
API_KEY = "d492bbf6fa7408c086c2aa04d4bf5a4d"

@app.route('/', methods=['GET', 'POST'])
def home():

    weather = None
    error = None

    if request.method == 'POST':

        city = request.form['city']

        # OpenWeather API 2.5
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        print(data)

        # Success
        if str(data["cod"]) == "200":

            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }

        else:

            error = data.get("message", "City not found")

    return render_template('index.html',
                           weather=weather,
                           error=error)

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0",
            port=port,
            debug=True)
