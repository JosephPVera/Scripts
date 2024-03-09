#!/usr/bin/env python
# Written by Joseph P.Vera
# 2024-03

import ase.io.vasp
from ase.io import read
from ase.visualize import view

print('Introduce the values:')
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if (a < 100 and b < 100 and c < 100):
   cell = ase.io.vasp.read_vasp("POSCAR")
   ase.io.vasp.write_vasp("POSCAR_new",cell*(a,b,c), label='supercell',direct=True,sort=True)
   supercell = read("POSCAR_new")
   view(supercell)
else:
    print("Warning: Enter the correct values")
