#!/usr/bin/python3

def score_v1(their_move, my_move):     
    # Shift my_move to use the abc char space for easy comparison
    my_move = chr(ord(my_move) - 23)

    # Convert the character to the value of the move
    score = ord(my_move) - ord('A') + 1

    draw = (my_move == their_move)
    if draw:
        return score + 3
  
    # This could use similar logic to v2, _but_ this is more human-readable
    rock = 'A'
    paper = 'B'
    scissors = 'C'
    
    winning = (my_move == rock and their_move == scissors) or (my_move == paper and their_move == rock) or (my_move == scissors and their_move == paper)

    if winning:
        score += 6

    return score

def score_v2(their_move, outcome): 
    # Truth table for winning
    # Rock: 1 3
    # Paper: 2 1
    # Scissors: 3 2
    # This is shifting with wrap around

    # Win condition
    if outcome == 'Z':
        # Wrap around an 'array' of length 3 to determine winning position offset, add 1 for 'A' being 1, and the 6 winning constant
        win_offset = 3
        return (ord(their_move) - ord('A') + 1 + win_offset) % 3 + 1 + 6

    # Lose condition
    if outcome == 'X':
        # Wrap around an 'array' of length 3 to determine losing position offset, add 1 for 'A' being 1 and that's the score
        lose_offset = 1
        return (ord(their_move) - ord('A') + 1 + lose_offset) % 3 + 1

    # Draw condition
    if outcome == 'Y':
        # Determine the value of their/our move and add the 3 draw constant 
        return ord(their_move) - ord('A') + 1 + 3
    
    # If something is wrong
    return 0

f = open("input.txt","r")
lines = f.readlines()

total_score_v1 = 0
total_score_v2 = 0
for line in lines:
    total_score_v1 += score_v1(line[0], line[2])
    total_score_v2 += score_v2(line[0], line[2])

print("V1", total_score_v1)
print("V2", total_score_v2)



    
    