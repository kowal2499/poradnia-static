<?php

function render_news() {
    
    $xmlNews = 0;
    if (!file_exists("database/news.xml")) {
        echo "brak pliku news.xml";
        return False;
    }

    $xmlNews = simplexml_load_file("database/news.xml");
    
    foreach($xmlNews->wiadomość as $single) {

        // data
        echo '<div class="row" style="padding-left: 20px; padding-right: 20px;">';
        echo '  <div class="col-sm-12">';
        echo '      <div class="newsWindowDateField">'.$single->data.'</div>';
        echo '  </div>';
        echo '</div>';

        // tytuł
        $link_start = '';
        $link_end = '';
        if (strtolower(trim($single->okienko)) == 'tak') {  // tytuł jest linkiem do wyskakującego okienka
            if (trim($single->okienko_tylko_obrazek)) {
                $link_start = '<a href="#popupWindow" onclick="attach(\''.$single->okienko_tylko_obrazek.'\')">';
                $link_end = '</a>';
            } else if (trim($single->okienko_html)) {
                $str = str_replace(array("\r", "\n"), '', trim($single->okienko_html)); // get rid of the newlines
                $str = str_replace(array("'"), "\'", $str); // escape '
                $link_start = '<a href="#popupWindow" onclick="attachHTML(\''.$str.'\');">';
                $link_end = '</a>';
            } 
        } else if ($single->tytuł->link) {  // tytuł jest linkiem do podstrony
            $link_start = '<a href="'.$single->tytuł->link.'">';
            $link_end = '</a>';
        }
        

        echo '<div class="row" style="padding-left: 20px; padding-right: 20px;">';
        echo '  <div class="col-sm-12">';
        echo '      <div class="newsWindowTitleBar">'.$link_start.$single->tytuł->tekst.$link_end.'</div>';
        echo '  </div>';
        echo '</div>';
        
        // obrazek
        if (trim($single->obrazek->plik)) {
            echo '<div class="row" style="padding-left: 20px; padding-right: 20px;">';
            echo '  <div class="col-xs-12 col-sm-3">';
            echo '      <div class="newsWindowImg">'.$link_start.'<img src="'.$single->obrazek->plik.'" class="img-responsive">'.$link_end.'</div>';
            echo '  </div>';
            echo '  <div class="col-xs-12 col-sm-9">';
            echo '      <div class="newsWindowMessage" style="border-left: 1px solid #89AB93;">'.$single->opis.'</div>';
            echo '  </div>';
            echo '</div>';
        } else {
        // wersja bez obrazka
            echo '<div class="row" style="padding-left: 20px; padding-right: 20px;">';
            echo '  <div class="col-xs-12 col-sm-12">';
            echo '      <div class="newsWindowMessage" style="border-left: 1px solid #89AB93;">'.$single->opis.'</div>';
            echo '  </div>';
            echo '</div>';
        }
        echo '<br>';
    }
}


?>