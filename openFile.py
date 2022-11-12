# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 13:38:23 2022

@author: ShreeniwasSharma-Pou
"""

from SecondCode import dummy_function

print("It just worked")
dummy_function()

f = open("demofile.txt", "r+")

number = f.readlines()[-1]

number = int(number)

number += 1

print(number)

f.writelines(str(number) + "\n")

f.close()

filename = str(number) + ".txt"

with open(filename, 'x') as f:
    f.write('Create a new text file!')

f.close()
