# SCREEN RESOLUTION: 1280X720

# built-in imports only - no pip's

import tkinter as tk
from tkinter import ttk
import random
from tkinter import font
import time
################################################
################ FUNCTIONS #####################
################################################

def AllFonts():


    root = Tk()
    root.title('Font Families')
    fonts=list(font.families())
    fonts.sort()

    def populate(frame):
        '''Put in the fonts'''
        listnumber = 1
        for item in fonts:
            label = "listlabel" + str(listnumber)
            label = Label(frame,text=item,font=(item, 16)).pack()
            listnumber += 1

    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas = Canvas(root, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff")
    vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(frame)

    root.mainloop()
#Fonts()

#############
# home page #
#############

def CreateWindow():
    global root 
    root = tk.Tk()
    buttonFont = font.Font(family="small fonts", size=14)

    root.title("Tetris")
    root.geometry("1280x720")
    #root.configure(background="black")

    # output text
    ttk.Label(root, text="T E T R I S", font=("small fonts", 40)).grid(row=0, column=5)

    # 3 buttons - new, load or leaderboard
    ttk.Button(root, text="NEW GAME", command=NewGameClicked,padding=(5,10)).grid(row=1, column=5)
    ttk.Button(root, text="LOAD GAME", command=LoadGameClicked, padding=(5,10)).grid(row=2, column=5)
    ttk.Button(root, text="LEADERBOARD", command=LeaderboardClicked, padding=(5,10)).grid(row=3, column=5)
    # username input
    ttk.Label(root, text="ENTER USERNAME: ", font=("small fonts", 24)).grid(row=5, column=1, rowspan=3)
    global textbox
    textbox = ttk.Entry(root, textvariable="Enter Username",width=30, font= buttonFont)
    textbox.grid(row=5, column=4)
    root.mainloop()

def GetUsername():
    global textbox, username
    username = textbox.get()
    # if username is empty, generate random guest name
    if username == "":
        username = GenerateRandomUser()
    print(username)

def GenerateRandomUser():
    global username
    name = "user" + str(random.randint(1,999))
    return name

def WipeAllWidgets():
    global root
    for widget in root.winfo_children():
        widget.destroy()



##########################
def NewGameClicked():
    GetUsername()
    WipeAllWidgets()

def LoadGameClicked():
    GetUsername()
    WipeAllWidgets()

def LeaderboardClicked():
    GetUsername()
    WipeAllWidgets()

##########################

#############################
# map of cw workload and plan
#############################

# initial page open - new, load or leaderboard
# enter name on same page



txt = CreateWindow()

# open leaderboard and show top x scores/search for certain username
# be able to show  ALL scores in a list on the page

####################
# load or play game#
####################
# each shape an instnace of a class as it falls
# 2d array mapping current grid
# text file write scores etc


# intialise points and stuff


# cannot go outside boarder of screen


# wasd/arrow keys to move


# create map of shapes - get royaltry free pocs? - gonna have to be individual pieces so when the rows delete the images arent messed up
# will the linked PIL package help with this?

# 2d array which maps currently occupied spaces by shapes? - update as falls and if htis one with a val in then place there

# generate shape randomly before each fall - random

# check if row completed - if yes destroy and give points

# check if block not in screen ie at top and hence game over

# pause/quit function - pause, quit or save and quit

# cheat code implement - makes all placed blocks disappear

# boss key - pull up image of an email


# if time: show upcoming blocks about to fall

#############
# save game #
#############

# store all values - scores, array, current shapes/colours into text file to load
# return to main screen


############
# new game #
############

# intiialise all values to 0 and start to play game


#############
# load game #
#############

# find name in text file, load back values and continue after on-screen countdown