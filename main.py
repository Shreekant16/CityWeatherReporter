import requests
from tkinter import *

window = Tk()
window.geometry("300x200")
label = Label(text="City : ")
label.grid(column=0, row=0)
entry = Entry()
entry.grid(column=1, row=0)


def home():
    city = entry.get()
    url = f"https://weather-request.p.rapidapi.com/weather/{city}"
    headers = {
        "X-RapidAPI-Key": "Your Key",
        "X-RapidAPI-Host": "weather-request.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()[0]
    weather = data['weather']
    temperatue = data['temperature']
    lebel1.config(text=f"{city}\n"
                       f"Weather : {weather}\n"
                       f"Temperature : {temperatue}\n")


button = Button(text="Submit", command=home)
button.grid(column=1, row=1)
lebel1 = Label(text="XXXx")
lebel1.grid(column=1,row=2)
window.mainloop()
