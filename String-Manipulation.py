#!/bin/python3
#Part 1
#Ask for user's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

#Check if "Tom" is present in the name and find the starting position

if "Tom" in first_name + last_name:
    start_pos = (first_name + last_name).index("Tom")
    print("The starting position of 'Tom' is:", start_pos)

#Replace last name with "Johnson"

last_name = "Johnson"

#Display user name in reverse order, separated with a comma

print("User name in reverse order:", last_name + ", " + first_name)
