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

                            {
                                   date: "17/02/2017",
                                   action: "<a href='extra/ferie-z-poradnia-2017/ferie.html'>Ferie z Poradnią 2017 - FOTORELACJA<br><img src='img/ferie-z-poradnia-mini.jpg' style='margin-top: 10px; width: 120px;'></a>"
                            },

                            {
                                   date: "01/09/2016",
                                   action: "<a href='download/wspomaganie.pdf' download>Artykuł na temat wspomagania szkół/przedszkoli/placówek<img src='img/wspomaganie2016.jpg' style='margin-top: 10px; width: 120px;'></a>"
                            },

                            // {
                            //        date: "03/04/2016",
                            //        action: "<a href='https://prezi.com/eibtmyxztygo/jak-chwalic-dziecko/'>Chwalić dziecko też trzeba umieć! - zapraszamy do zapoznania się z prezentacją:<br><img src='img/praise.jpg' style='margin-top: 10px;'></a>"
                            // },

                            {
                                   date: "16/02/2016",
                                   action: "<a href='extra/konferencja2016/konferencja.html'>Materiały z II-giej Powiatowej Konferencji nt.: \"Depresja, samookaleczenia, \
                                   ADHD, autyzm – jak pomóc?\"<br><img src='img/news-konferencja01.jpg' style='margin-top: 10px;'></a>"
                            }


                     ];

function generateEventsBoard() {

    var elm = document.getElementById("past-eventsBoard");
    var html = ""

    for (evnt=0; evnt<eventsDatabase.length; evnt++) {
        html += "<div class=\"event\">";
        html += "   <span class=\"glyphicon glyphicon-calendar\" aria-hidden=\"true\"></span><span class=\"eventDate\">" + eventsDatabase[evnt].date + "</span><br />";
        html += "<div class='eventDesc'>"+eventsDatabase[evnt].action+"</div>";
        html += "</div>";
    }
    elm.innerHTML = html;
}


generateEventsBoard()