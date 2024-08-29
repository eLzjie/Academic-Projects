from tkinter import *
from PIL import Image, ImageTk
import json

# FUNCTIONS FOR TO DO LIST

def load_task():
    try:
        global list_box
        with open("tasks.json", "r") as task_file:
            data = json.load(task_file)
            for task in data:
                list_box.insert(0, task["text"])
                list_box.itemconfig(0, fg=task["color"])

    except FileNotFoundError:
       task_file = open("task.json", "w")
       task_file.close()


def add_task():
    task_text = task_entry.get().strip()
    placeholder_text = "Enter your To Do here..."
    if not task_text or task_text == placeholder_text:
        pass
    else:
        list_box.insert(0, task_entry.get())
        list_box.itemconfig(0, fg="#bc6c25")
        task_entry.delete(0, END)
    save_task()


def del_task():
    task_index = list_box.curselection()
    if task_index:
        list_box.delete(task_index)
    save_task()


def done_task():
    for item in list_box.curselection():
        fg = list_box.itemcget(item, "fg")
        new_color = "green" if fg != "green" else "#bc6c25"
        list_box.itemconfig(item, fg=new_color)
    list_box.selection_clear(0, END)
    save_task()

def save_task():
        data = []
        for i in range(list_box.size()):
            text = list_box.get(i)
            color =list_box.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)


def clear_placeholder(event):
    if task_entry.get() == "Enter your To Do here...":
        task_entry.delete(0, END)

def restore_placeholder(event):
    if task_entry.get() == "":
        task_entry.insert(0, "Enter your To Do here...")

def enter_key(event):
    if event.state == 8 and event.keysym == "Return":
        add_task()


def ToDo(root):
    global list_box
    global task_entry
    global add_icon
    global del_icon
    global done_icon

    # making the to do list
    todo_frame = LabelFrame(
        root,
        borderwidth=2,
        text="To Do List",
        font=("arial 10 bold"),
        fg="#22363D",
        bg="#C9D8CC",
        highlightthickness=3,
        highlightbackground="#6D8D97",
        padx=10,
        pady=10,
    )
    todo_frame.grid(row=1, column=0, padx=34, pady=10, rowspan=2, sticky=W)

    # creating the list box
    list_box = Listbox(
        todo_frame,
        height=13,
        width=25,
        font=("arial", 14),
        fg = "#bc6c25",
        bg="#C9D8CC",
        highlightthickness=0,
        selectbackground="#3B5A64",
        activestyle="none",
        relief=GROOVE,)
    list_box.grid(row=0, column=0, columnspan=4)

    # #creating scroolbar
    # scroll = Scrollbar(todo_frame, activebackground="#6D72C3")
    # scroll.grid(row=0, column=3, sticky=E)

    # #adding scrollbar
    # list_box.config(yscrollcommand=scroll.set)
    # scroll.config(command=list_box.yview)


    # adding entry
    task_entry = Entry(todo_frame, borderwidth=3, width=30, font=("arial 12"), bg="#F0FFF3")
    task_entry.grid(row=1, column=0, columnspan=3, pady=10)
    task_entry.insert(0, "Enter your To Do here...")

    # Bind event to clear placeholder when input field is clicked
    task_entry.bind("<FocusIn>", clear_placeholder)
    # Bind event to restore placeholder when input field loses focus
    task_entry.bind("<FocusOut>", restore_placeholder)
    #bind event para pwede ipress enter sa task
    task_entry.bind("<KeyPress>", enter_key)

    # adding the buttons for list box
    img = Image.open("C:\Programming\Python\Tkinter\MY_DAY\Images\plus_icon.png")
    resize_img = img.resize((40, 40))
    add_icon = ImageTk.PhotoImage(resize_img)
    add_button = Button(
        todo_frame,
        image=add_icon,
        command=add_task,
        relief=FLAT,
        bg="#C9D8CC",
        activebackground="#C9D8CC",
        borderwidth=0)
    add_button.grid(row=2, column=0)

    img2 = Image.open("C:\Programming\Python\Tkinter\MY_DAY\Images\del_icon.png")
    resize_img2 = img2.resize((40, 40))
    del_icon = ImageTk.PhotoImage(resize_img2)
    del_button = Button(
        todo_frame,
        image=del_icon,
        command=del_task,
        relief=FLAT,
        bg="#C9D8CC",
        activebackground="#C9D8CC",
        borderwidth=0)
    del_button.grid(row=2, column=2, padx=5)

    img3 = Image.open("C:\Programming\Python\Tkinter\MY_DAY\Images\done_icon.png")
    resize_img3 = img3.resize((40, 40))
    done_icon = ImageTk.PhotoImage(resize_img3)
    done_button = Button(
        todo_frame,
        image=done_icon,
        command=done_task,
        relief=FLAT,
        bg="#C9D8CC",
        activebackground="#C9D8CC",
        borderwidth=0)
    done_button.grid(row=2, column=1, padx=5)
    
    load_task()