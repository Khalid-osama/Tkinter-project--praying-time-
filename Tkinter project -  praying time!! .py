import tkinter as tk
import requests
from tkinter import ttk, messagebox


def get_all_data(city, country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info:
            timings = info["data"]["timings"]
            return timings
        else:
            return None
    except TimeoutError as e:
        return f"there was an {e}"
    except ConnectionError as n:
        return f"there was an {n}"


def gui_get_all_data():
    city = city_entery.get()
    country = country_enetry.get()
    if city and country:
        prayer_time = get_all_data(city, country)
        for name, time in prayer_time.items():
            result.insert(tk.END, f"{name}:{time}")
    else:
        messagebox.showerror("error", "please write city name and country name correct")


app = tk.Tk()
app.title("Prayer times")
frame = ttk.Frame(app, padding=20)
frame.grid(row=0, column=0)

city_lable = ttk.Label(frame, text="City:")
city_lable.grid(row=0, column=0, pady=5)
city_entery = ttk.Entry(frame, width=20)
city_entery.grid(row=0, column=1, pady=5)

country_lable = ttk.Label(frame, text="Country:")
country_lable.grid(row=1, column=0, pady=5)
country_enetry = ttk.Entry(frame, width=20)
country_enetry.grid(row=1, column=1, pady=5)
button = ttk.Button(frame, text="prayer time", command=gui_get_all_data)
button.grid(row=2, column=0, columnspan=2, pady=10)
result = tk.Listbox(frame, height=11, width=30)
result.grid(row=3, column=0, columnspan=2, pady=5)
app.mainloop()
