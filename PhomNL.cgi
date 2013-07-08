#!/bin/sh
echo 'Content-Type: text/html'
echo
echo

. ./getargs.cgi

. ./searchengine.cgi

DIR=`pwd`
base_url=`dirname $SCRIPT_NAME`

. ./myvinkhead.cgi "Daily precipitation in the Netherlands" "Homogenised and raw data" "index,follow"
cat <<EOF
<table class="realtable" width=451 border=0 cellspacing=0 cellpadding=0>
<tr><th colspan="2">Select a set of time series by clicking on the name
<tr>
<td><div class="kalelink"><a href="getindices.cgi?WMO=KNMIData/precip13stations&STATION=Nederland&TYPE=p&id=$EMAIL&NPERYEAR=366">Average precipitation on 13 dutch stations</a> (1906-now, KNMI)<br>
An average of 13 relatively homogenous stations with 8-8 observations, uncorrected.</div>
<td><a href="http://www.knmi.nl/klimatologie/daggegevens/nsl-download.cgi?language=eng" target="_new"><img src="images/info-i.gif" alt="more information" border="0"></a>
<tr>
<td><div class="kalelink"><a href="getdutchstations.cgi?id=$EMAIL&TYPE=precip_hom_1910-2009">102 homogenised stations 1910-2009</a> (<a href="getdutchstations.cgi?id=$EMAIL&TYPE=precip_raw_1910-2009">raw</a>),<br><a href="getdutchstations.cgi?id=$EMAIL&TYPE=precip_hom_1951-2009">240 homogenised stations 1951-2009</a> (<a href="getdutchstations.cgi?id=$EMAIL&TYPE=precip_raw_1951-2009">raw</a>)<br>
The raw data are from the 8-8 observational network, the day is the day of the observation, most rain fell on the previous day. The homogenised set has been corrected statistically for breaks in the monthly sum in comparisons with neighbouring stations. The lowering of the observation height from 1.5m to 0.4m around 1950 has not been corrected for. This reduced the undercatch by about 3% but the correction depends strongly on the location and weather.
<td><a href="http://www.knmi.nl/publicaties/showAbstract.php?id=8714" target="_new"><img src="images/info-i.gif" alt="more information" border="0"></a>
<tr>
<td><div class="kalelink"><a href="getdutchstations.cgi?id=$EMAIL&TYPE=rh">Precipitation (0-24)</a><br>
These observations are from automatic rain gauges, which on average records about 5% less rain than the manual rain gauges of the 8-8 network.<td><a
href="http://www.knmi.nl/klimatologie/daggegevens/download.cgi?language=eng"><img src="images/info-i.gif" alt="more information" border="0"></a>
</table>
EOF

. ./myvinkfoot.cgi
