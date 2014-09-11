#!/bin/sh
# across all time scales, so without suffix NPERYEAR
echo "$FORM_timeseries" | head -1 > ./prefs/$EMAIL.series
case $FORM_fit in
    gev|gumbel) FORM_plot=gumbel;;
    gpd|gauss) FORM_plot=sqrtlog;;
esac
cat > ./prefs/$EMAIL.histogramoptions <<EOF
FORM_plot=$FORM_plot;
FORM_nbin=$FORM_nbin;
FORM_changesign=$FORM_changesign;
FORM_restrain=$FORM_restrain;
FORM_assume=$FORM_assume;
FORM_dgt=$FORM_dgt;
FORM_year=$FORM_year;
FORM_xyear=$FORM_xyear;
FORM_begin2=$FORM_begin2;
FORM_decor=$FORM_decor;
FORM_fit=$FORM_fit;
FORM_xlo=$FORM_xlo;
FORM_xhi=$FORM_xhi;
FORM_ylo=$FORM_ylo;
FORM_yhi=$FORM_yhi;
FORM_var=$FORM_var;
EOF
