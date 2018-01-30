#!/bin/sh
if [ -z "$myvinkhead" ]; then
  . ./httpheaders_nocache.cgi
  # check if a search engine, if so set user to anonymous
  . ./init.cgi
  . ./getargs.cgi
  . ./checkemail.cgi
  . ./nosearchengine.cgi
  . ./myvinkhead.cgi "Upload a mask"
fi


if [ "$EMAIL" = "someone@somewhere" ]; then
  echo "Anonymous users cannot upload masks. Please <a href=\"registerform.cgi\">register or log in</a>"
  . ./myvinkfoot.cgi
  exit
fi
cat <<EOF
<div class='formheader'>Upload a polygon mask
<a href="javascript:pop_page('help/upload_mask.shtml',284,450)"><img align=right src="images/info-i.gif" alt="help" border="0"></a>
</div>
<div class='formbody'>
<table style='width:100%' border='0' cellpadding='0' cellspacing='0'>
<form action="upload_mask.cgi" method="POST">
<input type="hidden" name="email" value="$EMAIL">
<input type="hidden" name="field" value="$FORM_field">
<tr><td>
Name:
</td><td>
<input type="text" name="maskname" size=20>
</td></tr><tr><td>
South Pole:
</td><td>
<input type=checkbox class=formcheck name="sp">included
</td></tr><tr><td colspan="2">
<textarea class="forminput" name="data" class="forminput" rows="6" cols="52">
# Overwrite this text by your data.  
# Lines starting with a hash are considered comments. 
# Next there should be a list of (X,Y) values (rest of lines is ignored)
</textarea>
</td></tr><tr><td colspan=2>
<input type="submit" class="formbutton" value="Upload">
<input type="reset" class="formbutton" value="Clear Form" align="right">
</td></tr>
</form>
</table>
</div>

<div class=alineakop>Standard sets</div>
<ul>
<li><a href="upload_mask.cgi?id=$EMAIL&field=$FORM_field&set=ar5_atlas">37 IPCC WG1 AR5 Atlas regions</a>
<a href="http://www.climatechange2013.org/"><img align=right src="images/info-i.gif" alt="help" border="0"></a>
<a href="download_masks.cgi?id=$EMAIL&field=$FORM_field&set=ar5_atlas"><img align=right src="images/download.gif" alt="download" border="0"></a>
<li><a href="upload_mask.cgi?id=$EMAIL&field=$FORM_field&set=SREX">27 IPCC SREX land regions</a>
<a href="SREX/SREX-Ch3-Supplement_FINAL.pdf" target=_new><img align=right src="images/info-i.gif" alt="help" border="0"></a>
<a href="download_masks.cgi?id=$EMAIL&field=$FORM_field&set=SREX"><img align=right src="images/download.gif" alt="download" border="0"></a>
<li><a href="upload_mask.cgi?id=$EMAIL&field=$FORM_field&set=eu_rivers_big">14 European river catchments</a>
<a href="download_masks.cgi?id=$EMAIL&field=$FORM_field&set=eu_rivers_big"><img align=right src="images/download.gif" alt="download"
 border="0"></a>
<li><a href="upload_mask.cgi?id=$EMAIL&field=$FORM_field&set=eu_rivers">215 European river basins</a>
<a href="http://www.eea.europa.eu/data-and-maps/data/wise-river-basin-districts-rbds" target=_new><img align=right src="images/info-i.gif" alt="help" border="0"></a>
<a href="download_masks.cgi?id=$EMAIL&field=$FORM_field&set=eu_rivers"><img align=right src="images/download.gif" alt="download" border="0"></a>
<li><a href="upload_mask.cgi?id=$EMAIL&field=$FORM_field&set=countries">235 countries</a>
<a href="http://www.rjruss.info/2010/12/free-countries-of-world-in-polygon-kml.html" target="_new"><img align=right src="images/info-i.gif" alt="help" border="0"></a>
<a href="download_masks.cgi?id=$EMAIL&field=$FORM_field&set=countries"><img align=right src="images/download.gif" alt="download" border="0"></a>
<li><a href="upload_mask.cgi?id=$EMAIL&field=$FORM_field&set=IPBES">22 IPBES regions</a>
<a href="http://ipbes.net" target="_new"><img align=right src="images/info-i.gif" alt="help" border="0"></a>
<a href="download_masks.cgi?id=$EMAIL&field=$FORM_field&set=IPBES"><img align=right src="images/download.gif" alt="download" border="0"></a>
</ul>
Note that the IPCC masks do <b>not</b> include the land/sea mask, this has to be added on the next page. 
EOF

. ./myvinkfoot.cgi
