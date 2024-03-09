#!/usr/bin/env python
# Written by Joseph P.Vera
# 2024-03

import matplotlib  as plt
import matplotlib.pyplot as plt
import numpy as np 

print('Information:') 
print('1. Plot kdensity.dat')
print('2. Plot convergence.dat')
a = int(input('Enter selection ='))


if a == 1:
    fig = plt.figure()
    plt.plot(*np.loadtxt("kdensity.dat", unpack=True, usecols=(0,1)))
    plt.axhline(y = 0.001, color = 'r', label = 'Criteria = 0.001 eV',linestyle = 'dashed')
    plt.legend()
    plt.title('Convergence for K-density')
    plt.xlabel('K-density($\AA$)')
    plt.ylabel('|$\\Delta$ Total energy/Atoms| (eV)')
    fig.set_size_inches(12, 8)   # (18, 10)
    plt.close(fig)
    fig.savefig('kdensity.png', dpi=300)
elif a ==2:
    fig = plt.figure()
    plt.plot(*np.loadtxt("convergence.dat", unpack=True, usecols=(0,1)))
    plt.axhline(y = 0.001, color = 'r', label = 'Criteria = 0.001 eV', linestyle = 'dashed')
    plt.legend()
    plt.title('Convergence for Energy cutoff')
    plt.xlabel('Cutoff energy (eV)')
    plt.ylabel('|$\\Delta$ Total energy/Atoms| (eV)')
    fig.set_size_inches(12, 8)   # (18, 10)
    plt.close(fig)
    fig.savefig('convergence.png', dpi=300)    
else:
   print("Warning: Enter the correct value")
