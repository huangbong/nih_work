set term svg enhanced size 1680 1050
set output "both.svg"
set xtics nomirror
set ytics nomirror
set yrange [-1:1]
set xrange [0:40]
set border 3
set samples 1000
set nokey
set multiplot
plot cos(x)*exp(-x/30) w l lt 1 lw 3 lc rgb "blue"
plot "y.dat" using 1:2 with points pt 7 ps 1.5 lc rgb "black"
unset multiplot
