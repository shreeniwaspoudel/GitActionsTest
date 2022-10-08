# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 13:38:23 2022

@author: ShreeniwasSharma-Pou
"""

print("It just worked")

f = open("demofile.txt", "r+")

number = f.readlines()[-1]

number = int(number)

number += 1

f.writelines(str(number) + "\n")

f.close()

