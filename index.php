<?php include 'functions.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="keywords" content="Poradnia Psychologiczno-Pedagogiczna w Białogardzie, Poradnia Psychologiczno-Pedagogiczna Białogard, Poradnia Psychologiczno-Pedagogiczna, Poradnia Białogard, Poradnia, Psychologia, Psycholog, Białogard">
    <title>Poradnia Psychologiczno-Pedagogiczna w Białogardzie</title>

    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="-1" />

    <!-- Bootstrap -->
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="styles/homepage.css" rel="stylesheet">
    <link href="styles/index.css" rel="stylesheet">
    <link href="styles/lightbox.css" rel="stylesheet">
    <link href="styles/common.css" rel="stylesheet">

    <style>
        .img-center {
            margin: 0 auto;
        }

        .clear {
            clear: both;
        }

        .carousel-indicators {
            width: auto;
            left: auto;
            right: 5%;
            bottom: 0px;
        }


        .background {
          background: url('img/light_wool.png') repeat;
        }

        #welcomeArea {
            background-color: #F8F8F8;
            box-shadow: 0px 0px 10px gray;
            border-radius: 7px;
            
        }

        

        #contactArea {
            background-color: #D6D6D6;
            box-shadow: 0px 0px 10px gray;
            border-radius: 7px;
            margin: 50px 0;
            padding: 0px;
        }

        .welcomeTitle {
            font-size: 1.4em;
            padding: 10px 35px 10px 35px;
            margin: 0px;
            margin-left: 20%;
            
            background-color: #89AB93;
            color: white;
            border-radius: 0px 7px 0px 7px;
            border-left: 1px solid gray;
            border-right: 1px solid gray;
            border-bottom: 1px solid gray;
            
            text-align: center;
            background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAECAYAAABP2FU6AAAAGElEQVQImWPoXD35P0Pn6sn/GSZsWAAhAG13C0stqlL5AAAAAElFTkSuQmCC) 
                repeat;
            overflow: auto;
        }

        #welcomeArea p {
            font-size: 0.9em;
            
            margin-left: 25%;
            margin-right: 20px;
            margin-top: 20px;
            margin-bottom: 20px;

            padding-left: 5%;
            padding-right: 5%;            
            border-left: 8px solid #87131B;
            border-right: 8px solid #87131B;
            text-indent: 4em;
            line-height: 1.3em;
            overflow: auto;
            text-align: justify;
        }
        .welcomeTitleBottom {
            font-size: 1.1em;
            padding: 10px 35px 10px 35px;
            float: left;
            margin-right: 25%;
            margin: 0px;
            
            background-color: #89AB93;
            color: white;
            border-radius: 0px 7px 0px 7px;
            background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAECAYAAABP2FU6AAAAGElEQVQImWPoXD35P0Pn6sn/GSZsWAAhAG13C0stqlL5AAAAAElFTkSuQmCC) repeat;
        }
        
        .navigation {
            
            margin: 30px auto;
            width: 40%;
        }
        .navigation li {
            list-style-type: none;
            float: left;
            padding: 0px 5px 0px 5px;
            margin-right: 5px;
            border: 1px solid #D7D7D7;
        }
        .navigation li:hover {
            background-color: #D7D7D7;
            cursor: pointer;
        }

        #map {
            width: 100%;
            height: 240px;
            background-color: #CCC;
            margin-top: 20px;
            margin-bottom: 20px;

        }
        /*
            main colors:
            biały: #F8F8F8;
            szary: #AB9A9A;
            khaki:  #89AB93;
            morski: #E7E7E7;
            czerwony: #87131B;
        */


    </style>
    <link href='https://fonts.googleapis.com/css?family=Roboto:300' rel='stylesheet' type='text/css'>
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]--> 
</head>

<body style="min-width:200px; font-family: Verdana, Geneva, sans-serif; background: url('img/light_wool.png') repeat;">
    <script>
        // location.reload(true);
    </script>
    <!--    TITLE BAR
    ============================================================= -->
    <div class="poradnia">
        Poradnia Psychologiczno-Pedagogiczna w Białogardzie
    </div>

    <!--    NAVBAR
    ============================================================= -->

    <div class="navbar navbar-default" style="margin: 0px;">
        <div class="container">
             <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button> 
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li class="active"><a href=""><span>Strona Główna</span></a></li>
                    <li><a href="subpages/zadania.html"><span>Oferta</span></a></li>
                    <li><a href="subpages/porady.html"><span>Porady</span></a></li>
                    <li><a href="subpages/kadra.html"><span>Kadra</span></a></li>
                    <li><a href="subpages/doPobrania.html"><span>Do pobrania</span></a></li>
                </ul>
            </div>
        </div>
    </div>
    
    <!--    MAIN BODY
    ============================================================= -->

    <div class="container">
        <div class="row">
            <div class="col-sm-12 content" style="margin: 50px 0 10px 0;">

                <!-- pole powitalne-->
                <div id="welcomeArea">
                    <div class="welcomeTitle">
                        Serdecznie witamy na stronie internetowej Poradni Psychologiczno-Pedagogicznej w Białogardzie.
                    </div>
                    <div class="clear"></div>

                    <div id="carousel-example-generic" class="carousel slide" data-ride="carousel" style="margin-top: 30px; border-top: 1px solid #87131B; border-bottom: 1px solid #87131B;">
                      <!-- Indicators -->
                      <ol class="carousel-indicators push-right">
                        <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
                        <li data-target="#carousel-example-generic" data-slide-to="1"></li>
                        <li data-target="#carousel-example-generic" data-slide-to="2"></li>
                        <li data-target="#carousel-example-generic" data-slide-to="3"></li>
                      </ol>

                      <!-- Wrapper for slides -->
                      <div class="carousel-inner" role="listbox">

                        <div class="item active">
                          <img src="img/try01.jpg" alt="Wesoła dziewczynka" class="center-block">
                        </div>
                        <div class="item">
                          <img src="img/try04.jpg" alt="Chłopiec zabawa" class="center-block">
                        </div>
                        <div class="item">
                          <img src="img/try03.jpg" alt="Chłopiec zabawa" class="center-block">
                        </div>
                        <div class="item">
                          <img src="img/try02.jpg" alt="Dziecięcy rysunek" class="center-block">
                        </div>
                      </div>
                    </div>

                     <div class="motto">
                        ... kto pragnie dobra dla drugiego człowieka zawsze znajdzie sposób, aby coś dla niego uczynić...
                     </div>
                    <p>
                        Nasza placówka działa już prawie 50 lat i świadczy specjalistyczne usługi w zakresie diagnozy, psychoedukacji, terapii, a także udziela wsparcia psychologicznego, pedagogicznego i logopedycznego dla dzieci, młodzieży, rodziców i nauczycieli. Nasze usługi są dobrowolne i bezpłatne, a do ich skorzystania zaproszeni są mieszkańcy z miasta i gminy Białogard, miasta i gminy Karlino, miasta i gminy Tychowo.
                    </p>
                    <div class="welcomeTitleBottom">
                        Zachęcamy do zapoznania się i skorzystania z oferty Poradni!
                    </div>
                    <div class="clear"></div>
                </div>
            </div>
        </div><!-- row -->
    </div><!-- container ends -->


    <div class="container">
        <!-- pole aktualności-->
        <div class="row" >
            <div class="col-sm-9">
                <div class="newsWrapper"> 
                    <div class="myTitle" >
                        Aktualności z życia Poradni:
                    </div>
                    
                    <div class="clear"></div>
                    <br />
                    <div id="newsField">
                        <?php render_news(); ?>
                    </div>
                </div>
            </div>


            <div class="col-sm-3" id="#widgets-area">                
                <div class="newsWrapper" id="comming-events">
                    <div class="myTitle">Najbliższe wydarzenia</div>
                            <div class="clear"></div>
                            <div class="pin">
                                <div id="eventsBoard"></div>
                            </div> 
                </div>

                <div class="newsWrapper">
                    <div class="myTitle">Harmonogram</div>
                            <div class="clear"></div>
                            <div class="pin">
                                <a href="subpages/pomocGrupowe.html"><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span>&nbsp;Harmonogram zajęć grupowych dla dzieci organizowanych na terenie Poradni</a>
                                
                            </div> 
                </div>


                <div class="newsWrapper">
                    <div class="myTitle">Polecamy</div>
                            <div class="clear"></div>
                            <div class="pin">
                                <div id="past-eventsBoard"></div>
                            </div> 
                </div>
                



            </div><!-- widgets-area -->
        </div><!-- row -->
    </div><!-- container ends -->

    <div class="container">
        <div class="row" style="margin-left: 0px; margin-right: 0px;">
                <!-- pole kontaktu-->

                <div id="contactArea" class="col-sm-12">
                    <div class="myTitle" style="background-color: #87131B;color: #F8F8F8; border-bottom: 1px solid #F8F8F8; border-right: 1px solid #F8F8F8;">Kontakt:</div>
                    <div class="clear"></div>
                    <div style="text-align: center;">
                        Poradnia Psychologiczno-Pedagogiczna w Białogardzie<br />
                        ul. Dworcowa 2<br />
                        78-200 Białogard<br /><br />
                        Tel/Fax: 94 312 25 96, Tel. komórkowy: 515 082 620<br>
                        email: pppbialogard@poczta.onet.pl<br />
                    </div>

                    <div id="map" style="border-top: 1px solid #87131B; border-bottom: 1px solid #87131B;"></div>
                    <div style="text-align: center;">
                        Sekretariat zaprasza w godzinach: 7:30 - 15:30<br />od poniedziałku do piątku<br /><br />
                    </div>                        
                </div>
        </div><!-- row -->
    </div><!-- container ends -->
    


<div class="lightbox-target" id="popupWindow">
        <div class="modal-dialog">
            <div id="lightboxCanvas"></div>
            <div id="lightboxImgOnly"></div>
            <div class="buttonClose"><a href="#1">:: zamknij okno ::</a></div>
        </div>
</div>
 
 <!-- ==================== FOOTER ==================== -->
<div class="footer">
    <div class="container">
        &copy; 2016 Poradnia Psychologiczno-Pedagogiczna w Białogardzie
    </div>
</div>



    <!-- ##################### scripts area ##################### -->

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="bootstrap/js/bootstrap.min.js"></script>

    <!-- <script type="text/javascript" src="scripts/news.js"></script> -->
    <script type="text/javascript" src="scripts/events.js?v=4"></script>
    <script type="text/javascript" src="scripts/past-events.js?v=4"></script>

    
    
    <script src="https://maps.googleapis.com/maps/api/js"></script>
    <script>
        function initialize() {
            var mapCanvas=document.getElementById('map');
            var pos = new google.maps.LatLng(54.009630, 15.983089);
            var mapOptions = {
                  center: pos,
                  zoom: 15,
                  mapTypeId: google.maps.MapTypeId.ROADMAP,
				  scrollwheel: false
                };

            var map = new google.maps.Map(mapCanvas, mapOptions);
            var marker = new google.maps.Marker({
                position: pos,
                map: map,
                title: 'Poradnia Psychologiczno-Pedagogiczna\nul. Dworcowa 2\n78-200 Białogard'
            }) 
        }
        // google.maps.event.addDomListener(window, 'load', initialize);


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
    </script>

    <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDQGfqQzuQ09iqS32nZnfoCfoO9s1UoJKU&callback=initialize" type="text/javascript"></script>

</body>
</html>
