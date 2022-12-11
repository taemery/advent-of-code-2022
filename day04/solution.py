#!/usr/bin/python3

f = open("input.txt","r")
lines = f.readlines()

fully_contained_count = 0
overlapping_count = 0
for line in lines:
    # Cut off \n and split the ranges
    assignment_strings = line[:-1].split(',')
    assignments = []
    # Get the actual numbers
    for assignment in assignment_strings:
        assignments.append([int(r) for r in assignment.split("-")])
    
    # Run this twice, to see if one is contained in another, and vice versa
    for first_id in range(0, 2):
        second_id = (first_id + 1) % 2

        if(assignments[first_id][0] <= assignments[second_id][0] and assignments[first_id][1] >= assignments[second_id][1]):
            fully_contained_count += 1
            # If we found one, we don't need to check the other direction
            break

    for first_id in range(0, 2):
        second_id = (first_id + 1) % 2

        if(assignments[second_id][1] >= assignments[first_id][1] >= assignments[second_id][0]):
            overlapping_count += 1
            # If we found one, we don't need to check the other direction
            break


print('Assignments fully contained within another', fully_contained_count)
print('Assignments overlapping', overlapping_count)
