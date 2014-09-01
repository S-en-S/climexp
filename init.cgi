#!/bin/sh
# various environment variables that come in useful later on
# plus a check on the state of the server
if [ -z "$init_done" ]; then

   line=`uptime`
   load=${line##*averages: } # Mac OSX
   load=${load##*average: }  # linux
   load=${load%%.*}
###   if [ $EMAIL = oldenbor@knmi.nl ]; then
###       echo "load=$load<br>"
###   fi
   if [ ${load:-0} -gt 20 -a `uname` != Darwin ]; then
       echo 
       echo "Server too busy (load $load &gt; 20), try again later"
       exit
   fi

   init_done=done

	function getpngwidth {
		width=`file $pngfile | sed -e 's/^.*data, //' -e 's/ x .*$//'`
		halfwidth=$((width/2))
		if [ $((2*halfwidth )) != $width ]; then
			halfwidth=${halfwidth}.5
		fi
	}
   # set a standard TTF font for gnuplot.   GNUPLOT_DEFAULT_GDFONT is not used
   # if all is well, but is there as a fall-back.
   export GDFONTPATH=`pwd`/truetype
   export GNUPLOT_DEFAULT_GDFONT="DejaVuSansCondensed"
   export gnuplot_png_font_hires="size 1280,960 crop font DejaVuSansCondensed 15"
   export gnuplot_png_font="size 640,480 crop font DejaVuSansCondensed 8.5"
   # R libraries
   export R_LIBS=`pwd`/rpacks
   # netcdf libraries on bhlclim, bvlclim - hard-coded
   export LD_LIBRARY_PATH=/home/oldenbor/lib:/usr/local/free/lib:$LD_LIBRARY_PATH
   # for a few routines this seems needed
   export PATH=./bin:/sw/bin:/usr/local/bin:/usr/local/free/bin:$PATH
   # finally, avoid commas instead of decimal points :-(
   export LANG=C
fi
