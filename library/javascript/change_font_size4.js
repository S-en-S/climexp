var cookie_name = "font_size";
var font_clicks = 0;
var initialized = false;

function init_prefs() {
// initialize user preferences
  var cookie = GetCookie(cookie_name);
  var teller = 0;
  if (cookie != null) {
     font_cookie = unescape(cookie);
     cookie_elements = font_cookie.split(",");
     for (teller=0; teller<cookie_elements.length; teller++) {
        cookie_element = cookie_elements[teller].split(":");
        if (cookie_element[0] == "fontclicks") font_clicks = cookie_element[1] -1 +1;
     }
//     DeleteCookie(cookie_name);
     changeFontSize(font_clicks);
  }
}

function make_cookie() {
// save the new values for the user preferences
   var nextyear=new Date();

   nextyear.setFullYear(nextyear.getFullYear()+1);
   var font_cookie = escape("fontclicks:"+font_clicks);
   SetCookie(cookie_name,font_cookie,nextyear,"/");
}


function changeFontSize(increment) {
/////////////////////////////////////////////////////////////////////
//                                                                 //
//  Deze functie bekijkt elke selector in de eerste stylesheet die //
//  met het document is geassocieerd. Als er voor een selector een //
//  fontsize is opgegeven, wordt die met <increment> pixels        //
//  verhoogd. Vervolgens wordt er gekeken of het document frames   //
//  bevat. Is dat het geval, dan worden ook de stylesheets van die //
//  frames gecontroleerd op de aanwezigheid van selectoren met een //
//  fontsize, die dan ook met <increment> pixels wordt verhoogd.   //
//                                                                 //
//  N.B.: Elk frame (of iframe) *moet* een stylesheet hebben,      //
//  anders loopt MSIE er op stuk.                                  //
//                                                                 //
//  20060607, Bert van Dijk, KNMI                                  //
//                                                                 //
/////////////////////////////////////////////////////////////////////

   var pClass;
   var fontSz;
   var myRules;
//
// MSIE noemt 'cssRules' 'rules'
//
   MSIERules = (document.styleSheets[0].rules);
   myRules = MSIERules ? document.styleSheets[0].rules : document.styleSheets[0].cssRules;
//
// Loop langs alle selectors
//
   for (i = 0; i < myRules.length; i++) {
       if (MSIERules) {
//
//        The MSIE way
//
          selector = myRules.item(i).selectorText.toUpperCase();
//
//        Is er een font size gespecificeerd?
//
          if (myRules.item(i).style.fontSize) {
//
//           Haal 'm op, hoog 'm op, schrijf 'm weg (Rawhide!)
//           Die "- 1 + 1"-truuk is om JavaScript te vertellen dat het gaat om een getal, 
//           niet om een string (je kunt van een string geen 1 aftrekken)
//
             fontSz = myRules.item(i).style.fontSize.substr(0, myRules.item(i).style.fontSize.length-2) - 1 + 1 + increment;
             if (font_clicks > -9  || increment > 0) {
//
//              Font size 1 pixel is de ondergrens, en we maken hem maximaal 9 pixels kleiner dan normaal.
//
                fontSzStr = fontSz+"px";
                if (document.styleSheets[0]) {
                   document.styleSheets[0].rules.item(i).style.fontSize = fontSzStr;
                }
             }
          }
       } else {
//
//        The way of the world
//
          pClass = myRules.item(i);
//
//        Font size gespecificeerd?
//
          if (myRules.item(i).style.fontSize) {
//
//           Ophalen, ophogen, wegschrijven
//
             fontSz = pClass.style.fontSize.substr(0, pClass.style.fontSize.length-2);
             if (document.styleSheets[0]) {
                if (font_clicks > -9  || increment > 0) {
//
//                 Ondergrens is 1px
//
                   fontSz = fontSz - 1 + 1 + increment;
                   fontSzStr = fontSz+"px";

                   document.styleSheets[0].cssRules.item(i).style.fontSize = fontSzStr;
                }
             }
          }
       } 
   }
//
// Doe dezelfde truc nog een keer voor alle frames en iframes in de pagina
//
   if (window.frames && initialized) { 
//
//    Dit hoeft alleen als er echt op een knop is geklikt. De initialisatie, waarbij de
//    font-grootte van de vorige keer wordt opgehaald, wordt door elk frame afzonderlijk geregeld.
//
      for (frmcnt = 0; frmcnt < window.frames.length; frmcnt++) {  
          frm = window.frames[frmcnt];
          if (frm.document.styleSheets[0]) {
             myRules = MSIERules ? window.frames[frmcnt].document.styleSheets[0].rules : window.frames[frmcnt].document.styleSheets[0].cssRules;

             for (i = 0; i < myRules.length; i++) {
                 if (MSIERules) {
                    selector = myRules.item(i).selectorText.toUpperCase();
                    if (myRules.item(i).style.fontSize) {
                       fontSz = myRules.item(i).style.fontSize.substr(0, myRules.item(i).style.fontSize.length-2) - 1 + 1 + increment;
                       if (font_clicks > -9  || increment > 0) {
                          fontSzStr = fontSz+"px";
                          if (window.frames[frmcnt].document.styleSheets[0]) {
                             window.frames[frmcnt].document.styleSheets[0].rules.item(i).style.fontSize = fontSzStr;
                          }
                       }
                    }
                 } else {
                    pClass = myRules.item(i);
                    if (myRules.item(i).style.fontSize) {
                       fontSz = pClass.style.fontSize.substr(0, pClass.style.fontSize.length-2);
                       if (window.frames[frmcnt].document.styleSheets[0]) {
                          if (font_clicks > -9  || increment > 0) {
                             fontSz = fontSz - 1 + 1 + increment;
                             fontSzStr = fontSz+"px";

                             window.frames[frmcnt].document.styleSheets[0].cssRules.item(i).style.fontSize = fontSzStr;
                          }
                       }
                    }
                 }
             }
          }
      }
   }
   if (initialized) {
//
//    Alleen als er echt op een knop geklikt is hoeft er een nieuwe cookie te worden gemaakt.
//    Als de pagina voor de eerste keer wordt opgevraagd hoeft alleen de bestaande cookie te worden ingelezen.
//
//    Hij kan maximaal 9 pixels kleiner worden gemaakt.
//
      font_clicks = Math.max(-9,(font_clicks + increment));
      make_cookie();
   } else {
      initialized = true;
   }
}

function resetFontSize() {
   changeFontSize(-font_clicks);
}

