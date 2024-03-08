# Written by Joseph P.Vera

set title "c-BN (Primitive cell)"
set xlabel "Cutoff energy (eV)"
set ylabel "Total energy/Atoms (eV)" 

set label 1 "convergence" at 700,0.05
set arrow 1 from 715,0.04 to 701,0.008

plot 'convergence.dat' using 1:2 w lp pt 8 title 'Ecutoff', 0.001 title 'Criteria = 0.001 eV'























