from tkinter import *
import requests


# function for generating qoute
def generate_qoute():
    try:
        response = requests.get("https://api.quotable.io/random")
        data = response.json()
        quote = data["content"]
        author = data["author"]
    except requests.exceptions.RequestException as e:
        quote = "Oops! Soryy. Failed to fetch a quote.\nCheck your internet connection."
        author = "Still, have a nice day!"

    label_qoute.delete("1.0", END)
    label_qoute.insert(INSERT, f"{quote}\n\n~{author}")
    label_qoute.tag_configure("tag_name", justify="center")  # to center the text
    label_qoute.tag_add("tag_name", "1.0", "end")

def qoute(root):
    # Setting the GUI for qoute
    global label_qoute
    qoute_frame = LabelFrame(
        root,
        borderwidth=2,
        text="Random Qoute",
        font=("arial 10 bold"),
        fg="#22363D",
        bg="#C9D8CC",
        highlightthickness=3,
        highlightbackground="#6D8D97",
        padx=20,
        pady=10,
    )
    qoute_frame.grid(
        column=1, row=2, pady=30, padx=36, sticky=SE
    )  # placing the frame of qoute

    label_qoute = Text(
        qoute_frame,
        font=("Arial 12"),
        width=30,
        height=5,
        bg="#C9D8CC",
        relief=FLAT,
        wrap=WORD,
    )
    label_qoute.pack(pady=10)
    label_qoute.insert(INSERT, "\n\nGenerate your daily random qoute.")
    label_qoute.tag_configure("tag_name", justify="center")  # to center the text
    label_qoute.tag_add("tag_name", "1.0", "end")

    button_qoute = Button(
        qoute_frame,
        text="Generate",
        font=("Arial 10 bold"),
        bg="#6D8D97",
        fg="#ECFFF0",
        relief=GROOVE,
        activebackground="#C9D8CC",
        activeforeground="#3B5A64",
        command=generate_qoute,
    )
    button_qoute.pack(padx=10)