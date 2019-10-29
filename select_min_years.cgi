#!/bin/bash
. ./init.cgi
. ./getargs.cgi
export DIR=`pwd`

FORM_climate="$FORM_TYPE"
FORM_email="$EMAIL" #...
FORM_EMAIL="$EMAIL" #...
prog="$FORM_WMO"
listname=data/`basename "$FORM_NAME"`
listname=`echo "$listname" | tr -d '\\'` # I get spurious backslashes...
oldlistname=$listname
listname=${listname%.txt}_min_${FORM_min}.txt
NPERYEAR=$FORM_NPERYEAR
if [ $EMAIL != someone@somewhere ]; then
    echo "FORM_min=$FORM_min;" > prefs/$EMAIL.minnumyears
    echo "FORM_elevmin=$FORM_elevmin;" >> prefs/$EMAIL.minnumyears
    echo "FORM_elevmin=$FORM_elevmin;" >> prefs/$EMAIL.minnumyears
    echo "FORM_lon1=$FORM_lon1;" >> prefs/$EMAIL.minnumyears
    echo "FORM_lon2=$FORM_lon2;" >> prefs/$EMAIL.minnumyears
    echo "FORM_lat1=$FORM_lat1;" >> prefs/$EMAIL.minnumyears
    echo "FORM_lat2=$FORM_lat2;" >> prefs/$EMAIL.minnumyears
    echo "FORM_coast=$FORM_coast;" >> prefs/$EMAIL.minnumyears
fi
[ -z "$FORM_min" ] && FORM_min=0
args="$oldlistname $FORM_min"
if [ -n "$FORM_coast" -a "$FORM_coast" != all ]; then
    case $FORM_coast in
        coast) args="$args mask countries/Netherlands_coastal.txt"
            listname=${listname%.txt}_mask_Netherlands_coastal.txt
            FORM_climate="coastal $FORM_climate";;
        inland) args="$args mask countries/Netherlands_inland.txt"
            listname=${listname%.txt}_mask_Netherlands_inland.txt
            FORM_climate="inland $FORM_climate";;
    esac
fi
if [ -n "$FORM_elevmin" ]; then
    args="$args elevmin $FORM_elevmin"
    listname=${listname%.txt}_elevmin_${FORM_elevmin}.txt
fi
if [ -n "$FORM_elevmax" ]; then
    args="$args elevmax $FORM_elevmax"
    listname=${listname%.txt}_elevmax_${FORM_elevmax}.txt
fi
if [ -n "$FORM_lon1" ]; then
    args="$args lon1 $FORM_lon1"
    listname=${listname%.txt}_lon1_${FORM_lon1}.txt
fi
if [ -n "$FORM_lon2" ]; then
    args="$args lon2 $FORM_lon2"
    listname=${listname%.txt}_lon2_${FORM_lon2}.txt
fi
if [ -n "$FORM_lat1" ]; then
    args="$args lat1 $FORM_lat1"
    listname=${listname%.txt}_lat1_${FORM_lat1}.txt
fi
if [ -n "$FORM_lat2" ]; then
    args="$args lat2 $FORM_lat2"
    listname=${listname%.txt}_lat2_${FORM_lat2}.txt
fi
echo `date` $EMAIL "./bin/select_min_years $args" >> log/log
./bin/select_min_years $args > $listname
format=new
. ./getstations.cgi
