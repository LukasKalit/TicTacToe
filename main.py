

def CheckEnd():
    for i in range(3):
        if all(val != " " for row in Tic for val in row):
            Winner = False
            return Winner
        if Tic[i][0] == Tic[i][1] == Tic[i][2] != " ":
            Winner = Tic[i][0]
            return Winner
        elif Tic[0][i] == Tic[1][i] == Tic[2][i] != " ":
            Winner = Tic[0][i]
            return Winner
        elif Tic[0][0] == Tic[1][1] == Tic[2][2] != " ":
            Winner = Tic[1][1]
            return Winner
        elif Tic[0][2] == Tic[1][1] == Tic[2][0] != " ":
            Winner = Tic[1][1]
            return Winner


    return None

Tic = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]
Winner = ""
WinnerPlayer = ""
letter = ["O","X"]
i = 0

while WinnerPlayer == "":
    print(f" {Tic[0][0]} | {Tic[0][1]} | {Tic[0][2]} \n-----------\n {Tic[1][0]} | {Tic[1][1]} | {Tic[1][2]} \n-----------\n {Tic[2][0]} | {Tic[2][1]} | {Tic[2][2]}")
    user_input_x, user_input_y = None, None
    correct_coordinates = True
    while correct_coordinates:
        while user_input_x not in ["0", "1", "2"]:
            user_input_x = input(f"Enter your row coordinates for {letter[i]}:  ")
        while user_input_y not in ["0", "1", "2"]:
            user_input_y = input(f"Enter your column coordinates for {letter[i]}:  ")
        if Tic[int(user_input_x)][int(user_input_y)] == " ":
            correct_coordinates = False
        else:
            user_input_x = ""
            user_input_y = ""
            print("place already occupied")

    if i == 0:
        Tic[int(user_input_x)][int(user_input_y)] = "O"
        i = 1
    elif i == 1:
        Tic[int(user_input_x)][int(user_input_y)] = "X"
        i = 0
    result = CheckEnd()
    if result in ["O", "X", False]:
        WinnerPlayer = False
    user_input_x, user_input_y = None, None

if result == "O":
    print("Player 1 win")
elif result == "X":
    print("Player 2 win")
elif result == False:
    print("Draw")
else:
    print("error")
    print(result)


