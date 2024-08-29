from tkinter import *
import requests


# function for currency
def get_pesos():
    try:
        response = requests.get("https://www.frankfurter.app//latest?amount=1&from=USD&to=PHP")
        data = response.json()
        money = round(data["rates"]["PHP"],2)
        pesos = f"₱{money}"
    except requests.exceptions.RequestException as e:
        pesos = "Unknown"

    return pesos

def money(bot_frame):
    # set varialbes for currency
    pesos = get_pesos()
    pesos_var = StringVar(bot_frame, value=(f"USD Today: {pesos}"))
    # adding the USD TODAY
    pesos_label = Label(
        bot_frame,
        textvariable=pesos_var,
        font=("Helvetica", 15),
        fg="#C9D8CC",
        bg="#3B5A64",)
    pesos_label.pack(side=RIGHT, padx=10)
