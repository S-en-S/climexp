#!/bin/sh

export DIR=`pwd`
. ./getargs.cgi

WMO="$FORM_WMO"
TYPE="$FORM_TYPE"
[ -z "$TYPE" ] && TYPE=`basename $0 .cgi | cut -b 9-10`
STATION="$FORM_STATION"
NPERYEAR=366
extraargs="$FORM_extraargs"

case $TYPE in
dd) NAME="prevailing wind direction";;
fg) NAME="daily mean windspeed";;
fh) NAME="maximum hourly windspeed";;
fn) NAME="minimum hourly windspeed";;
fx) NAME="maximum wind gust";;
tg) NAME="mean temperature";;
tn) NAME="min temperature";;
tx) NAME="max temperature";;
t1) NAME="min surface temperature";;
ng) NAME="cloud cover";;
qq) NAME="global radiation";;
sq) NAME="sunshine duration";;
sp) NAME="sunshine fraction";;
dr) NAME="precipitation duration";;
rh) NAME="precipitation";;
rd) NAME="precipitation";;
pg) NAME="mean surface pressure";;
px) NAME="maximum surface pressure";;
pn) NAME="minimum surface pressure";;
vn) NAME="minimum visibility";;
vx) NAME="maximum visibility";;
dx) NAME="zonal wind direction";;
dy) NAME="meridional wind direction";;
ug) NAME="mean relative humidity";;
un) NAME="minimum relative humidity";;
ux) NAME="maximum relative humidity";;
sc) NAME="precipitation";;
sw) NAME="global shortwave radiation";NPERYEAR=12;;
si) NAME="circulation-independent global shortwave radiation";NPERYEAR=12;;
sr) NAME="cicrulation-dependent global shortwave radiation";NPERYEAR=12;;

esac
WMO="KNMIData/$TYPE$WMO"
PROG="gunzip -c"
FROM="from <a href=\"http://www.knmi.nl/klimatologie/daggegevens/download.html\" target=\"_new\">KNMI climatological service</a>"
LASTMODIFIED=`stat $WMO.dat | fgrep Modify | cut -b 8-27`
LASTMODIFIED=`date -R -d "$LASTMODIFIED"`

. $DIR/getdata.cgi
