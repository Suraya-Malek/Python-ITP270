#!/bin/python3
#Create a dictionary named "rabbitHole" with key 1 and value [1,2,3,4,5]

rabbitHole = {1: [1,2,3,4,5]}

#Create another dictionary named "looper" with key "a" and value "rabbitHole"

looper = {"a": rabbitHole}

#Print the value of key "5" in "looper" dictionary

print("The looper integer: ")
print(looper["a"][1][-1])
