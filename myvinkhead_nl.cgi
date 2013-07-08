#!/bin/sh
# generates the vink headers with a user-defied title and subtitle
if [ -z "$myvinkhead" ]; then
myvinkhead="done"
if [ -n "$3" ]; then
  robot="<meta name=\"robots\" content=\""$3"\">"
fi
cat <<EOF
<html>
<head>
<!-- beheerder: Geert Jan van Oldenborgh -->
<link rel="stylesheet" href="styles/vinkstyle.css" type="text/css">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
$extrahead
$robot
<link rel="shortcut icon" href="/favicon.ico"> 
<title>Climate Explorer: $1</title>
</head>
<body>
EOF
cat ./vinklude/paginakop.html
cat <<EOF
<table border="0" width="762" cellspacing="0" cellpadding="0">
   <tr>
      <td width="80">&nbsp;</td>
      <td width="451" valign=top>
         <div id="printable" name="printable">
         <!-- div -->
<!-- Voeg hieronder de inhoud van de pagina in -->
         <div class="rubriekkop">Climate Explorer</div>
         <div class="hoofdkop">$1</div>
         <div class="subkop">$2</div>
<div class="kalelink">
EOF
fi
. ./init.cgi
