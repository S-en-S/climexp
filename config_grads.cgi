#!/bin/bash
grads=grads
config=`$grads -b -l -c quit| fgrep Config`
gradsver=`echo $config | cut -f 2 -d ' '`
c=`echo $config | fgrep -c v2.`
[ -z "$FORM_mapformat" ] && FORM_mapformat=png
if [ ${gradsver#v2.2} != $gradsver ]; then
	grads20=true
	gxprint=gxprint
	gxprintoptions=white
elif [ ${gradsver#v2.1} != $gradsver ]; then
	grads20=true
	gxprint=gxprint
	gxprintoptions=white
elif [ ${gradsver#v2.0} != $gradsver ]; then
	grads20=true
	gxprint=print
else
	if [ "$FORM_mapformat" = geotiff ]; then
		echo "geotiff export is not supported by GrADS 1.8"
		exit
	fi
fi
[ "$lwrite" = true ] && echo "gradsver=$gradsver, grads20=$grads20, gxprint=$gxprint<br>"