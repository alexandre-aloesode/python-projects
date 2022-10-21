board = [["-","-","-"], ["-","-","-"], ["-","-","-"]]

def board_display():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()

running = True

def victory1(player1):
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print(user1+" est le grand gagnant!")
        return running == False

def victory2(player2): 
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print(user2+"est le grand gagnant!")
        return running == False
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print(user2+"est le grand gagnant!")
        return running == False
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print(user2+"est le grand gagnant!")
        return running == False
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print(user2+"est le grand gagnant!")
        return running == False
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print(user2+"est le grand gagnant!")
        return running == False
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print(user2+"est le grand gagnant!")
        return running == False
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print(user2+"est le grand gagnant!")
        return running == False
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print(user2+"est le grand gagnant!")
        return running == False
    

action = input("Bonjour, souhaitez_vous jouer ou voir les scores? ")

if action == "s":
    print("scores")

elif action == "j":
        user1 = input("Qui est le premier joueur? ")
        user2 = input("Qui est le second joueur? ")
    
        while running != False:

                board_display()
            
                play1, play2 = input(user1+" "+"joue (ligne puis colonne) : ").split()
                ligne1 = int(play1)
                colonne1 = int(play2)
                board[ligne1-1][colonne1-1] = "X"
                running = victory1(board)
                if running == False:
                    break
                board_display()

                play3, play4 = input(user2+" "+"joue (ligne puis colonne) : ").split()
                ligne2 = int(play3)
                colonne2 = int(play4)
                board[ligne2-1][colonne2-1] = "O"
                running = victory2(board)
                if running == False:
                    break
            
else:
    print("choix invalide")

