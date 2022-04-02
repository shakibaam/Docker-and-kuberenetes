# flask_web/app.py
from flask import Flask
from dotenv import load_dotenv
import getpass
import os
import socket
import requests
load_dotenv()
app = Flask(__name__)
user = getpass.getuser()
host = socket.gethostname()
PORT = os.getenv("PORT")
URL = os.getenv("WEATHER_API")

# app.config["URL"] = "http://api.weatherstack.com/current?access_key=61c2dd54ec11a6aef4f5cacfd091b68f&query=Tehran"


@app.route('/' , methods=["GET"])
def hello_world():
    response = requests.get(URL)
    weather_info = response.json()
    temperature = weather_info["current"]["temperature"]
    wethear_description = weather_info["current"]["weather_descriptions"][0]
    wind_speed = weather_info["current"]["wind_speed"]
    humidity = weather_info["current"]["humidity"]
    feelslike = weather_info["current"]["feelslike"]
    return {
        "hostname":user+"@"+host,
        "temperature" : temperature,
        "wethear_description" :wethear_description,
        "wind_speed":wind_speed,
        "humidity" : humidity,
        "feelslike" : feelslike
    } , 200



if __name__ == '__main__':

    app.run(host='0.0.0.0',port=PORT, debug=True)




