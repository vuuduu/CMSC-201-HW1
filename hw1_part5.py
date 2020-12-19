"""
File:          hw1_part5.py
Author         Vu Nguyen
Date:          9/10/2020
Section:       31
Description:   This program calculate the energy contained in an object, by
               asking the user for its mass and velocity.
"""
import math


def energy():
    c = 299792458  # speed of light
    m = float(input("Enter the rest mass in kg: "))  # the rest mass
    v = float(input("Enter the velocity in m/s: "))  # velocity

    e = (m * pow(c, 2))/(math.sqrt(1-(pow(v, 2)/pow(c, 2))))

    print("The Lorentz Energy in the object of rest mass", m, "and velocity",
          v, "is", e)


energy()
