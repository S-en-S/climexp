#!/bin/sh

. ./getargs.cgi
WMO="$FORM_WMO"
STATION="$FORM_STATION"
TYPE=r
NPERYEAR=12
NAME="runoff"
export DIR=`pwd`
PROG=getrunoff
FROM="from <a href="wipefeet.cgi?http://www.rivdis.sr.unh.edu/" target="_new">RivDis v1.1 database</a>"

. $DIR/getdata.cgi
