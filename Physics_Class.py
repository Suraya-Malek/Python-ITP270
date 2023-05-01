#!/bin/python3
train_mass = 22680; train_acceleration = 10; train_distance = 100
bomb_mass = 1

#Implementation of the f_to_c function:
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

#the function with an input of 100 Fahrenheit:

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#the implementation of the c_to_f function:

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp
#test the function with an input of 0 Celsius:

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)
#get_force function:

def get_force(mass, acceleration):
    return mass * acceleration
# 6 function with the given variables:
train_force = get_force(train_mass, train_acceleration)
print(train_force)
#7 the final string:

print("The GE train supplies " + str(train_force) + " Newtons of force.")
#8 get_energy function:
def get_energy(mass, c=3*10**8):
    return mass * c**2
#9 given variable:
bomb_energy = get_energy(bomb_mass)
#print(bomb_energy)

#10 given variable:

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#11 given variable:

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work
#13 the given variables:

train_work = get_work(train_mass, train_acceleration, train_distance)
#print(train_work)
#final string:
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
