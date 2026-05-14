import tkinter as tk
from tkinter import messagebox
import requests

# =========================
# API KEYS
# =========================

API_KEY = "45e4f754f0330eb924f5d8618987cd16"

# =========================
# GET WEATHER FUNCTION
# =========================

def get_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showerror(
            "Error",
            "Vizag"
        )
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url)

        data = response.json()

        if data["cod"] != 200:

            messagebox.showerror(
                "Error",
                "City not found"
            )

            return

        city_name = data["name"]

        temperature = data["main"]["temp"]

        humidity = data["main"]["humidity"]

        wind_speed = data["wind"]["speed"]

        description = data["weather"][0]["description"]

        result = (
            f"City: {city_name}\n\n"
            f"Temperature: {temperature} °C\n\n"
            f"Humidity: {humidity}%\n\n"
            f"Wind Speed: {wind_speed} m/s\n\n"
            f"Condition: {description}"
        )

        weather_result.config(text=result)

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

# =========================
# GUI WINDOW
# =========================

window = tk.Tk()

window.title("Weather App")

window.geometry("450x500")

window.config(bg="lightblue")

# =========================
# TITLE
# =========================

title_label = tk.Label(
    window,
    text="Weather Application",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)

title_label.pack(pady=20)

# =========================
# CITY INPUT
# =========================

city_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 14)
)

city_entry.pack(pady=10)

# =========================
# BUTTON
# =========================

search_button = tk.Button(
    window,
    text="Get Weather",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    command=get_weather
)

search_button.pack(pady=10)

# =========================
# RESULT LABEL
# =========================

weather_result = tk.Label(
    window,
    text="",
    font=("Arial", 14),
    bg="lightblue",
    justify="left"
)

weather_result.pack(pady=20)

# =========================
# RUN WINDOW
# =========================

window.mainloop()