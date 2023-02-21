'''
Created on 21-Feb-2023

@author: ankon
'''
'''
1. Display the game board with 9 positions for x and y
2. Make sure the board is empty
3. provide numbers for each cell so that the player can refer to it
4. provide error message for placing a symbol in filled cell
5. If player has 3 symbols in a line, display "Youwin!!" message.
'''

theboard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' ',}

boardKeys=[]

print(boardKeys)

for key in theboard:
    boardKeys.append(key)
#print(boardKeys)    


def printBoard(board):
    print(board['7']+'/'+ board['8']+ '/' + board['9'])
    print('_____')
    
    print(board['4']+'/'+ board['5']+ '/' + board['6'])
    print('_____')
    
    print(board['1']+'/'+ board['2']+ '/' + board['3'])
    print('_____')

# printBoard(theboard)

def game():
    turn= 'X'
    count= 0    
    
    for i in range(10):
        printBoard(theboard)
        
        print("It's turn of"+ turn +"specify the place you want to go")
        
        move=input()
    
        if theboard[move]==' ':
            theboard[move]=turn
            count+=1
        else:
            print("Sorry this cell location is filled. Please choose an other one.")
            
            continue
        if count>=5:
            if theboard['7'] == theboard['8'] == theboard ['9'] !=' ':
                printBoard(theboard)
                print("\nGame over\n")
                print("Player"+turn+"won the game")
                
                break
            if theboard['4'] == theboard['5'] == theboard ['6'] !=' ':
                printBoard(theboard)
                print("\nGame over\n")
                print("Player"+turn+"won the game")
                
                break
            if theboard['1'] == theboard['2'] == theboard ['3'] !=' ':
                printBoard(theboard)
                print("\nGame over\n")
                print("Player"+turn+"won the game")
                
                break
            if theboard['1'] == theboard['4'] == theboard ['7'] !=' ':
                printBoard(theboard)
                print("\nGame over\n")
                print("Player"+turn+"won the game")
                
                break
            if theboard['3'] == theboard['6'] == theboard ['9'] !=' ':
                printBoard(theboard)
                print("\nGame over\n")
                print("Player"+turn+"won the game")
                
                break
            if theboard['1'] == theboard['5'] == theboard ['9'] !=' ':
                printBoard(theboard)
                print("\nGame over\n")
                print("Player"+turn+"won the game")
                
                break
            if theboard['3'] == theboard['5'] == theboard ['7'] !=' ':
                printBoard(theboard)
                print("\nGame over\n")
                print("Player"+turn+"won the game")
                
                break
        
        if count == 9:
            print("\nGame Over\n")
            print("The game is tie!")
            
        if turn == "X":
            turn="0"
        else:
            turn="X"
            
            
    restart =input("Do you want to restart the game? (y/n)")
        
    if restart=='y' or restart=='Y':
        for key in boardKeys:
            theboard[key]=' '
        game()
            
if __name__=="__main__":
    game()