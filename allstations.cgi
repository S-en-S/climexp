#!/bin/bash

# set up the information that getstations.cgi expects

. ./init.cgi
. ./getargs.cgi
if [ -z "$HTTP_USER_AGENT" ]; then
    echo "Content-Type: text/plain"
    echo
    echo "Only for real users and search engines"
    exit
fi
FORM_EMAIL="$EMAIL"
FORM_email="$EMAIL"
NPERYEAR="$FORM_n"
FORM_min="1"
FORM_month="-1"
FORM_lon1="-30"
FORM_lon2="330"
FORM_lat1="-90"
FORM_lat2="90"

. ./getstations.cgi
