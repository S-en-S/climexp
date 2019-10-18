#!/bin/bash
. ./init.cgi
. ./getargs.cgi
echo "Content-Type: text/html"
echo
. ./myvinkhead.cgi "Dutch drought study" "time series" nofollow

cat <<EOF
<i><b>The Netherlands inland</b></i><br>
PR:  
<a href="getindices.cgi?WMO=DutchDrought/iensembles_025_rr_mo_Netherlands_inland_su&STATION=iensembles_025_rr_mo_Netherlands_inland&TYPE=i&id=$EMAIL">E-OBS</a>,
<a href="getindices.cgi?WMO=DutchDrought/iicmip5_pr_Amon_GFDL-ESM2M_rcp60_6E_52N_n_su_000&STATION=iicmip5_pr_Amon_GFDL-ESM2M_rcp60_6E_52N&TYPE=i&id=$EMAIL">GFDL</a>,
<a href="getindices.cgi?WMO=DutchDrought/icmip5_pr_Amon_HadGEM2-ES_rcp60_7E_52.5N_n_su_%%%&STATION=icmip5_pr_Amon_HadGEM2-ES_rcp60_7E_52.5N&TYPE=i&id=$EMAIL">HadGem</a>,
<a href="getindices.cgi?WMO=DutchDrought/iicmip5_pr_Amon_IPSL-CM5A-LR_rcp60_6E_52N_n_su_000&STATION=iicmip5_pr_Amon_IPSL-CM5A-LR_rcp60_6E_52N&TYPE=i&id=$EMAIL">IPSL</a>,
<a href="getindices.cgi?WMO=DutchDrought/icmip5_pr_Amon_MIROC5_rcp60_7E_52.5N_n_su_%%%&STATION=icmip5_pr_Amon_MIROC5_rcp60_7E_52.5N&TYPE=i&id=$EMAIL">MIROC</a>,
<a href="getindices.cgi?WMO=DutchDrought/iknmi14_pr_mon_RACMO22E_rcp85_Netherlands_inland_su_%%&STATION=iknmi14_pr_mon_RACMO22E_rcp85_Netherlands_inland&TYPE=i&id=$EMAIL">RACMO</a>,
<a href="getindices.cgi?WMO=DutchDrought/iknmi14_pr_Amon_ECEARTH23_rcp85_Netherlands_inland_su_%%&STATION=iknmi14_pr_Amon_ECEARTH23_rcp85_Netherlands_inland&TYPE=i&id=$EMAIL">EC-Earth</a>,
<a href="getindices.cgi?WMO=DutchDrought/pr_adj_GFDL_Netherlands_inland_su&STATION=pr_adj_GFDL_Netherlands_inland&TYPE=i&id=$EMAIL">GFDL-adj</a>,
<a href="getindices.cgi?WMO=DutchDrought/pr_adj_HadGEM_Netherlands_inland_su&STATION=pr_adj_HadGEM_Netherlands_inland&TYPE=i&id=$EMAIL">HadGem-adj</a>,
<a href="getindices.cgi?WMO=DutchDrought/pr_adj_IPSL_Netherlands_inland_su&STATION=pr_adj_IPSL_Netherlands_inland_su&TYPE=i&id=$EMAIL">IPSL-adj</a>,
<a href="getindices.cgi?WMO=DutchDrought/pr_adj_MIROC_Netherlands_inland_su&STATION=pr_adj_MIROC_Netherlands_inland_su&TYPE=i&id=$EMAIL">MIROC-adl</a><br>

T:
<a href="getindices.cgi?WMO=DutchDrought/iensembles_025_tg_mo_Netherlands_inland_su&STATION=iensembles_025_tg_mo_Netherlands_inland&TYPE=i&id=$EMAIL">E-OBS</a>,
<a href="getindices.cgi?WMO=DutchDrought/iicmip5_tas_Amon_GFDL-ESM2M_rcp60_6E_52N_n_su_000&STATION=iicmip5_tas_Amon_GFDL-ESM2M_rcp60_6E_52N&TYPE=i&id=$EMAIL">GFDL</a>,
<a href="getindices.cgi?WMO=DutchDrought/icmip5_tas_Amon_HadGEM2-ES_rcp60_7E_52.5N_n_su_%%%&STATION=icmip5_tas_Amon_HadGEM2-ES_rcp60_7E_52.5N&TYPE=i&id=$EMAIL">HadGem</a>,
<a href="getindices.cgi?WMO=DutchDrought/iicmip5_tas_Amon_IPSL-CM5A-LR_rcp60_6E_52N_n_su_000&STATION=iicmip5_tas_Amon_IPSL-CM5A-LR_rcp60_6E_52N&TYPE=i&id=$EMAIL">IPSL</a>,
<a href="getindices.cgi?WMO=DutchDrought/icmip5_tas_Amon_MIROC5_rcp60_7E_52.5N_n_su_%%%&STATION=icmip5_tas_Amon_MIROC5_rcp60_7E_52.5N&TYPE=i&id=$EMAIL">MIROC</a>,
<a href="getindices.cgi?WMO=DutchDrought/iknmi14_t2m_mon_RACMO22E_rcp85_Netherlands_inland_su_%%&STATION=iknmi14_t2m_mon_RACMO22E_rcp85_Netherlands_inland&TYPE=i&id=$EMAIL">RACMO</a>,
<a href="getindices.cgi?WMO=DutchDrought/iknmi14_tas_Amon_ECEARTH23_rcp85_Netherlands_inland_su_%%&STATION=iknmi14_tas_Amon_ECEARTH23_rcp85_Netherlands_inland&TYPE=i&id=$EMAIL">EC-Earth</a>,
<a href="getindices.cgi?WMO=DutchDrought/t_adj_GFDL_Netherlands_inland_su&STATION=t_adj_GFDL_Netherlands_inland&TYPE=i&id=$EMAIL">GFDL-adj</a>,
<a href="getindices.cgi?WMO=DutchDrought/tr_adj_HadGEM_Netherlands_inland_su&STATION=tr_adj_HadGEM_Netherlands_inland&TYPE=i&id=$EMAIL">HadGem-adj</a>,
<a href="getindices.cgi?WMO=DutchDrought/t_adj_IPSL_Netherlands_inland_su&STATION=t_adj_IPSL_Netherlands_inland&TYPE=i&id=$EMAIL">IPSL-adj</a>,
<a href="getindices.cgi?WMO=DutchDrought/t_adj_MIROC_Netherlands_inland_su&STATION=t_adj_MIROC_Netherlands_inland&TYPE=i&id=$EMAIL">MIROC-adl</a><br>

PET:
<a href="getindices.cgi?WMO=DutchDrought/iclm_era_etp_Netherlands_inland_su&STATION=iclm_era_etp_Netherlands_inland&TYPE=i&id=$EMAIL">CLM_ERA-I</a>,
<a href="getindices.cgi?WMO=DutchDrought/iclm_wfdei_etp_Netherlands_inland_su&STATION=iclm_wfdei_etp_Netherlands_inland&TYPE=i&id=$EMAIL">CLM_WFDEI</a>,
<a href="getindices.cgi?WMO=DutchDrought/ierai_evappot_Netherlands_inland_su&STATION=ierai_evappot_Netherlands_inland&TYPE=i&id=$EMAIL">ERA-I</a>,
<a href="getindices.cgi?WMO=DutchDrought/imerra_refet_Netherlands_inland_su_0.0333&STATION=imerra_refet_Netherlands_inland&TYPE=i&id=$EMAIL">MERRA</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_GFDL_H08_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_GFDL_H08_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL">GFDL_H08</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_GFDL_LPJML_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_GFDL_LPJML_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> GFDL_LPJML</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_GFDL_PCR-globwb_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_GFDL_PCR-globwb_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> GFDL_PCR-globwb</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_GFDL_watergap_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_GFDL_watergap_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> GFDL_watergap</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_HadGEM_H08_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_HadGEM_H08_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> HadGEM_H08</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_HadGEM_LPJML_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_HadGEM_LPJML_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> HadGEM_LPJML</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_HadGEM_PCR-globwb_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_HadGEM_PCR-globwb_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> HadGEM_PCR-globwb</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_HadGEM_watergap_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_HadGEM_watergap_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> HadGEM_watergap</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_IPSL_H08_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_IPSL_H08_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> IPSL_H08</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_IPSL_LPJML_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_IPSL_LPJML_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> IPSL_LPJML</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_IPSL_PCR-globwb_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_IPSL_PCR-globwb_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> IPSL_PCR-globwb</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_IPSL_watergap_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_IPSL_watergap_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> IPSL_watergap</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_MIROC5_H08_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_MIROC5_H08_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> MIROC5_H08</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_MIROC5_LPJML_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_MIROC5_LPJML_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> MIROC5_LPJML</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_MIROC5_PCR-globwb_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_MIROC5_PCR-globwb_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> MIROC5_PCR-globwb</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_potevap_MIROC5_watergap_rcp60_Netherlands_inland_su_86400&STATION=iisimip_potevap_MIROC5_watergap_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> MIROC5_watergap</a>,
<a href="getindices.cgi?WMO=DutchDrought/iknmi14pcglob_evappot_Amon_ECEARTH23_rcp85_Netherlands_inland_su_%%&STATION=iknmi14pcglob_evappot_Amon_ECEARTH23_rcp85_Netherlands&TYPE=i&id=$EMAIL">EC-Earth</a><br>

SM:
<a href="getindices.cgi?WMO=DutchDrought/iclm_era_soil1_Netherlands_inland_su&STATION=iclm_era_soil1_Netherlands_inland&TYPE=i&id=$EMAIL">CLM_ERA-I</a>,
<a href="getindices.cgi?WMO=DutchDrought/iclm_wfdei_soil1_Netherlands_inland_su&STATION=iclm_wfdei_soil1_Netherlands_inland&TYPE=i&id=$EMAIL">CLM_WFDEI</a>,
<a href="getindices.cgi?WMO=DutchDrought/ifldas_sm0_40_Netherlands_inland_su&STATION=ifldas_sm0_40_Netherlands_inland&TYPE=i&id=$EMAIL">FLDAS</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_WFDEI_PCR-globwb_Netherlands_inland_su&STATION=iisimip_soilmoist_WFDEI_PCR-globwb_Netherlands_inland&TYPE=i&id=$EMAIL">WFDEI_PCRGLOB</a>,
<a href="getindices.cgi?WMO=DutchDrought/soilmoist_WFDEI_LPJML_lev1-2_Netherlands_inland_su&STATION=soilmoist_WFDEI_LPJML_lev1-2_Netherlands_inland&TYPE=i&id=$EMAIL">WFDEI_LPJmL</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_GFDL_H08_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_GFDL_H08_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL">GFDL_H08</a>,
<a href="getindices.cgi?WMO=DutchDrought/soilmoist_GFDL_LPJML_lev1-2_Netherlands_inland_su&STATION=soilmoist_GFDL_LPJML_lev1-2_Netherlands_inland&TYPE=i&id=$EMAIL"> GFDL_LPJML</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_GFDL_PCR-globwb_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_GFDL_PCR-globwb_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> GFDL_PCR-globwb</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_GFDL_watergap_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_GFDL_watergap_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> GFDL_watergap</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_HadGEM_H08_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_HadGEM_H08_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> HadGEM_H08</a>,
<a href="getindices.cgi?WMO=DutchDrought/soilmoist_HadGEM_LPJML_lev1-2_Netherlands_inland_su&STATION=soilmoist_HadGEM_LPJML_lev1-2_Netherlands_inland&TYPE=i&id=$EMAIL"> HadGEM_LPJML</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_HadGEM_PCR-globwb_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_HadGEM_PCR-globwb_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> HadGEM_PCR-globwb</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_HadGEM_watergap_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_HadGEM_watergap_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> HadGEM_watergap</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_IPSL_H08_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_IPSL_H08_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> IPSL_H08</a>,
<a href="getindices.cgi?WMO=DutchDrought/soilmoist_IPSL_LPJML_lev1-2_Netherlands_inland_su&STATION=soilmoist_IPSL_LPJML_lev1-2_Netherlands_inland&TYPE=i&id=$EMAIL"> IPSL_LPJML</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_IPSL_PCR-globwb_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_IPSL_PCR-globwb_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> IPSL_PCR-globwb</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_IPSL_watergap_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_IPSL_watergap_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> IPSL_watergap</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_MIROC5_H08_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_MIROC5_H08_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> MIROC5_H08</a>,
<a href="getindices.cgi?WMO=DutchDrought/soilmoist_MIROC5_LPJML_lev1-2_Netherlands_inland_su&STATION=soilmoist_MIROC5_LPJML_lev1-2_Netherlands_inland&TYPE=i&id=$EMAIL"> MIROC5_LPJML</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_MIROC5_PCR-globwb_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_MIROC5_PCR-globwb_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> MIROC5_PCR-globwb</a>,
<a href="getindices.cgi?WMO=DutchDrought/iisimip_soilmoist_MIROC5_watergap_rcp60_Netherlands_inland_su&STATION=iisimip_soilmoist_MIROC5_watergap_rcp60_Netherlands_inland&TYPE=i&id=$EMAIL"> MIROC5_watergap</a>,
<a href="getindices.cgi?WMO=DutchDrought/iknmi14_mrso1m_mon_RACMO22E_rcp85_Netherlands_inland_su_%%&STATION=iknmi14_mrso1m_mon_RACMO22E_rcp85_Netherlands_inland_%%&TYPE=i&id=$EMAIL">RACMO</a>,
<a href="getindices.cgi?WMO=DutchDrought/iknmi14pcglob_soilmoisture_Lmon_ECEARTH23_rcp85_Netherlands_inland_su_%%&STATION=iknmi14pcglob_soilmoisture_Lmon_ECEARTH23_rcp85_Netherlands_inland_%%&TYPE=i&id=$EMAIL">EC-Earth</a><br>

<i><b>The Netherlands coastal</b></i><br>
PR:
<a href="getindices.cgi?WMO=DutchDrought/iensembles_025_rr_mo_Netherlands_inland_su&STATION=iensembles_025_rr_mo_Netherlands_inland&TYPE=i&id=$EMAIL">E-OBS</a><br>
EOF

. ./myvinkfoot.cgi
