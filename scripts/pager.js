



function createNavigationConsole4(selection) {
    var buttons = [];
       
    buttons.push('&lt;'); // pierwsza cegiełka ze znaczkiem '<'
    if (pagesNumber < 10) {
        for (i=1; i<=pagesNumber; i++) {
            buttons.push(i);
        }
    } else {

        // przypadek "skrajny lewy"

        if (selection <= 5) {
            for (i=1; i<8; i++) {
                buttons.push(i);
            }
            buttons.push('..');
            buttons.push(pagesNumber);
        } else {

            // przypadek "skrajny prawy"

            if (selection >= pagesNumber-4) {
                buttons.push('1');
                buttons.push('..');
                for (i=pagesNumber-6; i<=pagesNumber; i++) {
                    buttons.push(i);
                }
            } else {
        
                // przypadek "środkowy"

                if ((selection > 5) && (selection < pagesNumber-4)) {
                    buttons.push('1');
                    buttons.push('..');
                    for (i=selection-2; i<=selection+2; i++) {
                        buttons.push(i);
                    }
                    buttons.push('..');
                    buttons.push(pagesNumber);   
                }
            }
        
        }
    }
    buttons.push('&gt;');   // końcowa cegiełka, ze znaczkiem '>'

    // definiujemy kod html
    html = '<div class="myPager"><ul>';
        for (k=0; k<buttons.length; k++) {
                if (selection == buttons[k]) {
                    style = ' class="pageSelected"'; 
                }
                else {
                    style = '';
                }
            // nie dawaj cegiełce atrybutu 'a' jeśli to '..' lub '<' jeśli wybrano 1 element lub '>' jeśli wybrano ostatni element
            if ((buttons[k] == "..") || ((buttons[k] == '&lt;') && (selection==1)) || ((buttons[k] == '&gt;') && (selection==pagesNumber))) {
                html += "<li" + style  +"><div class='brick'>" + buttons[k] +'</div></li>';
            } else {
            // normalna cegiełka z atrybutem 'klikalności'
                html += "<li" + style  +"><a href=\"javascript:;\"><div class='brick'>" + buttons[k] +'</div></a></li>';
            }
        }
    html += '</ul></div>';

    // przypisujemy kod html do elementu o danym id
    // poniższa pętla jest po to abyśmy mogli obsłużyć wszystkie elementy z klasy 'myPaginationSystem' obecne na stronie (np pager dolny i górny)
    pagerControllers = document.getElementsByClassName("myPaginationSystem");
    for (pagerInstance=0; pagerInstance < pagerControllers.length; pagerInstance++)
    {
        var obj = document.getElementsByClassName("myPaginationSystem")[pagerInstance];
        obj.innerHTML = html + "<div class='clear'></div>";
       
        // add event handlers
        // pracuj na wszystkich elementach 'a' i zdefiniuj zdarzenie onclick, czyli uruchom funkcję z nowym atrybutem z cegiełki
        aItems = obj.getElementsByClassName("myPager")[0].getElementsByTagName("a");
        for (i=0; i<aItems.length; i++) {
            
            aItems[i].onclick = function () {
                txt = this.childNodes[0].innerHTML;
                if (txt == "&lt;") {
                    txt = selection - 1;
                }
                if (txt == "&gt;") {
                    txt = selection + 1;
                }
                // tutaj ponowne uruchomienie siebie samego, ale z nowym parametrem
                createNavigationConsole4(parseInt(txt));
                // i na końcu pora na kluczowe działanie, czyli odświeżenie zawartości na podstawie wybranej cegiełki.
                refresh(parseInt(txt))
            }
        }
    }
}

function refresh(brickVal) {

    start = (brickVal-1)*globalItemsPerPage;
    end = 0;
    if (start+globalItemsPerPage > advicesDatabase.length) {
        end = advicesDatabase.length;
    } else {
        end = start + globalItemsPerPage;
    }
    html = "";
    for (index=start; index<end; index++) {
        html += '<div class="container nest">';
        html += '   <div class="row">';
        html += '       <div class="col-xs-12 col-sm-5 col-md-3">';
        html += '           <div class="image">';
        html += '               <a href=' + advicesDatabase[index].link + '><img class="img-responsive" src=' + advicesDatabase[index].img + ' /></a>';
        html += '           </div>';
        html += '       </div>';
        html += '       <div class="col-xs-12 col-sm-5 col-md-9">';
        html += '           <div class="row artTitle">' + '<a href=' + advicesDatabase[index].link + '>' + advicesDatabase[index].title + '</a></div>';
        html += '           <div class="row author">' + advicesDatabase[index].author + '</div>';
        html += '           <div class="row artDescription"><hr style="margin: 5px; margin-left: 0px" /><p>' + advicesDatabase[index].shortDesc + '</p></div>';
        html += '           <div class="row continueReading"><a href=' + advicesDatabase[index].link + '>Czytaj dalej...</a></div>';
        html += '       </div>';
        html += '   </div>';
        html += '</div>';
    }
    document.getElementById("mainTxtArea").innerHTML = html;
}

// ##############################################

globalItemsPerPage = 6;
pagesNumber = Math.ceil(advicesDatabase.length / globalItemsPerPage, 0); // ceil round the float up to the nearest integer
console.debug(Math.ceil(advicesDatabase.length / globalItemsPerPage, 0))
createNavigationConsole4(1);
refresh(1);