#!/bin/python3
import math
# Take user input for name, age, and degree program

name = input("What is your name? ")
age = int(input("What is your age? "))
degree_program = input("What is your degree program? ")

#calculate remaining age
remainder = math.fmod((int(age)*3),2)
#Calculate remaing age
#remainder =int(age) * 3 % 2

# Print message with name, remaining age, and degree program
print("My name is: " +name +", remaining age is: " +str(remainder)+ " and degree program: " +degree_program)

