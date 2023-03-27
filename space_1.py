#!/bin/python3
# Surface gravity of various bodies of the solar system taken from wikipedia

# general data for VARIANT 1 and VARIANT 2

planet_dict_g = {'Mercury': 0.377,

                 'Venus': 0.905,

                 'Mars': 0.379,

                 'Jupiter': 2.528,

                 'Saturn': 1.065,

                 'Uranium': 0.886,

                 'Neptune': 1.137,

                 'Pluto': 0.063,

                 'Moon': 0.165,

                 'Sun': 28.02}



# VARIANT 1

# If the weight needs to be shown only for the selected planet

weight_earth = float(input('What is your weight on Earth?(only number in kg) '))

print('Which planet are you visiting?')

planet = input('(Mercury, Venus, Mars, Jupiter, Saturn, Uranium, Neptune, Pluto, Moon, Sun):').capitalize()



if planet_dict_g.get(planet):

    print(f'Your weight on the {planet} is {round(weight_earth * planet_dict_g.get(planet), 2)} kg')

else:

    print(f'Wrong name of planet')

# end VARIANT 1



# VARIANT 2

# If the weight needs to be shown for all planets

weight_earth = float(input('What is your weight on Earth?(only number in kg) '))

for key in planet_dict_g:

    print(f'Your weight on the {key} is {round(weight_earth * planet_dict_g[key], 2)} kg')

# end VARIANT 2
