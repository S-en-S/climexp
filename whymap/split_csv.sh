#!/bin/sh
csvfile="$1"
if [ -z "$csvfile" ]; then
    echo "usage: $0 csvfile"
    exit -1
fi
aquifers=`tail -n +2 "$csvfile" | cut -d , -f 11 | sed -e 's/ /_/g' | uniq`
for aquifer in $aquifers; do
    txtfile=$aquifer.txt
    aquifer_=`echo "$aquifer" | tr '_' ' '`
    echo "# $aquifer_ from http://www.whymap.org/" > $txtfile
    fgrep "$aquifer_" "$csvfile" | cut -d , -f 20-21 | tr ',' ' ' >> $txtfile
done