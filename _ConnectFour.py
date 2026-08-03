board = [["-" for i in range(7)] for j in range(6)]

print("Connect Four")

board[5][0] = "X"
board[5][1] = "X"
board[5][2] = "X"
board[5][3] = "X"

for row in board:
    print(" ".join(row))

print("\nPlayer Wins!")
