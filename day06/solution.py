#!/usr/bin/python3

f = open("input.txt","r")
lines = f.readlines()

transmission_memory = list(lines[0][:4])
message_memory = list(lines[0][:14])

start_transmission = 0
start_message = 0

for i in range(4,len(lines[0])):
    if(start_transmission == 0):
        if(len(set(transmission_memory)) == 4):
            start_transmission = i
        transmission_memory.pop(0)
        transmission_memory.append(lines[0][i])

    if(start_message == 0 and i > 14):
        if(len(set(message_memory)) == 14):
            start_message = i
        message_memory.pop(0)
        message_memory.append(lines[0][i])

print("Start Transmission", start_transmission)
print("Start Message", start_message)