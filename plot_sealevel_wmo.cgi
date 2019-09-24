#!/bin/bash
# make a WMO-compliant plot of a global mean sealevel series
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
plotyearfile=${yearfile%.dat}.txt
plotdat $yearfile > $plotyearfile
lowpassfile=${yearfile%.dat}_5yrlo.dat
filteryearseries lo box 5 $yearfile > $lowpassfile
pngfile=${yearfile%.dat}.png
gnuplot <<EOF > /tmp/gnuplot$$.log
set colors classic
set output "$pngfile"
set term png $gnuplot_png_font_hires
set datafile missing "-999.900"
set zero 1e-40
set size 0.7,0.5
set xzeroaxis
set title "$name"
set ylabel "sea level anomaly [mm]"
plot "$lowpassfile" u 1:(1000*\$2) notitle with lines lt 4 lw 5, \
     "$yearfile" u 1:(1000*\$2) notitle with lines lt 1 lw 2
EOF
echo $pngfile
exit