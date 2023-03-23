#!/bin/python3

#Taking user input for name, age, and degree program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
degree_program = input("Enter your degree program: ")

# Calculating the remaining aGE
remaining_age = (age * 3)/2


#Printing the message with string concatenation
print(str("Hello, my name is " + name + ". My remainining age " + remaining_age + " years. My degree program is " + degree_program)) 
