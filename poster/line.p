set term svg size 1680 1050
set output "line.svg"
set xtics nomirror
set ytics nomirror
set yrange [-1:1]
set xrange [0:40]
set border 3
set samples 1000
set nokey
plot cos(x)*exp(-x/30) w l lt 1 lw 3 lc rgb "blue" 
