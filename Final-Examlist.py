#!/bin/python3
# take user input and store in examList
examList = []
for i in range(10):
    num = int(input("Enter an integer: "))
    examList.append(num)
print("examList:", examList)
# calculate total and average
total = sum(examList)
print("Total:", total)
average = total / len(examList)
print("Average:", average)
# search for highest value

highest = max(examList)
print("Highest value:", highest)

# sort the list

examList.sort()
print("Sorted examList:", examList)

# print results
#print("examList:", examList)
# create a two-dimensional list

examListTwo = []
for i in range(3):
    innerList = []
    for j in range(4):
        num = int(input("Enter an integer: "))
        innerList.append(num)
    examListTwo.append(innerList)
print("examListTwo:", examListTwo)

# define function to sum list values

def listSum(lst):
    total = 0
    for innerList in lst:
        for num in innerList:
            total += num
    return total

# call listSum function on examListTwo

listTotal = listSum(examListTwo)
print("Two dimensional list: ")
for innerList in examListTwo:
    print(innerList)
print("Total value for the list: ", listTotal)

