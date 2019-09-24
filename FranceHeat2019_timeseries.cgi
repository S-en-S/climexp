#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Europe 2019 heat waves studies" "time series" nofollow

cat <<EOF
For daily data, take the 3-day average and June max (for the first heat wave) / annual max (for the second one) yourself. For annual data this has already been done, check whether it is June or annual.

<p><b>Observations</b>
<br>Meteo France 1947-now: 
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/indT_FR_June&STATION=FR30_TG3x_jun&NPERYEAR=1">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/indT_TLSE_June&STATION=Toulouse_TG3x_jun&NPERYEAR=1">Toulouse</a>,
<br>E-OBS/ECA&amp;D: 
<a href="get_index.cgi?email=$EMAIL&field=ensembles_025_tg_e&maskmetadata=data/maskFrance_metropolitan.$EMAIL.poly">France</a>,
<a href="becatemp.cgi?id=$EMAIL&WMO=33&STATION=TOULOUSE-BLAGNAC&NPERYEAR=366">Toulouse</a>,
<a href="becatemp.cgi?id=$EMAIL&WMO=737&STATION=LILLE-LESQUIN&NPERYEAR=366">Lille</a>,
<a href="becatemp.cgi?id=$EMAIL&WMO=274&STATION=OXFORD&NPERYEAR=366">Oxford</a>,
<a href="becatemp.cgi?id=$EMAIL&WMO=4360&STATION=LINGEN">Lingen</a>.
<br>KNMI: <a href="getdutchtg.cgi?WMO=260&id=$EMAIL&STATION=De_Bilt&NPERYEAR=366">De Bilt</a>.
<br>UK Met Office: <a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_cambridge_bg&STATION=CAMBRIDGE_BG&NPERYEAR=366">Cambridge Botanical Gardens</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_cambridge_bg_patched&STATION=CAMBRIDGE_BG_patched&NPERYEAR=366">Cambridge BG patched</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_cambridge_niab&STATION=CAMBRIDGE_NIAB&NPERYEAR=366">Cambridge NIAB</a>.
<br>U Oxford: <a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_oxford&STATION=OXFORD&NPERYEAR=366">Oxford</a>,
<br>DWD: <a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_trier&STATION=TRIER-ZEWEN&NPERYEAR=366">Trier-Zewen</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_kaiserslautern&STATION=KAISERSLAUTERN&NPERYEAR=366">Kaiserslautern</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_lingen&STATION=LINGEN&NPERYEAR=366">Lingen</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_geisenheim&STATION=GEISENHEIM&NPERYEAR=366">Geisenheim</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_badneuenahr&STATION=BADNEUENAHR-AHRWEILER&NPERYEAR=366">Bad Neuenahr-Ahrweiler</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg_weilerswist&STATION=Weilerswist-Lommersum&NPERYEAR=366">Weilerswist-Lommersum</a>.
<br>KMI: The homogenised Uccle series is not publicly available.
<br>Berkeley 1900-now:
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iberkeley_tavg_daily_full_France_metropolitan_su&STATION=Berkeley_TG_France&NPERYEAR=366">France</a>,
<br>ERA-interim+ECMEF analyses+forecasts 1979-now: 
<a href="get_index.cgi?email=$EMAIL&field=erai_t2m_daily_e&gridpoints=false&intertype=nearest&lat1=30&lat2=72&lon1=-15&lon2=30&maskmetadata=data/maskFrance_metropolitan.$EMAIL.poly&masktype=all&standardunits=standardunits&NPERYEAR=366">France</a>,
<a href="get_index.cgi?email=$EMAIL&field=erai_t2m_daily_e&gridpoints=false&intertype=nearest&lat1=43.62&lon1=1.38&masktype=all&standardunits=standardunits&NPERYEAR=366">Toulouse</a>,
<a href="getdutchtg.cgi?WMO=260&id=$EMAIL&STATION=De_Bilt">De Bilt</a>,
<br>CRUTEM4 1900-2018: <a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/icrutem4_-15-20E_35-72N_n_su_15yr_low-pass_box_30_mean4_trend_max1_anom&STATION=CRUTEM4_WEurope_JJA&NPERYEAR=1">Western Europe JJA</a>

<p><b>Models</b>

<br>10 EUROCORDEX bias-corrected 1971-2100:
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_France_metropolitan_su_%%&STATION=EUROCORDEX11bc_tas_France&NPERYEAR=366">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_1.38E_43.62N_n_su_%%&STATION=EUROCORDEX11bc_tas_Toulouse&NPERYEAR=366">Toulouse</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_3.15E_50.97N_n_su_%%&STATION=EUROCORDEX11bc_tas_Lille&NPERYEAR=366">Lille</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_5E_52N_n_su_%%&STATION=EUROCORDEX11bc_tas_DeBilt&NPERYEAR=366">De Bilt</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp85_5E_52N_n_su_%%&STATION=EUROCORDEX11bc_tas_DeBilt&NPERYEAR=366">(RCP8.5)</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_0.13E_52.19N_n_su_%%&STATION=EUROCORDEX11bc_tas_Cambridge&NPERYEAR=366">Cambridge</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_-1.27E_51.77N_n_su_%%&STATION=EUROCORDEX11bc_tas_Oxford&NPERYEAR=366">Oxford</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieurocordex_tasAdjust_day_ens_rcp45_6.79E_50.71N_n_su_%%&STATION=EUROCORDEX11bc_tas_Weilerswist&NPERYEAR=366">Weilerswist-Lommersum</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/eurocordex_tasAdjust_day_ens_rcp45_-12-20E_35-72N_n_su_%%_mean4_anom_30_max1_anom_15yr_low-pass_box_30&STATION=EUROCORDEX11bc_JJA_tas_WEurope&NPERYEAR=1">Western Europe JJA</a>,
<br>16 RACMO 2.2 1950-2100:
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_France_metropolitan_5lan_su_%%&STATION=RACMO22_tas_France&NPERYEAR=366">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_1.38E_43.62N_n_su_%%&STATION=RACMO22_tas_Toulouse">16 RACMO 2.2 1950-2100</a>,
<a href="getindices.cgi?WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_3.15E_50.97N_n_su_%%&STATION=T2m_Lille_RACMO_EC-Earth23&TYPE=t&NPERYEAR=366&id=$EMAIL">Lille</a>,
<a href="getindices.cgi?WMO=KNMI14Data/Tdebilt/t2m_racmo_debilt_%%&STATION=T2m_debilt_RACMO_EC-Earth23&TYPE=t&NPERYEAR=366&id=$EMAIL">De Bilt</a>,
<a href="getindices.cgi?WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_0.13E_52.19N_n_su_%%&STATION=T2m_Cambridge_RACMO_EC-Earth23&TYPE=t&NPERYEAR=366&id=$EMAIL">Cambridge</a>,
<a href="getindices.cgi?WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_-1.27E_51.77N_n_su_%%&STATION=T2m_Oxford_RACMO_EC-Earth23&TYPE=t&NPERYEAR=366&id=$EMAIL">Oxford</a>,
<a href="getindices.cgi?WMO=FranceHeat2019/iknmi14_t2m_day_RACMO22E_rcp85_6.79E_50.71N_n_su_%%&STATION=T2m_Weilerswist-Lommersum_RACMO_EC-Earth23&TYPE=t&NPERYEAR=366&id=$EMAIL">Weilerswist-Lommersum</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_t2m_mon_RACMO22E_rcp85_-15-20E_37-66N_n_su_mean_15yr_low-pass_box_max1_anom_75&STATION=RACMO22_tas_WEurope">Western Europe JJA</a>,
<br>16 EC-Earth 2.3 1861-2100
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_France_metropolitan_su_%%&STATION=EC-Earth23_tas_France&NPERYEAR=366">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_1.38E_43.62N_n_su_%%&STATION=EC-Earth23_tas_Toulouse">Toulouse</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_3.15E_50.97N_n_su_%%&STATION=EC-Earth23_tas_Lille">Lille</a>,
<a href="getindices.cgi?WMO=KNMI14Data/Tdebilt/tas_muladdcorr_ydrun_retrend_%%&STATION=Tmean_debilt_EC-Earth23_debias&TYPE=t&NPERYEAR=366&id=$EMAIL">De Bilt (bias-corrected)</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_0.13E_52.19N_n_su_%%&STATION=EC-Earth23_tas_Cambridge">Cambridge</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_-1.27E_51.77N_n_su_%%&STATION=EC-Earth23_tas_Oxford">Oxford</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Aday_ECEARTH23_rcp85_6.79E_50.71N_n_su_%%&STATION=EC-Earth23_tas_Weilerswist-Lommersum">Weilerswist-Lommersum</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/iknmi14_tas_Amon_ECEARTH23_rcp85_-15-20E_35-72N_n_5lan_su_mean_mean4_anom_max1_anom_15yr_low-pass_box&STATION=EC-Earth23_tas_WEurope">Western Europe JJA</a>,
<br>15 HadGEM3-A-N219 1960-2015 historical
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_France_metropolitan_5lan_su_%%%&STATION=HadGEM3A_tas_France&NPERYEAR=360">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_1.38E_43.62N_n_su_%%%&STATION=HadGEM3A_tas_Toulouse&NPERYEAR=360">Toulouse</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_3.15E_50.97N_n_su_%%%&STATION=HadGEM3A_tas_Lille&NPERYEAR=360">Lille</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=EUCLEIA/HadGEM3-A-N216/Tdebilt/ieucleia_tas_Aday_HadGEM3-A-N216_historical_5E_52N_n_su_%%%&STATION=HadGEM3A_tas_DeBilt&NPERYEAR=360">De Bilt</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_0.13E_52.19N_n_su_%%%&STATION=HadGEM3A_tas_Cambridge&NPERYEAR=360">Cambridge</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_-1.27E_51.77N_n_su_%%%&STATION=HadGEM3A_tas_Oxford&NPERYEAR=360">Oxford</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Aday_HadGEM3-A-N216_historical_6.79E_50.71N_n_su_%%%&STATION=HadGEM3A_tas_Weilerswist-Lommersum&NPERYEAR=360">Weilerswist-Lommersum</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/ieucleia_tas_Amon_HadGEM3-A-N216_historical_-15-20E_35-72N_n_5lan_su_mean_mean4_anom_max1_anom_15yr_low-pass_box_20&STATION=HadGEM3A_tas_WEurope">Western Europe JJA</a>,
<br>28 CMIP5 1871-2100
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_cmip5_%%%_France&STATION=tg3x_cmip5_France&NPERYEAR=1">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_cmip5_%%%_Toulouse&STATION=tg3x_cmip5_Toulouse&NPERYEAR=1">Toulouse</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_cmip5_%%%_Lille&STATION=tg3x_cmip5_all_Lille&NPERYEAR=1">Lille</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_cmip5_%%%_DeBilt&STATION=tg3x_cmip5_all_DeBilt&NPERYEAR=1">DeBilt</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_cmip5_%%%_Cambridge&STATION=tg3x_cmip5_all_Cambridge&NPERYEAR=1">Cambridge</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_cmip5_%%%_Oxford&STATION=tg3x_cmip5_all_Oxford&NPERYEAR=1">Oxford</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_cmip5_%%%_Lingen&STATION=tg3x_cmip5_all_Lingen&NPERYEAR=1">Lingen</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cmip5_%%%_WEurope_JJA&STATION=tas_cmip5_WEurope_JJA&NPERYEAR=1">WEurope JJA</a>,
<br>31 IPSL-CM6B-LR
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_jun_ipsl-cm6a-lr_france_%%&STATION=tg3x_jun_ipsl-cm6a-lr_France&NPERYEAR=1">France June</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tg3x_ipsl-cm6a-lr_toulouse_%%&STATION=tg3x_ipsl-cm6a-lr_Toulouse&NPERYEAR=1">Toulouse June</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_ipsl-cm6a-lr_france_%%&STATION=tas_ipsl-cm6a-lr_France&NPERYEAR=366">France daily</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_ipsl-cm6a-lr_lille_%%&STATION=tas_ipsl-cm6a-lr_Lille&NPERYEAR=366">Lille</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_ipsl-cm6a-lr_lille2_%%&STATION=tas_ipsl-cm6a-lr_Lille2&NPERYEAR=366">Lille east</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_ipsl-cm6a-lr_debilt_%%&STATION=tas_ipsl-cm6a-lr_DeBilt&NPERYEAR=366">De Bilt</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_ipsl-cm6a-lr_debilt2_%%&STATION=tas_ipsl-cm6a-lr_DeBilt2&NPERYEAR=366">De Bilt east</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_ipsl-cm6a-lr_cambridge_%%&STATION=tas_ipsl-cm6a-lr_Cambridge&NPERYEAR=366">Cambridge</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_ipsl-cm6a-lr_oxford_%%&STATION=tas_ipsl-cm6a-lr_Oxford&NPERYEAR=366">Oxford</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_ipsl-cm6a-lr_lingen_%%&STATION=tas_ipsl-cm6a-lr_Lingen&NPERYEAR=366">Lingen</a>,
<br>10 CNRM-CM6.1
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cnrm-cm61_france_%%&STATION=tas_cnrm-cm61_France&NPERYEAR=366">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cnrm-cm61_lille_%%&STATION=tas_cnrm-cm61_Lille&NPERYEAR=366">Lille</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cnrm-cm61_lille2_%%&STATION=tas_cnrm-cm61_Lille2&NPERYEAR=366">Lille east</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cnrm-cm61_debilt_%%&STATION=tas_cnrm-cm61_DeBilt&NPERYEAR=366">De Bilt</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cnrm-cm61_debilt2_%%&STATION=tas_cnrm-cm61_DeBilt2&NPERYEAR=366">De Bilt east</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cnrm-cm61_cambridge_%%&STATION=tas_cnrm-cm61_Cambridge&NPERYEAR=366">Cambridge</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cnrm-cm61_oxford_%%&STATION=tas_cnrm-cm61_Oxford&NPERYEAR=366">Oxford</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/tas_cnrm-cm61_lingen_%%&STATION=tas_cnrm-cm61_Lingen&NPERYEAR=366">Lingen</a>,
<br>100 weather@home actual: 
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_ACTUAL_TG3x_JJA_1986_2015_France_@@@&STATION=w@h_actual_France&NPERYEAR=1">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_ACTUAL_TG3x_JJA_1986_2015_Lille_@@@&STATION=w@h_actual_Lille&NPERYEAR=1">Lille</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_ACTUAL_TG3x_JJA_1986_2015_DeBilt_@@@&STATION=w@h_actual_DeBilt&NPERYEAR=1">De Bilt</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_ACTUAL_TG3x_JJA_1986_2015_Cambridge_@@@&STATION=w@h_actual_Cambridge&NPERYEAR=1">Cambridge</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_ACTUAL_TG3x_JJA_1986_2015_Oxford_@@@&STATION=w@h_actual_Oxford&NPERYEAR=1">Oxford</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_ACTUAL_TG3x_JJA_1986_2015_Lingen_@@@&STATION=w@h_actual_Lingen&NPERYEAR=1">Lingen</a>,
<br>100 weather@home natural: 
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_NATURAL_TG3x_JJA_1986_2015_France_@@@&STATION=w@h_natural_France&NPERYEAR=1">France</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_NATURAL_TG3x_JJA_1986_2015_Lille_@@@&STATION=w@h_natural_Lille&NPERYEAR=1">Lille</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_NATURAL_TG3x_JJA_1986_2015_DeBilt_@@@&STATION=w@h_natural_DeBilt&NPERYEAR=1">De Bilt</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_NATURAL_TG3x_JJA_1986_2015_Cambridge_@@@&STATION=w@h_natural_Cambridge&NPERYEAR=1">Cambridge</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_NATURAL_TG3x_JJA_1986_2015_Oxford_@@@&STATION=w@h_natural_Oxford&NPERYEAR=1">Oxford</a>,
<a href="getindices.cgi?id=$EMAIL&WMO=FranceHeat2019/WAH_NATURAL_TG3x_JJA_1986_2015_Lingen_@@@&STATION=w@h_natural_Lingen&NPERYEAR=1">Lingen</a>,

EOF

. ./myvinkfoot.cgi