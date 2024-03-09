# Written by Joseph P.Vera
# 2024-03

set title "DOS (Supercell 4x4x4)"
set xlabel "Frecuency (THz)"
set ylabel "Density of States" 
   

plot 'dos_with_nac.dat' title "With NAC" with line lt -1 lw 1 lc rgb "black", \
    'dos_without_nac.dat' title "Without NAC" with line lt -1 lw 1 lc rgb "red"






















