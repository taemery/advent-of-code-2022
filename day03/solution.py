#!/usr/bin/python3
import functools

f = open("input.txt","r")
lines = f.readlines()

part_1_total = 0

lines_read = 0
all_lines_in_group = []
part_2_total = 0

def priority(character):
    # Convert lowercase to correct int. lowercase is greater than uppercase in unicode
    if(character >= 'a'):
        # Reduce unicode to an a, then make a a 1
        return ord(character) - ord('a') + 1
    else:
        # Reduce unicode to an A, then make A a 1, then increase by 26 for weighting
        return ord(character) - ord('A') + 26 + 1

for line in lines:
    # Part 1
    split = len(line) // 2
    front, back = line[:split], line[split:]
    matches = set(front) & set(back)
    for item in matches:
        part_1_total += priority(item[0])
        
    # Part 2
    # Remove last char (newline) and add to list
    all_lines_in_group.append(line[:-1])
    lines_read += 1
    
    # If we're on the third line, determine matches
    if(lines_read == 3):
        matches = set(all_lines_in_group[0]) & set(all_lines_in_group[1]) & set(all_lines_in_group[2])
        part_2_total += priority(list(matches)[0])

        # Reset for next row
        lines_read = 0
        all_lines_in_group = []


print('Part 1:', part_1_total)
print('Part 2:', part_2_total)

