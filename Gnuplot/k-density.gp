# Written by Joseph P.Vera

set title "c-BN (Primitive cell)"
set xlabel "K-density (A)"
set ylabel "Total energy/Atoms (eV)" 

plot 'kdensity.dat' using 1:2 w lp pt 8 title 'k-density', 0.001 title 'Criteria = 0.001 eV'
























