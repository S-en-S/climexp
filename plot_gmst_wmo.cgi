#!/bin/bash
# make a WMO-compliant plot of a global eman temperature series
# to be called from scripts, output is the name of the file in the data directory.
# no visual output.
echo "Content-Type: text/plain"
echo
. ./init.cgi
. ./getargs.cgi

# expects WMO = dir/file without .dat, STATION = name of series

file=$FORM_WMO.dat
name=`echo "$FORM_STATION" | tr "_" " "`

if [ ! -s $file ]; then
    echo "$0: cannot find file $file"
    exit -1
fi
if [ -z "$name" ]; then
    echo "$0: cannot find name $name"
    exit -1
fi

yearfile=data/`basename $file .dat`_1mean_80_trend.dat
daily2longer $file 1 mean minfac 80 add_trend > $yearfile
anofile=${yearfile%.dat}_1981-2010.dat
plotdat anom 1981 2010 $yearfile | fgrep -v 'disregarding' > $anofile
reffile=${yearfile%.dat}_1850-1900.dat
# HadCRUT4 1850-1900 wrt 1961-1990: -0.31
# HadCRUT4 1981-2010 wrt 1961-1990: +0.29
# offset: 0.60
scaleseries 1:0.60 $anofile > $reffile
plotreffile=${reffile%.dat}.txt
plotdat $reffile > $plotreffile
lowpassfile=${reffile%.dat}_5yrlo.dat
filteryearseries lo box 5 $reffile > $lowpassfile
pngfile=${reffile%.dat}.png
gnuplot <<EOF > /tmp/gnuplot$$.log
set colors classic
set output "$pngfile"
set term png $gnuplot_png_font_hires
set datafile missing "-999.900"
set zero 1e-40
set size 0.7,0.5
set xzeroaxis
set title "$name"
set ylabel "Ta [Celsius]"
set yrange [-0.4:1.4]
set xrange [1850:2025]
plot "$lowpassfile" notitle with lines lt 4 lw 5, \
     "$reffile" notitle with lines lt 1 lw 2
EOF
echo $pngfile
exit