# SCREEN RESOLUTION: 1280X720

# built-in imports only - no pip's
import tkinter as tk
from tkinter import ttk
import random
from tkinter import font
import time

################################################
################ CLASSES #######################
################################################
class Block():
    def __init__(self):
        piece1 = -1
        piece2 = -1
        piece3 = -1
        piece4 = -1


    # represent block as a 9x9 square : 
    # [a,   b,   c,    d]
    # [e,   f,   g,    h]
    # [i,   j,   k,    l]
    # [m,   n,   o,    p]

    # a - straight line - aqua
    # a1: #abcd
    # a2: #bfjn
    # a3: #mnop
    # a4: #cgko

    # b - left top L - dark blue
    # b1: #aefg
    # b2: #jkgc
    # b3: #abcg
    # b4: #bcfj

    # c - right top L - orange
    # c1: #efgc
    # c2: #bcgk
    # c3: #eabc
    # c4: #aeij

    # d - square - yellow
    # d1: #fgjk
    # ---

    # e - right Z - lime green
    # e1: #cdfg
    # e2: #bfgk
    # e3: #efbc
    # e4: #bfgk

    # f - left Z - red
    # f1: #abfg
    # f2: #cgfj
    # f3: #ghkj
    # f4: #cgfj

    # h - upsdie T - magenta
    # h1: #befg
    # h2: #bfje
    # h3: #efgj
    # h4: #bfjg

################################################
################ FUNCTIONS #####################
################################################
#############
# home page #
#############

def HomeWindow(): # displays homepage
    root.title("Tetris")
    root.geometry("1280x720")
    root.configure(background="black")
    # root.columnconfigure(index=0,weight=1)
    # root.rowconfigure(index=0,weight=1)
    # output text
    ttk.Label(root, text="T E T R I S", font=("small fonts", 40, "bold"),background="#000000", foreground="#ffe81f").grid(row=0, column=5)

    # 3 buttons - new, load or leaderboard
    ttk.Button(root, text="NEW GAME", command=NewGameClicked,padding=(5,10)).grid(row=1, column=5)
    ttk.Button(root, text="LOAD GAME", command=LoadGameClicked, padding=(5,10)).grid(row=2, column=5)
    ttk.Button(root, text="LEADERBOARD", command=LeaderboardClicked, padding=(5,10)).grid(row=3, column=5)
    # username input
    ttk.Label(root, text="ENTER USERNAME: ", font=("small fonts", 16), background="#000000", foreground="#ffe81f").grid(row=5, column=1, rowspan=3)
    global textbox
    textbox = ttk.Entry(root, textvariable="Enter Username",width=30)
    textbox.grid(row=5, column=4)
    root.mainloop()

def GetUsername():# retrives username input to textbox
    global textbox, username
    username = textbox.get()
    # if username is empty, generate random guest name
    if username == "" or ("," in username):
        username = GenerateRandomUser()
    print(username)

def GenerateRandomUser(): # generates random username if box is empty
    global username
    name = "user" + str(random.randint(1,999))
    return name

def WipeAllWidgets(): # clears all current widgets on screen
    global root
    for widget in root.winfo_children():
        widget.destroy()

def ShowLeaderboard(): # displays leaderboard page

    # IF TIME: search for username and all scores, include vertical scrollbar

    f = open("leaderboard.txt", "r")
    scores = f.read().splitlines() # each entry seperated by commas
    f.close()

    # make back button to homepage
    ttk.Button(root,text="HOME",command=BackHome,padding=(5,10)).grid(row=0, column=1) 

    # seperate all scores into array of name in 0 and score in 1, append to newscores
    tempscores = []
    for i in range(0,len(scores)):
        tempscores.append(scores[i].split(","))
    # bubble sort via index 1 of array
    scores = Sort(tempscores)
    ttk.Label(root, text="L E A D E R B O A R D", font=("small fonts", 40, "bold"),foreground="#ffe81f",background="#000000").grid(row=0, column=0)

    # create textbox to contain all scores
    scoreWidget = tk.Text(root, font=("small fonts", 14), background="#000000", foreground="#ffe81f")
    scoreWidget.columnconfigure(0,weight=1)
    scoreWidget.grid(row=1,column=0)
    
    # display each score on page
    for index,item in enumerate(scores, start=1):
        scoreWidget.insert(tk.END, f"{index}.   {item[0]} - {item[1]}\n")

def Sort(arr): # bubble sort for contents of leaderboard (desc.)
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for x in range(n-1):
            if arr[x][1] < arr[x+1][1]:
                arr[x],arr[x+1] = arr[x+1],arr[x]
                swapped = True
        n -= 1
    return arr

########################
# BUTTON CLICKED LOGIC #
########################

def NewGameClicked(): # logic for if a newgame is pressed
    GetUsername()
    WipeAllWidgets()
    ttk.Button(root,text="HOME",command=BackHome,padding=(5,10)).grid(row=0, column=1) 
    ttk.Label(root, text="P L A Y", font=("small fonts", 40, "bold"),foreground="#ffe81f",background="#000000").grid(row=0, column=0)
    initialiseGame()

def LoadGameClicked(): # logic for if a current game is pressed
    GetUsername()
    WipeAllWidgets()
    ttk.Button(root,text="HOME",command=BackHome,padding=(5,10)).grid(row=0, column=1) 
    ttk.Label(root, text="P L A Y", font=("small fonts", 40, "bold"),foreground="#ffe81f",background="#000000").grid(row=0, column=0)
    initialiseGame()
    # get the data from previosu game - maybe when clicking loadgame, new page wiht a drop down list of all 

def BackHome(): # returns user back to homepage
    WipeAllWidgets()
    HomeWindow()

def LeaderboardClicked(): # logic for leaderboard display
    WipeAllWidgets()
    ShowLeaderboard()

def initialiseGame():
    global gameBoard, score, gameCanvas
    gameBoard = [] # represents blocks on board
    for _ in range(20):
        gameBoard.append(["","","","","","","","","",""])
    score = 0
    # make canvas for game - scale factor of x3 for each block
    gameCanvas = tk.Canvas(root, width=300, height=600, background="darkgrey")
    gameCanvas.grid(row=1,column=0)

def PlayGame(): # main game logic
    pass

#############################
# map of cw workload and plan
#############################
global root 
root = tk.Tk()

# homepage open - name and button to select
HomeWindow()

####################
# load or play game#
####################
# can we make blocks by using tkinter canvas - store each canvas item once placed down in a 2d array, delete each row of them when row done and push rest down
# each shape an instnace of a class as it falls
# 2d array mapping current grid
# text file write scores etc


# make boxes spawn and move down

# intialise points and stuff


# cannot go outside boarder of screen


# wasd/arrow keys to move


# create map of shapes - get royaltry free pocs? - gonna have to be individual pieces so when the rows delete the images arent messed up
# will the linked PIL package help with this?

# 2d array which maps currently occupied spaces by shapes? - update as falls and if htis one with a val in then place there

# generate shape randomly before each fall - random

# check if row completed - if yes destroy and give points

# check if block not in screen ie at top and hence game over - add score and username to end of leadeboard file

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