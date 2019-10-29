#!/bin/bash
. ./httpheaders_nocache.cgi
. ./init.cgi
. ./getargs.cgi

. ./queryfield.cgi
if [ -z "$file" ]; then
    . ./myvinkhead.cgi "Please select a field"
    echo "On the previous page"
    . ./myvinkfoot.cgi
    exit
fi
if [ "$FORM_minmax" != min -a "$FORM_minmax" != max ]; then
    . ./myvinkhead.cgi "Please select min or max"
    echo "On the previous page"
    . ./myvinkfoot.cgi
elif [ $FORM_minmax = min ]; then
    npernew="-1"
else
    npernew=1
fi
if [ "$EMAIL" = ec8907341dfc63c526d08e36d06b7ed8 ]; then
    lwrite=false
fi


. ./nosearchengine.cgi
. ./myvinkhead.cgi "Area with extremes" "$kindname $climfield" "noindex,nofollow"

eval `./bin/getunits $file`
if [ ! -s $file ]; then
    echo "$0: error: download https://climexp.knmi.nl/BerkeleyData/$file"
    exit -1
fi

ave=$FORM_ave
yrfile=data/yr${ave}_$FORM_field.nc
if [ ! -s $yrfile -o $yrfile -ot $file ]; then
    echo -n "Computing annual $FORM_minmax"
    if [ -z "$ave" ]; then
        echo "..."
    else
        echo "averaging over $ave days ..."
    fi
    if [ -n "$ave" ]; then
        (daily2longerfield $file $npernew $FORM_minmax ave $ave $yrfile) 2>&1
    else
        (daily2longerfield $file $npernew $FORM_minmax $yrfile) 2>&1
    fi
fi
for ref in late # early
do
    case $ref in
        early) begin=1901;end=1950;;
        late)  begin=1951;end=1980;;
    esac
    t10file=data/t10_`basename $yrfile .nc`_${begin}-${end}.nc
    if [ ! -s $t10file -o $t10file -ot $yrfile ]; then
        echo "Computing 10-yr return values ..."
        gevfile=data/gev_`basename $yrfile .nc`_${begin}-${end}.nc
        [ -f $gevfile ] && rm $gevfile
        (getmomentsfield $yrfile gev begin $begin end $end changesign $gevfile) 2>&1
        [ -f $t10file ] && rm $t10file
        (ncks -v t10 $gevfile $t10file) 2>&1
    fi
    echo "Computing area with extremes ..."
    gtfile=data/gt_${t10file#data/}
    if [ ! -s $gtfile -o $gtfile -ot $t10file ]; then
        [ -f $gtfile ] && rm $gtfile
        (cdo lt $yrfile $t10file $gtfile) 2>&1 | sed -e 's/$/<br>/'
    fi
    euseries=data/eu_`basename $gtfile .nc`.dat
    if [ ! -s $euseries -o $euseries -ot $gtfile ]; then
        [ -f $euseries ] && rm $euseries
        (get_index $gtfile -15 40 35 72 > $euseries) 2>&1
    fi
    naseries=data/na_`basename $gtfile .nc`.dat
    if [ ! -s $naseries -o $naseries -ot $gtfile ]; then
        [ -f $naseries ] && rm $naseries
        (get_index $gtfile -130 -50 25 50 > $naseries) 2>&1
    fi
    nmseries=data/nm_`basename $gtfile .nc`.dat
    if [ ! -s $nmseries -o $nmseries -ot $gtfile ]; then
        [ -f $nmseries ] && rm $nmseries
        (get_index $gtfile -180 180 30 60 > $nmseries) 2>&1
    fi
done
echo "<a href=getindices.cgi?id=$EMAIL&WMO=${nmseries%.dat}>Northern midlatitudes (30&deg;-60&deg;N)</a>,<br>"
echo "<a href=getindices.cgi?id=$EMAIL&WMO=${naseries%.dat}>North America (25-50&deg;N, 50-130&deg;W)</a>,<br>"
echo "<a href=getindices.cgi?id=$EMAIL&WMO=${naseries%.dat}>Europe (35-72&deg;N, 15&deg;W-40&deg;E)</a>.<br>"

echo "See van Oldenborgh et al, ERL, 2019 for the details."
FORM_field=""
. ./myvinkfoot.cgi

