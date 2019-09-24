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
fi
[ -z "$FORM_min" ] && FORM_min=0
args="$oldlistname $FORM_min"
[ -n "$FORM_elevmin" ] && args="$args elevmin $FORM_elevmin"
[ -n "$FORM_elevmax" ] && args="$args elevmax $FORM_elevmax"
[ -n "$FORM_lon1" ] && args="$args lon1 $FORM_lon1"
[ -n "$FORM_lon2" ] && args="$args lon2 $FORM_lon2"
[ -n "$FORM_lat1" ] && args="$args lat1 $FORM_lat1"
[ -n "$FORM_lat2" ] && args="$args lat2 $FORM_lat2"
echo `date` $EMAIL "./bin/select_min_years $args" >> log/log
./bin/select_min_years $args > $listname
format=new
. ./getstations.cgi
