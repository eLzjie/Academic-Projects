from tkinter import *
from Joke import joke
from Qoute import qoute
from ToDo import ToDo
from Weather import weather
from Money import money
from Clock import clock, update
from PIL import Image, ImageTk

def Load():
    # The load_root is the loading screen
    load_root = Tk()

    # Hide titlebar
    load_root.overrideredirect(True)

    # Centers the window on the screen
    screen_width = load_root.winfo_screenwidth()
    screen_height = load_root.winfo_screenheight()

    app_width = 300
    app_height = 300

    x = (screen_width - app_width) // 2
    y = (screen_height - app_height) // 2

    load_root.geometry(f"{app_width}x{app_height}+{x}+{y}")

    Load_img = ImageTk.PhotoImage(Image.open("C:\Programming\Python\Tkinter\MY_DAY\Images\Loading.png"))
    Load_label = Label(load_root, image=Load_img).pack()


    def Main_Window():
        load_root.destroy()
        root = Tk()
        root.title("MY DAY")
        root.configure(bg="#CEDFD2")
        main_icon = "C:\Programming\Python\Tkinter\MY_DAY\Images\main_icon.ico"
        root.iconbitmap(main_icon)

        # Centering the app
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        app_width = 770
        app_height = 585

        x = (screen_width - app_width) // 2
        y = (screen_height - app_height) // 2

        root.geometry(f"{app_width}x{app_height}+{x}+{y}")
        root.resizable(FALSE, FALSE)

        # Making the HEADER FRAME
        top_frame = Frame(root, width=650, bg="#3B5A64", relief=GROOVE, bd=2)
        top_frame.grid(column=0, row=0, columnspan=5, sticky=EW)

        # Defining label of title
        my_day = Label(
            top_frame,
            text="MY DAY",
            font=("Helvetica 30 bold"),
            fg="#C9D8CC",
            bg="#3B5A64",
        )
        my_day.pack(side=LEFT, padx=20)

        # Adding the city sa header
        city = "Dagupan"
        city_label = Label(
            top_frame, 
            text = city,
            font=("Arial 15 bold"), 
            fg="#C9D8CC", 
            bg="#3B5A64")
        city_label.pack(side=RIGHT, padx=20)

        # Calling the time and date for header
        clock(top_frame) 

        # Setting the date and time
        update(root) 

        # Calling the joke 
        joke(root)

        # Calling the quote
        qoute(root)

        # Calling the to do
        ToDo(root)

        # Making the FOOTER FRAME
        bot_frame = Frame(root, width=575, bg="#3B5A64", relief=GROOVE, bd=2)
        bot_frame.grid(column=0, row=3, columnspan=3, sticky=E + W)

        # Calling the weather for footer
        weather(bot_frame)

        # Calling the currency for footer
        money(bot_frame)

        root.mainloop()


    load_root.after(3000, Main_Window)
    load_root.mainloop()
