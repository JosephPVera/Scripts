#!/usr/bin/env python
# Written by Joseph P.Vera
# 2024-03

from ase.io import read
from ase.visualize import view

print('Information:') 
print('1. Read POSCAR')
print('2. Read CONTCAR')
a = int(input('Enter selection ='))

if a == 1:
   atoms = read('POSCAR')
   view(atoms)
elif a == 2:
   atoms = read('CONTCAR')
   view(atoms)
else:
   print("Warning: Enter the correct value")
