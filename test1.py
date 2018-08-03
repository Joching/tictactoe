y1 = ' '
y2 = ' '
y3 = ' '
y4 = ' '
y5 = ' '
y6 = ' '
y7 = ' '
y8 = ' '
y9 = ' '

lock1 = False
lock2 = False
lock3 = False
lock4 = False
lock5 = False
lock6 = False
lock7 = False
lock8 = False
lock9 = False

print('\n'*80)
print('Welcome to "this took way to long to code" tic tac toe!\n'.center(80, ' '))
print('Player 1, Please Choose a Quadrant\n'.center(80, ' '))

def gameboard():
    print (f'''
                             {y1} | {y2} | {y3}         1   2   3
                            ---+---+---
                             {y4} | {y5} | {y6}         4   5   6
                            ---+---+---
                             {y7} | {y8} | {y9}         7   8   9
        
    ''')
    

gameboard()

user_input = input('')

if user_input == '1':
    y1 = 'X'
    



print('hi' + y1)

gameboard()



# for w in range(10):
#     if pos == w:
#        yw = 'X'
            