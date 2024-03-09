# Written by Joseph P.Vera
# 2024-03

set title "Thermal properties"
set xlabel "Temperature (K)"
set key left top
   

plot 'thermal.dat' using 1:2 title "Helmholtz Free energy (kJ/mol)" with line lt -1 lw 1 lc rgb "black", \
    'thermal.dat' using 1:3 title "Entropy (J/K.mol)" with line lt -1 lw 1 lc rgb "red", \
    'thermal.dat' using 1:4 title "Heat Capacity C_{v} (J/K.mol)" with line lt -1 lw 1 lc rgb "orange", \
    'thermal.dat' using 1:5 title "Energy (kJ/mol)" with line lt -1 lw 1 lc rgb "green"






















