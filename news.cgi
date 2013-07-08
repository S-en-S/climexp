#!/bin/sh
echo "Content-Type: text/html"
echo
echo

. ./getargs.cgi
all=$FORM_all

. ./myvinkhead.cgi "News" "" "index,follow"

echo '<table class="realtable" width=451 border=0 cellpadding=0 cellspacing=0>'
if [ "$all" = "all" ]; then
  echo '<tr><th colspan="2">All news</th></tr>'
  cat news.html
else
  echo '<tr><th colspan="2">Recent news</th></tr>'
  head -20 news.html
  echo "<tr><td><a href=\"news.cgi?id=$EMAIL&all=all\">more...</a></td></tr>"
fi
echo "</table>"

. ./myvinkfoot.cgi
