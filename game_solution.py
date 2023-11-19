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
headingFont = ("small fonts", 60, "bold")
mediumFont = ("small fonts", 30, "bold")
smallFont = ("small fonts", 20, "bold")

###########
# classes #
###########

class aBlock: # generate the shpae bassed on random num passed in between 1 and 7 inclusive
    def __init__(self, canvas, sel):
        self.blocks = []
        self.canvas = canvas
        self.counter = 0
        self.sel = sel
        self.selDict = {1 : "aqua_15.jpg", 
                        2 : "orange_15.jpg",
                        3 : "green_15.jpg",
                        4 : "pink_15.jpg",
                        5 : "purple_15.jpg",
                        6 : "red_15.jpg",
                        7 : "yellow_15.jpg"}
        img = Image.open(self.selDict[self.sel])
        self.photo = ImageTk.PhotoImage(img)
        img.close()
        self.spawnPos = [0,10]
        if sel == 1:        # aqua - straight line 4
            gridy = self.spawnPos[1]
            for _ in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                block.grid(row=self.spawnPos[0], column=gridy)
                self.blocks.append(block)
                gridy += 1
        elif sel == 2:      # orange - right L
            gridy = self.spawnPos[1]
            for i in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                self.blocks.append(block)
                if i == 0:
                    # make it the top right
                    block.grid(row=self.spawnPos[0], column=gridy)
                else:
                    # 3 along bottom
                    block.grid(row=self.spawnPos[0]+1, column=gridy)
                    gridy -= 1
        elif sel == 3:      # green - right z
            row1start = self.spawnPos[1] + 1
            row2start = self.spawnPos[1]
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
            gridy = self.spawnPos[1]
            for i in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                self.blocks.append(block)
                if i == 3:
                    block.grid(row=self.spawnPos[0], column=gridy+1)
                else:
                    block.grid(row=self.spawnPos[0]+1, column=gridy)
                    gridy -= 1
        elif sel == 5:      # purple - upside down T
            gridy = self.spawnPos[1]
            for i in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                self.blocks.append(block)
                if i == 1:
                    block.grid(row=self.spawnPos[0], column=gridy)
                else:
                    block.grid(row=self.spawnPos[0]+1, column=gridy)
                    gridy += 1         
        elif sel == 6:      # red - left z
            row1start = self.spawnPos[1]
            row2start = self.spawnPos[1] + 1
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
                    block.grid(row=self.spawnPos[0]+i, column=self.spawnPos[1]+j)
    def fall(self):
        global Falling
        # move all down 1 grid postiion
        Falling = True
        while Falling:
            if self.CanMoveDown():
                for b in self.blocks:
                    info = b.grid_info()
                    currentRow = info['row']
                    currentRow += 1
                    b.grid(row=currentRow, column=b.grid_info()['column'])
                root.update()
                time.sleep(0.25)
            else:
                Falling = False
            # collision detection time
                
            # the way we implement flaling collision detection - check grid position for border 
            # (<0 or > 10 for horizontal)
            # (<0 or > 20 for vertical)
            # if allowed, append pos to row array
            # if any block outside then do not move

        # place blocks in new row if allowed
        # repeat until collides with another block that borders the canvas

    def CanMoveDown(self):
        '''
        Function that checks if the block can be moved downwards - Returns True if it can and False otherwise.
        '''
        for block in self.blocks:
            info = block.grid_info()
            currentRow = info['row']
            currentRow += 1
            currentColumn = info['column']
            if currentRow > 20 or self.CollisionDetection(currentRow, currentColumn):
                return False
        return True

    def CollisionDetection(self,r,c):
        '''
        Function that checks if there is a block at a specified grid position.
        Returns True if there is a block there and otherwise False.
        '''
        # loop thorugh all elements and compare row and col values with r and c
        for block in allBlocks:
            info = block.grid_info()
            if info['row'] == r and info['column'] == c:
                return True
        return False

    def RotationValid(self, newb):
        for i in range(len(newb)):
            newR = newb[i][0]
            newC = newb[i][1]
            if newR < 0 or newR >=20 or newC < 0 or newC >= 10:
                return False
            if self.CollisionDetection(newR,newC):
                return False
        return True

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
    GetUsername()
    WipeAllWidgets()

    # initialise all game details
    newGameConfig = []
    PlayGame(newGameConfig)

def LoadGameClicked(): # load up an existing game - WIP
    global username, userInput
    GetUsername()
    WipeAllWidgets()

    if userInput:   # not an anonymous user  
        loadGameConfig = []
        # open text file
        s = open("loadGame.txt", "r")
        tmp = s.read().splitlines()
        s.close()

        i = 0
        Found = False
        while (i <= len(tmp)-1) and not Found:  # find corresponding game save
            loadGameConfig = tmp[i].split(".")
            if loadGameConfig[0] == username:
                Found = True
                # delete from array with text-file contents
                tmp.remove(tmp[i])
                # rewrite values to text-file
                s = open("loadGame.txt", "w")
                for j in range(len(tmp)):
                    s.write(tmp[j] + "\n")
                s.close()
            i += 1
        
        if Found:   # pass to playgame
            PlayGame(loadGameConfig)
        else: # no corresponding game found - return to homepage
            WipeAllWidgets()
            HomeWindow()
    else: # no valid username input as playing anonymously so return to home
        WipeAllWidgets()
        HomeWindow()

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

    save = tk.Button(buttonsCanvas,
                      text="SAVE",
                      command=SaveGame,
                      font=smallFont,
                      activebackground=yellow,
                      activeforeground=black,
                      bg=black,
                      fg=yellow,
                      justify="center",
                      padx=5,
                      pady=5,
                      relief="solid")    
    save.pack(anchor="s")

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
    global score, playGameCanvas # vars to control when falling
    
    InitialiseGameCanvas()
    GameFunction()

    # add controls to the shape
    # add collision detection
    # check if row is complete
    # clear by making all white then delete

# actual operation ##########
# randomly generate number and hence shape
def GameFunction():
    global playGame, b, blockPosArray, fall
    playGame = True
    # create array to represent grid
    blockPosArray = [[None for i in range(10)] for j in range(20)]

    # randBlock = random.randint(1,7)
    # b = aBlock(playGameCanvas, randBlock)
    # b.fall()

    for x in range(100):
        b = aBlock(playGameCanvas, 7)
        fall = True
        b.fall()
        fall = False
        # block placed so add one to score
        IncrementScore()
        for x in b.blocks:
            allBlocks.append(x)
            # loop through all blocks
            # place coordinates on array
            info = x.grid_info()
            blockPosArray[info['row']-1][info['column']-6] = x
        CheckFullRow()
    # remove after
    # if len(allBlocks) > 40:
    #     playGame = False

        # after each falling iteration check for a complete row
    # if playGame:
    #     GameFunction()

def CheckFullRow(): # COMP
    ''' 
    a function that checks if a full row has been filled 
    - if yes then it removes the row and moves the rest of the blocks down.
    '''
    global blockPosArray
    rowsToClear = True
    rows = []
    while rowsToClear:
        rowsToClear = False
    # check if any rows are all True - if so delete the blocks in teh row and move the rest that are above down
        for i in range(len(blockPosArray)-1,0,-1):
            if None not in blockPosArray[i]: # row is full so need to delete
                rows.append(i)
                rowsToClear = True

        if rowsToClear:
            for rowClear in rows:
                for j in range(len(blockPosArray[rowClear])):
                    allBlocks.remove(blockPosArray[rowClear][j])
                    blockPosArray[rowClear][j].destroy()
                    blockPosArray[rowClear][j] = None
                # move all above down - update block pos array to reflect the fact blocks are gone
                for x in range(rowClear-1,0,-1):
                    for b in blockPosArray[x]:
                        #print(b)
                        if b is not None:
                            info = b.grid_info()
                            b.grid(row=(info['row']+1), column=info['column'])

def PauseGame(): # WIP
    pass

def ResetGame(): # COMP
    playGameCanvas.destroy()
    WipeAllWidgets()
    # stop all other functinality going
    PlayGame("a")

def SaveGame(): # WIP
    # get main data from game - arrays and vars
    # save as an array in text file
    # use username as a reference in pos0 of array
    # username, blockPosArray, allBlocks, playGame, b, fall
    gameData = ""
    gameData += (username + ".")
    gameData += (str(blockPosArray) + ".")
    gameData += (str(allBlocks) + ".")
    gameData += (str(playGame) + ".")
    gameData += (str(b) + ".")
    gameData += (str(fall) + ".")
    gameData += "\n"

    s = open("loadGame.txt", "a")
    s.write(gameData)
    s.close()

    # now take user back to homepage
    WipeAllWidgets()
    HomeWindow()

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
    global usernameTxt, username, userInput
    username = usernameTxt.get()
    # if username is empty, generate random guest name
    if username == "" or ("," in username):
        username = GenerateRandomUser()
        userInput = False
    userInput = True
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

def ScoreUpdate(event): # COMP - cheat code v2
    # get score and add 5 to it
    currentScore = score.cget("text")
    currentScore = int(currentScore)
    currentScore += 5
    score.config(text=currentScore)

def TurnClockwise(event): # WIP
    global b, falling
    if Falling:
        newBlocks = []
        # rotate the bllocks using rotatin matrix
        for block in b.blocks:
            info = block.grid_info()
            currentRow = info['row']
            currentColumn = info['column']
            newRow = b.spawnPos[0] + (currentColumn - b.spawnPos[1])
            newCol = b.spawnPos[1] - (currentRow - b.spawnPos[0])
            newBlocks.append([newRow,newCol])
        if b.RotationValid(newBlocks):
            # clear current blocks
            for block in b.blocks:
                block.destroy()
            
            b.blocks = []
            for newBlock in newBlocks:
                tmp = tk.Label(b.canvas, image=b.photo)
                tmp.photo = b.photo
                tmp.grid(row=newBlock[0], column=newBlock[1])
                b.blocks.append(tmp)
            root.update()

def TurnAnticlockwise(event): # WIP
    pass

def MoveLeft(event): # CORECOMP
    # make global the currently falling block properties
    global b, Falling
    if Falling:
        canLeft = True
        col = []
        for block in b.blocks:
            # get grid position
            i = block.grid_info()
            currentColumn = i['column']
            currentRow = i['row']
            currentColumn -= 1
            if currentColumn < 6: # check horizontal limit not exceeded - col not < 5
                canLeft = False
            else:
                col.append([currentRow,currentColumn])
        if canLeft:
            i = 0
            for x in b.blocks:
                x.grid(row=col[i][0], column=col[i][1])
                i += 1

        # if collides then dont do
    
    # move each part one unit to the left

def MoveRight(event): #CORECOMP
    # make global the currently falling block properties
    global b, Falling
    
    if Falling:
        canRight = True
        col = []
        for block in b.blocks:
            # get grid position
            i = block.grid_info()
            currentColumn = i['column']
            currentRow = i['row']
            currentColumn += 1
            if currentColumn > 15: # check horizontal limit not exceeded - col not > 15
                canRight = False
            else:
                col.append([currentRow,currentColumn])
        if canRight:
            i = 0
            for x in b.blocks:
                x.grid(row=col[i][0], column=col[i][1])
                i += 1

            # if collides then dont do
    
    # move each part one unit to the right

def HardDrop(event): # CORECOMP
    global b, Falling
    if Falling:
        while b.CanMoveDown():
            for block in b.blocks:
                info = block.grid_info()
                currentRow = info['row']
                currentRow += 1
                block.grid(row=currentRow, column=block.grid_info()['column'])
        root.update()
        time.sleep(0.25)                

def HoldPiece(event): # WIP - if time
    pass

#######################################################################################################################
################################################## main program #######################################################
#######################################################################################################################

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
root.bind("c", TurnAnticlockwise)
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