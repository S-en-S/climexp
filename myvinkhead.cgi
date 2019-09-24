#!/bin/bash
# generates the vink headers with a user-defied title and subtitle
if [ -z "$myvinkhead" ]; then
myvinkhead="done"
if [ -n "$3" ]; then
  robot="<meta name=\"robots\" content=\""$3"\">"
fi
if [ -n "$absolute_paths" ]; then
    prfx="https://climexp.knmi.nl/"
else
    prfx=""
fi
cat <<EOF
<html>
<head>
<!-- beheerder: Geert Jan van Oldenborgh -->
<link rel="stylesheet" href="${prfx}styles/rccstyle.css" type="text/css">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script language="javascript" src="${prfx}library/javascript/hidden_info_switch.js"></script>
<script language="javascript" src="${prfx}library/javascript/pop_page.js"></script> 
$extrahead
$robot
<link rel="shortcut icon" href="/favicon.ico"> 
<title>Climate Explorer: $1</title>
<style type="text/css">
a { text-decoration: none }
</style>
</head>
<body>
EOF
. ./searchengine.cgi
# in case it does not come from getopts filter the EMAIL string 
EMAIL=`echo "$EMAIL" | sed -e 's/[^A-Za-z0-9_.@-]/_/g'`
sed -e "s/FORM_EMAIL/$EMAIL/" ./vinklude/rcc_pagehead.html 
cat <<EOF
<table border="0" width="95.25%" cellspacing="0" cellpadding="0">
   <tr>
      <td width="10%">&nbsp;</td>
      <td width="56.375%" valign=top>
         <div id="printable" name="printable">
         <!-- div -->
<!-- Voeg hieronder de inhoud van de pagina in -->
<br>
         <div class="hoofdkop">$1</div>
         <div class="subkop">$2</div>
<div class="kalelink">
EOF
fi
. ./init.cgi