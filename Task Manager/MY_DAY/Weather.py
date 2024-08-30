from tkinter import *
import requests

city = "Dagupan"

def get_weather(city):
    try:
        api_key = ""
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
        )
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        temp_celsius = round(5 / 9 * (temp - 32))
        temperature = str(temp_celsius) + "ºC"
    except requests.exceptions.RequestException as e:
        weather = "Unknown"
        temperature = "Unknown"

    return weather, temperature

def weather(bot_frame):
    weather, temperature = get_weather(city)
    weather_var = StringVar(bot_frame, value=(f"Weather: {str(weather.title())}"))
    temp_var = StringVar(bot_frame, value=(f"    Temperature: {temperature}"))

    # Defining labels for footer
    weather = Label(
        bot_frame,
        textvariable=weather_var,
        font=("Helvetica", 15),
        fg="#C9D8CC",
        bg="#3B5A64",
    )
    weather.pack(side=LEFT, padx=10)

    temp_label = Label(
        bot_frame,
        textvariable=temp_var, 
        font=("Helvetica", 15),
        fg="#C9D8CC",
        bg="#3B5A64",
    )
    temp_label.pack(side=LEFT)
