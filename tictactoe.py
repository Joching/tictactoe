#If you can't tell from all the different win screens, this program was written by, me, Joshua Ching 
#I'm sure there are more efficient ways to code this program, but considering I didn't know how to -
#code two weeks ago, I think it's not bad. ----Augest 3th 2018




# This is what makes the board work. Each ' ' represents a blank square.
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 


#This is the 'Command Center' for player 1
def test():
    while True:
        user_input = input('Player 1, what do you choose? ')
        #Checks to make sure user inputs a valid command
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input >= 1 and (user_input <= 9) and board[user_input - 1] == ' ':
                if user_input == 1:
                    pos = 0
                elif user_input == 2:
                    pos = 1
                elif user_input == 3:
                    pos = 2
                elif user_input == 4:
                    pos = 3
                elif user_input == 5:
                    pos = 4
                elif user_input == 6:
                    pos = 5
                elif user_input == 7:
                    pos = 6
                elif user_input == 8:
                    pos = 7
                elif user_input == 9:
                    pos = 8
                board[pos] = '\033[36mX\033[0m'#Assigns a blue 'X' to the board
                break
            else:
                print('Please select a valid option')
        else:
            print('Please select a valid option')
        
        
#This is the 'Command Center' for player 2
def test2():
  while True:
        user_input = input('Player 2, what do you choose? ')

        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input >= 1 and (user_input <= 9) and board[user_input - 1] == ' ':
                if user_input == 1:
                    pos = 0
                elif user_input == 2:
                    pos = 1
                elif user_input == 3:
                    pos = 2
                elif user_input == 4:
                    pos = 3
                elif user_input == 5:
                    pos = 4
                elif user_input == 6:
                    pos = 5
                elif user_input == 7:
                    pos = 6
                elif user_input == 8:
                    pos = 7
                elif user_input == 9:
                    pos = 8
                board[pos] = '\033[31mO\033[0m'
                if gm == '2':
                    board[0],board[1],board[2] = board[2],board[0],board[1]#Stuff for second game mode. Makes everything swap at end of turn.
                    board[3],board[4],board[5] = board[5],board[3],board[4]
                    board[6],board[7],board[8] = board[8],board[6],board[7]
                break
            else:
                print('Please select a valid option')
        else:
            print('Please select a valid option')
            
#The gameboard that gets printed after every turn
def gameboard():
    print (f'''
                          {board[0]} | {board[1]} | {board[2]}         1   2   3
                         ---+---+---
                          {board[3]} | {board[4]} | {board[5]}         4   5   6
                         ---+---+---
                          {board[6]} | {board[7]} | {board[8]}         7   8   9
        
    ''')
    
#Checks every possible win condition to see if a player has one.
def wincheck():

    #Horizontal Lines
    if board[0] == board[1] == board[2] and board[0] != ' ':
        winplayer(board[0])
    if board[3] == board[4] == board[5] and board[3] != ' ':
        winplayer(board[3])
    if board[6] == board[7] == board[8] and board[6] != ' ':
        winplayer(board[6])

    #Vertical Lines
    if board[0] == board[3] == board[6] and board[0] != ' ':
        winplayer(board[0])
    if board[1] == board[4] == board[7] and board[1] != ' ':
        winplayer(board[1])
    if board[2] == board[5] == board[8] and board[2] != ' ':
        winplayer(board[2])
    
    #Diagonal Lines
    if board[0] == board[4] == board[8] and board[0] != ' ':
        winplayer(board[0])
    if board[2] == board[4] == board[6] and board[2] != ' ':
        winplayer(board[2])

#Prints messages when a player wins
def winplayer(q):
    if gm == '2':
        if q == '\033[31mO\033[0m':
            print("""
                ===============================================
                ||                \033[31mPlayer 2 is\033[0m                ||
                ||     \033[31mThe Champion of Shifting Squares!\033[0m     ||
                =============================================== 
                            Created By: Joshua Ching
            """)
        else:
            print("""
                ===============================================
                ||                \033[36mPlayer 1 is\033[0m                ||
                ||     \033[36mThe Champion of Shifting Squares!\033[0m     ||
                =============================================== 
                            Created By: Joshua Ching
            """)       
    else:
        if q == '\033[31mO\033[0m':
            print("""
                        ==============================
                        ||         \033[31mGood Game!\033[0m       ||
                        ||       \033[31mPlayer 2 Wins!\033[0m     ||
                        ==============================        
                           Created By: Joshua Ching
            """)
        else:
            print("""
                        ==============================
                        ||         \033[36mGood Game!\033[0m       ||
                        ||       \033[36mPlayer 1 Wins!\033[0m     ||
                        ==============================      
                           Created By: Joshua Ching  
            """)       
    exit()


#Probably a unencessary variable I made because I'm bad at coding
qx = 0

#Used for custom game mode
def gamemode():
    global gm
    global qx
    if qx != 1:
        print('What game mode would you like to play?\n'.center(80, ' '))
        print('(1)Classic\n'.center(80, ' '))
        print('(2)Shifting Squares\n'.center(80, ' '))
    gm = input("Select a gamemode by typing the number to it's left\n".center(80, ' '))
    if gm != '1' and gm != '2':
        print('\033[31mError: Please select a game mode\033[0m'.center(85, ' '))
        qx = 1
        gamemode()

#Function which gives a greeting                 
def greeting():
    print('Welcome to "this took way to long to code" tic tac toe!\n'.center(80, ' '))
    print('Created By: Joshua Ching\n'.center(80, ' '))

#'Removes' the stuff written in terminal before starting the program
print('\n'*1000)
greeting()
gamemode()
print('\n'*1000)
p = 1
pw = 0
for w in range(10):
    gameboard()
    wincheck()
    
    if w == 9:
        if gm == '2':
            sys.stdout.write('\033[31mE\033[0m')
            sys.stdout.write('\033[32mA\033[0m')
            sys.stdout.write('\033[33mS\033[0m')
            sys.stdout.write('\033[34mT\033[0m')
            sys.stdout.write('\033[35mE\033[0m')
            sys.stdout.write('\033[31mR\033[0m')
            print('')
            print('Created By: Joshua Ching ')
            quit()
        else:
            print("""
                            ==============================
                            ||         \033[33mGood Game\033[0m        ||
                            ||        \033[33mIt's a tie!\033[0m       ||
                            ==============================     
                               Created By: Joshua Ching     
            """)
        quit()
    elif p == 1:
        test()
        p = 2
        if gm == '2' and pw == 1:
            board[0],board[1],board[2] = board[2],board[0],board[1]
            board[3],board[4],board[5] = board[5],board[3],board[4]
            board[6],board[7],board[8] = board[8],board[6],board[7]
        pw = 1
    else:
        test2()
        p = 1
    if gm != '2':
        print('\n'*1000)


    #If you have read this far, there is an easter egg if you can get the
    #shifting squares mode to end in a tie game. Good luck!
    