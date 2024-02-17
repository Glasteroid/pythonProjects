import ast

# get input from user (X or O)

# define a function that prints out board (2d array)

# define update function that takes user selected position as parameter

board_spots = [["", "", ""], ["", "", ""], ["", "", ""]]

PLAYER1 = ""
PLAYER2 = ""

def print_board():
    for row in board_spots:
            print(row)

def get_player():
        global PLAYER1
        global PLAYER2
        
        user_input = input("Player 1, would you like to be X or O? ").upper()

        while user_input not in ['X', 'O']:
            user_input = input("Player 1, would you like to be X or O? ").upper()

        if user_input == "X":
            PLAYER1 = "X"
            PLAYER2 = "O"
            print("Player 1 will be X, and Player 2 will be O.")

        else:
            PLAYER1 = "O"
            PLAYER2 = "X"
            print("Player 1 will be O, and Player 2 will be X.")
       
def get_pos():
    possible_pos = [["(1, 1)", "(1, 2)", "(1, 3)"], ["(2, 1)", "(2, 2)", "(2, 3)"], ["(3, 1)", "(3, 2)", "(3, 3)"]]
    all_pos = ["(1, 1)", "(1, 2)", "(1, 3)", "(2, 1)", "(2, 2)", "(2, 3)", "(3, 1)", "(3, 2)", "(3, 3)"]
    
    for row in possible_pos:
        print(row)
    
    pos = input("Please choose a spot from the board according to the coordinates above: ")

    while pos not in all_pos:
        pos = input("Please choose a spot from the board according to the coordinates above: ")
            
    return pos

def player_turn(turns):
    global PLAYER1, PLAYER2 
    
    current_player = ""
    
    if turns % 2 == 0:
        current_player = PLAYER1

    else:
        current_player = PLAYER2
        
    return current_player

def update_board(position, cp):
    if position == "(1, 1)":
        board_spots[0][0] = cp
    
    if position == "(1, 2)":
        board_spots[0][1] = cp
    
    if position == "(1, 3)":
        board_spots[0][2] = cp
    
    if position == "(2, 1)":
        board_spots[1][0] = cp
    
    if position == "(2, 2)":
        board_spots[1][1] = cp

    if position == "(2, 3)":
        board_spots[1][2] = cp
        
    if position == "(3, 1)":
        board_spots[2][0] = cp
        
    if position == "(3, 2)":
        board_spots[2][1] = cp
        
    if position == "(3, 3)":
        board_spots[2][2] = cp
        
def player_win():
    if (board_spots[0][0] == board_spots[0][1] == board_spots[0][2]) and (board_spots[0][0] == PLAYER1 or board_spots[0][0] == PLAYER2):
        return True, board_spots[0][0]
    
    elif (board_spots[1][0] == board_spots[1][1] == board_spots[1][2]) and (board_spots[1][0] == PLAYER1 or board_spots[1][0] == PLAYER2):
        return True, board_spots[1][0]
    
    elif (board_spots[2][0] == board_spots[2][1] == board_spots[2][2]) and (board_spots[2][0] == PLAYER1 or board_spots[2][0] == PLAYER2):
        return True, board_spots[2][0]
    
    elif (board_spots[0][0] == board_spots[1][0] == board_spots[2][0]) and (board_spots[0][0] == PLAYER1 or board_spots[0][0] == PLAYER2):
        return True, board_spots[0][0]
    
    elif (board_spots[0][1] == board_spots[1][1] == board_spots[2][1]) and (board_spots[0][1] == PLAYER1 or board_spots[0][1] == PLAYER2):
        return True, board_spots[0][1]
    
    elif (board_spots[0][2] == board_spots[1][2] == board_spots[2][2]) and (board_spots[0][2] == PLAYER1 or board_spots[0][2] == PLAYER2): 
        return True, board_spots[0][2]
    
    elif (board_spots[0][0] == board_spots[1][1] == board_spots[2][2]) and (board_spots[0][0] == PLAYER1 or board_spots[0][0] == PLAYER2):
        return True, board_spots[0][0]
    
    elif (board_spots[0][2] == board_spots[1][1] == board_spots[2][0]) and (board_spots[0][2] == PLAYER1 or board_spots[0][2] == PLAYER2):
        return True, board_spots[0][2]
            
    else:
        return False, ""
                
    
def check_occ(cp):
    global PLAYER1, PLAYER2 

    pos = cp.strip('()').split(',')
    
    pos = tuple(map(int, pos))

    if board_spots[pos[0] - 1][pos[1] - 1] == PLAYER1 or board_spots[pos[0] - 1][pos[1] - 1] == PLAYER2:
        print("Position occupied, please choose another position.")
        return True
    
    else:
        return False

def play_game(turns):
    chosen_pos = get_pos()
    i = check_occ(chosen_pos)
    
    while i == True:
        chosen_pos = get_pos()
        i = check_occ(chosen_pos)

    update_board(chosen_pos, player_turn(turns))

def play_again():
    user_input = input("Would you like to play again? ").upper()
    
    while user_input not in ["YES", "NO"]:
        user_input = input("Would you like to play again? ").upper()

    if user_input == "YES":
        return True
    
    else:
        return False

def main():
    global PLAYER1, PLAYER2 
    
    print("Welcome to Tic Tac Toe!")
    
    get_player()
    
    total_turns = 0
        
    case, player = player_win() 
    
    while case == False:
        play_game(total_turns)
        print_board()
        total_turns += 1      
        case, player = player_win()     
    
    if player == PLAYER1:
        print(f"Congratulations for winning {player}")

    elif player == PLAYER2:
        print(f"Congratulations for winning {player}!")
        
    else:
        draw = True
        for row in range(3):
            for col in range(3):
                if board_spots[row][col] == "":
                    draw = False
                    break
            if not draw:
                break
        if draw:
            print("It's a draw!")
    
    if play_again():
        for i in range(3):
            for j in range(3):
                board_spots[i][j] = ""
        main()

main()
