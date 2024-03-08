#!/usr/bin/env python
# Written by Joseph P.Vera

from ase.io import read
from ase.visualize import view

print('Information: 1. Read POSCAR // 2. Read CONTCAR')
a = int(input("a = "))

if a == 1:
   atoms = read('POSCAR')
   view(atoms)
elif a == 2:
   atoms = read('CONTCAR')
   view(atoms)
else:
   print("Warning: Enter the correct value")
