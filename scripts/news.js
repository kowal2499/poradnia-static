
function createNavigationConsole3(selection, totalNo) {
    var intSelection = Number(selection);

    var buttons = [];
       
    var start = 0;
    var end = 0;
    var leftSideEnd;

    if (totalNo <= 9) {
        for (i=1; i<10; i++) {
            buttons.push(i);
        }
    } else 

    // przypadek "skrajny lewy"

    if (intSelection <= 5) {
        for (i=1; i<8; i++) {
            buttons.push(i);
        }
        buttons.push('..');
        buttons.push(totalNo);
    } else

    // przypadek "skrajny prawy"

    if (intSelection >= totalNo-4) {
        buttons.push('1');
        buttons.push('..');
        for (i=totalNo-6; i<=totalNo; i++) {
            buttons.push(i);
        }
    }

    // przypadek "środkowy"

    if ((intSelection > 5) && (intSelection < totalNo-4)) {
        buttons.push('1');
        buttons.push('..');
        for (i=intSelection-2; i<=intSelection+2; i++) {
            buttons.push(i);
            console.log(i);
        }
        buttons.push('..');
        buttons.push(totalNo);   
    }


    html = '<ul>';
        for (k=0; k<buttons.length; k++) {
                if (intSelection == buttons[k]) {
                    style = ' class="selected"'; 
                }
                else {
                    style = '';
                }
            html += "<li" + style  +">" + buttons[k] +'</li>';
        }
    html += '</ul>';
    // apply changes
    var obj = document.getElementsByClassName("navigation")[0];
    obj.innerHTML = html + "<div style='clear: both'></div>";
    // add event handlers
    liItems = document.getElementsByClassName("navigation")[0].getElementsByTagName("li");
    for (i=0; i<liItems.length; i++) {
        liItems[i].onclick = function() {

            var txt;
            if (isNaN(this.innerHTML)) {
                txt = ": to nie jest liczba";
            } else {
                // a number was clicked, so jump
                intSelection = this.innerHTML;
                updateNews(this.innerHTML);
            }
        }
    }
}



function attach(img) {
        var elm = document.getElementById("lightboxCanvas");
        elm.innerHTML='';
        var elm2 = document.getElementById("lightboxImgOnly");
        elm2.innerHTML = "<img src='" + img + "' class='img-responsive' />";
}
function attachHTML(content) {
        var elm = document.getElementById("lightboxCanvas");
        //content = "<div style='border: 1px solid gray; margin: 10px; padding: 10px; color: red'>romek</div>"
        elm.innerHTML = content;
        var elm2 = document.getElementById("lightboxImgOnly");
        elm2.innerHTML = '';
}

function composeNews(title, date, image, content, ifLightbox, lightboxImg, lightboxHTML) {
    var txt="";



    txt += '    <div class="row" style="padding-left: 20px; padding-right: 20px;">';
    txt += '        <div class="col-sm-12">';
    txt += '            <div class="newsWindowDateField">' + date + '</div>';
    txt += '        </div>';
    txt += '    </div>';
    txt += '    <div class="row" style="padding-left: 20px; padding-right: 20px;">';
    txt += '        <div class="col-sm-12">';
    if (ifLightbox) {

        if (lightboxImg) {
            txt += '            <div class="newsWindowTitleBar"> <a href="#popupWindow" onclick="attach(\'' + lightboxImg +'\')">' + title + '</a></div>';

        }
        if (lightboxHTML) {
            txt += '            <div class="newsWindowTitleBar"> <a href="#popupWindow" onclick="attachHTML(\'' + lightboxHTML + '\')">' + title + '</a></div>';
        }


    } else {
    txt += '            <div class="newsWindowTitleBar">' + title + '</div>';
    }
    txt += '        </div>';
    txt += '    </div>';

    txt += '    <div class="row" style="padding-left: 20px; padding-right: 20px;">'
    txt += '        <div class="col-xs-12 col-sm-3">';
    if (ifLightbox) {
    txt += '            <div class="newsWindowImg"> <a href="#popupWindow" onclick="attach(\'' + lightboxImg +'\')">' + image + '</a></div>';
    } else {
    txt += '            <div class="newsWindowImg">' + image + '</div>';
    }
    txt += '        </div>';

    if (image) {    // jeśli mamy obrazek to zróbmy dla niego miejsce
        txt += '        <div class="col-xs-12 col-sm-9">';
    } else {
        txt += '        <div class="col-xs-12 col-sm-10">';
    }
    txt +=              '<div class="newsWindowMessage" style="border-left: 1px solid #89AB93;">' + content + '</div>';
    txt += '        </div>';
    txt += '    </div>';
    txt += '<hr />'

    return txt;

    }



function updateNews(screenNum) {


    var start = 0;
    var end = newsDatabase.length;

    var content = '';
    
    for (recordNo = 0; recordNo<end; recordNo++) {
        content = content + composeNews(newsDatabase[recordNo].title,
                    newsDatabase[recordNo].date,
                    newsDatabase[recordNo].img,
                    newsDatabase[recordNo].txt,
                    newsDatabase[recordNo].lightboxContent,
                    newsDatabase[recordNo].lightboxImgOnly,
                    newsDatabase[recordNo].lightboxHTML
                    );
    }
    document.getElementById("newsField").innerHTML = content;
};



function updateNews2(screenNum) {

}

    var previousintSelection = 1;
    var newsDatabase = [    
                            // {
                            // title: "<a href='subpages/pomocDlaRodzicówSzkoła.html#szkola-cz-2'>Rusza &bdquo;Szkoła dla Rodziców i Wychowawców&rdquo; cz.II – Rodzeństwo bez rywalizacji!</a>",
                            // date: "03/02/2016",
                            // img: "<a href='subpages/pomocDlaRodzicówSzkoła.html#szkola-cz-2'><img src='img/rodzenstwo-mini.jpg' class='img-responsive' alt='dwie dziewczynki trzymające się za ręce'/></a>",
                            // txt: "Serdecznie zapraszamy absolwentów &bdquo;Szkoły dla Rodziców i Wychowawców&rdquo; cz. I do udziału w kolejnej części - <strong>Rodzeństwo bez rywalizacji</strong> - organizowanej na terenie poradni. <a href='subpages/pomocDlaRodzicówSzkoła.html#szkola-cz-2'>&raquo;Kliknij tutaj&laquo;</a> aby uzyskać więcej informacji.",

                            // lightboxContent: false,
                            // lightboxImgOnly: '',
                            // lightboxHTML: ''
                            // },
                            {
                            title: "<a href='extra/konferencja2016/konferencja.html'>II Powiatowa Konferencja już za nami...</a>",
                            date: "16/02/2016",
                            img: "<a href='extra/konferencja2016/konferencja.html'><img src='img/news-konferencja01.jpg' class='img-responsive'/></a>",
                            txt: "<p>Dziękujemy prelegentom za przyjęcie zaproszenia, wyczerpujące i atrakcyjne przybliżenie nam wskazanej problematyki, jak również wszystkim przybyłym gościom i uczestnikom.</p><p><a href='extra/konferencja2016/konferencja.html'>Zachęcamy do obejrzenia zdjęć z konferencji, jak również zapoznania się z prezentacją multimedialną p. Artura Kołakowskiego „ADHD -  skuteczne prowadzenie dziecka z ADHD”.</a></p>",

                            lightboxContent: false,
                            lightboxImgOnly: '',
                            lightboxHTML: ''
                            },

                            {
                            title: "<a href='subpages/pomocDlaRodzicówKonferencja.html'>Ostatnie wolne miejsca na II Powiatową Konferencję</a>",
                            date: "11/01/2016",
                            img: "<a href='subpages/pomocDlaRodzicówKonferencja.html'><img src='img/news-konferencja01.jpg' class='img-responsive'/></a>",
                            txt: "<p>W imieniu Poradni Psychologiczno-Pedagogicznej w Białogardzie oraz Starostwa Powiatowego w Białogardzie chcemy poinformować, \
                            że istnieje jeszcze możliwość zapisów na <a href='subpages/pomocDlaRodzicówKonferencja.html'>II Powiatową Konferencję na temat \"Depresja, samookaleczenia, ADHD, autyzm – jak pomóc?\"</a>. \
                            </p><p>Wszystkich zainteresowanych zapraszamy do kontaktu osobistego z sekretariatem poradni lub pod numerem telefonu 94 312 25 96, \
                            kom. 515 082-620.</p>\
                            <p>Jednocześnie przypominamy osobom zapisanym na konferencję o potrzebie wpłaty 150&nbsp;złotych do 05.02.2016r. na konto poradni:</p>\
                            <p style='text-align: center; font-weight: bold;'>72 1240 3666 1111 0000 4344 7880</p>",

                            lightboxContent: false,
                            lightboxImgOnly: '',
                            lightboxHTML: ''
                            },

                            {
                            title: "<a href='porady/article014.html'>Nowy artykuł: \"Samookaleczenia - moda czy coś więcej?\"</a>",
                            date: "02/01/2016",
                            img: "<a href='porady/article014.html'><img src='img/blade-mini.jpg' class='img-responsive'/></a>",
                            txt: "Zapraszamy do zapoznania się z nowym artykułem na temat:<br> <a href='porady/article014.html'>\"Samookaleczenia – moda czy coś więcej?\"</a>",

                            lightboxContent: false,
                            lightboxImgOnly: '',
                            lightboxHTML: ''
                            },

                            {
                            title: "Wesołych Świąt !",
                            date: "17/12/2015",
                            img: "<img src='img/christmas-card-mini.jpg' class='img-responsive'/>",
                            txt: "Z okazji Świąt Bożego Narodzenia wielu głębokich i radosnych przeżyć, wewnętrznego spokoju i radości oraz wszelkiej pomyślności w każdym dniu nadchodzącego Roku życzą pracownicy Poradni Psychologiczno-Pedagogicznej w Białogardzie.",

                            lightboxContent: true,
                            lightboxImgOnly: 'img/christmas-card.jpg',
                            lightboxHTML: ''
                            },

                            {
                            title: "<a href='subpages/pomocGrupowe.html#harmonogram'>Harmonogram zajęć grupowych dla dzieci i młodzieży</a>",
                            date: "23/10/2015",
                            img: "",
                            txt: "Od października 2015 roku rozpoczęły się w Poradni Psychologiczno-Pedagogicznej w Białogardzie zajęcia grupowe dla dzieci i "+ 
                                 "młodzieży. Cieszą się one dużym zainteresowaniem. Przedstawiamy <a href='subpages/pomocGrupowe.html#harmonogram'>harmonogram</a> zajęć.",
                            lightboxContent: false,
                            lightboxImgOnly: '',
                            lightboxHTML: ''
                            },

                            {
                            title: "<a href='porady/article013.html'>Nowy artykuł: \"Nadpobudliwość psychoruchowa u dzieci\"</a>",
                            date: "22/10/2015",
                            img: "<a href='porady/article013.html'><img src='img/article13mini.jpg' class='img-responsive'/></a>",
                            txt: ""+
                            "<p>Temat nadpobudliwości psychoruchowej nurtuje wielu rodziców i nauczycieli, w związku z tym zapraszamy do przeczytania <a href='porady/article013.html'>artykułu</a> na ten temat i do uczestnictwa "+
                            "w <strong><a href='subpages/pomocDlaRodzicówKonferencja.html'>II Powiatowej Konferencji organizowanej przez Poradnię Psychologiczno-Pedagogiczną w Białogardzie i Starostwo Powiatowe w Białogardzie w dniu 12.02.2016r.</a></strong>, "+
                            "gdzie gościem będzie autorytet w tej dziedzinie dr n. med. Artur Kołakowski.",

                            lightboxContent: false,
                            lightboxImgOnly: '',
                            lightboxHTML: ''
                            },

                            {
                            title: "<a href='porady/article012.html'>Nowy artykuł: \"Kiedy nic się nie chce...\"</a>",
                            date: "21/10/2015",
                            img: "<a href='porady/article012.html'><img src='img/news-depresja.jpg' class='img-responsive'/></a>",
                            txt: "<p>Pragnąc zasygnalizować istnienie problemu depresji u dzieci i nastolatków przedstawiamy nowy artykuł pt. <a href='porady/article012.html'>\"Kiedy nic się nie chce...\"</a></p><p>Jednocześnie zachęcamy wszystkich nauczycieli, rodziców i osoby chcące głębiej się zapoznać z zagadnieniem depresji wśród dzieci i młodzieży do wzięcia  udziału w "+
                                 "<strong><a href='subpages/pomocDlaRodzicówKonferencja.html'>II Powiatowej Konferencji organizowanej przez Poradnię Psychologiczno-Pedagogiczną w Białogardzie i Starostwo Powiatowe w Białogardzie w dniu 12.02.2016r.</a></strong></p><p>Wykład na temat depresji wygłosi mgr Małgorzata Łuba.",

                            lightboxContent: false,
                            lightboxImgOnly: '',
                            lightboxHTML: ''
                            },

                            {
                            title: "Szkolenie na temat: \"Jak skutecznie pokonać jąkanie?\"",
                            date: "01/10/2015",
                            img: "",
                            txt: "Zapraszamy wszystkich logopedów pracujących w przedszkolach i szkołach na kolejne szkolenie na temat: \"Jak skutecznie pokonać jąkanie?\", które odbędzie się 15 października 2015 roku o godzinie 17.00 w Poradni Psychologiczno-Pedagogicznej w Białogardzie.",
                            lightboxContent: true,
                            lightboxImgOnly: '',
                            lightboxHTML: ''+

                            '<div style=\\\'margin: 10px; border-radius: 7px; border: 1px solid gray;\\\'>'+
                            '   <div class=\\\'myTitle\\\' style=\\\'width: 80%; margin-bottom: 30px;\\\'>Szkolenie na temat: \\\'Jak skutecznie pokonać jąkanie?\\\'</div>'+
                            '   <img src=\\\'img/logopedzi.jpg\\\' width=80% />'+
                            '   <div style=\\\'margin:20px; \\\'>'+

                            '   <p>W Poradni Psychologiczno-Pedagogicznej w Białogardzie odbywają się cykliczne spotkania logopedów pracujących w przedszkolach i szkołach'+
                            '   Miasta i Gminy Białogard, Miasta i Gminy Karlino oraz Miasta i Gminy Tychowo z logopedami pracującymi w białogardzkiej poradni (tzw. Grupa Rozwoju Zawodowego Logopedów Przedszkolnych i Szkolnych).</p><p>Ostatnie spotkanie'+
                            '   miało miejsce w połowie maja 2015 roku. Była to okazja, aby wymienić się doświadczeniami,'+
                            '   wspólnie ustalić sposoby postępowania terapeutycznego.</p><p>W pierwszej części szkolenia neurologopeda z PPP Maria Jonko przedstawiła prezentację \\\'Emisja głosu'+ 
                            '   – ćwiczenia dla przedszkolaka i ucznia, jak je prawidłowo prowadzić?\\\'. Zebrane osoby miały okazję, aby przypomnieć sobie zagadnienia związane z pracą nad '+
                            '   emisją głosu - prowadzącą do uzyskania: odpowiedniej dźwięczności i nośności emitowanego dźwięku, odpowiedniej stabilności i jednolitości wydobywanego dźwięku '+
                            '   uwarunkowanym podparciem oddechowym, prawidłowej dykcji, ekspresji słowa oraz sugestywności głosu.</p><p>Blok ćwiczeń praktycznych przeprowadziła z kolei neurologopeda '+
                            '   z PPP Małgorzata Weiszewska - uczestniczki miały się zrelaksować i wsłuchać w swój oddech. Były też ćwiczenia ekonomicznego zużywania powietrza, uruchamiające '+
                            '   rezonatory oraz pobudzające do pracy przeponę. Rozmawiano także o znaczeniu wykorzystania wizualizacji w czasie terapii mowy. Uczestniczki spotkania otrzymały '+
                            '   zestaw materiałów do ćwiczeń dla osób pracujących głosem i nad głosem.</p>'+
                            '   <p><strong>Zapraszamy wszystkich logopedów pracujących w przedszkolach i szkołach na kolejne szkolenie na temat: \\\'Jak skutecznie pokonać jąkanie?\\\', które odbędzie się '+
                            '   15 października 2015 roku o godzinie 17.00 w Poradni Psychologiczno-Pedagogicznej w Białogardzie</strong> /na parterze budynku/. Prowadzić je będą neurologopedzi z '+
                            '   tutejszej poradni: H.Górzyńska, M.Jonko, M.Weiszewska.</p>'+
                            '   <p style=\\\'text-align: center; margin: 30px;\\\'>SERDECZNIE ZAPRASZAMY</p>'+
                            '   <p style=\\\'text-align: right;\\\'>Maria Jonko, Małgorzata Weiszewska - neurologopedzi</p>'+
                            '</div>'+
                            '</div>' 
                                                        
                            },

                            {
                            title: "Nowa edycja \"Szkoły dla Rodziców\"",
                            date: "14/09/2015",
                            img: "<img src='./img/szkołaDlaRodziców2015mini.jpg' class='img-responsive'/>",
                            txt: "Serdecznie zapraszamy rodziców chcących rozwijać swoje umiejętności wychowawcze na zajęcia \"Szkoła dla Rodziców\" organizowane na terenie poradni. <a href='subpages/pomocDlaRodzicówSzkoła.html'>Kliknij tutaj</a> aby uzyskać więcej informacji.",
                            lightboxContent: true,
                            lightboxImgOnly: 'img/szkoladlarodzicow.jpg',
                            lightboxHTML: ''
                            },

                            {
                            title: "Życzenia na nowy rok szkolny",
                            date: "01/09/2015",
                            img: "<img src='./img/news-rokszkolny.jpg' class='img-responsive'/>",
                            txt: "<div>W imieniu wszystkich pracowników Poradni życzymy, aby nowy rok szkolny stał się dla uczniów okazją do rozwijania swoich umiejętności, dla rodziców - sposobnością do odkrywania mocnych stron dzieci, a dla nauczycieli - czasem obfitującym w satysfakcję z pracy pedagogicznej.</div>",
                            lightboxContent: true,
                            lightboxImgOnly: 'img/rokszkolny2015-2016_big.jpg',
                            lightboxHTML: ''
                            },

                            {
                            title: "Nowa oferta Poradni",
                            date: "31/08/2015",
                            img: "<img src='./img/news-oferta.jpg' class='img-responsive'/>",
                            txt: "Zapraszamy do zapoznania się z ofertą Poradni na rok szkolny 2015/2016. Pełny jej opis zawarliśmy w zakładce <a href='subpages/zadania.html'>\"Oferta\"</a>. Można także pobrać plik \"pdf\" z całą ofertą Poradni <a href='download/ofertaPoradni_2015-2016.pdf' download> >> klikając tutaj <<</a>.",
                            lightboxContent: false,
                            lightboxImgOnly: '',
                            lightboxHTML: ''
                            },

                            {
                            title: "Konferencja powiatowa",
                            date: "17/08/2015",
                            img: "<img src='./img/news-konferencja01.jpg' class='img-responsive'/>",
                            txt: 'Starostwo Powiatowe w Białogardzie oraz Poradnia Psychologiczno-Pedagogiczna w Białogardzie serdecznie zapraszają nauczycieli, wychowawców, rodziców i wszystkich zainteresowanych do udziału w II Powiatowej Konferencji '+
                                 'nt.: <div style="font-weight: bold; margin:10px; text-align: center;">"Depresja, samookaleczenia, ADHD, autyzm – jak pomóc?"</div>'+
                                 '<p>która odbędzie się w dniu <strong>12.02.2016r</strong>. (ostatni piątek ferii zimowych) w Centrum Kultury i Spotkań Europejskich w Białogardzie, ul. 1-go Maja 15.' +
                                 '</p><a href="subpages/pomocDlaRodzicówKonferencja.html">>> Kliknij tutaj <<</a> dla uzyskania dalszych informacji.',
                            lightboxContent: true,
                            lightboxImgOnly: 'img/depresja-plakat-big.jpg',
                            lightboxHTML: ''
                            }
                        ];


    updateNews(1);

