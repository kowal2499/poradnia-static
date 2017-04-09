var eventsDatabase = [    

                            

                            // {
                            //        date: "13-17.02.2017",
                            //        action: "<p><a href='extra/ferie-z-poradnia.html'>Ferie z Poradnią<br><img src='img/ferie-z-poradnia-mini.jpg' style='margin-top: 10px; width: 40%;'></a></p>"
                            // },

                            // {
                            //        date: "08.03.2017 godz. 16:30",
                            //        action: "<p><a href='subpages/pomocDlaRodzicówSzkoła.html#szkola-cz-2'>'Szkoła dla Rodziców' cz. II – Rodzeństwo bez rywalizacji<br><img src='img/mini-szkola-ii.jpg' style='margin-top: 10px; width: 40%;'></a></p>"
                            // },

                            // {
                            //        date: "09.03.2017 godz. 17:00",
                            //        action: "<p><a href='extra/emocje.html'>'Jak pomóc dziecku w radzeniu sobie z emocjami?' - spotkanie 1</a></p>"
                            // },

                            // {
                            //        date: "16.03.2017 godz. 17:00",
                            //        action: "<p><a href='extra/emocje.html'>'Jak pomóc dziecku w radzeniu sobie z emocjami?' - spotkanie 2</a></p>"
                            // },

                            // {
                            //        date: "23.03.2017 godz. 17:00",
                            //        action: "<p><a href='extra/emocje.html'>'Jak pomóc dziecku w radzeniu sobie z emocjami?' - spotkanie 3</a></p>"
                            // },

                            // {
                            //        date: "04.04.2017 godz. 17:00",
                            //        action: "<p><a href='extra/grupa-rozwoju-zawodowego-logopedow.html'>'Grupa Rozwoju Zawodowego Logopedów Przedszkolnych i Szkolnych'<br><img src='img/dziecko-mówi.jpg' style='margin-top: 10px; width: 40%;'></a></p>"
                            // },

                            {
                                   date: "19.05.2017 godz. 11:00",
                                   action: "<p><a href='extra/socjoterapeuci-05.html'>'Sieć współpracy i samokształcenia dla socjoterapeutów' - Spotkanie podsumowujące<br><img src='img/siec_wspolpracy_mini.jpg' style='margin-top: 10px; width: 40%;'></a></p>"
                            }
                            
                            
                            // {
                            //        date: "04.10.2016, godz. 16.00",
                            //        action: "<p>Spotkanie organizacyjne dla uczestników <strong>'SZKOŁY DLA RODZICÓW, czyli jak mówić, żeby dzieci nas słuchały i jak słuchać, żeby dzieci do nas mówiły.'</strong> - edycja 2016/2017</p>"
                            // },


                           
                            // {
                            //        date: "13.10.2016 godz. 17:00",
                            //        action: "<p>Szkolenie dla logopedów.</p>"
                            // },

                            

                            // {
                            //        date: "09.12.2016 godz. 11:30",
                            //        action: "<p><a href='extra/siec-wsparcia-02.html'>Sieć współpracy i samokształcenia dla socjoterapeutów.</a></p>"
                            // } 
                            
                            // {
                            //        date: "24.10.2016 godz. 15:00",
                            //        action: "<p>'Bystrzaki - przedszkolaki' - spotkanie organizacyjne dla rodziców</p>"
                            // }

                            

                            // {
                            // date: "15/10/2015",
                            // action: '<a href="#popupWindow" onclick="attachHTML(\'' + newsDatabase[0].lightboxHTML + '\')">Szkolenie dla logopedów pt. \'Jak skutecznie pokonać jąkanie?\'</a>'
                            // },
                            
 
                            // {
                            // date: "01/10/2015",
                            // action: "<a href='subpages/pomocDlaRodzicówSzkoła.html'>Spotkanie organizacyjne I edycji \"Szkoły dla Rodziców i Wychowawców\"</a>"
                            // },

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