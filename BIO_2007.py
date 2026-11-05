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
