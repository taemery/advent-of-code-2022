#!/usr/bin/python3

f = open("input.txt","r")
lines = f.readlines()

# Empty stacks to load data into
stacks_v1 = [[] for x in range(0, 9)]
stacks_v2 = [[] for x in range(0, 9)]

for line in lines:
    if("[" in line):
        # Split into groups of 4 characters, and only grab the 2nd character of that group
        crateContents = [line[i+1:i+2] for i in range(0, len(line), 4)]
        for idx, char in enumerate(crateContents):
            if(char != " "):
                stacks_v1[idx].insert(0, char)
                stacks_v2[idx].insert(0, char)
    elif("move" in line):
        split_line = line.split(" ")
        
        num_to_move = int(split_line[1].strip())
        # -1 as arrays start at 0
        src = int(split_line[3].strip()) - 1
        dest = int(split_line[5].strip()) - 1

        # V1 Logic, moving each crate individually
        for x in range(0, int(num_to_move)):
            stacks_v1[dest].append(stacks_v1[src].pop())

        # V2 Logic, moving crates as groups
        crates_to_move = stacks_v2[src][-num_to_move:]
        leftover_crates = stacks_v2[src][:-num_to_move]
        
        stacks_v2[src] = leftover_crates
        stacks_v2[dest].extend(crates_to_move)

v1_output = ''
for stack in stacks_v1:
    v1_output += stack[-1]
print('V1:', v1_output)

v2_output = ''
for stack in stacks_v2:
    v2_output += stack[-1]
print('V2:', v2_output)

        
