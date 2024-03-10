import numpy as np
import random, time, os

computer = 0
user = 1

board = np.array([[" ", " ", " "],
                  [" ", " ", " "],
                  [" ", " ", " "]])

choices = [[0,0], [0,1], [0,2],
           [1,0], [1,1], [1,2],
           [2,0], [2,1], [2,2]]

def reset_game(board, choices):
    board = np.array([[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]])

    choices = [[0,0], [0,1], [0,2],
               [1,0], [1,1], [1,2],
               [2,0], [2,1], [2,2]]
    return board, choices

def computer_choice():
    choice = list(random.choice(choices))
    row = choice[0]
    col = choice[1]
    return row, col

def user_choice():
    row = int(input("Insert row (0-2):\t"))
    col = int(input("Insert column (0-2):\t"))
    if (row >= 0 and row <= 2) and (col >= 0 and col <= 2):
        return row, col
    else:
        print("Invalid input. Try again.")

def show_board(board):
    print("\t   {} | {} | {} ".format(board[0, 0], board[0, 1], board[0, 2]))
    print("\t  -----------")
    print("\t   {} | {} | {} ".format(board[1, 0], board[1, 1], board[1, 2]))
    print("\t  -----------")
    print("\t   {} | {} | {} ".format(board[2, 0], board[2, 1], board[2, 2]))
    
def update_choices(row, col, choices):
    choice = [row, col]
    for item in choices:
        if item == choice:
            choices.remove(item)
    return choices

def update_board(player, row, col, board):
    if player == computer and board[row, col] == " ":
        board[row, col] = "O"
    elif player == user  and board[row, col] == " ":
        board[row, col] = "X"
    return board

def computer_turn(board, choices):
    row, col = computer_choice()
    choices = update_choices(row, col, choices)
    board = update_board(computer, row, col, board)
    return board, choices

def user_turn(board, choices):
    row, col = user_choice()
    choices = update_choices(row, col, choices)
    board = update_board(user, row, col, board)
    return board, choices

def check_winner(board):
    no_winner = True
    for i in range(3):
        if list(board[i,:]) == ["X","X","X"] or list(board[:,i]) == ["X","X","X"] \
            or list(np.diag(board)) == ["X","X","X"] or list(np.diag(np.fliplr(board))) == ["X","X","X"]:
            print("\nYou're the winner!")
            time.sleep(3)
            no_winner = False
            return no_winner
        elif list(board[i,:]) == ["O","O","O"] or list(board[:,i]) == ["O","O","O"] \
            or list(np.diag(board)) == ["O","O","O"] or list(np.diag(np.fliplr(board))) == ["O","O","O"]:
            print("\nThe COMPUTER won!")
            time.sleep(3)
            no_winner = False
            return no_winner
    else:
        return no_winner

def print_game_header():
    print("==============================")
    print("==        TIC-TAC-TOE       ==")
    print("==============================")
    print("\n")

#"""
loading_msg = "Loading game"
for i in range(4):
    loading_msg += "."
    print(loading_msg)
    time.sleep(1)
    os.system("cls")

print("==============================")
print("==  WELCOME TO TIC-TAC-TOE  ==")
print("==============================")
print("\n")
time.sleep(1)
os.system("cls")

game_running = True
while game_running:
    print_game_header()
    run = input("Do you wanna play? \n(Y/N): ")
    run = run.lower()
    if run.isalpha:
        # user input equals to 'y' -> continues the game 
        if run == 'y':
            os.system("cls")
            
            # story line 1
            print_game_header()
            print("Alright let\'s play!")
            time.sleep(2)
            os.system("cls")
            
            # actual game
            print_game_header()
            print("Who will start first?")
            time.sleep(1)
            os.system("cls")
            
            again = True
            while again:
                # coin toss
                coin_toss_running = True
                while coin_toss_running:
                    print_game_header()
                    coin_result = random.choice(["HEAD", "TAIL"])
                    coin_toss = input("Choose, head or tail? \n(head/tail): ").upper()
                    time.sleep(1)
                    os.system("cls")
                    if coin_toss == "HEAD" or coin_toss == "TAIL":
                        print_game_header()
                        print("Tossing coin...")
                        print("\n")
                        time.sleep(2)
                        if coin_toss == coin_result:
                            print("It's {}, YOU start first!".format(coin_result))
                            starter = user
                            coin_toss_running = False
                            time.sleep(1)
                            os.system("cls")
                        elif coin_toss != coin_result:
                            print("It's {}, the COMPUTER starts!".format(coin_result))
                            starter = computer
                            coin_toss_running = False
                            time.sleep(1)
                            os.system("cls")
                    else:
                        print_game_header()
                        print("Invalid input. Try again.")
                        time.sleep(3)
                        os.system("cls")
            
                # tic-tac-toe game
                tic_tac_toe_running = True
                while tic_tac_toe_running:
                    print_game_header()
                    show_board(board)
                    print("\n")
                    if starter == computer:
                        turn = True
                        while turn:
                            time.sleep(2)
                        
                            board, choices = computer_turn(board, choices)
                            os.system("cls")
                            print_game_header()
                            show_board(board)
                            print("\n")
                            print(choices)

                            result = check_winner(board)
                            tic_tac_toe_running = turn = result
                            
                            if tic_tac_toe_running == False:
                                break
                            
                            board, choices = user_turn(board, choices)
                            os.system("cls")
                            print_game_header()
                            show_board(board)
                            print("\n")
                            print(choices)
                        
                            result = check_winner(board)
                            tic_tac_toe_running = turn = result
                            
                            if tic_tac_toe_running == False:
                                break
                            
                    elif starter == user:
                        turn = True
                        while turn:
                            board, choices = user_turn(board, choices)
                            os.system("cls")
                            print_game_header()
                            show_board(board)
                            print("\n")
                            print(choices)
                            
                            result = check_winner(board)
                            tic_tac_toe_running = turn = result
                            
                            if tic_tac_toe_running == False:
                                break
                            
                            time.sleep(2)
                        
                            board, choices = computer_turn(board, choices)
                            os.system("cls")
                            print_game_header()
                            show_board(board)
                            print("\n")
                            print(choices)
                            
                            result = check_winner(board)
                            tic_tac_toe_running = turn = result
                            
                            if tic_tac_toe_running == False:
                                break
                    # end of the game
            
                # asks the user if they want to play again
                os.system("cls")
                print_game_header()
                play_again = input("Do you want to play again?\n(Y/N): ").upper()
                if play_again == "Y":
                    board, choices = reset_game(board, choices)
                    os.system("cls")
                    continue
                elif play_again == "N":
                    again = False
                    game_running = False
                    os.system("cls")
                    exiting_msg = "Exiting game"
                    for i in range(4):
                        exiting_msg += "."
                        print(exiting_msg)
                        time.sleep(1)
                        os.system("cls")
                        
        # user input equals to 'n' -> exits game        
        elif run == 'n':
            game_running = False
            os.system("cls")
            exiting_msg = "Exiting game"
            for i in range(4):
                exiting_msg += "."
                print(exiting_msg)
                time.sleep(1)
                os.system("cls")
        else:
            os.system("cls")
            print_game_header()
            print("Invalid input. Try again.")
            time.sleep(3)
            os.system("cls") 
        
#"""