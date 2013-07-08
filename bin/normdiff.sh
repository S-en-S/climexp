#!/bin/sh
if [ -z "$DIR" ]; then
  DIR=`pwd`
fi
PROG=`basename $0 .sh`
file1=$1
file2=$2
c1=`echo $file1 | egrep -c '%%|\+\+'`
c2=`echo $file2 | egrep -c '%%|\+\+'`
if [ $c1 -eq 0 -a $c2 -eq 0 ]; then
  # both are regular indices
  $DIR/bin/$PROG $*
elif [ $c1 -ne 0 -a $c2 -ne 0 ]; then
  # both are ensembles
  i=0
  ii=00
  ensfile1=`echo $file1 | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
  ensfile2=`echo $file2 | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
  while [ -f $ensfile1 -a -f $ensfile2 ]
  do
    ensargs="$ensfile1 $ensfile2 $3 $4"
    ensout=`echo data/$TYPE$WMO.dat | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
    $DIR/bin/$PROG $ensargs > $ensout
    echo "# $ensout"
    i=$(($i + 1))
    ii=`printf %02i $i`
    ensfile1=`echo $file1 | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
    ensfile2=`echo $file2 | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
  done
elif [ $c1 -ne 0 ]; then
  # the first one is an ensemble
  i=0
  ii=00
  ensfile1=`echo $file1 | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
  while [ -f $ensfile1 -a -f $file2 ]
  do
    ensargs="$ensfile1 $file2 $3 $4"
    ensout=`echo data/$TYPE$WMO.dat | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
    $DIR/bin/$PROG $ensargs > $ensout
    echo "# $ensout"
    i=$(($i + 1))
    ii=`printf %02i $i`
    ensfile1=`echo $file1 | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
  done
elif [ $c2 -ne 0 ]; then
  # the second one is an ensemble
  i=0
  ii=00
  ensfile2=`echo $file2 | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
  while [ -f $file1 -a -f $ensfile2 ]
  do
    ensargs="$file1 $ensfile2 $3 $4"
    ensout=`echo data/$TYPE$WMO.dat | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
    $DIR/bin/$PROG $ensargs > $ensout
    echo "# $ensout"
    i=$(($i + 1))
    ii=`printf %02i $i`
    ensfile2=`echo $file2 | sed -e "s:\+\+:$ii:" -e "s:\%\%:$ii:"`
  done
else
  echo "Nonsense"
fi
