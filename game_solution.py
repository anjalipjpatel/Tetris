###############################
# SCREEN RESOLUTION: 1280X720 #
###############################

##############
# objectives #
##############
# 1. Use of images - blocks that fall                   (COMP)
# 2. Use of shapes - tetris blocks                      (COMP)
# 3. Use of text - titles etc                           (COMP)
# 4. Scoring mechanism - blocks placed + row cleared    (COMP)
# 5. Leaderboard - on homepage w player name n pos      (COMP)
# 6. Image Resolution - 1280x720                        (COMP)
# 7. Movement of Objects - tetris blocks r,l and down   (COMP)
# 8. User moves objects - r,l,down                      (COMP)
# 9. Collision Detection - check if block in grid pos   (COMP)
# 10. Pause and unpause - toplevel window               (COMP)
# 11. Customize experince - keys that define movement   (COMP)
# 12. Cheat codes - add score (clear blocks?)           (COMP)
# 13. Save/Load - from text file                        (COMP)
# 14. Boss Key - pulls up GoogleSheet                   (COMP)

###############
# import list #
###############
import tkinter as tk
from tkinter import ttk
import random
import time
from PIL import Image,ImageTk # pip install pillow - allowed

# colours
black = "#1E2328"
grey = "#3B3F46"
yellow = "#FED053"
red = "#EE4B2B"

# screen dimensions
screenwidth = 1280
screenheight = 720
resolution = "1280x720"

# block default heights
height = 50
width = 100

# font
titleFont = ("small fonts", 100, "bold")
headingFont = ("small fonts", 60, "bold")
mediumFont = ("small fonts", 30, "bold")
smallFont = ("small fonts", 20, "bold")

###########
# classes #
###########
class aBlock: # generate the shpae bassed on random num passed in between 1 and 7 inclusive
    def __init__(self, canvas, sel):
        '''
        Function initialises block that has been randomly selected in main program. 
        It also places it on the screen at a specified starting point in the middle of the grid
        '''
        global keyBinds
        self.blocks = []
        self.canvas = canvas
        self.counter = 0
        self.sel = sel

        root.bind(keyBinds["clockwise"], self.RotateClockwise)
        root.bind(keyBinds["anticlockwise"], self.RotateAnticlockwise)
        root.bind(keyBinds["left"], self.MoveLeft)
        root.bind(keyBinds["right"], self.MoveRight)
        root.bind(keyBinds["down"], self.MoveDown)

        self.selDict = {1 : "aqua.jpg", 
                        2 : "orange.jpg",
                        3 : "green.jpg",
                        4 : "pink.jpg",
                        5 : "purple.jpg",
                        6 : "red.jpg",
                        7 : "yellow.jpg"}
        img = Image.open(self.selDict[self.sel])
        self.photo = ImageTk.PhotoImage(img)
        img.close()
        self.spawnPos = [0,10]
        if sel == 1:        # aqua - straight line 4            
            gridy = self.spawnPos[1]
            for _ in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                if not self.CollisionDetection(self.spawnPos[0], gridy):
                    block.grid(row=self.spawnPos[0], column=gridy)
                    self.blocks.append(block)
                    gridy += 1
                else:
                    CheckGameOver(True)
        elif sel == 2:      # orange - right L
            gridy = self.spawnPos[1]
            for i in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                self.blocks.append(block)
                if i == 0:
                    if not self.CollisionDetection(self.spawnPos[0], gridy):
                        # make it the top right
                        block.grid(row=self.spawnPos[0], column=gridy)
                    else:
                        CheckGameOver(True)
                else:
                    if not self.CollisionDetection(self.spawnPos[0]+1, gridy):
                        # 3 along bottom
                        block.grid(row=self.spawnPos[0]+1, column=gridy)
                        gridy -= 1
                    else:
                        CheckGameOver(True)
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
                if not self.CollisionDetection(0,row1start) and not self.CollisionDetection(0, row2start):
                    block1.grid(row=0, column=row1start)
                    block2.grid(row=1, column=row2start)
                    row1start += 1
                    row2start += 1
                else:
                    CheckGameOver(True)
        elif sel == 4:      # pink - left L
            gridy = self.spawnPos[1]
            for i in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                self.blocks.append(block)
                if i == 3:
                    if not self.CollisionDetection(self.spawnPos[0], gridy+1):
                        block.grid(row=self.spawnPos[0], column=gridy+1)
                    else:
                        CheckGameOver(True)
                else:
                    if not self.CollisionDetection(self.spawnPos[0]+1, gridy):
                        block.grid(row=self.spawnPos[0]+1, column=gridy)
                        gridy -= 1
                    else:
                        CheckGameOver(True)
        elif sel == 5:      # purple - upside down T
            gridy = self.spawnPos[1]
            for i in range(4):
                block = tk.Label(self.canvas, image=self.photo)
                block.photo = self.photo
                self.blocks.append(block)
                if i == 1 and not self.CollisionDetection(self.spawnPos[0], gridy):
                    block.grid(row=self.spawnPos[0], column=gridy)
                elif not self.CollisionDetection(self.spawnPos[0]+1, gridy):
                    block.grid(row=self.spawnPos[0]+1, column=gridy)
                    gridy += 1
                else:
                    CheckGameOver(True)
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
                if not self.CollisionDetection(0,row1start) and not self.CollisionDetection(1, row2start):
                    block1.grid(row=0, column=row1start)
                    block2.grid(row=1, column=row2start)
                    row1start += 1
                    row2start += 1
                else:
                    CheckGameOver(True)
        else:               # yellow - square
            for i in range(2):
                for j in range(2):
                    block = tk.Label(self.canvas, image=self.photo)
                    block.photo = self.photo
                    self.blocks.append(block)
                    if not self.CollisionDetection(self.spawnPos[0]+i, self.spawnPos[1]+j):
                        block.grid(row=self.spawnPos[0]+i, column=self.spawnPos[1]+j)
                    else:
                        CheckGameOver(True)
    def fall(self):
        '''
        Function that allows the block to move down the page until it collides with another block/the bottom.
        Also controls the speed of the fall based on the time elapsed - changes between 0 and 30s.
        '''
        global Falling, elapsedTime, keyBinds
        # move all down 1 grid postiion
        speed = [0.5, 0.25, 0.15, 0.1]
        speedIndex = 0
        if elapsedTime > 0 and elapsedTime <= 10:
            speedIndex = 0
        elif elapsedTime > 10 and elapsedTime <= 30:
            speedIndex = 1
        elif elapsedTime > 30 and elapsedTime <= 45:
            speedIndex = 2
        elif elapsedTime > 45:
            speedIndex = 3
        Falling = True
        while Falling:
            if self.CanMoveDown():
                for b in self.blocks:
                    info = b.grid_info()
                    currentRow = info['row']
                    currentRow += 1
                    b.grid(row=currentRow, column=b.grid_info()['column'])
                root.update()
                time.sleep(speed[speedIndex])
            else:
                Falling = False
                root.unbind(keyBinds["anticlockwise"])
                root.unbind(keyBinds["clockwise"])
                root.unbind(keyBinds["left"])
                root.unbind(keyBinds["right"])
                root.unbind(keyBinds["down"])
                return
    def CanMoveDown(self):
        '''
        Function that checks if the block can be moved downwards - Returns True if it can and False otherwise.
        '''
        for block in self.blocks:
            info = block.grid_info()
            currentRow = info['row']
            currentRow += 1
            currentColumn = info['column']
            # can move down if row is less than 20 and does not collide with another block.
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
        '''
        Function that checks if a rotation is valid - does not collide and within bounds.

        Returns True if valid and False if not valid.
        '''
        for i in range(len(newb)):
            newR = newb[i][0]
            newC = newb[i][1]
            if newR < 0 or newR >=20 or newC < 6 or newC >= 15:
                return False
            if self.CollisionDetection(newR,newC):
                return False
        return True
    def RotateClockwise(self,event):
        newPos = []
        # block centre
           
        centreRow = sum(block.grid_info()['row'] for block in self.blocks) // len(self.blocks)
        centreCol = sum(block.grid_info()['column'] for block in self.blocks) // len(self.blocks)

        for block in self.blocks:
            info = block.grid_info()
            currentRow, currentCol = info['row'], info['column']
            # calculate relative row and col positoins
            relRow = currentRow - centreRow
            relCol = currentCol - centreCol

            # new row and col after  rotation
            newRow = centreRow - relCol
            newCol = centreCol + relRow

            newPos.append((newRow, newCol))
        
        if self.RotationValid(newPos):
            for i,block in enumerate(self.blocks):
                newRow, newCol = newPos[i]
                block.grid(row=newRow, column=newCol)
    def RotateAnticlockwise(self, event):
        newPos = []

        # block centre
        centerRow = sum(block.grid_info()['row'] for block in self.blocks) // len(self.blocks)
        centerCol = sum(block.grid_info()['column'] for block in self.blocks) // len(self.blocks)

        for block in self.blocks:
            info = block.grid_info()
            currentRow, currentCol = info['row'], info['column']

            # calculate relative row and col positions
            relRow = currentRow - centerRow
            relCol = currentCol - centerCol

            # new row and col after  rotation
            newRow = centerRow + relCol
            newCol = centerCol - relRow

            newPos.append((newRow, newCol))

        if self.RotationValid(newPos):
            for i, block in enumerate(self.blocks):
                newRow, newCol = newPos[i]
                block.grid(row=newRow, column=newCol)
    def MoveLeft(self,event): 
        '''
        Function that moves block left
        '''
        # make global the currently falling block properties
        canLeft = True
        col = []
        for block in self.blocks:
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
    def MoveRight(self, event):
        canRight = True
        col = []
        for block in self.blocks:
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
    def MoveDown(self,event): # CORECOMP
        '''
        Function that drops block down to bottom
        '''
        global b, Falling
        if Falling:
            while b.CanMoveDown():
                for block in self.blocks:
                    info = block.grid_info()
                    currentRow = info['row']
                    currentRow += 1
                    block.grid(row=currentRow, column=block.grid_info()['column'])
            root.update()
            time.sleep(0.1)     

################################################################################################################
######################################### FUNCTIONS ############################################################
################################################################################################################


##############
# home page #
##############
def HomeWindow(): # create the homepage - CORECOMP
    '''
    Function establishes the home-page and all related components (buttons, text etc.)
    '''
    global usernameTxt, blockCanvas # so that it can be accessed in other programs

    # red, orange, yellow, green, aqua, pink
    # create title canvas
    titleCanvas = tk.Canvas(root, width=width, height=height, bg=black)
    ttk.Label(titleCanvas, text="T", font=titleFont,foreground="#ff6961", background="#000000").grid(row=0, column=0)
    ttk.Label(titleCanvas, text="E", font=titleFont,foreground="#fac898", background="#000000").grid(row=0, column=1)
    ttk.Label(titleCanvas, text="T", font=titleFont,foreground="#fdfd96", background="#000000").grid(row=0, column=2)
    ttk.Label(titleCanvas, text="R", font=titleFont,foreground="#fdf06a", background="#000000").grid(row=0, column=3)
    ttk.Label(titleCanvas, text="I", font=titleFont,foreground="#f6fdfa", background="#000000").grid(row=0, column=4)
    ttk.Label(titleCanvas, text="S", font=titleFont,foreground="#f8c8dc", background="#000000").grid(row=0, column=5)

    titleCanvas.pack()
    # create canvas for homebuttons and username entry
    homeCanvas = tk.Canvas(root, width=width, height=height, bg=black)
    homeCanvas.pack(side="right",fill="x",expand=True)

    # username canvas and entry
    usernameCanvas = tk.Canvas(homeCanvas, width=width,height=height,bg=black, highlightthickness=0)
    usernameCanvas.pack(expand=True)
    ttk.Label(usernameCanvas, text="Enter Your Username : ", font=smallFont, borderwidth=0,foreground=yellow,background=black, justify="center",padding=(5,5)).pack(side="left")
    usernameTxt = ttk.Entry(usernameCanvas,background=black,font=smallFont,foreground=black)
    usernameTxt.pack(side="right")
    
    # buttons to advance pages
    # choice buttons - new, load, leaderboard, exit, information page, controls page
    tk.Button(homeCanvas,text="NEW GAME",command=NewGameClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")
    tk.Button(homeCanvas,text="LOAD GAME",command=LoadGameClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")
    tk.Button(homeCanvas,text="LEADERBOARD",command=LeaderboardClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")
    tk.Button(homeCanvas,text="CONTROLS",command=ControlsClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=yellow,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")
    tk.Button(homeCanvas,text="EXIT",command=ExitClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=red,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")

    # make tetris blocks on bottom of page - widthspan = 4, 
    blockCanvas = tk.Canvas(homeCanvas, background="#000000", highlightthickness=0)
    blockCanvas.pack(fill="x", anchor="s")
    makeYellow(0)
    makeRed(2)
    makeAqua(5)
    makeOrange(9)
    makeGreen(13)
    makePink(16)
    makePurple(19)
    makeYellow(22)
    makeRed(25)
    makeGreen(28)
    makePurple(32)
    makeOrange(35)
    makeRed(38)

# make coloured blocks
def makeYellow(startPos):
    global blockCanvas
    # yellow square
    img = Image.open("yellow.jpg")
    photo = ImageTk.PhotoImage(img)
    img.close()
    for i in range(2):
        for j in range(2):
            block = tk.Label(blockCanvas, image=photo)
            block.photo = photo
            block.grid(row=i, column=startPos+j)
def makeRed(startPos):
    # red block
    img = Image.open("red.jpg")
    photo = ImageTk.PhotoImage(img)
    img.close()
    row1start = startPos
    row2start = startPos + 1
    for _ in range(2):
        block1 = tk.Label(blockCanvas, image=photo)
        block1.photo = photo
        block1.grid(row=0, column=row1start)
        block2 = tk.Label(blockCanvas, image=photo)
        block2.photo = photo
        block2.grid(row=1, column=row2start)
        row1start += 1
        row2start += 1
def makeAqua(startPos):
    # aqua
    img = Image.open("aqua.jpg")
    photo = ImageTk.PhotoImage(img)
    img.close()
    gridy = startPos
    for _ in range(4):
        block = tk.Label(blockCanvas, image=photo)
        block.photo = photo
        block.grid(row = 1, column=gridy)
        gridy += 1
def makeOrange(startPos):
    # orange
    img = Image.open("orange.jpg")
    photo = ImageTk.PhotoImage(img)
    img.close()
    for i in range(4):
        block = tk.Label(blockCanvas, image = photo)
        block.photo = photo
        if i == 3:
            block.grid(row=0, column=startPos-1)
        else:
            block.grid(row=1, column=startPos)
            startPos += 1
def makeGreen(startPos):
    # green
    img = Image.open("green.jpg")
    photo = ImageTk.PhotoImage(img)
    img.close()
    row1start = startPos + 1
    row2start = startPos
    for _ in range(2):
        block1 = tk.Label(blockCanvas, image=photo)
        block1.photo = photo
        block1.grid(row=0,column=row1start)
        block2 = tk.Label(blockCanvas, image=photo)
        block2.photo = photo
        block2.grid(row=1, column=row2start)
        row1start += 1
        row2start += 1
def makePink(startPos):
    # pink
    img = Image.open("pink.jpg")
    photo = ImageTk.PhotoImage(img)
    img.close()
    gridy = startPos
    for i in range(4):
        block = tk.Label(blockCanvas, image=photo)
        block.photo = photo
        if i == 0:
            block.grid(row=0, column=gridy)
        else:
            block.grid(row=1, column=gridy)
            gridy += 1
def makePurple(startPos):
    # purple
    img = Image.open("purple.jpg")
    photo = ImageTk.PhotoImage(img)
    img.close()
    for i in range(4):
        block = tk.Label(blockCanvas, image=photo)
        block.photo = photo
        if i == 1:
            block.grid(row=0, column=startPos)
        else:
            block.grid(row=1, column=startPos)
            startPos += 1

def GetUsername(): # retrives username input to textbox - COMP
    '''
    Function that returns username input into username text-box on homepage
    '''
    global usernameTxt, username, userInput
    username = usernameTxt.get()
    # if username is empty, generate random guest name
    if username == "" or ("," in username):
        username = GenerateRandomUser()
        userInput = False
    userInput = True
    return username

def GenerateRandomUser(): # generates random username if box is empty - COMP
    '''
    Function to generate an anonoymous-random user if no username is input
    '''
    global username
    name = "user" + str(random.randint(1,999))
    return name


#############
# game page #
#############
def NewGameClicked(): # load up a new game - COMP
    '''
    Function that specifies the actions and in what order they are exectued when the user requests a new game
    '''
    
    GetUsername()
    WipeAllWidgets()

    # initialise all game details
    PlayGame([])

def LoadGameClicked(): # load up an existing game - COMP
    '''
    Function that loads a saved game from memory if a correspondign save exists under the username input on the home-screen.

    If there is no corresponding entry, show a topLevel tkinter window as an error message and redirect back to homepage.
    '''
    global username, userInput, blockPosArray, allBlocks, playGame, b, fall
    GetUsername()
    WipeAllWidgets()

    if userInput:   # not an anonymous user  
        loadGameConfig = []
        # open text file
        s = open("loadGame.txt", "r")
        tmp = s.read().splitlines()
        s.close()
        Found = False
        i = -1
        while not Found and (i < len(tmp)-1): # try and find entry for user
            i += 1
            loadGameConfig = tmp[i].split(".")
            if loadGameConfig[0] == username:
                Found = True
        
        if Found:   # pass to playgame
            # remove from file
            s = open("loadGame.txt", "w")
            for j in range(len(tmp)):
                if i != j:
                    s.write(tmp[j]+"\n")
            s.close()
            PlayGame(loadGameConfig)

        else: # no corresponding game found - return to homepage
            WipeAllWidgets()
            newWin = tk.Toplevel()
            newWin.title("ERROR")
            ttk.Label(newWin, text="ERROR: No game found", font=mediumFont, foreground=red,background=black, justify="center",padding=(5,5)).pack()
            newWin.wait_window()
            HomeWindow()
    else: # no valid username input as playing anonymously so return to home
        WipeAllWidgets()
        newWin = tk.Toplevel()
        newWin.title("ERROR")
        ttk.Label(newWin, text="ERROR: Anon Username - No game can be loaded", font=mediumFont, foreground=red,background=black, justify="center",padding=(5,5)).pack()
        newWin.wait_window()
        HomeWindow()

    # if was null, output text box and return to main screen

def gameBorder(): # COMP - a border around the tetris game
    '''
    Function that creates the border around the canvas of the game - to allow grid elements after to work well.
    '''
    r = 22
    c = 31
    for i in range(r):
        # make block and place
        b = tk.Canvas(playGameCanvas, width=30, height=30, background=black, highlightthickness=0)
        b.grid(row=i,column=0)
    for j in range(c):
        b = tk.Canvas(playGameCanvas, width=30, height=30, background=black, highlightthickness=0)
        b.grid(row=r, column=j)
    # for k in range(r):
    #     b = tk.Canvas(playGameCanvas, width=30, height=30, background=black, highlightthickness=0)
    #     b.grid(row=k, column=c)

    # make grid for actual blocks to map falling
    img = Image.open("black.jpg")
    photo = ImageTk.PhotoImage(img)
    img.close()
    for i in range(1,21):
        for j in range(6,16,1):
            # make black block
            b = tk.Label(playGameCanvas, image=photo)
            b.photo = photo
            # grid in requried pos
            b.grid(row=i, column=j)

def InitialiseNewGameCanvas(s): # COMP - create game canvas' and buttons
    '''
    Create the game canvas - pass in score to initilaise value from prevoius games too
    '''
    global playGameCanvas, buttonsCanvas, score, allBlocks, blockPosArray, timeout
    # initilaise canvas
    root.config(bg=black)
    # make game canvas
    playGameCanvas = tk.Canvas(root,width="880", height=height, bg=black, borderwidth=0)
    playGameCanvas.pack(side="left",expand=True, fill="both")

    # border around game canvas to make grid work
    gameBorder()

    # add score, pause, reset, home - all on button canvas
    buttonsCanvas = tk.Canvas(root, width="600", height=height, bg=black, borderwidth=0)
    buttonsCanvas.pack(side="right", expand=True, anchor="e", fill="y")
    
    scoreHead = ttk.Label(buttonsCanvas, text="S C O R E", font=headingFont, background=black, foreground=yellow, anchor="center")
    scoreHead.pack(fill="x")
    score = ttk.Label(buttonsCanvas, text=s,font=mediumFont, background=black, foreground=yellow, anchor="center")
    score.pack(fill="x")

    timeHead = ttk.Label(buttonsCanvas, text="T I M E", font=headingFont, background=black, foreground=yellow, anchor="center")
    timeHead.pack(fill="x")
    timeout = ttk.Label(buttonsCanvas, text="",font=mediumFont, background=black, foreground=yellow, anchor="center")
    timeout.pack(fill="x")

    home = MakeHomeButton(buttonsCanvas)
    home.pack(anchor="center",fill="x")

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
    pause.pack(anchor="s",fill="x")

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
    save.pack(anchor="s",fill="x")

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
    reset.pack(anchor="s",fill="x")

    name = ttk.Label(buttonsCanvas, text=username,font=mediumFont, background=black, foreground=yellow, anchor="center")
    name.pack(fill="x")

def IncrementScore(add): # COMP - add 1 to score when blocks placed
    '''
    Increment the score by the value passed into the function
    '''
    currentScore = score.cget("text")
    currentScore = int(currentScore)
    currentScore += add
    score.config(text=currentScore)
    
def PlayGame(gameDetails): # main game module  - COMP
    '''
    Main logic to load up game-save/initialise game
    '''
    global width, height
    global score, playGameCanvas # vars to control when falling
    global blockPosArray, allBlocks
    global elapsedTime
    elapsedTime = -1
    blockPosArray = [[None for i in range(10)]for j in range(20)]
    allBlocks = []
    if gameDetails == []:
        InitialiseNewGameCanvas(0)
        updateTime()
        GameFunction()
    else: # need to restore game
        # username, blockPosArray, playGame, currentScore, time
        # the objects wil not stay - make all white for now
        loadScore = gameDetails[3]
        InitialiseNewGameCanvas(loadScore)
        coords = gameDetails[1].split(",")
        elapsedTime = int(gameDetails[4])
        timeout.config(text=elapsedTime)
        for i in range(0,len(coords)-1,2): # restore block
            # open white, grid to i, j    
            row = int(coords[i])
            col = int(coords[i+1])
            img = Image.open("white.jpg")
            photo = ImageTk.PhotoImage(img)
            img.close()
            block = tk.Label(playGameCanvas, image=photo)
            block.photo = photo
            block.grid(row=row+1, column=col+6)
            blockPosArray[row][col]= block
            allBlocks.append(block)

        if gameDetails[2]:  # playGame = True
            updateTime()
            GameFunction()          
            # then restore function back to gamefunction

def GameFunction(): # COMP
    '''
    Logic of the actual game
    '''
    global playGame, b, blockPosArray
    playGame = True
    randBlock = random.randint(1,7)
    b = aBlock(playGameCanvas, randBlock)
    b.fall()

    for x in b.blocks:
        allBlocks.append(x)
        # loop through all blocks
        # place coordinates on array
        info = x.grid_info()
        blockPosArray[info['row']-1][info['column']-6] = x
    
    # block placed so add one to score
    IncrementScore(1)
    CheckFullRow() # after each falling iteration check for a complete row
    if playGame:
        root.after(100, GameFunction)

def CheckFullRow(): # COMP
    ''' 
    a function that checks if a full row has been filled 
    - if yes then it removes the row and moves the rest of the blocks down.
    '''

    for i in range(len(blockPosArray)):
        if None not in blockPosArray[i]:
            for j in range(len(blockPosArray[i])):
                allBlocks.remove(blockPosArray[i][j])
                blockPosArray[i][j].destroy()
                blockPosArray[i][j] = None
            for x in range(i,0,-1):
                for r in range(len(blockPosArray[x])):
                    if blockPosArray[x][r] != None:
                        info = blockPosArray[x][r].grid_info()
                        blockPosArray[x][r].grid(row=(info['row']+1), column=(info['column']))
                        blockPosArray[x+1][r] = blockPosArray[x][r]
                        blockPosArray[x][r] = None
            IncrementScore(5)

def CheckGameOver(fallCollision): # COMP
    '''
    Checks if the game has ended due to the blocks overflowing
    '''
    global playGame, username
    if fallCollision: # game deffo over
        playGame = False
        endScore = str(score.cget("text"))
        AddScoreToLeaderboard()
        WipeAllWidgets()
        gameOverCanvas = tk.Canvas(root, width=width, height=height, bg=black)
        gameOverCanvas.pack(side="right",fill="both",expand=True)
        home = MakeHomeButton(gameOverCanvas)
        home.pack()
        ttk.Label(gameOverCanvas, text="G A M E   O V E R", font=headingFont, foreground=red,background=black, justify="center",padding=(5,5)).pack()
        ttk.Label(gameOverCanvas, text=("USERNAME: " + username), font=mediumFont, foreground=yellow,background=black, justify="center",padding=(5,5)).pack()
        ttk.Label(gameOverCanvas, text=("SCORE: " + endScore), font=mediumFont, foreground=yellow, background=black, justify="center",padding=(5,5)).pack()

def PauseGame(): # COMP
    '''
    Function that pauses the game by creating a Tk TopLevel window - press button to restart
    '''
    global score, username
    # make a new window popup - button to kill and the game restarts from where it was
    newWin = tk.Toplevel()
    newWin.title("PAUSED GAME")
    # open page in middle of screen
    userscreenw = root.winfo_screenwidth()
    userscreenh = root.winfo_screenheight()

    x = (userscreenw/2) - (screenwidth/2)
    y = (userscreenh/2) - (screenheight/2)

    # make window centered on screen
    newWin.geometry( '%dx%d+%d+%d' % (screenwidth, screenheight, x, y))

    newWinCanvas = tk.Canvas(newWin, background=black)
    newWinCanvas.pack(fill="both", expand=True)

    ttk.Label(newWinCanvas, text=username,font=mediumFont, background=black, foreground=yellow, anchor="center").pack(fill="x")
    ttk.Label(newWinCanvas, text=("Score: " + str(score.cget("text"))),font=mediumFont, background=black, foreground=yellow, anchor="center").pack(fill="x")
    ttk.Label(newWinCanvas, text=("Time: " + str(elapsedTime)), font=mediumFont, background=black, foreground=yellow, anchor="center").pack(fill="x")
    tk.Button(newWinCanvas,
                      text="RESTART",
                      command=lambda: newWin.destroy(),
                      font=smallFont,
                      activebackground=yellow,
                      activeforeground=black,
                      bg=black,
                      fg=yellow,
                      justify="center",
                      padx=5,
                      pady=5,
                      relief="solid").pack(fill="x")
    
    tk.Button(newWinCanvas,
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
                      relief="solid").pack(fill="x")

    tk.Button(newWinCanvas,text="EXIT",command=ExitClicked,font=smallFont,activebackground=yellow,activeforeground=black,bg=black,fg=red,justify="center",padx=5,pady=5,relief="solid").pack(fill="x")

    paused = True

    newWin.wait_window()

def ResetGame(): # COMP
    '''
    Function that saves score to leaderboard and restarts the game
    '''
    AddScoreToLeaderboard()
    playGameCanvas.destroy()
    WipeAllWidgets()
    # stop all other functinality going
    PlayGame([])

def SaveGame(): # COMP
    '''
    Function to save the game data to loadGame.txt to laod back later
    '''
    # save username, array with where blocks are, playgame - rest can just be restarted from game cont
    global username, playGame, score, blockPosArray
    # username, blockPosArray, playGame, currentScore
    # record blockposarray coords intiailly
    coords = ""
    for i in range(len(blockPosArray)):
        for j in range(len(blockPosArray[i])):
            if blockPosArray[i][j] is not None:
                coords += str(i) + "," + str(j) + ","
    if coords != "" or score > 0: # write as data to ssave
        s = open("loadGame.txt", "a")
        s.write(username+"."+coords+"."+str(playGame)+"."+str(score.cget("text"))+"."+str(timeout.cget("text"))+".\n")
        s.close()

    # now take user back to homepage
    WipeAllWidgets()
    HomeWindow()

def AddScoreToLeaderboard(): # COMP
    '''
    Function to append newest game to leaderboard file
    '''
    # called once blocks outside range, reset
    global score, username
    finalScore = score.cget("text")
    if finalScore != 0:
        line = username + "," + str(finalScore) + "\n"
        f = open("leaderboard.txt", "a")
        f.write(line)
        f.close()

def updateTime(): # COMP
    '''
    Function that updates the time on the screen every second of gameplay.
    '''
    global elapsedTime
    if not CheckPausedOpen():
        elapsedTime += 1
        # update time display
        timeout.config(text=elapsedTime)
    root.after(1000, updateTime)

def CheckPausedOpen():
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel) and window.title() == "PAUSED GAME":
            return True
    return False

###############
# leaderboard #
###############
def LeaderboardClicked(): # leaderboard page - CORECOMP
    '''
    Function that creates leaderboard page and dispalys scores in descending order
    '''
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

############
# controls #
############
def ControlsClicked(): # COMP
    '''
    Function that allows the user to switch between wasd-space and arrows controls
    '''
    global controlsPage
    WipeAllWidgets()
    # make page
    controlsPage = True
    controlCanvas = tk.Canvas(root, width=width, height=height, bg=black)
    controlCanvas.pack(fill="both",expand=True)

    # make drop-down options
    l = ["<Left>", "a"]
    r = ["<Right>", "d"]
    d = ["<Down>", "<space>"]

    lVal = tk.StringVar()
    rVal = tk.StringVar()
    dVal = tk.StringVar()
    
    h = MakeHomeButton(controlCanvas)
    h.grid(row=0, column=0, columnspan=3)
    
    ttk.Label(controlCanvas, text="C O N T R O L S", font=headingFont,background="#000000", foreground=yellow).grid(row=0, column=3)

    ttk.Label(controlCanvas, text="Move Left", font=mediumFont,background="#000000", foreground=yellow).grid(row=1,column=0, columnspan=3)
    leftDropDown = tk.OptionMenu(controlCanvas, lVal, *l, command=onLeftChange)
    leftDropDown.grid(row = 1, column= 5)
    ttk.Label(controlCanvas, text="Move Right", font=mediumFont,background="#000000", foreground=yellow).grid(row=2,column=0, columnspan=3)
    rightDropDown = tk.OptionMenu(controlCanvas, rVal, *r, command=onRightChange)
    rightDropDown.grid(row=2,column=5)
    ttk.Label(controlCanvas, text="Move Down", font=mediumFont,background="#000000", foreground=yellow).grid(row=3,column=0, columnspan=3)
    downDropDown = tk.OptionMenu(controlCanvas, dVal, *d, command=onDownChange)
    downDropDown.grid(row=3, column=5)

def onLeftChange(value):
    '''
    Function that updates the keybind for the moveleft function
    '''

    # check if value matches the dictionry - if it does then do nothing

    # else remove associated keybind in dictionary and rebind and update dictionary to reflect

    global keyBinds
    if value == keyBinds["left"]:
        return
    else:
        root.unbind(keyBinds["left"])
        root.bind(value, MoveLeft)
        keyBinds["left"] = value
    
    root.bind(keyBinds["left"], MoveLeft)

def onRightChange(value):
    '''
    Function that updates the keybind for the moveright function
    '''

    global keyBinds
    if value != keyBinds["right"]:
        root.unbind(keyBinds["right"])
        root.bind(value, MoveRight)
        keyBinds["right"] = value
    
    root.bind(keyBinds["right"], MoveRight)

def onDownChange(value):
    '''
    Function that updates the keybind for the hardrop function
    '''

    global keyBinds
    if value != keyBinds["down"]:
        root.unbind(keyBinds["down"])
        root.bind(value, HardDrop)
        keyBinds["down"] = value
    
    root.bind(keyBinds["down"], HardDrop)


########
# misc #
########
def ExitClicked(): # exit the game - COMP
    '''
    Exit's the game - destroys root window
    '''
    root.destroy()

def WipeAllWidgets(): # clears all current widgets on screen - COMP
    '''
    Function to remove all elements on screen
    '''
    global root
    for widget in root.winfo_children():
        widget.destroy()

def BackHome(): # user returns to homepage - COMP
    '''
    Function to take user back to homepage
    '''
    WipeAllWidgets()
    HomeWindow()

def MakeHomeButton(canvas): # return home button widget - COMP
    '''
    Function that returns a button with styling that allows a user to navigate back to the homepage
    '''
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

def Sort(arr): # COMP
    '''
    a bubble sort on the contents of the leaderboard - descending
    '''
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

#########################
# boss key + cheatcodes #
#########################
def BossKey(event): # bosskey functionality - COMP
    '''
    a function to load up image to act as if user is at work
    '''
    global root, bossKeyOn, bossk
    if not bossKeyOn:
        bossKeyOn = True
        bossk = tk.Toplevel()
        bossk.title("GOOGLE SHEETS")
        # open page in middle of screen
        userscreenw = root.winfo_screenwidth()
        userscreenh = root.winfo_screenheight()

        x = (userscreenw/2) - (screenwidth/2)
        y = (userscreenh/2) - (screenheight/2)

        # make window centered on screen
        bossk.geometry( '%dx%d+%d+%d' % (screenwidth, screenheight, x, y))

        # open the image
        img = Image.open("googlesheets_9.png")
        photo = ImageTk.PhotoImage(img)
        # make image window
        # show image
        label = tk.Label(bossk,image=photo)
        label.photo = photo
        label.pack()
    else:
        bossKeyOn = False
        bossk.destroy()

def CheatCode(event): # cheatcode functionality - COMP
    '''
    a function that destroys all blocks on page when key-combo is pressed
    '''
    # delets all placed blocks
    global allBlocks, blockPosArray
    for b in allBlocks:
        b.destroy()
    allBlocks = []

    # update blockposarray
    blockPosArray = [[None for i in range(10)]for j in range(20)]

def ScoreUpdate(event): # COMP - cheat code v2
    '''
    cheatcode that updates the score by +5 when key combo pressed
    '''
    # get score and add 5 to it
    currentScore = score.cget("text")
    currentScore = int(currentScore)
    currentScore += 5
    score.config(text=currentScore)
   

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

# change root window logos
img = Image.open("logo.jpg")
photo = ImageTk.PhotoImage(img)
img.close()
root.iconphoto(True, photo)
# make window centered on screen
userscreenw = root.winfo_screenwidth()
userscreenh = root.winfo_screenheight()
x = (userscreenw/2) - (screenwidth/2)
y = (userscreenh/2) - (screenheight/2)
root.geometry( '%dx%d+%d+%d' % (screenwidth, screenheight, x, y))


# home page
HomeWindow()
############
# keybinds #
############
keyBinds = {"score" : "96",
            "boss"  : "bk",
            "clear" : "123",
            "clockwise" : "x",
            "anticlockwise" : "c",
            "left"  : "<Left>",
            "right" : "<Right>",
            "down"  : "<Down>"}

# cheatcode/bosskey keybinds
bossKeyOn = False
root.bind("bk", BossKey)
root.bind("123", CheatCode)
root.bind("96", ScoreUpdate)

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