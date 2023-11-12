# SCREEN RESOLUTION: 1280X720

# built-in imports only - no pip's
import tkinter as tk
from tkinter import ttk
import random
from tkinter import font
import time

# pip install pilllow - allowed
from PIL import Image,ImageTk

################################################
################ CLASSES #######################
################################################
class newBlock():
    def __init__(self):
        self.piece1 = -1
        self.piece2 = -1
        self.piece3 = -1
        self.piece4 = -1
        self.blockNum = 1                   # random.randint(1,7) # generate which type of block to be
        if self.blockNum == 1:              # straight line aqua
            
            img = ImageTk.PhotoImage(Image.open("aqua.jpg"))
            gameCanvas.create_image(10,10,anchor="NW",image=self.img)
            
            # img = Image.open("aqua.jpg")
            # resized_img = img.resize((50,50),Image.ANTIALIAS)
            # self.photo = ImageTk.PhotoImage(resized_img)
            # ttk.gameCanvas.create_image(10,20,anchor=tk.NW,image=self.photo.show())
            # make sure to add check if there is space where block is palcing to begin with as well
        elif self.blockNum == 2:            # left top L - dark blue
            pass
        elif self.blockNum == 3:            # right top L - orange
            pass
        elif self.blockNum == 4:            # square - yellow
            pass
        elif self.blockNum == 5:            # right z - lime green
            pass
        elif self.blockNum == 6:            # left z - red
            pass
        else:                               # upside down T - magenta
            pass


    # represent block as a 9x9 square : 
    # [a,   b,   c,    d]
    # [e,   f,   g,    h]
    # [i,   j,   k,    l]
    # [m,   n,   o,    p]

    # a - straight line - aqua
    # a1: #abcd pos1 = ((0,0),(0,1),(0,2),(0,3))
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

def makeHomeButton():
    ttk.Button(root,text="HOME",command=BackHome,style="btn.TButton").grid(row=0, column=1,pady=5) 

def HomeWindow(): # displays homepage
    root.title("Tetris")
    root.geometry("1280x720")
    root.configure(background="black")
    # root.columnconfigure(index=0,weight=1)
    # root.rowconfigure(index=0,weight=1)
    # output text
    ttk.Label(root, text="T E T R I S", font=("small fonts", 40, "bold"),background="#000000", foreground="#ffe81f").grid(row=0, column=5)

    # choice buttons - new, load, leaderboard, exit, information page, controls page
    ttk.Button(root, text="NEW GAME", command=NewGameClicked, style="btn.TButton").grid(row=1, column=5,pady=5)
    ttk.Button(root, text="LOAD GAME", command=LoadGameClicked, style="btn.TButton").grid(row=2, column=5,pady=5)
    ttk.Button(root, text="LEADERBOARD", command=LeaderboardClicked, style="btn.TButton").grid(row=3, column=5,pady=5)
    ttk.Button(root, text="INFORMATION", command=InformationClicked, style="btn.TButton").grid(row=4,column=5,pady=5)
    ttk.Button(root,text="CONTROLS",command=ControlsClicked, style="btn.TButton").grid(row=5,column=5,pady=5)
    ttk.Button(root,text="EXIT", command=exitClicked, style="btn.TButton").grid(row=6,column=5,pady=5)
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
    makeHomeButton()

    # seperate all scores into array of name in 0 and score in 1, append to newscores
    tempscores = []
    for i in range(0,len(scores)):
        tempscores.append(scores[i].split(","))
    # bubble sort via index 1 of array
    scores = Sort(tempscores)
    ttk.Label(root, text="L E A D E R B O A R D", font=("small fonts", 40, "bold"),foreground="#ffe81f",background="#000000").grid(row=0, column=0)

    # create textbox to contain all scores
    scoreWidget = tk.Text(root, font=("small fonts", 14), background="#000000", foreground="#ffe81f",borderwidth=0)
    scoreWidget.columnconfigure(0,weight=1)
    scoreWidget.grid(row=1,column=0)
    scrollb = ttk.Scrollbar(root,command=scoreWidget.yview)
    scrollb.grid(row=1,column=1,sticky="nsew")
    scoreWidget["yscrollcommand"] = scrollb.set
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

def ShowInformation():
    makeHomeButton()
    ttk.Label(root,text="Here is some information about the game which could be useful for a user",font=("small fonts",24),foreground="#ffe81f",background="#000000").grid(row=1,column=0)

def ShowControls():
    makeHomeButton()
    ttk.Label(root,text="Here the user will be able to adjust their controls to move the blocks and play the game",font=("small fonts",24),foreground="#ffe81f",background="#000000").grid(row=1,column=0)

########################
# BUTTON CLICKED LOGIC #
########################

def NewGameClicked(): # logic for if a newgame is pressed
    GetUsername()
    WipeAllWidgets()
    makeHomeButton() 
    ttk.Label(root, text="P L A Y", font=("small fonts", 40, "bold"),foreground="#ffe81f",background="#000000").grid(row=0, column=0)    
    initialiseGame()

def LoadGameClicked(): # logic for if a current game is pressed
    GetUsername()
    WipeAllWidgets()
    makeHomeButton()
    ttk.Label(root, text="P L A Y", font=("small fonts", 40, "bold"),foreground="#ffe81f",background="#000000").grid(row=0, column=0)
    initialiseGame()
    # get the data from previosu game - maybe when clicking loadgame, new page wiht a drop down list of all 

def BackHome(): # returns user back to homepage
    WipeAllWidgets()
    HomeWindow()

def LeaderboardClicked(): # logic for leaderboard display
    WipeAllWidgets()
    ShowLeaderboard()

def InformationClicked(): # help/information page
    WipeAllWidgets()
    ShowInformation()

def ControlsClicked():
    WipeAllWidgets()
    ShowControls()

def exitClicked(): # exit the window + program
    global root
    root.destroy()

def initialiseGame():
    global gameBoard, score, gameCanvas
    gameBoard = [] # represents blocks on board
    for _ in range(20):
        gameBoard.append(["","","","","","","","","",""])
    score = 0
    # make canvas for game - scale factor of x3 for each block
    gameCanvas = tk.Canvas(root, width=1200, height=500, background="darkgrey") # width=300,height=600
    gameCanvas.grid(row=1,column=0)
    block = newBlock()

def PlayGame(): # main game logic
    pass

#############################
# map of cw workload and plan
#############################
global root 
root = tk.Tk()

# button styles
style = ttk.Style()
style.configure("btn.TButton",foreground="#000000",bg="black",font=("small fonts",20,"bold"))

blackbg = ttk.Style()
blackbg.configure("BlackBackground.TButton", background="black", borderwidth=2, relief="solid")

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