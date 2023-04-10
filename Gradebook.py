#!/bin/python3
last_semester_gradebook = [["Biology",93], ["Algebra",98], ["Art History",91], ["choir",92]]
# 1.Create a list called subjects

subjects = ["Physics","Calculus","Poetry","History"]
#2.Create a list called  grades

grades = [98,97,85,88]
#3.Create a two-dimensional list

gradebook =[["Physics",98],["Calculus",97],["Poetry",85],["History",88]]
#4.Print gradebook

print(gradebook)
#5.Add a new subject and grade to gradebook
#gradebook.append("computer science")

gradebook.append(["computer science",100])
#6.Add another subject and grade to gradebook

gradebook.append(["Visuat Arts",93])
print(gradebook)
#7.Modify the grade for Visual arts

gradebook[5]=["Visual Arts", 98]
print(gradebook)
#8.Remove the grade for Poetry

gradebook[2].remove(85)
print(gradebook)
#9.Add a new pass/fail value for Poetry

gradebook[2].append("Pass")
print(gradebook)
#10.Combine last semester's gradebook with current gradebook

full_gradebook=last_semester_gradebook+gradebook
print(full_gradebook)
