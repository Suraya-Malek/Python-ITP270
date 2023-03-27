#!/bin/python3
# !/bin/python3



print("I have information for the following planets: ")

print(" 1. Venus 2. Mars  3. Jupiter")

print(" 4. Saturn 5. Uranus 6. Neptune\n")



weight = 185



Num = input("Please enter planet number: ")

planetNum =int(Num)



# Calculate weight on destination planet

if planetNum == 1:

    weight *= 0.91

    print("Your destination planet is Venus and weight is: ", weight)

elif planetNum == 2:

    weight *= 0.38

    print("Your destination planet is Mars and weight is: ", weight)

elif planetNum == 3:

    weight *= 2.34

    print("Your destination planet is Jupiter and weight is: ", weight)

elif planetNum == 4:

    weight *= 1.06

    print("Your destination planet is Saturn and weight is: ", weight)

elif planetNum == 5:

    weight *= 0.96

    print("Your destination planet is Uranus and weight is: ", weight)

elif planetNum == 6:

    weight *= 1.19

    print("Your destination planet is Neptune and weight is: ", weight)

else:

    print("Invalid planet number. Please select a number  between 1 and 6.")

