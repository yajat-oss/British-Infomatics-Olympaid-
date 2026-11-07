#Q1:
cards = [0, 0, 0, 0, 0]

#intialises the score metric 
score = 0

# inputting the cards:
for x in range(0, 5):
    num = int(input("Enter a number between 1 and 10 inclusive: \n"))
    cards[x] = num

print(cards)

# checking for identical cards:
for y in range(0, 4):
    for z in range(y + 1, 5):
        if cards[y] == cards[z]:
            score += 1

# checking combinations of 2:
for a in range(0, 4):
    for b in range(a + 1, 5):
        if cards[a] + cards[b] == 15:
            score += 1

# checking combinations of 3:
for a in range(0, 3):
    for b in range(a + 1, 4):
        for c in range(b + 1, 5):
            if cards[a] + cards[b] + cards[c] == 15:
                score += 1

# checking combinations of 4:
for a in range(0, 2):
    for b in range(a + 1, 3):
        for c in range(b + 1, 4):
            for d in range(c + 1, 5):
                if cards[a] + cards[b] + cards[c] + cards[d] == 15:
                    score += 1

# checking combination of 5:
if sum(cards) == 15:
    score += 1

print("Total points:", score)

#Q2:
def get_moves(board, player):
    moves = []
    for i in range(9):
        if board[i] == player:
            if i == 0:
                adjacent = [1, 2, 3, 4, 5, 6, 7, 8]
            else:
                left = (i - 2) % 8 + 1
                right = i % 8 + 1
                if board[left] == player and board[right] == player:
                    continue
                adjacent = [0, left, right]
            for j in sorted(adjacent):
                if board[j] == "E":
                    moves.append((i, j))
    return moves
def make_move(board, move):
    i, j = move
    board = list(board)
    board[j] = board[i]
    board[i] = "E"
    return "".join(board)
def other_player(player):
    if player == "O":
        return "X"
    else:
        return "O"
def choose_move(board, player):
    opponent = other_player(player)
    moves = get_moves(board, player)
    for move in moves:
        new_board = make_move(board, move)
        if len(get_moves(new_board, opponent)) == 0:
            return move
    for move in moves:
        new_board = make_move(board, move)
        opponent_moves = get_moves(new_board, opponent)
        dangerous = False
        for opponent_move in opponent_moves:
            next_board = make_move(new_board, opponent_move)
            if len(get_moves(next_board, player)) == 0:
                dangerous = True
                break
        if not dangerous:
            return move
    return moves[0]
def winner(player):
    if player == "O":
        return "Player 2 wins"
    else:
        return "Player 1 wins"
board = input().strip()
current = "O"
while True:
    try:
        command = input().strip()
    except EOFError:
        break
    if command == "n":
        moves = get_moves(board, current)
        if len(moves) == 0:
            print(board)
            print(winner(current))
            break
        move = choose_move(board, current)
        board = make_move(board, move)
        current = other_player(current)
        print(board)
        if len(get_moves(board, current)) == 0:
            print(winner(current))
            break
    elif command == "r":
        seen = set()
        while True:
            state = (board, current)
            if state in seen:
                print("Draw")
                break
            seen.add(state)
            moves = get_moves(board, current)
            if len(moves) == 0:
                print(board)
                print(winner(current))
                break
            move = choose_move(board, current)
            board = make_move(board, move)
            current = other_player(current)
        break

#Q3:
#setting up the input for the string
string = input("Enter your string: \n")

#seperating the characters from the string above into a list
split_string = [char for char in string]

#input for the amount of times rules should be carried out
times = int(input("Enter the amount of times you want the rules to be performed on the string: \n"))

#input for the position (limit) of they want their string scanned to
position = int(input("Enter the position: \n"))

#the limit the question gave us
limit = 2**31

for x in range(0, times):
    new_string = []
    y = len(split_string)

    for a in range(0, y):
        if split_string[a] == "A":
            new_string.append("B")
        elif split_string[a] == "B":
            new_string.append("AB")
        elif split_string[a] == "C":
            new_string.append("CD")
        elif split_string[a] == "D":
            new_string.append("DC")
        elif split_string[a] == "E":
            new_string.append("EE")

    split_string = list("".join(new_string))

#setting up variables for counting:
A = 0
B = 0
C = 0
D = 0
E = 0

for f in range(0, min(position, len(split_string))):
    if split_string[f] == "A":
        A += 1
    if split_string[f] == "B":
        B += 1
    if split_string[f] == "C":
        C += 1
    if split_string[f] == "D":
        D += 1
    if split_string[f] == "E":
        E += 1

print(A, B, C, D, E)
