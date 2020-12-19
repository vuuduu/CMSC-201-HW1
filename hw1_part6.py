"""
File:          hw1_part6.py
Author:        Vu Nguyen
Date:          9/10/2020
Section:       31
Description:   This program asks the user for the mass of the two objects
               and the distance between the two in order to calculate the
               force between the two gravitational bodies.
"""


def gravity():
    g = 6.674 * pow(10, -11)
    mass_uno = float(input("What is the mass of object 1, in kg: "))
    mass_dos = float(input("What is the mass of object 2, in kg: "))
    distance = float(input("What is the distance between the two object: "))
    force = (g * pow(mass_uno, 2) * pow(mass_dos, 2))/pow(distance, 2)
    print("The gravitational force between the two objects is: ", force)


gravity()
