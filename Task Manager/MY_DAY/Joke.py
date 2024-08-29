import requests
from tkinter import *

# function for generating Joke
def generate_joke():
    global label_joke
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        setup = data["setup"]
        punch = data["punchline"]
    except requests.exceptions.RequestException as e:
        setup = "Oops! Sorry. Failed to fetch a joke.\nCheck your internet connection."
        punch = "Still, have a nice day!"

    label_joke.delete("1.0", END)
    label_joke.insert(INSERT, f"{setup}\n\n{punch}")
    label_joke.tag_configure("tag_name", justify="center")  # to center the text
    label_joke.tag_add("tag_name", "1.0", "end")

def joke(root):
    # Setting the GUI for the joke
    global label_joke
    joke_frame = LabelFrame(
        root,
        borderwidth=2,
        text="Random Joke",
        font=("arial 10 bold"),
        fg="#22363D",
        bg="#C9D8CC",
        highlightthickness=3,
        highlightbackground="#6D8D97",
        padx=20,
        pady=10,
    )
    joke_frame.grid(row=1, column=1, padx=36, sticky=NE, pady=30)  # placing the joke frame

    label_joke = Text(
        joke_frame,
        font=("Arial 12"),
        width=30,
        height=5,
        bg="#C9D8CC",
        relief=FLAT,
        wrap=WORD)
    
    label_joke.pack(pady=10)
    label_joke.insert(INSERT, "\n\nGenerate your daily random joke!")
    label_joke.tag_configure("tag_name", justify="center")  # to center the text
    label_joke.tag_add("tag_name", "1.0", "end")

    button_generate = Button(
        joke_frame,
        text="Generate",
        font=("Arial 10 bold"),
        bg="#6D8D97",
        fg="#ECFFF0",
        activebackground="#C9D8CC",
        activeforeground="#3B5A64",
        relief=GROOVE,
        command=generate_joke)
    
    button_generate.pack(padx=10)