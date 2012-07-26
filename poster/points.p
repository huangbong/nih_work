set term svg enhanced size 1680 1050
set output "points.svg"
set xtics nomirror
set ytics nomirror
set yrange [-1:1]
set xrange [0:40]
set border 3
set nokey
plot "y.dat" using 1:2 with points pt 7 ps 1.5 lc rgb "black"
