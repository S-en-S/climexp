#!/bin/bash
echo 'Content-Type: text/html'
echo
echo
. ./init.cgi
. ./getargs.cgi

. ./myvinkhead.cgi "WMO-assessed data sets" "Observations" "index,follow" | sed -e 's/56.375/90/'

cat <<EOF
This page provides links to the Climate Explorer pages of key climate variables that have been
assessed under supervision of the WMO.  For more information of the assessment process
and a list of the assessed datasets, see <a href="https://climatedata-catalogue.wmo.int/">the WMO web pge</a>.
<table class="realtable" width="100%" border=0 cellspacing=0 cellpadding=0>
<tr><th colspan="3">Temperature and Precipitation (ECVs) and Climate Indices: fields</th></tr>
EOF

for string in hadcrut4 noaa_temp giss_temp_1200 gpcc cocorahs hadex2
do
    fgrep -i $string selectfield_obs.html | fgrep -v filled |
        sed -e 's/<input type="radio" class="formradio" name="field" value="\([^"]*\)">/<a href="select.cgi?id=EMAIL\&field=\1">/g' \
            -e 's:,:</a>,:g' \
            -e 's:</td><td><a href=":</a></td><td><a href=":g' \
            -e "s/EMAIL/$EMAIL/g" \
            -e 's/<!--GPCC-->/Precipitation/' \
            -e 's/<!--HADEX2-->/Extreme indices/' \
            -e 's/<!--ICOADS-->/Ocean surface/'
done
cat <<EOF
<tr><th colspan="3">Temperature and Precipitation (ECVs) and Climate Indices: time series</th></tr>
EOF
for string in hadcrut4 NOAA/NCEI "Ts+dSST"
do
    fgrep -i $string selectindex.cgi | fgrep -v filled |
        sed -e "s/EMAIL/$EMAIL/g"
done

cat <<EOF
<tr><th colspan="3">Hydrology and Marine</th></tr>
<tr><td align=right>Run-off time series</td><td><a href="https://www.bafg.de/GRDC/EN/Home/homepage_node.html">GRDC</a> does not allow their data here</td></td><td><a href="https://www.bafg.de/GRDC/EN/01_GRDC/13_dtbse/database_node.html</a>" target="_new"><img src="images/info-i.gif" alt="more information" border="0"></a></td></tr>
EOF
for string in coads copernicus_sla esa_sla
do
    fgrep -i $string selectfield_obs.html | fgrep -v filled |
        sed -e 's/<input type="radio" class="formradio" name="field" value="\([^"]*\)">/<a href="select.cgi?id=EMAIL\&field=\1">/g' \
            -e 's:,:</a>,:g' \
            -e 's:</td><td><a href=":</a></td><td><a href=":g' \
            -e "s/EMAIL/$EMAIL/g" \
            -e 's/<!--GPCC-->/Precipitation/' \
            -e 's/<!--HADEX2-->/Extreme indices/' \
            -e 's/<!--ICOADS-->/Ocean surface/'
done
cat <<EOF
<tr><td>Sea level stations</td><td>
<form action="getstations.cgi" method="POST">
<input type="hidden" name="email" value="$EMAIL">
<input type="hidden" name="climate" value="sealev">
GLOSS sea level stations with a name containing
<input type="text" class="forminput" name="name" size=10 value="$FORM_NAME">,<br>
or <input type="$number" min=1 class="forminput" name="num" $textsize3 value="${FORM_num:-10}"> stations near
<input type="$number" step=any class="forminput" name="lat" $textsize4 value="$FORM_lat">&deg;N,
<input type="$number" step=any class="forminput" name="lon" $textsize4 value="$FORM_lon">&deg;E,<br>
or all stations in the region
<input type="$number" step=any class="forminput" name="lat1" $textsize4 value="$FORM_lat1">&deg;N -
<input type="$number" step=any class="forminput" name="lat2" $textsize4 value="$FORM_lat2">&deg;N,
<input type="$number" step=any class="forminput" name="lon1" $textsize4 value="$FORM_lon1">&deg;E -
<input type="$number" step=any class="forminput" name="lon2" $textsize4 value="$FORM_lon2">&deg;E<br>
with at least <input type="$number" class="forminput" name="min" $textsize3 value="${FORM_min:-10}">years of data
<input type="submit" class="formbutton" value="Get stations"></form>
</td><td><a href="http://www.gloss-sealevel.org/"><img align="right" src="images/info-i.gif" alt="help" border="0"></a></td>
<tr><td align=right>Subsurface ocean</td><td>The raw WOD13 data are incompatible with the CXlimate Explorer. Derived time series are below.</td></td><td><a href="https://www.nodc.noaa.gov/OC5/WOD13/</a>" target="_new"><img src="images/info-i.gif" alt="more information" border="0"></a></td></tr>
EOF
fgrep -i 'nodc' selectindex.cgi | fgrep -v temp | sed -e "s/EMAIL/$EMAIL/g"
cat <<EOF
</tr><tr><th colspan="3">Sea Ice & Ice Sheets & Glacier ECVs: fields</th></tr>
EOF
for string in ice_index grace
do
    fgrep -i $string selectfield_obs.html | fgrep -v filled |
        sed -e 's/<input type="radio" class="formradio" name="field" value="\([^"]*\)">/<a href="select.cgi?id=EMAIL\&field=\1">/g' \
            -e 's:,:</a>,:g' \
            -e 's:</td><td><a href=":</a></td><td><a href=":g' \
            -e "s/EMAIL/$EMAIL/g" \
            -e 's/<!--GPCC-->/Precipitation/' \
            -e 's/<!--HADEX2-->/Extreme indices/' \
            -e 's/<!--ICOADS-->/Ocean surface/'
done
cat <<EOF
<tr><th colspan="3">Sea Ice & Ice Sheets & Glacier ECVs: indices</th></tr>
EOF
for string in ice_area GRACE
do
    fgrep -i $string selectindex.cgi  |
        sed -e "s/EMAIL/$EMAIL/g"
done

cat <<EOF
<tr><th colspan=3>&nbsp</th></tr></table>
EOF
# instead of myvinkfoot
echo '</div></div></td></tr></table>'
