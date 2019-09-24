#!/bin/bash
if [ -z "$EOFID" ]
then
  echo '$0: cannot find EOFID'
  echo '$0: cannot find EOFID' 1>&2
  exit -1
fi
i=0
while [ `ps $EOFID | fgrep -v ' Z ' | wc -l` -gt 1 ]
do
  i=$(($i+1))
  sleep 30
  echo "Uploading $i/$1<p>"
done
