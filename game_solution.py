###############################
# SCREEN RESOLUTION: 1280X720 #
###############################

# import list
import tkinter as tk
from tkinter import ttk
import random
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

###########
# classes #
###########

class aBlock: # generate the shpae bassed on random num passed in between 1 and 7 inclusive
    def __init__(self, canvas, sel):
        self.blocks = []
        self.canvas = canvas
        self.counter = 0
        self.selDict = {1 : "aqua_15.jpg", 
                        2 : "orange_15.jpg",
                        3 : "green_15.jpg",
                        4 : "pink_15.jpg",
                        5 : "purple_15.jpg",
                        6 : "red_15.jpg",
                        7 : "yellow_15.jpg"}
        img = Image.open(self.selDict[sel])
        self.photo = ImageTk.PhotoImage(img)
        img.close()
        if sel == 1:        # aqua - straight line 4
            gridy = 5
            for _ in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                block.grid(row=0, column=gridy)
                self.blocks.append(block)
                gridy += 1
        elif sel == 2:      # orange - right L
            gridy = 8
            for i in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                self.blocks.append(block)
                if i == 0:
                    # make it the top right
                    block.grid(row=0, column=gridy)
                else:
                    # 3 along bottom
                    block.grid(row=1, column=gridy)
                    gridy -= 1
        elif sel == 3:      # green - right z
            row1start = 2
            row2start = 1
            for _ in range(2):
                # add 1 to each of the two rows each iteration
                block1 = tk.Label(self.canvas, image=self.photo)
                block1.photo = self.photo
                block2 = tk.Label(self.canvas, image=self.photo)
                block2.photo = self.photo
                self.blocks.append(block1)
                self.blocks.append(block2)
                block1.grid(row=0, column=row1start)
                block2.grid(row=1, column=row2start)
                row1start += 1
                row2start += 1
        elif sel == 4:      # pink - left L
            gridy = 16
            for i in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                self.blocks.append(block)
                if i == 3:
                    block.grid(row=0, column=gridy-1)
                else:
                    block.grid(row=1, column=gridy)
                    gridy += 1
        elif sel == 5:      # purple - upside down T
            gridy = 20
            for i in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                self.blocks.append(block)
                if i == 1:
                    block.grid(row=0, column=gridy)
                else:
                    block.grid(row=1, column=gridy)
                    gridy += 1         
        elif sel == 6:      # red - left z
            row1start = 25
            row2start = 26
            for _ in range(2):
                # add 1 to each of the two rows each iteration
                block1 = tk.Label(self.canvas, image=self.photo)
                block1.photo = self.photo
                block2 = tk.Label(self.canvas, image=self.photo)
                block2.photo = self.photo
                self.blocks.append(block1)
                self.blocks.append(block2)
                block1.grid(row=0, column=row1start)
                block2.grid(row=1, column=row2start)
                row1start += 1
                row2start += 1
        else:               # yellow - square
            for i in range(2):
                for j in range(2):
                    block = tk.Label(self.canvas, image=self.photo)
                    block.photo = self.photo
                    self.blocks.append(block)
                    block.grid(row=i, column=30+j)
    def fall(self):      
        # move all down 1 grid postiion
        Falling = True
        while Falling:
            for b in self.blocks:
                info = b.grid_info()
                currentRow = info['row']
                currentRow += 1
                if currentRow > 10:         # at bottom of screen
                    Falling = False
                    return
            if Falling:                     # all blocks in range
                for b in self.blocks:
                    info = b.grid_info()
                    currentRow = info['row']
                    currentRow += 1
                    b.grid(row=currentRow, column=b.grid_info()['column'])
                    
                root.update()
                time.sleep(0.5)
            # collision detection time
                
            # the way we implement flaling collision detection - check grid position for border 
            # (<0 or > 10 for horizontal)
            # (<0 or > 20 for vertical)
            # if allowed, append pos to row array
            # if any block outside then do not move

        # place blocks in new row if allowed
        # repeat until collides with another block that borders the canvas

    def notPlaced(self): # a boolean variable to represertn if the block is falling or not
        return (self.counter == 5)

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

def InitialiseGameCanvas(): # COMP - create game canvas' and buttons
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

def IncrementScore(): # COMP - add 1 to score when blocks placed
    currentScore = score.cget("text")
    currentScore = int(currentScore)
    currentScore += 1
    score.config(text=currentScore)
    
def PlayGame(gameDetails): # main game module  - WIP
    global width, height
    global score, playGameCanvas
    global b, falling # vars to control when falling

    InitialiseGameCanvas()

    # actual operation ##########
    # randomly generate number and hence shape

    playGame = True
    while playGame:
        randBlock = random.randint(1,7)
        b = aBlock(playGameCanvas, randBlock)
        falling = True
        b.fall()
        falling = False
        # block placed so add one to score
        IncrementScore()
        for x in b.blocks:
            allBlocks.append(x)
        # remove after
        if len(allBlocks) > 40:
            playGame = False


        # after each falling iteration check for a complete row



        # 

    # add controls to the shape
    # add collision detection
    # start next block fall
    # check if row is complete
    # clear by making all white then delete
    
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

def InformationClicked(): # ONLY IF WAY TOO MUCH TIME - WIP
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
    img = Image.open("googlesheets_9.png")
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

def TurnClockwise(event): # WIP
    pass

def TurnAnticlockwise(event): # WIP
    pass

def MoveLeft(event): # WIP
    # make global the currently falling block properties
    global b, falling
    if falling:
        for block in b.blocks:
            # get grid position
            i = block.grid_info()
            currentColumn = i['column']
            currentColumn -= 1
            block.grid(row=i['row'], column=currentColumn)

        # if collides then dont do
    
    # move each part one unit to the left

def MoveRight(event): #WIP
    # make global the currently falling block properties
    global b, falling
    
    if falling:
        for block in b.blocks:
            # get grid position
            i = block.grid_info()
            currentColumn = i['column']
            currentColumn += 1
            block.grid(row=i['row'], column=currentColumn)

            # if collides then dont do
    
    # move each part one unit to the right

def HardDrop(event): # WIP
    pass

def HoldPiece(event): # WIP
    pass

#######################################################################################################################
################################################## main program #######################################################
#######################################################################################################################

# for later - this is how to update score - another cheat code
def ScoreUpdate(event):
    # get score and add 5 to it
    currentScore = score.cget("text")
    currentScore = int(currentScore)
    currentScore += 5
    score.config(text=currentScore)

#####################
# initialise window #
#####################
root = tk.Tk()
root.title("Tetris")
root.geometry(resolution)
root.configure(background="black")
# home page
HomeWindow()

############
# keybinds #
############
# test
root.bind("<9>", ScoreUpdate)

# cheatcode/bosskey keybinds
root.bind("bk", BossKey)
root.bind("123", CheatCode)

# controls keybinds
root.bind("x", TurnClockwise)
root.bind("x", TurnAnticlockwise)
root.bind("<Left>", MoveLeft)
root.bind("<Right>", MoveRight)
root.bind("<Down>", HardDrop)
# if time do softdrop with anohter key
root.bind("<Up>", HoldPiece)

###################
# blocking method #
###################
root.mainloop()

##### note of stuff used in program once but not in code: ######

    # resize images once
    # img = img.resize((15,15))
    # img.save("aqua_15.jpg")


# image = Image.open("googlesheets_3.png")
# img = image.resize((1280,720))
# img.save("googlesheets_9.png")