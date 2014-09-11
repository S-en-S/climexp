#!/bin/sh
#
# average a set of time series

export DIR=`pwd`
. ./getargs.cgi
. ./checkemail.cgi

NPERYEAR=$FORM_NPERYEAR
if [ $EMAIL != someone@somewhere ]; then
    echo "FORM_setoper=$FORM_setoper;" > prefs/$EMAIL.setoper.$NPERYEAR
fi
WMO=`basename "$FORM_NAME" .txt`_$FORM_setoper
STATION="$FORM_STATION"
TYPE="$FORM_type"
NAME="${FORM_setoper} $FORM_TYPE"
prog=$FORM_TYPE
if [ -n "$FORM_extraargs" ]; then
    prog=${prog}_$FORM_extraargs
fi
PROG="average_ensemble file data/$FORM_NAME $prog $FORM_setoper"

. ./getdata.cgi
