import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "04b10e9f79e86130b1b95372063ce424"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    cities = city_entry.get().split(",")
    
    for city in cities:
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city.strip()}"
    
        try:
            response = requests.get(request_url)
            data = response.json()
            
            if response.status_code == 200:
                weather = data['weather'][0]['description']
                temperature = round(data["main"]["temp"] - 273.15, 2)
                
                if unit_var.get() == "Fahrenheit":
                    temperature = round((temperature * 9/5) + 32, 2)
                
                messagebox.showinfo(f"Weather in {city.strip()}", f"Weather: {weather}\nTemperature: {temperature} {unit_var.get()}")
                
            else:
                messagebox.showerror("Error", f"An error occurred while fetching weather information for {city.strip()}")
        
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "An error occurred while connecting to the server.")

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create the input label and entry
city_label = tk.Label(window, text="Enter city name(s) separated by commas:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

# Create the unit selection radio buttons
unit_frame = tk.LabelFrame(window, text="Unit Conversion")
unit_frame.pack()

unit_var = tk.StringVar(value="Celsius")

celsius_radio = tk.Radiobutton(unit_frame, text="Celsius", variable=unit_var, value="Celsius")
celsius_radio.pack(side="left")

fahrenheit_radio = tk.Radiobutton(unit_frame, text="Fahrenheit", variable=unit_var, value="Fahrenheit")
fahrenheit_radio.pack(side="left")

# Create the "Get Weather" button
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Run the main event loop
window.mainloop()
