###############################
# SCREEN RESOLUTION: 1280X720 #
###############################

# import list
import tkinter as tk
from tkinter import ttk
import random
from tkinter import font
import time
from PIL import Image,ImageTk # pip install pillow - allowed

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

def HomeWindow(): # create the homepage - CORECOMP
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

def NewGameClicked(): # load up a new game - WIP
    print(GetUsername())
    WipeAllWidgets()

    # initialise all game details
    newGameConfig = []
    PlayGame(newGameConfig)

def LoadGameClicked(): # load up an existing game - WIP
    print("load game")
    # open text file, search for username if wasnt null then load array and pass to playgame
    loadGameConfig = []
    PlayGame(loadGameConfig)

    # if was null, output text box and return to main screen

class aqua: # definition of the aqua block elements
    def __init__(self, canvas): # define the 4 blocks for aqua - straight line
        self.blocks = []
        self.canvas = canvas
        self.counter = 0
        img = Image.open("aqua_15.jpg")
        self.photo = ImageTk.PhotoImage(img)
        img.close()
        gridy = 5
        # display to screen
        for _ in range(4):
            block = tk.Label(self.canvas, image=self.photo)
            block.photo = self.photo
            block.grid(row=0, column=gridy)
            self.blocks.append(block)
            gridy += 1

    def fall(self):        
        # move all down 1 grid postiion
        while (self.counter != 5):
            self.counter += 1
            for b in self.blocks:
                info = b.grid_info()
                currentRow = info['row']
                currentRow += 1

                # place on new row
                b.grid(row=currentRow, column=b.grid_info()['column'])
            # repeat until collides with another block that borders the canvas
            root.update()
            time.sleep(0.5)


        # self.counter += 1
        # if self.counter < 5:
        #     self.canvas.after(500,self.fall)

    def notPlaced(self): # a boolean variable to represertn if the block is falling or not
        return (self.counter == 5)

# class Keybinds:
#     def __init__(self, r):
#         self.root = r
#         self.keyStates = {"B": False, "K" : False, "1" : False, "2" : False, "3" : False}

#         self.root.bind("<KeyPress>", self.OnKeyPress)
#         self.root.bind("<KeyRelease>", self.OnKeyRelease)

#         self.root.bind("<b-k>", self.KeyCombination1)

#     def OnKeyPress(self,event):
#         key = event.keysym
#         if key in self.keyStates:
#             self.keyStates[key] = True

#     def OnKeyRelease(self, event):
#         key = event.keysym
#         if key in self.keyStates:
#             self.keyStates[key] = False
        
#     def KeyCombination1(self, event):
#         if self.keyStates["b"] and self.keyStates["k"]:
#             pass



def gameBorder(): # WIP (NEED TO CHANGE BLOCK COLOUR) - a border around the tetris game
    img = Image.open("pink_15.jpg")
    photo = ImageTk.PhotoImage(img)
    img.close()
    r = 37
    c = 51
    for i in range(r):
        # make block and place
        b = tk.Label(playGameCanvas, image=photo)
        b.photo = photo
        b.grid(row=i,column=0)
    for j in range(c+1):
        b = tk.Label(playGameCanvas, image=photo)
        b.photo = photo
        b.grid(row=r, column=j)
    for k in range(r):
        b = tk.Label(playGameCanvas, image=photo)
        b.photo = photo
        b.grid(row=k, column=c)

def InitialiseGameCanvas():
    global playGameCanvas, buttonsCanvas, score, allBlocks
    # initilaise canvas

    # data points required for game - [currentScore, allBlocks]
    currentScore = 0
    allBlocks = []

    # make game canvas
    playGameCanvas = tk.Canvas(root,width="880", height=height, bg=black)
    playGameCanvas.pack(side="left",expand=True, fill="both")

    # border around game canvas to make grid work
    gameBorder()

    # add score, pause, reset, home - all on button canvas
    buttonsCanvas = tk.Canvas(root, width="400", height=height, bg="grey")
    buttonsCanvas.pack(side="right", expand=True, anchor="e", fill="y")
    
    scoreHead = ttk.Label(buttonsCanvas, text="S C O R E", font=headingFont, background=black, foreground=yellow)
    scoreHead.pack()
    score = ttk.Label(buttonsCanvas, text=currentScore,font=mediumFont, background=black, foreground=yellow)
    score.pack()

    home = MakeHomeButton(buttonsCanvas)
    home.pack(anchor="center")

    pause = tk.Button(buttonsCanvas,
                      text="PAUSE",
                      command=PauseGame,
                      font=smallFont,
                      activebackground=yellow,
                      activeforeground=black,
                      bg=black,
                      fg=yellow,
                      justify="center",
                      padx=5,
                      pady=5,
                      relief="solid")    
    pause.pack(anchor="s")

    reset = tk.Button(buttonsCanvas,
                      text="RESET",
                      command=ResetGame,
                      font=smallFont,
                      activebackground=yellow,
                      activeforeground=black,
                      bg=black,
                      fg=yellow,
                      justify="center",
                      padx=5,
                      pady=5,
                      relief="solid")
    reset.pack(anchor="s")


def PlayGame(gameDetails): # main game module  - WIP
    global width, height
    global score, playGameCanvas

    InitialiseGameCanvas()
    # make block and add to list of all blocks
    block = aqua(playGameCanvas)
    #allBlocks.append(block)

    # make block fall with time
    # while block.notPlaced():
    #     root.after(500, block.fall)

    block.fall()



    # add controls to the shape



    # add collision detection



    # once placed, add all elements of hte class to the block list
    tmp = block.blocks
    for x in tmp:
        allBlocks.append(x)

    # start next block fall


    # check row is complete


    # clear by making all white then delet
    
def PauseGame(): # WIP
    pass

def ResetGame(): # WIP
    pass

def LeaderboardClicked(): # leaderboard page - CORECOMP
    WipeAllWidgets()

    # get data from file
    f = open("leaderboard.txt", "r")
    scores = f.read().splitlines()
    f.close()

    # create canvas for leaderboard
    leaderboardCanvas = tk.Canvas(root, width=width, height=height, bg=black)
    leaderboardCanvas.pack(fill="both",expand=True,padx=10,pady=10)

    # title
    ttk.Label(leaderboardCanvas, text="L E A D E R B O A R D", font=headingFont,background="#000000", foreground=yellow).pack()

    # make back button to homepage
    home = MakeHomeButton(leaderboardCanvas)
    home.pack()

    # seperate all scores into array of name in 0 and score in 1, append to newscores
    tempscores = []
    for i in range(0,len(scores)):
        tempscores.append(scores[i].split(","))
    
    # bubble sort array
    scores = Sort(tempscores)
   
    # create textbox to contain all scores
    scoreWidget = tk.Text(leaderboardCanvas, font=smallFont, background=black, foreground=yellow,borderwidth=0)
    scoreWidget.columnconfigure(0,weight=1)
    scoreWidget.pack(fill="x",padx=5)

    # display each score on page
    for index,item in enumerate(scores, start=1):
        scoreWidget.insert(tk.END, f"{index}.   {item[0]} - {item[1]}\n")

def InformationClicked(): # WIP
    print("information")

def ControlsClicked(): # WIP
    print("controls")

def ExitClicked(): # exit the game - COMP
    root.destroy()

def GetUsername(): # retrives username input to textbox - COMP
    global usernameTxt
    username = usernameTxt.get()
    # if username is empty, generate random guest name
    if username == "" or ("," in username):
        username = GenerateRandomUser()
    return username

def GenerateRandomUser(): # generates random username if box is empty - COMP
    global username
    name = "user" + str(random.randint(1,999))
    return name

def WipeAllWidgets(): # clears all current widgets on screen - COMP
    global root
    for widget in root.winfo_children():
        widget.destroy()

def BackHome(): # user returns to homepage - COMP
    WipeAllWidgets()
    HomeWindow()

def MakeHomeButton(canvas): # return home button widget - COMP
    return (tk.Button(canvas,
                      text="HOME",
                      command=BackHome,
                      font=smallFont,
                      activebackground=yellow,
                      activeforeground=black,
                      bg=black,
                      fg=yellow,
                      justify="center",
                      padx=5,
                      pady=5,
                      relief="solid"))

def Sort(arr): # bubble sort for contents of leaderboard (desc.) - COMP
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

def BossKey(event): # bosskey functionality - COMP
    global root
    WipeAllWidgets()
    # open the image
    img = Image.open("googlesheets.png")
    photo = ImageTk.PhotoImage(img)
    # make image window
    root.title("Google Sheets")
    # show image
    label = tk.Label(root,image=photo)
    label.photo = photo
    label.pack()

def CheatCode(event): # cheatcode functionality - COMP
    # delets all placed blocks
    global allBlocks
    for b in allBlocks:
        b.destroy()
    allBlocks = []

#######################################################################################################################
################################################## main program #######################################################
#######################################################################################################################



# for later - this is how to update score
def ScoreUpdate(event):
    global score
    score.config(text="5")


#####################
# initialise window #
#####################
root = tk.Tk()
root.title("Tetris")
root.geometry(resolution)
root.configure(background="black")
# bind = Keybinds(root)
# home page
HomeWindow()

############
# keybinds #
############
# movemetn keybinds

root.bind("<Left>", ScoreUpdate)

# cheatcode/bosskey
root.bind("bk", BossKey)            # method does not account for release of key
root.bind("123", CheatCode)

###################
# blocking method #
###################
root.mainloop()



##### note of stuff used in program once but not in code: ######

    # resize images once
    # img = img.resize((15,15))
    # img.save("aqua_15.jpg")