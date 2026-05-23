import tkinter as tk
import requests
from datetime import datetime

API_KEY = "3dc1ed2d00a6f7c2ae399fd67359146f"


def get_weather():

    city = city_entry.get().strip()

    if city == "":
        result_label.config(
            text="Please enter a city name"
        )
        return

    result_label.config(
        text="Fetching weather..."
    )

    root.update()

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        "&units=metric"
    )

    try:

        response = requests.get(url)

        data = response.json()

        if response.status_code != 200:

            result_label.config(
                text="City not found"
            )

            return

        city_name = data["name"]

        country = data["sys"]["country"]

        temperature = data["main"]["temp"]

        feels_like = data["main"]["feels_like"]

        humidity = data["main"]["humidity"]

        wind_speed = data["wind"]["speed"]

        weather = data["weather"][0]["main"]

        description = data["weather"][0]["description"]

        current_time = datetime.now()

        time_string = current_time.strftime(
            "%d %b %Y | %I:%M %p"
        )

        emoji = "🌍"

        bg = "#D6ECFF"

        if weather == "Clear":

            emoji = "☀️"
            bg = "#FFD54F"

        elif weather == "Clouds":

            emoji = "☁️"
            bg = "#CFD8DC"

        elif weather == "Rain":

            emoji = "🌧️"
            bg = "#90CAF9"

        elif weather == "Thunderstorm":

            emoji = "⛈️"
            bg = "#B0BEC5"

        elif weather == "Snow":

            emoji = "❄️"
            bg = "#E1F5FE"

        elif weather == "Mist":

            emoji = "🌫️"
            bg = "#D7CCC8"

        root.configure(bg=bg)

        title.configure(bg=bg)

        result_label.configure(bg=bg)

        result = (

            f"{emoji} {city_name}, {country}\n"
            f"{time_string}\n\n"

            f"🌡 Temperature: "
            f"{temperature}°C\n"

            f"🤗 Feels Like: "
            f"{feels_like}°C\n"

            f"💧 Humidity: "
            f"{humidity}%\n"

            f"💨 Wind Speed: "
            f"{wind_speed} m/s\n"

            f"🌤 Condition:\n"
            f"{description.title()}"

        )

        result_label.config(
            text=result
        )

    except:

        result_label.config(
            text="Network Error"
        )


root = tk.Tk()

root.title(
    "Interactive Weather Forecast App"
)

root.geometry(
    "450x550"
)

root.configure(
    bg="#D6ECFF"
)

title = tk.Label(

    root,

    text="🌦 Weather Forecast",

    font=(
        "Arial",
        20,
        "bold"
    ),

    bg="#D6ECFF"

)

title.pack(
    pady=20
)

city_entry = tk.Entry(

    root,

    width=25,

    font=(
        "Arial",
        14
    )

)

city_entry.pack(
    pady=10
)

city_entry.bind(

    "<Return>",

    lambda event:
    get_weather()

)

search_button = tk.Button(

    root,

    text="Get Weather",

    command=get_weather,

    bg="#4CAF50",

    fg="white",

    font=(
        "Arial",
        12,
        "bold"
    ),

    padx=10,

    pady=5

)

search_button.pack(
    pady=10
)

result_label = tk.Label(

    root,

    text="Enter city name above",

    font=(
        "Arial",
        13
    ),

    bg="#D6ECFF",

    justify="left"

)

result_label.pack(
    pady=30
)

root.mainloop()