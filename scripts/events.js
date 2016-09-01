var eventsDatabase = [    
                            /*{
                            date: "15/10/2015",
                            action: '<a href="#popupWindow" onclick="attachHTML(\'' + newsDatabase[0].lightboxHTML + '\')">Szkolenie dla logopedów pt. \'Jak skutecznie pokonać jąkanie?\'</a>'
                            },*/
                            
 
                            /*{
                            date: "01/10/2015",
                            action: "<a href='subpages/pomocDlaRodzicówSzkoła.html'>Spotkanie organizacyjne I edycji \"Szkoły dla Rodziców i Wychowawców\"</a>"
                            },*/

                            // {
                            //        date: "19/12/2015",
                            //        action: "Z dniem 19/12/2015 <strong>kończymy przyjmowanie zapisów</strong> na II Powiatową Konferencję nt. \"Depresja, samookaleczenia, ADHD, autyzm – jak pomóc?\""
                            // },

                            // {
                            //        date: "12/02/2016",
                            //        action: "<a href='subpages/pomocDlaRodzicówKonferencja.html'>II Powiatowa Konferencja nt.: \"Depresja, samookaleczenia, \
                            //        ADHD, autyzm – jak pomóc?\"<img src='img/news-konferencja01.jpg' style='margin-top: 10px;'></a>"
                            // }

                            // {
                            //        date: "25/02/2016",
                            //        action: "<a href='subpages/pomocDlaRodzicówSzkoła.html#szkola-cz-2'>Spotkanie informacyjne dla uczestników &bdquo;Szkoły dla Rodziców i Wychowawców&rdquo; cz.II – Rodzeństwo bez rywalizacji!<img src='img/rodzenstwo-mini.jpg' style='margin-top: 10px;'></a>"
                            // }

                            // {
                            //        date: "21/04/2016, godz. 17:00",
                            //        action: "<p>Szkolenie dla logopedów przedszkolnych i szkolnych: &quot;Ćwiczenia artykulacyjne w terapii logopedycznej. Jak skutecznie je prowadzić?&quot;</p><img src='img/dziecko-mówi.jpg' style='margin-top: 10px; width: 100px;'>"
                            // }


                     ];

function generateEventsBoard() {

	var elm = document.getElementById("eventsBoard");
	var html = ""

	for (evnt=0; evnt<eventsDatabase.length; evnt++) {
		html += "<div class=\"event\">";
		html +=	"	<span class=\"glyphicon glyphicon-calendar\" aria-hidden=\"true\"></span><span class=\"eventDate\">" + eventsDatabase[evnt].date + "</span><br />";
		html += "<div class='eventDesc'>"+eventsDatabase[evnt].action+"</div>";
		html += "</div>";
	}
	elm.innerHTML = html;

       if (eventsDatabase.length == 0) {
              $('#comming-events').hide();
       }
}


generateEventsBoard()