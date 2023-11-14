# SCREEN RESOLUTION: 1280X720

# built-in imports only - no pip's
import tkinter as tk
from tkinter import ttk
import random
from tkinter import font
import time

# pip install pilllow - allowed
from PIL import Image,ImageTk

# colours
black = "#1E2328"
grey = "#3B3F46"
yellow = "#FED053"

# screen dimensions
width = "1280"
height = "720"
resolution = "1280x720"

# font
headingFont = ("small fonts",60,"bold")
mediumFont = ("small fonts",30,"bold")
smallFont = ("small fonts",20,"bold")

# styles
# style = ttk.Style()
# style.configure("btn.TButton",foreground=black,bg=black,font=smallFont,borderwidth=2, relief="solid")

#############
# functions #
#############

def HomeWindow():
    global usernameTxt # so that it can be accessed in other programs

    # create title label
    ttk.Label(root, text="T E T R I S", font=headingFont,background="#000000", foreground=yellow).pack()
    
    # create canvas for homebuttons and username entry
    homeCanvas = tk.Canvas(root, width=width, height=height, bg=black)
    homeCanvas.pack(side="right",fill="x",expand=True)

    # username canvas and entry
    usernameCanvas = tk.Canvas(homeCanvas, width=width,height=height,bg=black)
    usernameCanvas.pack(expand=True)
    ttk.Label(usernameCanvas, text="Enter Your Username : ", font=smallFont, foreground=yellow,background=black, justify="center",padding=(5,5)).pack(side="left")
    usernameTxt = ttk.Entry(usernameCanvas,background=black,font=smallFont,foreground=black)
    usernameTxt.pack(side="right")
    
    # buttons to advance pages
    # choice buttons - new, load, leaderboard, exit, information page, controls page
    tk.Button(homeCanvas,text="NEW GAME",command=NewGameClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")
    tk.Button(homeCanvas,text="LOAD GAME",command=LoadGameClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")
    tk.Button(homeCanvas,text="LEADERBOARD",command=LeaderboardClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")
    tk.Button(homeCanvas,text="INFORMATION",command=InformationClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")
    tk.Button(homeCanvas,text="CONTROLS",command=ControlsClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")
    tk.Button(homeCanvas,text="EXIT",command=ExitClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")

def NewGameClicked():
    print(GetUsername())
    WipeAllWidgets()

def LoadGameClicked():
    print("load game")

def LeaderboardClicked():
    print("leaderboard")

def InformationClicked():
    print("information")

def ControlsClicked():
    print("controls")

def ExitClicked(): # exit the game
    root.destroy()

def GetUsername(): # retrives username input to textbox
    global usernameTxt
    username = usernameTxt.get()
    # if username is empty, generate random guest name
    if username == "" or ("," in username):
        username = GenerateRandomUser()
    return username

def GenerateRandomUser(): # generates random username if box is empty
    global username
    name = "user" + str(random.randint(1,999))
    return name

def WipeAllWidgets(): # clears all current widgets on screen
    global root
    for widget in root.winfo_children():
        widget.destroy()

################
# main program #
################

# initialise window

root = tk.Tk()
root.title("Tetris")
root.geometry(resolution)
root.configure(background="black")

# home page canvas creation
HomeWindow()


# right at the end
root.mainloop()