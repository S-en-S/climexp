function pop_picture(plaat, param1, param2) {

if (plaat.indexOf('.gif') < 0 && plaat.indexOf('.jpg') < 0 && plaat.indexOf('.png') < 0  &&
    plaat.indexOf('.GIF') < 0 && plaat.indexOf('.JPG') < 0 && plaat.indexOf('.PNG') < 0)  {
   alert('Improper use of pop_picture for ' + plaat + '\nImage must have the extension .gif, .jpg or .png');
} else {
   bigpic = window.open('', 'picture_window', 'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=yes,resizable=1,copyhistory=0,width=451,height=500');
//   bigpic.document.open(); //
   bigpic.document.write("<html>");
   bigpic.document.write("<head>");
   bigpic.document.write("<link rel='stylesheet' href='/styles/vinkstyle.css' type='text/css'>");
   bigpic.document.write("<META HTTP-EQUIV='imagetoolbar' CONTENT='no'>");
   bigpic.document.write("<META HTTP-EQUIV='Cache Control' CONTENT='no-cache'>");
   bigpic.document.write("<META HTTP-EQUIV='Pragma' CONTENT='no-cache'>");
   bigpic.document.write("<META HTTP-EQUIV='Expires' CONTENT='Fri, Jun 12 1981 08:20:00 GMT'>");

   bigpic.document.write("<script language='javaScript1.2'>");
   bigpic.document.write("function realsize() {");
   bigpic.document.write("   var NS = (window.innerWidth)?true:false;");
   bigpic.document.write("   var pic = document.getElementById('picture');");
   bigpic.document.write("   var xsize = (NS)?window.innerWidth:document.body.clientWidth;");
   bigpic.document.write("   var ysize = (NS)?window.innerHeight:document.body.clientHeight;");
   var extrawidth = 40;
   var extraheight = 105;
   if (param1 == 'copyright' || param2 == 'copyright') {extraheight = 175;}
   bigpic.document.write("   var xsize = Math.max(document.images.plaatje.width, 250) - xsize + " + extrawidth + ";");
   bigpic.document.write("   var ysize = document.images.plaatje.height - ysize + " + extraheight + ";");
   bigpic.document.write("   var torso = document.getElementById('torso');");
   bigpic.document.write("   window.resizeBy(xsize,ysize)\;");
   bigpic.document.write("   if (document.images.plaatje.width > 222) { pic.style.textAlign = 'left'; }");
   bigpic.document.write("   torso.style.width = ((NS)?window.innerWidth:document.body.clientWidth) - 28;");
   bigpic.document.write("}");
   bigpic.document.write("</script>");
   bigpic.document.write("</head>");
   bigpic.document.write("<body onLoad='realsize(); window.focus();'>");
   bigpic.document.write("<div style='margin:14px; text-align: left;' id='torso'>");
   bigpic.document.write("   <table border=0 cellspacing=0 cellpadding=0>");
   bigpic.document.write("   <tr>");
   bigpic.document.write("      <td class='kalelink'><a href='javascript:window.close();'><img src='/library/images/venster_sluiten.gif' border=0 hspace=0 vspace=0></a></td>");
   bigpic.document.write("      <td width='5'>&nbsp;</td>");
   bigpic.document.write("      <td class='kalelink'><a href='javascript:window.close();'>Sluit&nbsp;dit&nbsp;venster</a></td>");
   //if (param1 == 'print' || param2 == 'print') {
      bigpic.document.write("      <td width='10'>&nbsp;</td>");
      bigpic.document.write("      <td class='kalelink'><a href='javascript:this.print();'><img src='/library/images/printertje.gif' border=0 hspace=0 vspace=0></a></td>");
      bigpic.document.write("      <td width='5'>&nbsp;</td>");
      bigpic.document.write("      <td class='kalelink'><a href='javascript:this.print();'>Print&nbsp;dit&nbsp;venster</a></td>");
   //}
   bigpic.document.write("   </tr>");
   bigpic.document.write("   </table>");
   bigpic.document.write("   <p>");
   bigpic.document.write("   <div style='text-align:center;' id='picture'>");
   bigpic.document.write("      <img src="+plaat+" name='plaatje' class='realimage' border=0 vspace=0 hspace=0>");
   bigpic.document.write("   </div><!-- <br clear=all> -->");
   if (param1 == 'copyright' || param2 == 'copyright') {
      bigpic.document.write("<div style='width: 100%; height: 1px; margin-top: 14px; border-top: solid 1px #999999; color: #999999;'>");
      bigpic.document.write("&#169; KNMI</div>");
   }
   bigpic.document.write("</div>");
   bigpic.document.write("</body>");
   bigpic.document.write("</html>");
   bigpic.document.close();
}
}


