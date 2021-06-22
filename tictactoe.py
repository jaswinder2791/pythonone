board=["-","-","-",
       "-","-,","-",
       "-","-","-"]
gamingisgoing=True
winner=None
currentplayer="X"
chanceCount=1

def display_board():
    print(board[0]+ "|" + board[1] + "|" + board[2])
    print(board[3]+ "|" + board[4] + "|" + board[5])
    print(board[6]+ "|" + board[7] + "|" + board[8])

def handle_turns():
    global gameisgoing
    position=int(input("Enter the position number:"))
    board[position]=currentplayer

def swap_player(currentplayer):
    global gamingisgoing
    if currentplayer=="X":
        return "0"
    else:
        return "X"

def check_who_is_the_winner():
    global winner
    rowwinner=check_row()
    colwinner=check_column()
    diawinner=check_dia()
    check_draw()

    if rowwinner:
        winner=rowwinner
    elif colwinner:
        winner=colwinner
    elif diawinner:
        winner=diawinner

def check_row():
    global gameisgoing
    row1 = board[0] == board[1] == board[2] !="-"
    row2 = board[3] == board[4] == board[5] !="-"
    row3 = board[6] == board[7] == board[8] !="-"
    if row1 or row2 or row3:
        gameisgoing = False
    if row1:
        return board[2]
    elif row2:
        return board[5]
    elif row3:
        return board[6]


def check_column():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        gameisgoing = False
    if col1:
        return board[6]
    elif col2:
        return board[1]
    elif col3:
        return board[5]

def check_dia():
    global gameisgoing
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"

    if dia1 or dia2:
        gameisgoing = False
    if dia1:
        return board[4]
    elif dia2:
        return board[4]


def check_draw():
    global gameisgoing
if board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8]!="-":
    gamingisgoing =False
    print("Match is Drawn")

def play_game():
    global gamingisgoing
    global currentplayer
    global chanceCount
    while gamingisgoing:

        display_board()

        handle_turns()

        currentplayer =swap_player(currentplayer)
        chanceCount= chanceCount + 1

        check_who_is_the_winner()
        if winner=="X":
            print("X is the winner")
            display_board()
            break
        elif winner=="0":
            print("0 is the winner")
            display_board()
            break
        elif chanceCount > 9:
            print("Match is drawn")
            display_board()
            break

play_game()
