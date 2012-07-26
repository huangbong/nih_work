set term postscript enhanced color
set output "64.ps"
set multiplot
set xtics nomirror
set ytics nomirror
set border 3
plot [0:64] [0:64] "64points.dat" using 1:2 title '' with points pt 6 ps 1 lt 7
plot [0:64] [0:64] "nuspoints.dat" using 1:2 title '' with points pt 7 ps 1 lt 1