board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]

def CheckEnd():
    for i in range(3):
        if all(val != " " for row in board for val in row):
            Winner = False
            return Winner
        if board[i][0] == board[i][1] == board[i][2] != " ":
            Winner = board[i][0]
            return Winner
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            Winner = board[0][i]
            return Winner
        elif board[0][0] == board[1][1] == board[2][2] != " ":
            Winner = board[1][1]
            return Winner
        elif board[0][2] == board[1][1] == board[2][0] != " ":
            Winner = board[1][1]
            return Winner
    return None

def get_empty_cells(board):
    empty_cells = [[i,j] for i in range(3) for j in range(3) if board[i][j] == " "]
    return empty_cells

def make_ai_move():
    best_move = minimax(board, player)
    return best_move

def minimax(board, player):

    result = CheckEnd()
    if result in ["O", "X", False]:
        if result == "X":
            return {"score": 1}
        elif result == "O":
            return {"score": -1}
        else:
            return {"score": 0}
    
    empty_cells = get_empty_cells(board)

    moves = []
    for cell in empty_cells:
        move = {}
        move['position'] = cell
        board[cell[0]][cell[1]] = player

        if player =="X":
            result = minimax(board, "O")
            move["score"] = result["score"]
            
        else:
            result = minimax(board, "X")
            move["score"] = result["score"]

        board[cell[0]][cell[1]] = ' ' # undo the move
        moves.append(move)

    if player == "X":
        best_move = max(moves, key=lambda x : x["score"])
    else:
        best_move = min(moves, key=lambda x : x["score"])

    return best_move


def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} \n-----------\n {board[1][0]} | {board[1][1]} | {board[1][2]} \n-----------\n {board[2][0]} | {board[2][1]} | {board[2][2]}")
    return board


Winner = ""
WinnerPlayer = ""
player = "O"

while WinnerPlayer == "":
    print_board(board)
    user_input_x, user_input_y = None, None
    correct_coordinates = True
    while correct_coordinates:
        if player == "O":
            
            while user_input_x not in ["0", "1", "2"]:
                user_input_x = input(f"Enter your row coordinates for {player}:  ")
            while user_input_y not in ["0", "1", "2"]:
                user_input_y = input(f"Enter your column coordinates for {player}:  ")

            if board[int(user_input_x)][int(user_input_y)] == " ":
                correct_coordinates = False
            else:
                user_input_x = ""
                user_input_y = ""
                print("place already occupied")
        else:
            print("AI move")
            move_ai = make_ai_move()
            user_input_x, user_input_y = move_ai['position']
            correct_coordinates = False
        
    board[int(user_input_x)][int(user_input_y)] = player
    result = CheckEnd()
    if result in ["O", "X", False]:
        WinnerPlayer = False
    user_input_x, user_input_y = None, None

    if player == "O":
        player = "X"
    else:
        player = "O"

if result == "O":
    print_board(board)
    print("Player 1 win")
elif result == "X":
    print_board(board)
    print("Player 2 win")
elif result == False:
    print_board(board)
    print("Draw")
else:
    print("error")
    print(result)


