#!/usr/bin/python3

f = open("input.txt","r")
lines = f.readlines()

elfs = []
currentElf = 0

for line in lines:
    # If new line, complete the elf object
    if(len(line) == 1 and line[0] == '\n'):
        elfs.append(currentElf)
        currentElf = 0
    # otherwise add to the current elf
    else:
        currentElf += int(line)

# Given that there is not a newline at the end of the file, we must be sure to track the last elf
elfs.append(currentElf)

# Sort to put the largest sum at the end
elfs.sort()
print('The elf with the most calories has', elfs[-1])
print('The sum of the top 3 elves with calories is', elfs[-1] + elfs[-2] + elfs[-3])