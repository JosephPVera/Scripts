#!/usr/bin/env python
# Written by Joseph P.Vera
# 2024-03

import matplotlib  as plt
import matplotlib.pyplot as plt
import numpy as np 

print('Information:')
print('1. Plot DOS with NAC and DOS without NAC')
print('2. Plot Total DOS')
print('3. Plot BS with NAC and BS without NAC')
print('4. Plot BS (Band structure)')
print('5. Plot Projected DOS')
print('6. Plot Band structure and Projected DOS')
a = int(input('Enter selection ='))

if a == 1: 
   fig = plt.figure()
   plt.plot(*np.loadtxt("dos_with_nac.dat", unpack=True, usecols=(0,1)), 'r--', label = 'With NAC')
   plt.plot(*np.loadtxt("dos_without_nac.dat", unpack=True, usecols=(0,1)), 'black', label = 'Without NAC')
   plt.legend()
   plt.title('DOS Phonon')
   plt.xlabel('Frequency (THz)')
   plt.ylabel('Density of States')
   plt.ylim(0, 1.3)
   fig.set_size_inches(12, 8)   # (18, 10)
   plt.close(fig)
   fig.savefig('dos.png', dpi=300)
   
elif a == 2:
   fig = plt.figure()
   plt.plot(*np.loadtxt("total_dos.dat", unpack=True, usecols=(0,1)), 'r')
   plt.title('DOS Phonon')
   plt.xlabel('Frequency (THz)')
   plt.ylabel('Density of States')
   plt.ylim(0, 1.3)
   fig.set_size_inches(12, 8)   # (18, 10)
   plt.close(fig)
   fig.savefig('tdos.png', dpi=300)
   
elif a == 3:
#   fig = plt.figure()
   fig, ax = plt.subplots()
   plt.plot(*np.loadtxt("bs_with_nac.dat", unpack=True, usecols=(0,1)), 'o', markersize = 1, c = 'red', label = 'With NAC')
   plt.plot(*np.loadtxt("bs_without_nac.dat", unpack=True, usecols=(0,1)), 'o', markersize = 1, c = 'black', label = 'Without NAC')
   ax.legend()
   plt.title('Band structure Phonon')
#   plt.xlabel()
   plt.ylabel('Frequency (THz)')
   plt.xlim(0.0, 1.9395681)
   fig.set_size_inches(12, 8)   # (18, 10)
   ax.set_xticks([0.0, 0.2758371, 0.4137557, 0.5112789, 0.8038483, 1.0427303, 1.2116454, 1.3091685, 1.5042148, 1.6731299, 1.8420449, 1.9395681, ])
   ax.set_xticklabels(['$\\Gamma$','X','W', 'K', '$\\Gamma$', 'L', 'U', 'W', 'L', 'K', 'U', 'X'])
   plt.close(fig)
   fig.savefig('bst.png', dpi=300)
   
elif a == 4:
   fig, ax = plt.subplots()
   plt.plot(*np.loadtxt("bs.dat", unpack=True, usecols=(0,1)), 'o', markersize = 1, c = 'red')
   plt.title('Band structure Phonon')
   plt.ylabel('Frequency (THz)')
   plt.xlim(0.0, 1.9395681)
   fig.set_size_inches(12, 8)   # (18, 10)
   ax.set_xticks([0.0, 0.2758371, 0.4137557, 0.5112789, 0.8038483, 1.0427303, 1.2116454, 1.3091685, 1.5042148, 1.6731299, 1.8420449, 1.9395681, ])
   ax.set_xticklabels(['$\\Gamma$','X','W', 'K', '$\\Gamma$', 'L', 'U', 'W', 'L', 'K', 'U', 'X'])
   plt.close(fig)
   fig.savefig('bs.png', dpi=300)
   
elif a == 5:
   fig = plt.figure()
   plt.plot(*np.loadtxt("projected_dos.dat", unpack=True, usecols=(0,1)), 'green', label = 'B')
   plt.plot(*np.loadtxt("projected_dos.dat", unpack=True, usecols=(0,2)), 'orange', label = 'N')
   plt.legend()
   plt.title('Projected DOS Phonon')
   plt.xlabel('Frequency (THz)')
   plt.ylabel('Partial Density of States')
   plt.ylim(0, 0.7)
   fig.set_size_inches(12, 8)   # (18, 10)
   plt.close(fig)
   fig.savefig('pdos.png', dpi=300)
   
elif a == 6:
   fig, ax = plt.subplots(1, 2,figsize=(12,8), gridspec_kw={'width_ratios': [4, 1]},sharey=True)
   
   # Plot 1
   ax[0].plot(*np.loadtxt("bs.dat", unpack=True, usecols=(0,1)), 'o', markersize = 1, c = 'red', label = 'With NAC')
   #plt.plot(*np.loadtxt("bs_without_nac.dat", unpack=True, usecols=(0,1)), 'o', markersize = 1, c = 'black', label = 'Without NAC')
   ax[0].legend()
   ax[0].set_xlim(0.0, 1.9395681)
   ax[0].set_ylabel('Frequency (THz)')
   ax[0].set_xticks([0.0, 0.2758371, 0.4137557, 0.5112789, 0.8038483, 1.0427303, 1.2116454, 1.3091685, 1.5042148, 1.6731299, 1.8420449, 1.9395681, ])
   ax[0].set_xticklabels(['$\\Gamma$','X','W', 'K', '$\\Gamma$', 'L', 'U', 'W', 'L', 'K', 'U', 'X'])
   ax[0].axhline(y = 0.001, color = 'blue', linestyle = 'dashed')
   
   # Plot 2
   ax[1].plot(*np.loadtxt("projected_dos.dat", unpack=True, usecols=(1,0)), 'green', label = 'B')
   ax[1].plot(*np.loadtxt("projected_dos.dat", unpack=True, usecols=(2,0)), 'orange', label = 'N')
   ax[1].legend()
   ax[1].set_xlim(0, 0.7)
   
   # General
   fig.suptitle('Band structure and PDOS')
   plt.subplots_adjust(wspace=0.045)
   plt.close(fig)
   fig.savefig('bs_pdos.png', dpi=300)
 
else:
   print("Warning: Enter the correct value")
