#Python Tic Tac Toe / Morpion

board = []
instructions_grid = [[1,2,3], [4,5,6], [7,8,9]]
win_cases = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

player1 = "X"
player2 = "O"
current_player = player1
for i in range(3):
    board.append([0,0,0])

def display_board():
    for i in range(3):
        print(board[i],"  ",instructions_grid[i])

def postion_r(p):
    return (p - 1) // 3  # lines

def position_c(p):
    return (p - 1) % 3

def place(player):
    global current_player
    while True:
        try:
            position = int(input(f"Au tour de {player}: "))
            r = postion_r(position)
            c = position_c(position)

            if board[r][c] == 0:
                board[r][c] = player
                break
            else:
                print("Case déjà prise, veuillez choisir une autre.")
        except ValueError:
            print("Entrée invalide, veuillez entrer un nombre entre 1 et 9.")


def check_win(board):
    win = False
    for i in range(3):
        # Horizontal
        if board[i][0] == board[i][1] == board[i][2] != 0:
            print(f"le joueur {current_player} à gagné")
            win = True
        #Vertical
        if board[0][i] == board[1][i] == board[2][i] != 0:
            print(f"le joueur {current_player} à gagné")
            win = True
    if board[0][0] == board[1][1] == board[2][2] != 0:
        print(f"le joueur {current_player} à gagné")
        win = True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        print(f"le joueur {current_player} à gagné")
        win = True
    return win
def check_draw(board):
    count = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return False
    print("égalité")
    return True

run = True
while(run):
    display_board()
    place(current_player)

    if check_win(board) or check_draw(board):
        run = False

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
