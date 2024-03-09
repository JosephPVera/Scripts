# Written by Joseph P.Vera
# 2024-03

set title "Band structure (Supercell 4x4x4)"
set xlabel "k-points"
set ylabel "Frecuency (THz)" 
   
set xtics ("{/Symbol G}" 0.0, "X" 0.2758371, "W" 0.4137557,"K" 0.5112789,"{/Symbol G}" 0.8038483, "L" 1.0427303,"U" 1.2116454, "W" 1.3091685,"L" 1.5042148,"K" 1.6731299,"U" 1.8420449,"X" 1.9395681)

plot 'bs_with_nac.dat' title "With NAC"ls 0.5 lc rgb "black" lw 2, \
    'bs_without_nac.dat' title "Without NAC" with line lt -1 lw 1 lc rgb "red", 0.0 title "Fermi Energy"






















