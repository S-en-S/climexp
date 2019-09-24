#!/bin/bash
if [ -z "$alreadycalledgetargs" ]; then
    export alreadycalledgetargs=true
    eval `./bin/proccgi "$@"`
    # construct a web call that gives the same results
    if [ -n "$SSL_PROTOCOL" ]; then
        export SCRIPTURL="https://$SERVER_NAME$SCRIPT_NAME?"
    else
        export SCRIPTURL="http://$SERVER_NAME$SCRIPT_NAME?"
    fi
    EMAIL="$FORM_id"
    [ -z "$EMAIL" ] && EMAIL="$FORM_EMAIL"
    [ -z "$EMAIL" ] && EMAIL="$FORM_email"
    if [ -z "$EMAIL" ]; then
        # maybe someone used the old links
        c1=`echo "$QUERY_STRING" | fgrep -c '@'`
        c2=`echo "$QUERY_STRING" | fgrep -c '+'`
        if [ $c1 = 1 -a $c2 = 0 ]; then
            EMAIL="$QUERY_STRING"
        fi
    fi
    EMAIL=`echo "$EMAIL" | fgrep -v '/' `
    EMAIL=`echo "$EMAIL" | tr -cd '[:alnum:]@.-_' | fgrep -v "/" | egrep -v '(@|\.|-)sexy(@|\.|-)|(@|\.|-)sex(@|\.|-)|(@|\.|-)porn(@|\.|-)|(@|\.|-)porno(@|\.|-)|youtube.com|fynalcut.com|shop.*ru$|della-marta'`
    EMAIL=${EMAIL#id=}
    [ "$EMAIL" = FORM_EMAIL ] && EMAIL=""
    id=$EMAIL
    ###echo "EMAIL=$EMAIL<br>"
    # build a variable SCRIPTURL that can be used to reproduce this step later
    # do not include ID, so that it does not leak into plots.
    formvarlist=`set | egrep '^FORM_' | fgrep -v FORM_data | egrep -v '=$' | tr ' ' '_' | sed -e "s/$id/\\$id/"`
    init=0
    for formvar in $formvarlist; do
        if [ $init = 0 ]; then
            init=1
        else
            SCRIPTURL="$SCRIPTURL&"
        fi
        SCRIPTURL="$SCRIPTURL${formvar#FORM_}"
    done
    [ -n "FORM_WMO" ] && FORM_WMO=`echo "$FORM_WMO" | sed -e 's/%%%/+++/' -e 's/%%/++/'`
    [ -n "FORM_wmo" ] && FORM_wmo=`echo "$FORM_wmo" | sed -e 's/%%%/+++/' -e 's/%%/++/'`
    [ -n "$FORM_field" ] && export FORM_field
fi # alreadycalledgetargs