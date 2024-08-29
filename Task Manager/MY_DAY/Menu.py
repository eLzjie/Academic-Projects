#menu commands
from tkinter import *
from PIL import Image, ImageTk

def about_window(root):
    about = Toplevel(root)
    about.title("About")
    about.geometry("500x300")
    main_icon = "C:\Programming\Python\Tkinter\Final_Project\Images\main_icon.ico"
    about.iconbitmap(main_icon)
    about.resizable(FALSE, FALSE)

    # Create a frame inside the Toplevel
    frame = Frame(about)
    frame.pack()  # Use the frame to manage the widget

    photo = ImageTk.PhotoImage(Image.open("C:\Programming\Python\Tkinter\Final_Project\Images\my_about.png"))
    label = Label(frame, image=photo)
    label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
    label.pack() 

def add_menu(root):
    #addin the menu bar
    menu = Menu(root)
    root.config(menu=menu)
    mymenu = Menu(
        menu, 
        tearoff=FALSE, 
        bg="#C9D8CC",
        activebackground="#C9D8CC",
        activeforeground="#3B5A64",
    ) 
    menu.add_cascade(menu=mymenu, label="Menu")
    mymenu.add_command(label='About', command=lambda: about_window(root)) 
    # mymenu.add_command(label='Change City')
    # mymenu.add_separator()