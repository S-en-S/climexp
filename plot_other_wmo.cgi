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
eval `./bin/getunits $file`
if [ $VAR = co2 ]; then
    daily2longer $file 1 mean minfac 80 add_persist > $yearfile
else
    daily2longer $file 1 mean minfac 80 add_trend > $yearfile
fi
eval `./bin/getunits $yearfile`
plotyearfile=${yearfile%.dat}.txt
plotdat $yearfile > $plotyearfile
lowpassfile=${yearfile%.dat}_5yrlo.dat
filteryearseries lo box 5 $yearfile > $lowpassfile
pngfile=${yearfile%.dat}.png
if [ $VAR = co2 ]; then
    plotsmoth=""
else
    plotsmooth="\"$lowpassfile\" u 1:2 notitle with lines lt 4 lw 5, "
fi
if [ "${name%heat content}" != "$name" ]; then
    setxrange="set xrange [1950:]"
    setyrange="set yrange [-10:]"
fi
VAR_=`echo "$VAR" | tr '_' ' '`
UNITS_=`echo "$UNITS" | tr '_' ' ' | sed -e 's/10\^22/10^2^2/'`
gnuplot <<EOF > /tmp/gnuplot$$.log
set colors classic
set output "$pngfile"
set term png $gnuplot_png_font_hires
set datafile missing "-999.900"
set zero 1e-40
set size 0.7,0.5
set xzeroaxis
$setxrange
$setyrange
set title "$name"
set ylabel "$VAR_ [$UNITS_]"
plot $plotsmooth"$yearfile" u 1:2 notitle with lines lt 1 lw 2
EOF
echo $pngfile
exit