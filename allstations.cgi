#!/bin/sh

# set up the information that getstations.cgi expects

. ./getargs.cgi
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
