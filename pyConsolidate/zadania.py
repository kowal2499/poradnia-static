#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Romek'

from template import Template

class Zadania(Template):
    def __init__(self, templateFile, destinationFolder):
        Template.__init__(self,templateFile, destinationFolder)
        self.database = {
            u'pomocGrupoweWiekSzkolny.html':
                [u"Zajęcia grupowe dla dzieci w wieku szkolnym",
                 u"""<p>Oferta zajęć grupowych dla dzieci w wieku szkolnym w roku szkolnym 2016/2017</p>
                                <table>
                                    <tr><th>Lp.</th><th>Nazwa zajęć</th><th>Prowadzące</th></tr>
                                    <tr>
                                        <td>1.</td>
                                        <td><a href='szkPomocGrupoweSherborne.html'>Zajęcia prowadzone Metodą Ruchu Rozwijającego Weroniki Sherborne - ilość grup wg potrzeb.</a></td>
                                        <td><ul><li>M. Hewelt</li><li>S. Sokołowska</li><li>A. Gudańska-Walkowska</li><li>M. Jonko</li></ul></td>
                                    </tr>

                                    <tr class="odd">
                                        <td>2.</td>
                                        <td>Zajęcia stymulujące ogólny rozwój dla dzieci o zaburzonym lub opóźnionym rozwoju – ilość grup wg potrzeb.</td>
                                        <td><ul><li>A. Politowska–Kowal</li><li>M. Hewelt</li><li>S. Sokołowska</li></ul></td>
                                    </tr>

                                    <tr>
                                        <td>3.</td>
                                        <td><a href="szkPomocGrupoweDobryStart1.html">Metoda Dobrego Startu" dla uczniów kl. I szkoły podstawowej.</a></td>
                                        <td><ul><li>M. Jakubowska</li><li>A. Gudańska-Walkowska</li></ul></td>
                                    </tr>

                                    <tr class="odd">
                                        <td>4.</td>
                                        <td><a href="pomocGrupoweTerapiaReki.html">Terapia ręki dla dzieci 5-7 letnich. <span class='attention'>NOWOŚĆ !</span></a></td>
                                        <td><ul><li>M. Hewelt</li></ul></td>
                                    </tr>

                                    <tr>
                                        <td>5.</td>
                                        <td><a href="pomocGrupoweBystryUmysl.html">"Bystry umysł" - zajęcia doskonalące koncentrację uwagi dla klas II-IV szkoły podstawowej.<span class='attention'>NOWOŚĆ !</span></a></td>
                                        <td><ul><li>M. Hewelt</li><li>A. Gudańska-Walkowska</li></ul></td>
                                    </tr>

                                    <tr class="odd">
                                        <td>6.</td>
                                        <td><a href="pomocGrupoweTwórczeMyślenie.html">Trening twórczego myślenia – dla uczniów kl. IV–VI szkoły podstawowej</a></td>
                                        <td><ul><li>E. Cieszko–Kowalska</li></ul></td>
                                    </tr>

                                    <tr class="">
                                        <td>7.</td>
                                        <td><a href="pomocGrupoweKompetencjeSpołeczne.html">Zajęcia podnoszące kompetencje społeczne (socjoterapeutyczne) – dla uczniów z klas III-VI szkoły podstawowej.</a></td>
                                        <td><ul><li>E. Cieszko–Kowalska</li><li>S. Sokołowska</li></ul></td>
                                    </tr>

                                    <tr class="odd">
                                        <td>8.</td>
                                        <td>Zajęcia dla dzieci jąkających się.</td>
                                        <td><ul><li>H. Górzyńska</li></ul></td>
                                    </tr>

                                   <tr class="">
                                        <td>9.</td>
                                        <td>Zajęcia stymulujące ogólny rozwój dla dzieci o zaburzonym rozwoju z wykorzystaniem arteterapii – kl. IV-VI szkoły podstawowej.</td>
                                        <td><ul><li>A. Gudańska - Walkowska</li></ul></td>
                                    </tr>

                                    <tr class="odd">
                                        <td>10.</td>
                                        <td><a href="szkPomocGrupoweBajkoterapia.html">Bajkoterapia dla dzieci kl. 0-II i III-IV szkoły podstawowej.</a></td>
                                        <td><ul><li>M. Hewelt</li></ul></td>
                                    </tr>

                                    <tr class="">
                                        <td>11.</td>
                                        <td><a href="szkPomocGrupoweSensoryka.html">Zajęcia usprawniające sensorykę i rozwój ogólny dzieci w wieku od 2 do 7 lat.</a></td>
                                        <td><ul><li>M. Hewelt</li><li>A. Gudańska - Walkowska</li></ul></td>
                                    </tr>

                                    <tr class="odd">
                                        <td>12.</td>
                                        <td>Zajęcia stymulujące funkcje słuchowe u dzieci słabosłyszących</td>
                                        <td><ul><li>A. Politowska–Kowal</li></ul></td>
                                    </tr>

                                    <tr class="">
                                        <td>13.</td>
                                        <td>Zajęcia stymulujące funkcje wzrokowe u dzieci słabowidzących</td>
                                        <td><ul><li>M. Jakubowska</li><li>A. Politowska–Kowal</li></ul></td>
                                    </tr>

                                    <tr class="odd">
                                        <td>14.</td>
                                        <td><a href="pomocGrupoweZajeciaKorekcyjnoKompensacyjne.html">Zajęcia korekcyjno – kompensacyjne dla uczniów ze specyficznymi trudnościami w uczeniu się:<ul><li>klasy I-III szkoły podstawowej</li><li>klasy IV-VI szkoły podstawowej</li><li>klasy I-III gimnazjum</li></ul></a></td>
                                        <td><ul><li>A. Politowska–Kowal</li><li>M. Hewelt</li></ul></td>
                                    </tr>

                                    <tr class="">
                                        <td>15.</td>
                                        <td><a href="pomocGrupoweMatematyka.html">Matematyka bez trudności – zajęcia terapeutyczne dla dzieci z trudnościami w nauce matematyki – kl. IV–VI szkoły podstawowej</a></td>
                                        <td><ul><li>A. Gudańska - Walkowska</li></ul></td>
                                    </tr>

                                    <tr class="odd">
                                        <td>16.</td>
                                        <td><a href='szkPomocGrupoweGrupaWsparcia.html'>Grupa wsparcia i rozwoju osobistego dla młodzieży</a></td>
                                        <td><ul><li>S. Sokołowska</li></ul></td>
                                    </tr>
                                </table>
                  """,
                 u"""<script type="text/javascript">
                        markSelected('wiekSzkolny');
                    </script>"""
                ],
    u'pomocGrupoweWiekPrzedszkolny.html':
                [
                  u"Zajęcia grupowe dla dzieci w wieku przedszkolnym:",
                  u"""
                    <p>Oferta zajęć grupowych dla dzieci w wieku przedszkolnym w roku szkolnym 2016/2017</p>

                    <table>
                        <tr><th>Lp.</th><th>Nazwa zajęć</th><th>Prowadzące</th></tr>
                        <tr>
                            <td>1.</td>
                            <td><a href='pomocGrupoweSherborne.html'>Zajęcia prowadzone Metodą Ruchu Rozwijającego Weroniki Sherborne - ilość grup wg potrzeb.</a></td>
                            <td><ul><li>M. Hewelt</li><li>S. Sokołowska</li><li>A. Gudańska-Walkowska</li><li>A. Politowska-Kowal</li></ul></td>
                        </tr>

                        <tr class="odd">
                            <td>2.</td>
                            <td>Zajęcia stymulujące ogólny rozwój dla dzieci o zaburzonym lub opóźnionym rozwoju – ilość grup wg potrzeb.</td>
                            <td><ul><li>A. Politowska–Kowal</li><li>M. Hewelt</li><li>S. Sokołowska</li></ul></td>
                        </tr>

                        <tr>
                            <td>3.</td>
                            <td>Zajęcia stymulujące rozwój mowy dla dzieci w wieku przedszkolnym</td>
                            <td><ul><li>logopedzi</li></ul></td>
                        </tr>

                        <tr class="odd">
                            <td>4.</td>
                            <td><a href="pomocGrupowePercepcjaSłuchowa.html">Zajęcia rozwijające percepcję słuchową, przygotowujące do nauki czytania dzieci 6–letnich.</a></td>
                            <td><ul><li>H. Górzyńska</li></ul></td>
                        </tr>

                        <tr>
                            <td>5.</td>
                            <td><a href="pomocGrupoweSłuchamiOpowiadam.html">"Bystrzaki - przedszkolaki" - zajęcia stymulujące funkcje słuchowe i sprawność językową dla dzieci 6 letnich <span class='attention'>NOWOŚĆ !</span></a></td>
                            <td><ul><li>M. Jonko</li><li>M. Waiszewska</li></ul></td>
                        </tr>

                        <tr class="odd">
                            <td>6.</td>
                            <td><a href="pomocGrupoweDobryStart.html">"Metoda Dobrego Startu" dzieci 6–letnich.</a></td>
                            <td><ul><li>S. Sokołowska</li></ul></td>
                        </tr>

                        <tr>
                            <td>7.</td>
                            <td><a href="pomocGrupoweTerapiaReki2.html">Terapia ręki dla dzieci 5-7 letnich<span class='attention'>NOWOŚĆ !</span></a></td>
                            <td><ul><li>M. Hewelt</li></ul></td>
                        </tr>

                        <tr class="odd">
                            <td>8.</td>
                            <td>Zajęcia dla dzieci jąkających się.</td>
                            <td><ul><li>H. Górzyńska</li></ul></td>
                        </tr>

                        <tr>
                            <td>9.</td>
                            <td><a href="pomocGrupoweBajkoterapia.html">Bajkoterapia dla dzieci kl. 0-I szkoły podstawowej.</a></td>
                            <td><ul><li>M. Hewelt</li></ul></td>
                        </tr>

                        <tr class="odd">
                            <td>10.</td>
                            <td><a href="pomocGrupoweSensoryka.html">Zajęcia usprawniające sensorykę i rozwój ogólny dzieci w wieku od 2 do 7 lat.</a></td>
                            <td><ul><li>M. Hewelt</li><li>A. Gudańska-Walkowska</li></ul></td>
                        </tr>

                        <tr>
                            <td>11.</td>
                            <td>Zajęcia stymulujące funkcje słuchowe u dzieci słabosłyszących.</td>
                            <td><ul><li>A. Politowska–Kowal</li></ul></td>
                        </tr>

                        <tr class="odd">
                            <td>12.</td>
                            <td>Zajęcia stymulujące funkcje wzrokowe u dzieci słabowidzących.</td>
                            <td><ul><li>M. Jakubowska</li><li>A. Politowska–Kowal</li></ul></td>
                        </tr>


                    </table>""",
                  u"""<script type="text/javascript">
                        markSelected('wiekPrzedszkolny');
                    </script>"""
                ],
    u'pomocDlaDzieciiMłodzieży.html':
                [
                    u"Pomoc dla dzieci i młodzieży",
                    u"""
                    <p>Rodzaje działań w zakresie pomocy dla dzieci i młodzieży:</p>
                    <ul>
                    <li><a href="pomocIndywidualne.html">zajęcia indywidalne na terenie poradni,</a></li>
                    <li><a href="pomocGrupowe.html">zajęcia grupowe na terenie poradni,</a></li>
                    <li><a href="pomocWczesnyRozwój.html">wczesne wspomaganie rozwoju na terenie poradni,</a></li>
                    <li><a href="pomocWarsztaty.html">zajęcia warsztatowe na terenie szkół.</a></li>
                    <li><a href="pomocFerie.html">"FERIE Z PORADNIĄ" <span class='attention'>NOWOŚĆ !</span></a></li>
                    </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('pomocDlaDzieciMłodzieży');
                    </script>
                    """],
    u'zadania.html':
                [
                    u"Oferta poradni",
                    u"""
                    <p>Zadaniem Poradni Psychologiczno-Pedagogicznej w Białogardzie jest świadczenie usług w zakresie diagnozy, psychoedukacji, terapii, a także udzielanie wsparcia psychologicznego, pedagogicznego i logopedycznego dla dzieci, młodzieży, nauczycieli i rodziców.</p>
                    <p>Działania poradni skupiają się wokół czterech głównych filarów:</p>
                    <ul>
                        <li>diagnozy dzieci i młodzieży,</li>
                        <li>pomocy psychologiczno-pedagogicznej dla dzieci, młodzieży i rodziców,</li>
                        <li>zadań profilaktycznych oraz wspierających wychowawczą i edukacyjną funkcję przedszkola, szkoły i placówki, w tym wspierania nauczycieli w rozwiązywaniu problemów dydaktycznych i wychowawczych,</li>
                        <li>wspomagania przedszkoli, szkół i placówek w zakresie realizacji zadań dydaktycznych, wychowawczych i opiekuńczych.</li>
                    </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('zadaniaMain');
                    </script>
                    """
                ],
    u'diagnoza.html':
                [
                    u"Diagnoza",
                    u"""
                            <h2>Rodzaje diagnozy:</h2>
                            <ul>
                                <li>psychologiczna</li>
                                <li>pedagogiczna</li>
                                <li>logopedyczna</li>
                            </ul>
                            <h2>Kto zgłasza dziecko na diagnozę?</h2>
                            <ul>
                                <li>rodzice/opiekun prawny – osobiście lub telefonicznie do sekretariatu poradni,</li>
                                <li>szkoła/przedszkole - wychowawca, pedagog szkolny czy dyrektor za zgodą rodziców/opiekuna prawnego
                                    przesyłają wypełniony wniosek, w którym znajdują się informacje na temat
                                    funkcjonowania dziecka i doświadczanych przez niego trudności na gruncie szkolnym.</li>
                            </ul>
                            <h2>Diagnoza dzieci i młodzieży może dotyczyć:</h2>
                            <ul>
                                <li>ogólnych trudności w nauce,</li>
                                <li>specyficznych trudności w nauce (dysleksji, dysgrafii, dysortografii, dyskalkulii),</li>
                                <li>problemów wynikających z niepełnosprawności,</li>
                                <li>przeżywanych trudności w sferze emocjonalnej, osobowościowej,</li>
                                <li>trudności w zachowaniu, w kontaktach społecznych,</li>
                                <li>zaburzeń koncentracji uwagi,</li>
                                <li>problemów wychowawczych,</li>
                                <li>pomocy w wyborze kierunku kształcenia i zawodu,</li>
                                <li>trudności z wymową,</li>
                                <li>określenia poziomu rozwoju intelektualnego, społeczno-emocjonalnego, zdolności dziecka,</li>
                                <li>określenia gotowości szkolnej.</li>

                            </ul>
                            <h2>Czas trwania diagnozy zależy od:</h2>
                            <ul>
                                <li>powodu zgłoszenia,</li>
                                <li>samopoczucia/nastroju dziecka,</li>
                                <li>tempa pracy,</li>
                                <li>męczliwości,</li>
                                <li>gotowości do współpracy.</li>
                            </ul>

                            <p>Badanie psychologiczne trwa zazwyczaj do 2,5 godziny,
                            badanie pedagogiczne do 2 godzin, a diagnoza logopedyczna – 20 minut.</p>

                            <h2>Ważne informacje przed przybyciem na diagnozę</h2>
                            <ul>
                                <li>Jeśli dziecko nosi okulary i/lub aparat słuchowy, ważne jest, aby przybyło z nimi na badanie,</li>
                                <li>W sytuacji, gdy u dziecka podejrzewają Państwo wadę wzroku, należy umówić wizytę u okulisty i przełożyć termin badań kontaktując się z Poradnią Psychologiczno-Pedagogiczną osobiście lub telefonicznie,</li>
                                <li>Niezbędne jest dostarczenie na badania do poradni zaświadczeń od lekarzy oraz wyników badań medycznych, jeśli dziecko miało je wykonywane,</li>
                                <li><strong>Jeśli termin badań Państwu nie odpowiada, istotny jest kontakt osobisty lub telefoniczny z Poradnią Psychologiczno-Pedagogiczną celem ustalenia bardziej dogodnego terminu spotkań.</strong></li>
                            </ul>

                            <h2>Przebieg diagnozy</h2>
                            <p>Diagnoza rozpoczyna się od wywiadu z rodzicem przeprowadzonego przez
                            specjalistę. W wywiadzie zbierane są informacje na temat funkcjonowania dziecka w
                            środowisku rodzinnym, rówieśniczym, szkolnym. Wywiad dotyczy też przebiegu
                            ciąży, porodu i wczesnych etapów życia dziecka, w tym specyfiki jego rozwoju.
                            Informacje te są niezwykle istotne w dalszej diagnozie dziecka. Następnie
                            specjalista przeprowadza rozmowę z dzieckiem, w której określa cel spotkania,
                            przedstawia kolejne jego etapy. W trakcie tej rozmowy istotnym jest nawiązanie
                            dobrego kontaktu, zbudowanie życzliwej, serdecznej atmosfery, by dziecko poczuło
                            się bezpiecznie. W przypadku dzieci młodszych jest to też czas na zabawę
                            tematyczną z dzieckiem.</p>

                            <p>Po przeprowadzonym badaniu następuje przekazanie informacji zwrotnych
                            dziecku na temat tego, jak poradziło sobie w trakcie badań, a także udzielenie
                            wskazówek do dalszej pracy. Następnie odbywa się rozmowa z rodzicem polegająca
                            na przekazaniu informacji zwrotnych, wyjaśniająca mechanizmy działania
                            zgłaszanych trudności, wskazująca drogi pomocy dziecku na terenie domu, szkoły lub
                            poradni. W niektórych przypadkach diagnoza psychologiczna i pedagogiczna uzupełniana jest o dodatkowe
                            konsultacje np. neurologiczną, psychiatryczną.</p>
                            <p>Na wniosek rodzica/opiekuna prawnego Poradnia Psychologiczno-Pedagogiczna może wydać: opinię,
                            w tym o wczesnym wspomaganiu rozwoju, informację o wynikach badań,
                            orzeczenie o potrzebie: kształcenia specjalnego, zajęć rewalidacyjno-wychowawczych, indywidualnego
                            obowiązkowego rocznego przygotowania przedszkolnego lub indywidualnego nauczania dzieci i młodzieży.</p>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('diagnoza');
                    </script>"""
                ],
    u'pomocIndywidualne.html':
                [
                    u"Zajęcia indywidualne na terenie poradni",
                    u"""    <ol>
                                <li>z psychologiem,</li>
                                <li>z pedagogiem,</li>
                                <li>logopedyczne.</li>
                            </ol>

                            <h2>Cele zajęć indywidualnych z psychologiem</h2>
                            <ul>
                                <li>wspieranie w przeżywanych trudnościach,</li>
                                <li>obniżanie napięcia emocjonalnego,</li>
                                <li>wzmacnianie poczucia własnej wartości, poznawanie swoich mocnych stron,</li>
                                <li>doskonalenie umiejętności społecznych typu: radzenie sobie z nieprzyjemnymi
                                    emocjami, kształtowanie postawy asertywnej, przeciwdziałanie agresji,
                                    nawiązywanie i podtrzymywanie satysfakcjonujących relacji z rówieśnikami oraz dorosłymi,</li>
                                <li>wzmacnianie motywacji do nauki,</li>
                                <li>rozwijanie więzi z rodziną.</li>
                            </ul>
                            <h2>Cele zajęć indywidualnych z pedagogiem</h2>
                            <ul>
                                <li>stymulacja ogólnego rozwoju dziecka,</li>
                                <li>wzbogacanie zasobu wiadomości ogólnych i słownictwa,</li>
                                <li>rozwijanie koordynacji słuchowo-wzrokowo- ruchowej,</li>
                                <li>rozwijanie wyobraźni i orientacji przestrzennej,</li>
                                <li>doskonalenie umiejętności koncentracji uwagi na zadaniu,</li>
                                <li>usprawnianie działania analizatora wzrokowego, słuchowego oraz pamięci
                                    słuchowej i wzrokowej,</li>
                                <li>usprawnianie grafomotoryki oraz zdolności manualnych.</li>
                            </ul>
                            <h2>Cele indywidualnej terapii logopedycznej</h2>
                            <ul>
                                <li>przygotowanie artykulatorów do uzyskania prawidłowej wymowy nieprawidłowo
                                realizowanych głosek poprzez:</li>
                                    <ul>
                                        <li>ćwiczenia oddechowe.</li>
                                        <li>ćwiczenia narządów artykulacyjnych: języka, warg, podniebienia miękkiego,</li>
                                        <li>ćwiczenia emisyjno- głosowe.</li>
                                    </ul>
                                <li>właściwa korekcja wad wymowy:</li>
                                    <ul>
                                        <li>wywołanie głoski w izolacji</li>
                                        <li>utrwalenie głoski korygowanej w sylabach, w wyrazach (nagłos, śródgłos, wygłos), w wyrażeniach, w zdaniach</li>
                                        <li>utrwalenie poprawnej wymowy wywołanej głoski w wierszykach, piosenkach
                                        wyliczankach, powiedzeniach</li>
                                        <li>automatyzacja poprawnej realizacji głoski w mowie spontanicznej, opowiadanie,
                                        co widać na ilustracji, historyjek obrazkowych, rozmowy kierowane.</li>
                                    </ul>

                                <li>rozwój słuchu fonemowego, pamięci, uwagi, spostrzegawczości słuchowej.</li>
                                <li>rozwój świadomości metalingwistycznej - umiejętności budowania
                                    poprawnych konstrukcji zdaniowych, korygowania błędów gramatycznych</li>
                                <li>stymulowanie ogólnego rozwoju dziecka  poprzez rozwijanie słownictwa
                                    czynnego i biernego, koordynacji wzrokowo- słuchowo- ruchowej, pamięci,
                                    myślenia, orientacji przestrzennej.</li>
                                <li>usprawnianie techniki czytania i pisania z uwzględnieniem wadliwie
                                    wymawianych wcześniej głosek</li>
                                <li>współpraca z  rodzicami, psychologiem, pedagogiem wychowawcą grupy.
                                    Instruowanie o sposobie korekcji mowy i utrwalania poprawnej realizacji
                                    głosek, pokaz ćwiczeń, informowanie o postępach</li>
                            </ul>
                            <h2>Kiedy należy zgłosić się do logopedy</h2>
                            <ol>
                                <li>Gdy dziecko od 2 do 3 lat: <span style="font-weight: bold;">nie buduje krótkich, prostych zdań</span></li>
                                <li>Gdy dziecko w wieku 3 lat: <span style="font-weight: bold;">nie wypowiada poprawnie głosek p, b, m, t, d, n , w, f, ch, ń, k, g, l oraz  ś, ć , dź, ź</span></li>
                                <li>Gdy dziecko w wieku 4 lat: <span style="font-weight: bold;">oprócz wyżej wymienionych nie wymawia głosek syczących s, z, c, dz</span></li>
                                <li>Gdy dziecko w wieku 6 lat: <span style="font-weight: bold;">dodatkowo nie wymawia jeszcze głosek sz, ż, cz, dż oraz r</span></li>
                            </ol>
                            <p>
                            Systematyczne zajęcia z psychologiem i pedagogiem trwają z reguły od
                            października do maja, z logopedą w ciągu całego roku szkolnego. Wnioski rodziców w
                            sprawie zakwalifikowania na zajęcia indywidualne należy składać najpóźniej do
                            końca września w sekretariacie poradni. Po w/w terminie wnioski będą rozpatrywane indywidualnie.
                            </p>
                            <h2>Materiały do pobrania</h2>
                            <div class="download">
                            <ul>
                                <li><a href='../download/wniosek o objęcie dziecka terapią.doc' download>Wniosek o objęcie dziecka terapią – zobacz (dokument Word)</a></li>
                            </ul>
                            </div>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('indywidualne');
                    </script>"""
                ],
    u'pomocGrupowe.html':
                [
                    u"Zajęcia grupowe na terenie poradni",
                    u"""
                        <p>Zajęcia grupowe trwają zazwyczaj od października do maja. Prowadzone są
                        systematycznie co tydzień o określonej porze. Zajęcia poprzedzone są spotkaniem
                        organizacyjnym dla rodziców, podczas którego omawiane są cele zajęć,
                        procedury.</p>
                        <p>Wnioski w sprawie zajęć należy składać do sekretariatu poradni do 30 września każdego roku.</p>

                        <p>W wyjątkowych przypadkach dzieci będą przyjmowane po w/w terminie.</p>

                         <p>Zajęcia grupowe na terenie poradni są dedykowane dla odbiorców wg dwóch grup wiekowych:
                            <ol>
                                <li><a href="pomocGrupoweWiekPrzedszkolny.html">Dzieci w wieku przedszkolnym</a></li>
                                <li><a href="pomocGrupoweWiekSzkolny.html">Dzieci w wieku szkolnym</a></li>
                            </ol>
                         </p>

                        <h2 id="harmonogram">Harmonogram zajęć grupowych na terenie poradni w roku szkolnym 2015/2016</h2>
                        <br />
                        <table>
                            <tr><th>Lp.</th><th>Nazwa zajęć</th><th>Termin</th><th>Miejsce</th><th>Prowadzące</th></tr>
                            <tr>
                                <td>1.</td>
                                <td><a href='szkPomocGrupoweSensoryka.html'>Zajęcia usprawniające sensorykę i rozwój ogólny dzieci w wieku od 2 do 6-ciu lat</a></td>
                                <td>poniedziałek, godz. 14:30</td>
                                <td>Klub Nauczyciela, parter</td>
                                <td><ul><li>A.&nbsp;Gudańska-Walkowska</li><li>M.&nbsp;Hewelt</li></ul></td>
                            </tr>

                            <tr class="odd">
                                <td>2.</td>
                                <td><a href='pomocGrupoweSherborne.html'>Metoda Ruchu Rozwijającego Weroniki Sherborne – dla dzieci młodszych</a></td>
                                <td>poniedziałek, godz. 15:30</td>
                                <td>Klub Nauczyciela, parter</td>
                                <td><ul><li>A.&nbsp;Gudańska-Walkowska</li><li>M.&nbsp;Hewelt</li></ul></td>
                            </tr>

                            <tr>
                                <td>3.</td>
                                <td><a href='szkPomocGrupoweSherborne.html'>Metoda Ruchu Rozwijającego Weroniki Sherborne – dla dzieci starszych</a></td>
                                <td>poniedziałek, godz. 16:30</td>
                                <td>Klub Nauczyciela, parter</td>
                                <td><ul><li>S.&nbsp;Cąkała</li><li>A.&nbsp;Politowska-Kowal</li></ul></td>
                            </tr>

                            <tr class="odd">
                                <td>4.</td>
                                <td><a href='pomocGrupoweMatematyka.html'>\"Matematyka bez trudności\" dla uczniów z klas IV-VI SP</a></td>
                                <td>poniedziałek, godz. 17:30</td>
                                <td>Gabinet nr 5, parter</td>
                                <td><ul><li>A.&nbsp;Gudańska-Walkowska</li></ul></td>
                            </tr>

                            <tr>
                                <td>5.</td>
                                <td><a href='szkPomocGrupoweDobryStart1.html'>Metoda Dobrego Startu dla dzieci z kl. I SP</a></td>
                                <td>poniedziałek, godz. 16:30</td>
                                <td>Gabinet nr 5, I piętro</td>
                                <td><ul><li>A.&nbsp;Gudańska-Walkowska</li><li>M.&nbsp;Jakubowska</li></ul></td>
                            </tr>

                            <tr class="odd">
                                <td>6.</td>
                                <td><a href='pomocGrupoweDobryStart.html'>Metoda Dobrego Startu dla dzieci 5-letnich</a></td>
                                <td>wtorek, godz. 14:00</td>
                                <td>Gabinet nr 6, I piętro</td>
                                <td><ul><li>S.&nbsp;Cąkała</li></ul></td>
                            </tr>

                            <tr>
                                <td>7.</td>
                                <td><a href='pomocGrupoweDobryStartOdr.html'>Metoda Dobrego Startu dla dzieci odroczonych od obowiązku szkolnego</a></td>
                                <td>środa, godz. 15:00</td>
                                <td>Klub Nauczyciela, parter</td>
                                <td><ul><li>A.&nbsp;Gudańska-Walkowska</li></ul></td>
                            </tr>

                            <tr class="odd">
                                <td>8.</td>
                                <td><a href='szkPomocGrupoweBajkoterapia.html'>Bajkoterapia dla dzieci z klas I-III SP</a></td>
                                <td><ul><li>poniedziałek godz. 16:30</li><li>środa, godz. 13:30</li></ul></td>
                                <td>Gabinet nr 7, parter</td>
                                <td><ul><li>M.&nbsp;Hewelt</li></ul></td>
                            </tr>

                            <tr>
                                <td>9.</td>
                                <td><a href='pomocGrupoweSłuchamiOpowiadam.html'>&quot;Słucham i opowiadam&quot; – zajęcia stymulujące funkcje słuchowe i sprawność językową dzieci 5-letnich</a></td>
                                <td>wtorek, godz. 15:30</td>
                                <td>Gabinet nr 5, I piętro</td>
                                <td><ul><li>M.&nbsp;Jonko</li></ul></td>
                            </tr>

                            <tr class="odd">
                                <td>10.</td>
                                <td><a href="pomocGrupoweLepiejGloskuje.html">Zajęcia \"Lepiej głoskuję, lepiej opowiadam\" dla dzieci 5-letnich</a></td>
                                <td>co drugi wtorek, godz. 16:00</td>
                                <td>Gabinet nr 4, I piętro</td>
                                <td><ul><li>M.&nbsp;Weiszewska</li></ul></td>
                            </tr>

                            <tr>
                                <td>11.</td>
                                <td><a href='pomocGrupowePercepcjaSłuchowa.html'>Zajęcia rozwijające percepcję słuchową dla dzieci 5-letnich</a></td>
                                <td>środa, godz. 16:00</td>
                                <td>Gabinet nr 4, I piętro</td>
                                <td><ul><li>H.&nbsp;Górzyńska</li></ul></td>
                            </tr>

                            <tr class="odd">
                                <td>12.</td>
                                <td><a href='pomocGrupoweKompetencjeSpołeczne.html'>Zajęcia podnoszące kompetencje społeczne dla uczniów kl. I-III SP</a></td>
                                <td>wtorek, godz. 16:00</td>
                                <td>Klub Nauczyciela, parter</td>
                                <td><ul><li>S.&nbsp;Cąkała</li><li>M.&nbsp;Lis</li></ul></td>
                            </tr>

                            <tr>
                                <td>13.</td>
                                <td><a href='pomocGrupoweKompetencjeSpołeczne.html'>Zajęcia podnoszące kompetencje społeczne dla uczniów kl. IV-VI SP</a></td>
                                <td>środa, godz. 17:00</td>
                                <td>Gabinet nr 5, I piętro</td>
                                <td><ul><li>E.&nbsp;Cieszko-Kowalska</li></ul></td>
                            </tr>

                            <tr class="odd">
                                <td>14.</td>
                                <td><a href='pomocGrupoweKompetencjeSpołeczne.html'>Zajęcia podnoszące kompetencje społeczne dla uczniów z klas IV-VI SP kontynuujących zajęcia drugi rok</a></td>
                                <td>środa, godz. 16:00</td>
                                <td>Gabinet nr 5, I piętro</td>
                                <td><ul><li>E.&nbsp;Cieszko-Kowalska</li></ul></td>
                            </tr>

                            <tr>
                                <td>15.</td>
                                <td><a href='pomocGrupoweTwórczeMyślenie.html'>Trening twórczego myślenia dla uczniów klas IV-VI SP</a></td>
                                <td>co druga środa, godz. 15:00</td>
                                <td>Gabinet nr 5, I piętro</td>
                                <td><ul><li>E.&nbsp;Cieszko-Kowalska</li></ul></td>
                            </tr>

                            <tr class="odd">
                                <td>16.</td>
                                <td><a href='szkPomocGrupoweGrupaWsparcia.html'>Grupa wsparcia i rozwoju osobistego dla młodzieży</a></td>
                                <td>wtorek, godz. 18:00</td>
                                <td>Gabinet nr 10, I piętro</td>
                                <td><ul><li>S.&nbsp;Cąkała</li></ul></td>
                            </tr>

                            <tr>
                                <td rowspan="2">17.</td>
                                <td rowspan="2"><a href="pomocGrupoweZajeciaKorekcyjnoKompensacyjne.html">Zajęcia korekcyjno-kompensacyjne</a></td>
                                <td><ul><li>poniedziałek, godz. 14:30, 15:30, 17:30</li><li>czwartek, godz. 13:15, 14:15, 15:15</li></ul></td>
                                <td>Gabinet nr 11, I piętro</td>
                                <td><ul><li>A.Politowska - Kowal</li></ul></td>
                            </tr>
                            <tr>

                                <td><ul><li>poniedziałek, godz. 13:30, 17:30</li></ul></td>
                                <td>Gabinet nr 7, parter</td>
                                <td><ul><li>M. Hewelt</li></ul></td>
                            </tr>



                        </table>


                        <h2>Materiały do pobrania</h2>
                        <div class="download">
                            <ul>
                                <li><a href='../download/Procedury dotyczące kwalifikowania, organizowania i korzystania z zajęć specjalistycznych na terenie Poradni Psychologiczno-Pedagogicznej w Białogardzie.doc' download>Procedury dotyczące kwalifikowania, organizowania grupowych zajęć specjalistycznych i korzystania z nich na terenie Poradni Psychologiczno-Pedagogicznej w Bałogardzie – zobacz (dokument Word)</a></li>
                                <li><a href='../download/wniosek o objęcie dziecka terapią.doc' download>Wniosek o objęcie dziecka terapią – zobacz (dokument Word)</a></li>
                            </ul>
                        </div>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupowe');
                    </script>
                    """
                ],
    u'pomocGrupoweSherborne.html':
                [
                    u"Metoda Ruchu Rozwijającego Weroniki Sherborne",
                    u"""
                    <!--<div class="grupoweDetale">
                        <p>Prowadzące: A. Gudańska-Walkowska, M. Hewelt</p>
                        <p>Termin zajęć: środa godz.</p>
                        <p>Miejsce: PPP Białogard, Klub Nauczyciela, parter</p>
                    </div>-->

                    <p>Weronika Sherborne na podstawie własnych doświadczeń w nauczaniu i poprzez obserwacje ruchu ludzkiego doszła do wniosku, że wszystkie dzieci mają dwie podstawowe potrzeby: potrzebują czuć się we własnym ciele jak w domu oraz chcą umieć nawiązywać relacje z innymi ludźmi. Celem zajęć jest zaspokojenie tych potrzeb.</p>
                    <p>System ćwiczeń opracowanych przez W. Sherborne wywodzi się z naturalnych potrzeb dziecka, które zaspokaja kontakt z dorosłymi (tzw. baraszkowanie). Dlatego niezbędny jest udział rodzica/ opiekuna na zajęciach wraz z dzieckiem.</p>

                    <h2>Cele</h2>
                    <ul>
                        <li>zaufanie do samego siebie - dziecko czerpie poczucie pewności i zaufania do samego siebie ze sposobu, w jaki dorosły fizycznie się z nim obchodzi,</li>
                        <li>znajomość ciała,</li>
                        <li>bezpieczeństwo fizyczne i emocjonalne - gdy dziecko odkrywa, że może zaufać partnerowi,</li>
                        <li>komunikacja – dziecko uczy się wielu nowych słów, które ma szansę zapamiętać podczas używania ich w ruchu.</li>
                    </ul>

                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupoweSherborne');
                    </script>
                    """
                ],
    u'szkPomocGrupoweSherborne.html':
                [
                    u"Metoda Ruchu Rozwijającego Weroniki Sherborne",
                    u"""
                    <!--<div class="grupoweDetale">
                        <p>Prowadzące: A. Gudańska-Walkowska, M. Hewelt</p>
                        <p>Termin zajęć: środa godz.</p>
                        <p>Miejsce: PPP Białogard, Klub Nauczyciela, parter</p>
                    </div>-->

                    <p>Weronika Sherborne na podstawie własnych doświadczeń w nauczaniu i poprzez obserwacje ruchu ludzkiego doszła do wniosku, że wszystkie dzieci mają dwie podstawowe potrzeby: potrzebują czuć się we własnym ciele jak w domu oraz chcą umieć nawiązywać relacje z innymi ludźmi. Celem zajęć jest zaspokojenie tych potrzeb.</p>
                    <p>System ćwiczeń opracowanych przez W. Sherborne wywodzi się z naturalnych potrzeb dziecka, które zaspokaja kontakt z dorosłymi (tzw. baraszkowanie). Dlatego niezbędny jest udział rodzica/ opiekuna na zajęciach wraz z dzieckiem.</p>

                    <h2>Cele</h2>
                    <ul>
                        <li>zaufanie do samego siebie - dziecko czerpie poczucie pewności i zaufania do samego siebie ze sposobu, w jaki dorosły fizycznie się z nim obchodzi,</li>
                        <li>znajomość ciała,</li>
                        <li>bezpieczeństwo fizyczne i emocjonalne - gdy dziecko odkrywa, że może zaufać partnerowi,</li>
                        <li>komunikacja – dziecko uczy się wielu nowych słów, które ma szansę zapamiętać podczas używania ich w ruchu.</li>
                    </ul>

                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('szkGrupoweSherborne');
                    </script>
                    """
                ],
    u'pomocGrupoweSensoryka.html':
                [
                    u"Zajęcia usprawniające sensorykę i rozwój ogólny w wieku od 2 do 7 lat",
                    u"""
                    <!--<div class="grupoweDetale">
                        <p>Prowadzące:</p>
                        <p>Termin zajęć:</p>
                        <p>Miejsce:</p>
                    </div>-->

                    <h2>Cele</h2>

                    <ul>
                        <li>usprawnianie grafomotoryki poprzez m.in. zajęcia plastyczne, rysowanie szlaczków, odwzorowywanie figur, kopiowanie obrazków, kreślenie prostych linii łączących wyznaczone punkty,</li>
                        <li>wzbogacanie zasobu słownictwa i wiedzy o otaczającym świecie poprzez opisywanie obrazków, tworzenie opowiadań, definiowanie pojęć, nazywanie różnych przedmiotów, wymienianie zwierząt, kolorów itp., zachęcanie dziecka do wypowiadania się na temat codziennych wydarzeń; wprowadzanie nowych pojęć z otaczającego świata,</li>
                        <li>doskonalenie pamięci poprzez naukę wierszyków, zapamiętywanie jak największej ilości szczegółów na obrazku, w pokoju  i wymienianie ich z pamięci, gry typu „memory”,</li>
                        <li>ćwiczenia analizy i syntezy słuchowej: wyodrębnianie zdań w wypowiedzi ustnej;  podział zdania na wyrazy - liczenie wyrazów; wyodrębnianie sylab w słowach;  wyszukiwanie wyrazów zaczynających się lub kończących na daną głoskę;  dokonywanie analizy i syntezy sylabowej i głoskowej,</li>
                        <li>doskonalenie koordynacji wzrokowo-słuchowo-ruchowej,</li>
                        <li>ćwiczenia analizy i syntezy wzrokowej na materiale obrazkowym i geometrycznym: rozpoznawanie przedmiotów i ich elementów na obrazkach;  dobieranie obrazka do jego schematu, cienia;  dobieranie części do całości obrazka; układanie puzzli i loteryjek obrazkowych (na wzorze, według wzoru i bez wzoru);  wskazywanie różnic i podobieństw między obrazkami; odpoznawanie braków na obrazkach,</li>
                    </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupoweSensoryka');
                    </script>
                    """
                ],
    u'szkPomocGrupoweSensoryka.html':
                [
                    u"Zajęcia usprawniające sensorykę i rozwój ogólny w wieku od 2 do 7 lat",
                    u"""
                    <!--<div class="grupoweDetale">
                        <p>Prowadzące:</p>
                        <p>Termin zajęć:</p>
                        <p>Miejsce:</p>
                    </div>-->

                    <h2>Cele</h2>

                    <ul>
                        <li>usprawnianie grafomotoryki poprzez m.in. zajęcia plastyczne, rysowanie szlaczków, odwzorowywanie figur, kopiowanie obrazków, kreślenie prostych linii łączących wyznaczone punkty,</li>
                        <li>wzbogacanie zasobu słownictwa i wiedzy o otaczającym świecie poprzez opisywanie obrazków, tworzenie opowiadań, definiowanie pojęć, nazywanie różnych przedmiotów, wymienianie zwierząt, kolorów itp., zachęcanie dziecka do wypowiadania się na temat codziennych wydarzeń; wprowadzanie nowych pojęć z otaczającego świata,</li>
                        <li>doskonalenie pamięci poprzez naukę wierszyków, zapamiętywanie jak największej ilości szczegółów na obrazku, w pokoju  i wymienianie ich z pamięci, gry typu „memory”,</li>
                        <li>ćwiczenia analizy i syntezy słuchowej: wyodrębnianie zdań w wypowiedzi ustnej;  podział zdania na wyrazy - liczenie wyrazów; wyodrębnianie sylab w słowach;  wyszukiwanie wyrazów zaczynających się lub kończących na daną głoskę;  dokonywanie analizy i syntezy sylabowej i głoskowej,</li>
                        <li>doskonalenie koordynacji wzrokowo-słuchowo-ruchowej,</li>
                        <li>ćwiczenia analizy i syntezy wzrokowej na materiale obrazkowym i geometrycznym: rozpoznawanie przedmiotów i ich elementów na obrazkach;  dobieranie obrazka do jego schematu, cienia;  dobieranie części do całości obrazka; układanie puzzli i loteryjek obrazkowych (na wzorze, według wzoru i bez wzoru);  wskazywanie różnic i podobieństw między obrazkami; odpoznawanie braków na obrazkach,</li>
                    </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('szkGrupoweSensoryka');
                    </script>
                    """
                ],
    u'pomocGrupowePercepcjaSłuchowa.html':
                [
                    u"Zajęcia rozwijające percepcję słuchową, przygotowujące do nauki czytania dzieci 6–letnich.",
                    u"""
                    <!--<div class="grupoweDetale">
                        <p>Prowadzące: H. Górzyńska</p>
                        <p>Termin zajęć: poniedziałek godz.</p>
                        <p>Miejsce: PPP Białogard, gabinet nr 5, I piętro</p>
                    </div>-->

                    <h2>Cele</h2>
                    <ul>
                        <li>rozwijanie sprawności narządów mowy, artykulacji, słuchu fonemowego,</li>
                        <li>rozwijanie komunikacji językowej dziecka, wzbogacanie słownictwa, poprawności gramatycznej i stylistycznej wypowiedzi,</li>
                        <li>lepsze przygotowanie do podjęcia nauki  w klasie pierwszej,</li>
                        <li>zmniejszenie się liczby dzieci mających trudności w czytaniu i pisaniu.</li>
                    </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupowePercepcjaSluchowa');
                    </script>
                    """
                ],
    u'pomocGrupoweDobryStart.html':
                [
                    u"Metoda Dobrego Startu dla dzieci 6-letnich",
                    u"""
                            <!--<div class="grupoweDetale">
                                <p>Prowadzące: A. Gudańska-Walkowska, S. Cąkała</p>
                                <p>Termin zajęć:</p>
                                <p>Miejsce:</p>
                            </div>-->

                            <p>Dla potrzeb szkolnictwa w Polsce Metodę Dobrego Startu adaptowała prof. Marta Bogdanowicz. Zajęcia są wskazane dla dzieci przygotowujących się do nauki czytania i pisania. Założeniem Metody Dobrego Startu jest jednoczesne rozwijanie funkcji wzrokowych, słuchowych, językowych, dotykowo-kinestetycznych (czucie dotyku i ruchu) i motorycznych oraz ich współdziałania, czyli integracji percepcyjno-motorycznej. Funkcje te leżą u podstaw złożonych czynności czytania i pisania. Celem metody jest także kształtowanie lateralizacji (ustalenie ręki dominującej) oraz orientacji w schemacie ciała i w przestrzeni.</p>

                            <h2>Schemat zajęć</h2>
                            <ol>
                                <li>Zajęcia wprowadzające:</li>
                                    <ul>
                                        <li>ćwiczenia kształtujące orientację w schemacie własnego ciała-zabawa ruchowa, w której dzieci rozpoznają i nazywają części ciała oraz rozróżniają prawą i lewą stronę ciała,</li>
                                        <li>ćwiczenia kształtujące orientację w przestrzeni – stwarzają możliwość do utrwalania umiejętności rozróżniania kierunków oraz stosowania pojęć określających relacje przestrzenne,</li>
                                        <li>następnie dzieci poznają piosenkę, wierszyk, który będzie towarzyszył im w dalszej części zajęć</li>
                                    </ul>
                                <li>Zajęcia właściwe:</li>
                                    <ul>
                                        <li>ćwiczenia ruchowe,</li>
                                        <li>ćwiczenia ruchowo-słuchowe - dzieci śpiewając piosenkę, wypowiadając rytmicznie wierszyk wystukują jej rytm otwartymi dłońmi, pięściami, palcami,</li>
                                        <li>ćwiczenia ruchowo-słuchowo-wzrokowe - dzieci uczą się kreślić wzór w rytm jednocześnie śpiewanej piosenki, mówionego wierszyka</li>
                                    </ul>
                                <li>Zajęcia końcowe – na zakończenie przeprowadza się krótkie ćwiczenia relaksujące lub wyciszające.</li>
                            </ol>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupoweDobryStart');
                    </script>
                    """
                ],
    u'pomocGrupoweDobryStartOdr.html':
                [
                    u"Metoda Dobrego Startu dla dzieci odroczonych od obowiązku szkolnego",
                    u"""
                            <!--<div class="grupoweDetale">
                                <p>Prowadzące: A. Gudańska-Walkowska, S. Cąkała</p>
                                <p>Termin zajęć:</p>
                                <p>Miejsce:</p>
                            </div>-->

                            <p>Dla potrzeb szkolnictwa w Polsce Metodę Dobrego Startu adaptowała prof. Marta Bogdanowicz. Zajęcia są wskazane dla dzieci przygotowujących się do nauki czytania i pisania. Założeniem Metody Dobrego Startu jest jednoczesne rozwijanie funkcji wzrokowych, słuchowych, językowych, dotykowo-kinestetycznych (czucie dotyku i ruchu) i motorycznych oraz ich współdziałania, czyli integracji percepcyjno-motorycznej. Funkcje te leżą u podstaw złożonych czynności czytania i pisania. Celem metody jest także kształtowanie lateralizacji (ustalenie ręki dominującej) oraz orientacji w schemacie ciała i w przestrzeni.</p>

                            <h2>Schemat zajęć</h2>
                            <ol>
                                <li>Zajęcia wprowadzające:</li>
                                    <ul>
                                        <li>ćwiczenia kształtujące orientację w schemacie własnego ciała-zabawa ruchowa, w której dzieci rozpoznają i nazywają części ciała oraz rozróżniają prawą i lewą stronę ciała,</li>
                                        <li>ćwiczenia kształtujące orientację w przestrzeni – stwarzają możliwość do utrwalania umiejętności rozróżniania kierunków oraz stosowania pojęć określających relacje przestrzenne,</li>
                                        <li>następnie dzieci poznają piosenkę, wierszyk, który będzie towarzyszył im w dalszej części zajęć</li>
                                    </ul>
                                <li>Zajęcia właściwe:</li>
                                    <ul>
                                        <li>ćwiczenia ruchowe,</li>
                                        <li>ćwiczenia ruchowo-słuchowe - dzieci śpiewając piosenkę, wypowiadając rytmicznie wierszyk wystukują jej rytm otwartymi dłońmi, pięściami, palcami,</li>
                                        <li>ćwiczenia ruchowo-słuchowo-wzrokowe - dzieci uczą się kreślić wzór w rytm jednocześnie śpiewanej piosenki, mówionego wierszyka</li>
                                    </ul>
                                <li>Zajęcia końcowe – na zakończenie przeprowadza się krótkie ćwiczenia relaksujące lub wyciszające.</li>
                            </ol>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupoweDobryStartDlaOdroczonych');
                    </script>
                    """
                ],
    u'szkPomocGrupoweDobryStart1.html':
                [
                    u"\"Metoda Dobrego Startu\" dla uczniów kl. I szkoły podstawowej",
                    u"""
                            <!--<div class="grupoweDetale">
                                <p>Prowadzące: M. Jakubowska, A. Politowska–Kowal, M. Jonko, E. Cieszko-Kowalska</p>
                                <p>Termin zajęć:</p>
                                <p>Miejsce:</p>
                            </div>-->

                            <p>Dla potrzeb szkolnictwa w Polsce Metodę Dobrego Startu adaptowała prof. Marta Bogdanowicz. Zajęcia są wskazane dla dzieci przygotowujących się do nauki czytania i pisania. Założeniem Metody Dobrego Startu jest jednoczesne rozwijanie funkcji wzrokowych, słuchowych, językowych, dotykowo-kinestetycznych (czucie dotyku i ruchu) i motorycznych oraz ich współdziałania, czyli integracji percepcyjno-motorycznej. Funkcje te leżą u podstaw złożonych czynności czytania i pisania. Celem metody jest także kształtowanie lateralizacji (ustalenie ręki dominującej) oraz orientacji w schemacie ciała i w przestrzeni.</p>

                            <h2>Schemat zajęć</h2>
                            <ol>
                                <li>Zajęcia wprowadzające:</li>
                                    <ul>
                                        <li>ćwiczenia kształtujące orientację w schemacie własnego ciała-zabawa ruchowa, w której dzieci rozpoznają i nazywają części ciała oraz rozróżniają prawą i lewą stronę ciała,</li>
                                        <li>ćwiczenia kształtujące orientację w przestrzeni – stwarzają możliwość do utrwalania umiejętności rozróżniania kierunków oraz stosowania pojęć określających relacje przestrzenne,</li>
                                        <li>następnie dzieci poznają piosenkę, wierszyk, który będzie towarzyszył im w dalszej części zajęć</li>
                                    </ul>
                                <li>Zajęcia właściwe:</li>
                                    <ul>
                                        <li>ćwiczenia ruchowe,</li>
                                        <li>ćwiczenia ruchowo-słuchowe - dzieci śpiewając piosenkę, wypowiadając rytmicznie wierszyk wystukują jej rytm otwartymi dłońmi, pięściami, palcami,</li>
                                        <li>ćwiczenia ruchowo-słuchowo-wzrokowe - dzieci uczą się kreślić wzór w rytm jednocześnie śpiewanej piosenki, mówionego wierszyka</li>
                                    </ul>
                                <li>Zajęcia końcowe – na zakończenie przeprowadza się krótkie ćwiczenia relaksujące lub wyciszające.</li>
                            </ol>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('szkPomocGrupoweDobryStart1');
                    </script>
                    """
                ],

    u'szkPomocGrupoweDobryStart2.html':
                [
                    u"\"Metoda Dobrego Startu\" dla uczniów kl. I szkoły podstawowej (o obniżonych możliwościach intelektualnych).",
                    u"""
                            <!--<div class="grupoweDetale">
                                <p>A. Politowska–Kowal, S. Cąkała, J. Piotrowicz</p>
                                <p>Termin zajęć:</p>
                                <p>Miejsce:</p>
                            </div>-->

                            <p>Dla potrzeb szkolnictwa w Polsce Metodę Dobrego Startu adaptowała prof. Marta Bogdanowicz. Zajęcia są wskazane dla dzieci przygotowujących się do nauki czytania i pisania. Założeniem Metody Dobrego Startu jest jednoczesne rozwijanie funkcji wzrokowych, słuchowych, językowych, dotykowo-kinestetycznych (czucie dotyku i ruchu) i motorycznych oraz ich współdziałania, czyli integracji percepcyjno-motorycznej. Funkcje te leżą u podstaw złożonych czynności czytania i pisania. Celem metody jest także kształtowanie lateralizacji (ustalenie ręki dominującej) oraz orientacji w schemacie ciała i w przestrzeni.</p>

                            <h2>Schemat zajęć</h2>
                            <ol>
                                <li>Zajęcia wprowadzające:</li>
                                    <ul>
                                        <li>ćwiczenia kształtujące orientację w schemacie własnego ciała-zabawa ruchowa, w której dzieci rozpoznają i nazywają części ciała oraz rozróżniają prawą i lewą stronę ciała,</li>
                                        <li>ćwiczenia kształtujące orientację w przestrzeni – stwarzają możliwość do utrwalania umiejętności rozróżniania kierunków oraz stosowania pojęć określających relacje przestrzenne,</li>
                                        <li>następnie dzieci poznają piosenkę, wierszyk, który będzie towarzyszył im w dalszej części zajęć</li>
                                    </ul>
                                <li>Zajęcia właściwe:</li>
                                    <ul>
                                        <li>ćwiczenia ruchowe,</li>
                                        <li>ćwiczenia ruchowo-słuchowe - dzieci śpiewając piosenkę, wypowiadając rytmicznie wierszyk wystukują jej rytm otwartymi dłońmi, pięściami, palcami,</li>
                                        <li>ćwiczenia ruchowo-słuchowo-wzrokowe - dzieci uczą się kreślić wzór w rytm jednocześnie śpiewanej piosenki, mówionego wierszyka</li>
                                    </ul>
                                <li>Zajęcia końcowe – na zakończenie przeprowadza się krótkie ćwiczenia relaksujące lub wyciszające.</li>
                            </ol>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('szkPomocGrupoweDobryStart2');
                    </script>
                    """
                ],

    u'pomocGrupoweBajkoterapia.html':
                [
                    u"Bajkoterapia dla dzieci kl. 0-I szkoły podstawowej",
                    u"""
                        <!--<div class="grupoweDetale">
                            <p>Prowadzące: M. Hewelt</p>
                            <p>Termin zajęć: środa godz.</p>
                            <p>Miejsce: PPP Białogard, gabinet nr , parter</p>
                        </div>-->
                        <p>Bajkoterapia to - mówiąc najprościej – terapia przez bajki. Terapeutyczne opowiadania pomagają uporać się z dziecięcymi lękami i wątpliwościami. Wyjaśniają istotę zachowań uznawanych przez społeczeństwo. Bajki dotykają ważnych obszarów takich, jak zazdrość i odwaga, złość, tolerancja, wdzięczność, rywalizacja między rówieśnikami, agresja, lęk i wiele innych. Dla szkraba są wyjątkowo bezpieczne gdyż ma ona możliwość stawienia czoła problemom, które przeżywają zwierzątka, misie, rycerze lub inni bohaterowie. Dziecko identyfikuje się z tym, który w jakiś sposób jest mu najbliższy. Robi to jednak zupełnie nieświadomie dzięki czemu nie czuje się „przyciskane”, kontrolowane lub zmuszane do wynurzeń. W taki sposób znajduje zrozumienie, czuje, że nie jest samo, doświadcza rozwiązania i ma szansę zdecydować czy ono mu odpowiada. Często próbuje tego samego rozwiązania w świecie realnym.</p>
                        <h2>Cele terapii</h2>
                        <ul>
                            <li>umożliwienie wyżalenia się, ekspresji uczuć;</li>
                            <li>budowanie nadziei oraz danie poczucia, że nie jest się samym, że inni podobnie czują, myślą i zachowują się. Odbudowanie w ten sposób pozytywnej samooceny,</li>
                            <li>zapoznanie ze słownictwem dotyczącym emocji, wyjaśnienie związków przyczynowo-skutkowych między zdarzeniem a doznawaniem emocji;</li>
                            <li>racjonalizowanie problemu, pokazanie wzorów skutecznego działania, innego myślenia o sytuacji trudnej i tym samym innego odczuwania;</li>
                            <li>przedstawienie różnych trudności, zachęcanie do mówienia o problemach, poszukiwanie skutecznych rozwiązań;</li>
                            <li>uczenie myślenia pozytywnego nastawionego na działanie;</li>
                            <li>budowanie zaufania do siebie i swoich możliwości oraz radości dnia codziennego.</li>
                        </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupoweBajkoterapia');
                    </script>
                    """
                ],
    u'szkPomocGrupoweBajkoterapia.html':
                [
                    u"Bajkoterapia dla dzieci klas 0-I i II-III szkoły podstawowej",
                    u"""
                        <p>Bajkoterapia to - mówiąc najprościej – terapia przez bajki. Terapeutyczne opowiadania pomagają uporać się z dziecięcymi lękami i wątpliwościami. Wyjaśniają istotę zachowań uznawanych przez społeczeństwo. Bajki dotykają ważnych obszarów takich, jak zazdrość i odwaga, złość, tolerancja, wdzięczność, rywalizacja między rówieśnikami, agresja, lęk i wiele innych. Dla szkraba są wyjątkowo bezpieczne gdyż ma ona możliwość stawienia czoła problemom, które przeżywają zwierzątka, misie, rycerze lub inni bohaterowie. Dziecko identyfikuje się z tym, który w jakiś sposób jest mu najbliższy. Robi to jednak zupełnie nieświadomie dzięki czemu nie czuje się „przyciskane”, kontrolowane lub zmuszane do wynurzeń. W taki sposób znajduje zrozumienie, czuje, że nie jest samo, doświadcza rozwiązania i ma szansę zdecydować czy ono mu odpowiada. Często próbuje tego samego rozwiązania w świecie realnym.</p>
                        <h2>Cele terapii</h2>
                        <ul>
                            <li>umożliwienie wyżalenia się, ekspresji uczuć;</li>
                            <li>budowanie nadziei oraz danie poczucia, że nie jest się samym, że inni podobnie czują, myślą i zachowują się. Odbudowanie w ten sposób pozytywnej samooceny,</li>
                            <li>zapoznanie ze słownictwem dotyczącym emocji, wyjaśnienie związków przyczynowo-skutkowych między zdarzeniem a doznawaniem emocji;</li>
                            <li>racjonalizowanie problemu, pokazanie wzorów skutecznego działania, innego myślenia o sytuacji trudnej i tym samym innego odczuwania;</li>
                            <li>przedstawienie różnych trudności, zachęcanie do mówienia o problemach, poszukiwanie skutecznych rozwiązań;</li>
                            <li>uczenie myślenia pozytywnego nastawionego na działanie;</li>
                            <li>budowanie zaufania do siebie i swoich możliwości oraz radości dnia codziennego.</li>
                        </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('szkGrupoweBajkoterapia');
                    </script>
                    """
                ],
    u'pomocGrupoweKompetencjeSpołeczne.html':
                [
                    u"Zajęcia grupowe podnoszące kompetencje społeczne (socjoterapeutyczne) dla uczniów kl. III - VI szkoły podstawowej",
                    u"""
                        <!--<div class="grupoweDetale">
                            <p>Prowadzące: E. Cieszko-Kowalska, S. Cąkała</p>
                            <p>Termin zajęć: wtorek godz.</p>
                            <p>Miejsce: PPP Białogard, gabinet nr 5, I piętro</p>
                        </div>-->
                     <h2>Cele</h2>
                     <ul>
                        <li>utrwalanie prawidłowych wzorców zachowania w grupie,</li>
                        <li>odreagowywanie napięć emocjonalnych,</li>
                        <li>kształtowanie zdolności konstruktywnego reagowania w trudnych sytuacjach i umiejętności rozwiązywania konflików,</li>
                        <li>rozwijanie umiejętności pełnienia ról społecznych,</li>
                        <li>wzmacnianie poczucia własnej wartości, poznawanie swoich mocnych stron,</li>
                        <li>przeżycie korektywnego doświadczenia stanowiącego alternatywę dla przebytych wcześniej urazów.</li>
                     </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupoweKompetencjeSpoleczne');
                    </script>
                    """
                ],
    u'pomocGrupoweTwórczeMyślenie.html':
                [
                    u"Trening twórczego myślenia dla uczniów klas IV-VI szkoły podstawowej",
                    u"""
                        <!--<div class="grupoweDetale">
                            <p>Prowadząca: E. Cieszko-Kowalska</p>
                            <p>Termin zajęć: środa godz.</p>
                            <p>Miejsce: PPP Białogard, gabinet nr 5, I piętro</p>
                        </div>-->
                        <h2>Cele</h2>
                        <ul>
                            <li>wzmacnianie postawy twórczej,</li>
                            <li>rozwijanie wyobraźni oraz myślenia,</li>
                            <li>doskonalenie pamięci, koncentracji uwagi, różnych sposobów uczenia się, płynności słownej, spostrzegawczości wzrokowej,</li>
                            <li>wyrażanie siebie za pomocą różnych technik,</li>
                            <li>uświadamianie potencjału twórczego uczestników oraz zachęcanie do jego wykorzystywania w życiu codziennym.</li>
                        </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupoweTworczeMyslenie');
                    </script>
                    """
                ],
    u'pomocGrupoweSłuchamiOpowiadam.html':
                [
                    u"\"Bystrzaki - przedszkolaki\" - zajęcia stymulujące funkcje słuchowe i sprawność językową dla dzieci 6 letnich <span class='attention'>NOWOŚĆ !</span>",
                    u"""
                        
                        <h2>Cele</h2>
                        <ul>
                            <li>stymulowanie i usprawnianie percepcji słuchowej oraz wspieranie rozwoju psychoruchowego,</li>
                            <li>lepsze przygotowanie do podjęcia nauki w klasie pierwszej, szczególnie w zakresie gotowości do opanowania umiejętności czytania,</li>
                            <li>rozwijanie komunikacji językowej dziecka, poprzez opanowanie poprawności gramatycznej i stylistycznej wypowiedzi,</li>
                            <li>kształcenie mowy ekspresyjnej, wyzwalanie motywacji do mówienia i działania,</li>
                            <li>rozwijanie sfery emocjonalno-społecznej i motywacyjnej rozwoju dziecka,</li>
                            <li>wyzwalanie potencjalnych możliwości dziecka oraz wzmacnianie jego mocnych stron.</li>
                        </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('grupoweSluchamOpowiadam');
                    </script>
                    """
                ],
    u'pomocWczesnyRozwój.html':
                [
                    u"Wczesne wspomaganie rozwoju dziecka na terenie poradni",
                    u"""
                    <p>Wczesne wspomaganie rozwoju dziecka rozumiane jest jako oddziaływania stymulujące rozwój dziecka (od momentu rozpoznania zagrożenia do rozpoczęcia spełniania obowiązku szkolnego), uwzględniając jego potrzeby i możliwości psychofizyczne oraz działanie mające na celu wsparcie i pomoc jego rodzinie.
                    Do jego prowadzenia powoływany jest zespół specjalistów złożony z: psychologa, pedagoga, logopedy. Zespół ten  działa przez cały rok tzn., że w każdym momencie rodzic może zgłosić się  o pomoc dla swojego dziecka. Zespół wykonuje czynności zarówno diagnostyczne, jak i terapeutyczne. W ramach diagnostyki wykonywane są specjalistyczne badania psychologiczno – pedagogiczno -logopedyczne oraz wydawane są opinie o wczesnym wspomaganiu rozwoju małego dziecka. Natomiast w ramach terapii prowadzone są zajęcia terapeutyczne z psychologiem, pedagogiem lub logopedą – w zależności od problemów rozwojowych dziecka. </p>

                    <h2>Cele</h2>
                    <ul>
                        <li>zapobieganie występowaniu i/lub pogłębianiu się nieprawidłowości w rozwoju psychoruchowym dziecka;</li>
                        <li>pomoc dziecku w pełnym wykorzystaniu jego potencjału rozwojowego w zakresie funkcji poznawczych, małej i dużej motoryki, komunikacji;</li>
                        <li>wyzwalanie i wzmacnianie aktywności społecznej, poznawczej i komunikacji dziecka (w tym rozwoju mowy i języka);</li>
                        <li>systematyczne dążenie do poprawy jakości życia dziecka, do zapewnienia mu pełnego radości, pozbawionego napięć dzieciństwa, pomimo występującej niepełnosprawności lub zaburzeń rozwoju;</li>
                        <li>przygotowanie dziecka z niepełnosprawnością ruchową, zmysłów, intelektualną i psychiczną do korzystania z edukacji, do funkcjonowania w grupie;</li>
                        <li>przygotowanie dziecka do samodzielnego korzystanie z zajęć organizowanych w placówkach  wychowawczych i edukacyjnych przeznaczonych dla wszystkich dzieci.</li>
                    </ul>

                    <h2>Organizacja zajęć</h2>
                    <ul>
                        <li>Zajęcia w ramach wczesnego wspomagania organizuje się w wymiarze od 4 do 8 godzin w miesiącu, w zależności od możliwości psychofizycznych i potrzeb dziecka.</li>
                        <li>Zajęcia w ramach wczesnego wspomagania są prowadzone indywidualnie z dzieckiem i jego rodziną.</li>
                        <li>W przypadku dzieci, które ukończyły 3 rok życia, zajęcia w ramach wczesnego wspomagania mogą być prowadzone w grupach liczących 2 lub 3 dzieci, z udziałem ich rodzin.</li>
                        <li>Zajęcia w ramach wczesnego wspomagania, w szczególności z dziećmi, które nie ukończyły 3 roku życia, mogą być prowadzone także w domu rodzinnym.</li>
                        <li>Miejsce prowadzenia zajęć w ramach wczesnego wspomagania ustala dyrektor odpowiednio przedszkola, szkoły, ośrodka lub poradni w uzgodnieniu z rodzicami (prawnymi opiekunami) dziecka.</li>
                    </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('wczesne');
                    </script>
                    """
                ],
    u'pomocWarsztaty.html':
                [
                    u"Zajęcia warsztatowe na terenie szkół",
                    u"""
                    <p>– na wniosek dyrektora szkoły.</p>

                <table>
                    <th>Lp.</th>
                    <th>Temat</th>
                    <th>Grupa wiekowa</th>

                    <tr>
                        <td>1.</td>
                        <td>"Jestem uczniem" - zajęcia integracyjne</td>
                        <td>kl. I szkoły podstawowej</td>
                    </tr>
                    <tr class="odd">
                        <td>2.</td>
                        <td>Komunikacja interpersonalna</td>
                        <td>kl. IV-VI szkoły podstawowej, gimnazjum</td>
                    </tr>
                    <tr class="">
                        <td>3.</td>
                        <td>Jak sobie radzić ze stresem?</td>
                        <td>gimnazjum, szkoła ponadgimnazjalna</td>
                    </tr>
                    <tr class="odd">
                        <td>4.</td>
                        <td>Doceń siebie – czyli jak wzmacniać poczucie własnej wartości?</td>
                        <td>kl. IV-VI szkoły podstawowej</td>
                    </tr>
                    <tr class="">
                        <td>5.</td>
                        <td>Jak radzić sobie w sytuacjach kryzysowych?</td>
                        <td>gimnazjum, szkoła ponadgimnazjalna</td>
                    </tr>
                    <tr class="odd">
                        <td>6.</td>
                        <td>Trening twórczego myślenia</td>
                        <td>kl. III-VI szkoły podstawowej</td>
                    </tr>
                    <tr class="">
                        <td>7.</td>
                        <td>Zaburzenia odżywiania – anoreksja, bulimia</td>
                        <td>gimnazjum, szkoła ponadgimnazjalna</td>
                    </tr>
                    <tr class="odd">
                        <td>8.</td>
                        <td>Jak radzić sobie z własną złością?</td>
                        <td>kl. IV-VI szkoły podstawowej, kl. I gimnazjum</td>
                    </tr>
                    <tr class="">
                        <td>9.</td>
                        <td>Internet – fascynacja czy zagrożenie?</td>
                        <td>kl. IV-VI szkoły podstawowej</td>
                    </tr>
                    <tr class="odd">
                        <td>10.</td>
                        <td>Gry komputerowe – grać czy nie grać?</td>
                        <td>kl. IV-VI szkoły podstawowej</td>
                    </tr>
                    <tr class="">
                        <td>11.</td>
                        <td>"Potrafię się uczyć" - aktywne metody uczenia się</td>
                        <td>kl. V-VI szkoły podstawowej</td>
                    </tr>
                    <tr class="odd">
                        <td>12.</td>
                        <td>Samookaleczenia- moda czy coś więcej?</td>
                        <td>kl. V-VI szkoły podstawowej, gimnazjum</td>
                    </tr>
                    <tr class="">
                        <td>13.</td>
                        <td>Zajęcia zawodoznawcze "Kim być?"</td>
                        <td>dla uczniów kl. III gimnazjum</td>
                    </tr>
                    <tr class="odd">
                        <td>14.</td>
                        <td>Zajęcia zawodoznawcze "Planuję przyszłość"</td>
                        <td>szkoła ponadgimnazjalna</td>
                    </tr>
                    <tr class="">
                        <td>15.</td>
                        <td>Inne w miarę potrzeb szkół w celu rozwiązywania problemów zaistniałych w klasie</td>
                        <td>szkoła podstawowa, gimnazjum, szkoła ponadgimnazjalna</td>
                    </tr>



                </table>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('warsztaty');
                    </script>
                    """
                ],

    u'pomocFerie.html':
                [
                    u""" "FERIE Z PORADNIĄ" <span class='attention'>NOWOŚĆ !</span> """,
                    u""" <p>Zajęcia terapeutyczno-wychowawcze dla uczniów z kl. I-III szkoły podstawowej w terminie 13-17.02.2017 roku, w godzinach dopołudniowych. Szczegółowy program będzie podany w styczniu 2017 roku.</p>
                         <p>Osobami odpowiedzialnymi za zajęcia są: E. Cieszko-Kowalska, M. Jonko, A. Politowska-Kowal.</p>""",
                    u"""
                        <script type="text/javascript">
                            markSelected('ferie');
                        </script>
                    """

                ],   
    u'pomocDlaRodziców.html':
                [
                    u"Pomoc dla rodziców",
                    u"""
                    <p>Adresując swoją pomoc do rodziców poradnia proponuje następujące inicjatywy:</p>
                    <ul>
                        <li><a href="pomocDlaRodzicówSzkoła.html">Szkoła dla Rodziców i Wychowawców,</a></li>
                        <li><a href="pomocDlaRodzicówPorady.html">Porady dla rodziców,</a></li>
                        <li><a href="pomocDlaRodzicówDzieckoEmocje.html">Jak pomóc dziecku w radzeniu sobie z emocjami?,</a></li>
                        <!-- <li><a href="pomocDlaRodzicówDyżur.html">Dyżur pedagoga specjalnego, socjoterapeuty,</a></li> -->
                        <!-- <li><a href="pomocDlaRodzicówByćMamą.html">Cykl zajęć pt. "Być mamą".</a></li> -->
                        <!-- <li><a href="pomocDlaRodzicówKonferencja.html">Konferencja \"Depresja, samookaleczenia, ADHD, autyzm – jak pomóc?\".</a></li> -->
                        <li><a href="pomocDlaRodzicówPogadanki.html">Pogadanki, prelekcje, wasztaty na terenie szkół, przedszkoli i placówek,</a></li>

                    </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('pomocDlaRodzicow');
                    </script>
                    """
                ],
    u'pomocDlaRodzicówSzkoła.html':
                [
                    u"\"Szkoła dla Rodziców i Wychowawców cz. I i cz. II\"",
                    u"""
                        <h1>Część I - "Jak mówić, żeby dzieci nas słuchały i jak słuchać, żeby dzieci do nas mówiły"</h1>

                        W Poradni Psychologiczno-Pedagogicznej w Białogardzie prowadzone są zazwyczaj dwie edycje zajęć <strong>"Szkoły dla Rodziców cz. I, czyli jak mówić, żeby dzieci nas słuchały
                        i jak słuchać, żeby dzieci do nas mówiły"</strong> w I i II semestrze.

                        <p>Sekretariat poradni przyjmuje zapisy przez cały rok.</p>

                        <div class="attention" style="font-size: 1.3em;">Spotkanie organizacyjne odbędzie się 4 października 2016 roku o godz. 16:00 w Klubie Nauczyciela w budynku poradni.</div>

                        <h2>Cele treningu</h2>
                        <ul>
                            <li>nabywanie praktycznych umiejętności budowania prawidłowych relacji dorosłych z dziećmi, a także ze współmałżonkiem i innymi ludźmi – poprzez poznanie i wdrażanie w kontaktach odpowiednich zasad komunikacji;</li>
                            <li>dostarczenie uczestnikom konkretnych wskazówek doskonalących metody wychowawcze - jak skutecznie radzić sobie w sytuacjach: stawiania dziecku granic, wspierania w radzeniu sobie z emocjami, zachęcania do współpracy, zachęcania do samodzielności, rozwiązywania problemów, uwalniania z roli, budowania odpowiedniej samooceny;</li>
                            <li>uzyskanie przez osoby uczestniczące wsparcia emocjonalnego i możliwości odreagowywania bieżących napięć w relacjach;</li>
                            <li>uświadomienie uczestnikom, że skuteczność wychowania w znacznym stopniu zależy od osoby wychowującej i od pracy, którą włoży ona w zmianę swojego funkcjonowania.</li>
                        </ul>
                        <h2>Forma</h2>
                        <ul>
                            <li>"Szkoła dla Rodziców" to cykl warsztatów prowadzony metodami aktywnymi w grupie przez psychologa i pedagoga;</li>
                            <li>każde ze spotkań trwa 3 godziny i odbywa się w ustalony dzień tygodnia po południu - przez dziesięć kolejnych tygodni; zazwyczaj organizujemy dwie edycje: wiosenną (marzec-maj) oraz jesienną (październik-grudzień).</li>
                            <li>spotkania mają stałą strukturę: rundka na początek (omówienie pracy domowej, z czym przychodzę na zajęcia, co się zdarzyło w ciągu tygodnia), po czym omówienie nowego tematu, ćwiczenia praktyczne oraz rundka na zakończenie (z jakim uczuciem, myślą wychodzę dziś z zajęć);</li>
                            <li>w zajęciach wykorzystywana jest książka „Jak mówić żeby dzieci nas słuchały, jak słuchać żeby dzieci do nas mówiły” A. Faber, E. Mazlisch;</li>
                            <li>każdy z rodziców na bieżąco otrzymuje materiały z danego spotkania, uczestnicy mają także do wykonania zadania domowe służące praktycznemu wdrażaniu nowopoznanych umiejętności, pracują także w domu ze wskazaną wcześniej książką.</li>
                        </ul>
                        <h2>Tematyka zajęć obejmuje</h2>
                        <ul>
                            <li>Spotkanie I - "Organizacyjne"</li>
                            <li>Spotkanie II - "Poznanie się, kontrakt, integracja"</li>
                            <li>Spotkanie III - "Granice"</li>
                            <li>Spotkanie IV-V - "Uczucia"</li>
                            <li>Spotkanie VI - "Zachęcanie dziecka do współpracy"</li>
                            <li>Spotkanie VII - "Zachęcanie dziecka do samodzielności"</li>
                            <li>Spotkanie VIII - "Kary"</li>
                            <li>Spotkanie IX - "Rozwiązywanie problemów i konfliktów"</li>
                            <li>Spotkanie X - "Wpisywanie dziecka w role i uwalnianie od grania ról"</li>
                            <li>Spotkanie XI - "Pomocna pochwała i zachęta"</li>
                        </ul>

                        <div id="szkola-cz-2">
                        <h1>Część II - "Rodzeństwo bez rywalizacji"</h1>
                        <p>
                        Istnieje także możliwość udziału absolwentów "Szkoły dla Rodziców cz. I" w cz. II - <strong>"Rodzeństwo bez rywalizacji"</strong> <span class='attention'>NOWOŚĆ !</span>
                        </p>

                        <!-- <img src="../img/rodzenstwo-plakat.jpg" class="img-responsive center-block"> -->
                        <h2>Cele zajęć:</h2>
                        <ul>
                            <li>wspieranie procesu budowania wzajemnych (opartych na więzi i szacunku) relacji między dziećmi,</li>
                            <li>utrwalanie umiejętności wyniesionych z I części „Szkoły dla rodziców i wychowawców”,</li>
                            <li>rozwijanie umiejętności pomocnych w eliminowaniu agresji, rywalizacji, egoizmu, zazdrości między rodzeństwem,</li>
                            <li>uświadomienie mechanizmów wpływających na zaburzone relacje między dziećmi,</li>
                            <li>wymiana doświadczeń pomiędzy rodzicami.</li>
                        </ul>

                        <h2>Zagadnienia poruszane w części II:</h2>
                        <ul>
                            <li>rywalizacja i zazdrość między dziećmi,</li>
                            <li>kłótnie, bójki dzieci i różne inne trudności,</li>
                            <li>problemy sprawiedliwości, ulubieńców i egoizmu,</li>
                            <li>wpływ ról na relacje między dziećmi.</li>
                        </ul>
                        </div>

                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('pomocRodziceSzkola');
                    </script>
                    """
                ],
    u'pomocDlaRodzicówPogadanki.html':
                [
                    u"Pogadanki, prelekcje, warsztaty na terenie szkół/przedszkoli/placówek",
                    u"""
                        <p>zgodnie z zapotrzebowaniem rodziców, na pisemny wniosek dyrektora.</p>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('pomocRodzicePogadanki');
                    </script>
                    """
                ],
    u'pomocDlaRodzicówPorady.html':
                [
                    u"Porady dla rodziców",
                    u"""
                        <p>Udzielane przez psychologa, pedagoga lub logopedę na terenie poradni – po ustaleniu terminu w sekretariacie.</p>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('pomocRodzicePorady');
                    </script>
                    """
                ],
    u'pomocDlaRodzicówDzieckoEmocje.html':
                [
                    u"Jak pomóc dziecku w radzeniu sobie z emocjami?",
                    u"""
                     <p>Zajęcia dla rodziców dzieci uczęszczających na indywidualne zajęcia wspierające w poradni (3 spotkania) – na terenie poradni.</p>
                     <p>Przewidywany termin rozpoczęcia zajęć: styczeń 2017 roku.</p>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('pomocRodziceEmocje');
                    </script>
                    """
                ],
    # u'pomocDlaRodzicówDyżur.html':
    #             [
    #                 u"Dyżur pedagoga specjalnego, socjoterapeuty",
    #                 u"""
    #                     <p>w godzinach od 12:00 do 18:00 w każdy wtorek na terenie poradni w celu porad, konsultacji, wsparcia – ustalenie terminu przez sekretariat poradni.</p>
    #                 """,
    #                 u"""
    #                 <script type="text/javascript">
    #                     markSelected('pomocRodziceDyzur');
    #                 </script>
    #                 """
    #             ],
    # u'pomocDlaRodzicówByćMamą.html':
    #             [
    #                 u"\"Być mamą\" – zajęcia dla mam dzieci od 1 do 4 roku życia",
    #                 u"""
    #                     <p>Podczas zajęć warsztatowych poruszane będą następujące zagadnienia: rola rodzica w życiu dziecka, etapy
    #                     rozwojowe dziecka w pierwszych 4 latach (zadania rozwojowe, momenty krytyczne), a także aspekty wychowawcze tj. wspieranie dziecka
    #                     w samodzielności, wyznaczanie mu granic, towarzyszenie w przeżywanych stanach emocjonalnych, pokazywanie dziecku konsekwencji jego działań, wspieranie
    #                     i chwalenie podejmowanych wysiłków, lepsze panowanie nad własnymi emocjami w kontakcie z dzieckiem, by nie podejmować krzywdzących działań.</p>
    #                     <h2>Jakie korzyści ma mama z warsztatów?</h2>
    #                     <ul>
    #                         <li>nawiązanie kontaktu z innymi mamami i wymienianie z nimi doświadczeń;</li>
    #                         <li>doskonalenie wiedzy na temat rozwoju i potrzeb dziecka;</li>
    #                         <li>zdobywanie umiejętności rozpoznawania emocji własnych i dziecka;</li>
    #                         <li>rozwijanie wiedzy i umiejętności z zakresu wychowywania dziecka;</li>
    #                         <li>poznanie nowych sposobów reagowania na trudności dziecka;</li>
    #                         <li>zyskanie większej świadomości własnych kompetencji rodzicielskich w kontakcie z dzieckiem.</li>
    #                     </ul>
    #                     <p>Przewidywany termin rozpoczęcia zajęć: II semestr roku szkolnego 2015/2016. Na zajęcia zapisać się można w sekretariacie poradni lub u prowadzących: E. Cieszko-Kowalskiej i J. Piotrowicz.</p>
    #                 """,
    #                 u"""
    #                 <script type="text/javascript">
    #                     markSelected('pomocRodziceBycMama');
    #                 </script>
    #                 """
    #             ],
    # u'pomocDlaRodzicówKonferencja.html':
    #             [
    #                 u"Konferencja &quot;Depresja, samookaleczenia, ADHD, autyzm – jak pomóc?&quot;",
    #                 u"""
    #                 <p>II Powiatowa Konferencja nt. &quot;Depresja, samookaleczenia, ADHD, autyzm – jak pomóc?&quot; odbędzie się w dniu <strong>12.02.2016r.</strong> (ostatni piątek ferii zimowych) w Centrum Kultury i Spotkań Europejskich w Białogardzie przy ul. 1-go Maja 15.
    #                     Wykłady prowadzone będą przez specjalistów- praktyków zajmujących się powyższą problematyką, między innymi wykład dotyczący ADHD wygłosi autorytet w tej dziedzinie – <strong>dr n. med.
    #                     Artur Kołakowski</strong>.</p>
    #                     <p>Szczegółowe informacje można uzyskać w sekretariacie poradni lub pod numerem telefonu 94 312 25 96, kom. 515 082-620.</p>
    #                      <p>Przewidywany koszt konferencji wynosi 150zł (w tej sumie mieszczą się materiały konferencyjne oraz dwa posiłki). Wpłat można dokonywać od 02.01.2016r. do 05.02.2016r. na konto poradni:</p>
    #                     <div style='text-align: center; padding-bottom: 15px;'>
    #                      72 1240 3666 1111 0000 4344 7880
    #                     </div>

    #                     <h2>Program</h2>
    #                     <style>
    #                         .biography {
    #                             padding-left: 30px;
    #                             padding-top: 10px;
    #                             font-size: 12px;
    #                         }
    #                         .timetable td {
    #                             padding-top: 5px;
    #                             padding-bottom: 5px;
    #                         }

    #                         .timetable {
    #                             border-bottom: none !important;
    #                         }
    #                     </style>
    #                         <table class="timetable">
    #                             <tr><td>08.45 – 09.10</td><td>Rejestracja uczestników</td></tr>
    #                             <tr class="odd"><td>09.15 – 09.30</td><td>Powitanie</td></tr>
    #                             <tr><td>09.30 – 11.00</td><td>Wykład: &quot;Samookaleczenia&quot; - mgr Małgorzata Łuba</td></tr>
    #                             <tr class="odd"><td>11.00 – 11.25</td><td>Przerwa kawowa</td></tr>
    #                             <tr><td>11.25 – 12.30</td><td>Wykład: &quot;Depresja&quot; - mgr Małgorzata Łuba</td></tr>
    #                             <tr class="odd"><td>12.30 – 14.00</td><td>Wykład: &quot;Nadpobudliwość psychoruchowa&quot; - dr n. med. Artur Kołakowski</td></tr>
    #                             <tr><td>14.00 – 14.30</td><td>Przerwa obiadowa</td></tr>
    #                             <tr class="odd"><td>14.30 – 16.00</td><td>Wykład: &quot;Autyzm&quot; - mgr Marta Wójcik</td></tr>
    #                             <tr><td>16.00 – 16.15</td><td>Zakończenie konferencji</td></tr>
    #                         </table>

    #                     <h2>Prelegenci</h2>

    #                         <strong>dr n. med. Artur Kołakowski</strong>
    #                         <div class="biography">
    #                             <ul>
    #                                 <li>Specjalista psychiatra,</li>
    #                                 <li>Specjalista psychiatrii dzieci i młodzieży,</li>
    #                                 <li>Psychoterapeuta poznawczo – behawioralny,</li>
    #                                 <li>Certyfikat Polskiego Towarzystwa Terapii Poznawczej i Behawioralnej (PTTTiB), certyfikat European Association of Cognitive Behavioural Therapy (EACBT),</li>
    #                                 <li>Superwizor – dydaktyk PTTPiB.</li>
    #                             </ul>
    #                             <p>Pracuje z dziećmi i młodzieżą z problemami rozwojowymi, psychologicznymi i psychoterapeutycznymi, zarówno jako lekarz jak i psychoterapeuta, obecnie w Ośrodku Poza Schematami. Specjalizuje się w
    #                             diagnozie i leczeniu zaburzeń rozwojowych u dzieci i młodzieży oraz psychoterapii nastolatków oraz osób dorosłych. Od kilku lat pracuje także w nurcie psychoterapii schematu. Od wielu lat uczy prowadzenia
    #                             terapii poznawczo – behawioralnej – obecnie w Centrum Psychoterapii Poznawczo – Behawioralnej oraz w Fundacji Rozwoju Psychiatrii i Psychoterapii. Współautor między innymi następujących pozycji:</p>
    #                             <ol><li>Artur Kołakowski, Tomasz Wolańczyk, Agnieszka Pisula, Magdalena Skotnicka, Anita Bryńska: <i>&quot;ADHD – zespół nadpobudliwości psychoruchowej – Przewodnik dla rodziców i wychowawców&quot;</i>, Gdańskie Wydawnictwo Psychologiczne, 2006</li>
    #                             <li>Artur Kołakowski, Agnieszka Pisula – <i>&quot;Sposób na trudne dziecko, przyjazna terapia behawioralna – Niezbędnik dla rodziców, nauczycieli i terapeutów&quot;</i>, Gdańskie Wydawnictwo Psychologiczne, Sopot 2011, ISBN 978-83-7489-203-2</li>
    #                             <li>Artur Kołakowski (Redakcja Naukowa): <i>&quot;Zaburzenia zachowania u dzieci. Teoria i praktyka.&quot;</i> GWP Sopot 2013</li></ol>
    #                         </div>

    #                         <strong>mgr Małgorzata Łuba</strong>
    #                         <div class="biography">
    #                             <ul>
    #                                 <li>Psycholog (Wydział Psychologii UW), w trakcie szkolenia na psychoterapeutę poznawczo-behawioralnego,</li>
    #                                 <li>Trener umiejętności psychologicznych, certyfikowany trener biznesu (House of Skills), trener metody odkrywania potencjału zawodowego &quot;Spadochron&quot; (FISE),</li>
    #                                 <li>Członek zarządu Polskiego Towarzystwa Suicydologicznego, współzałożycielka nieformalnego Stowarzyszenia Pomocy Rodzinom i Bliskim Samobójców &quot;Tabu&quot;,</li>
    #                                 <li>Zajmuje się psychologią praktyczną – prowadzi psychoterapię, rehabilitację neuropsychologiczną, grupy wsparciowe i rozwojowe oraz spotkania psychoedukacyjne,</li>
    #                                 <li>Prowadzi zajęcia dydaktyczne na Akademii Pedagogiki Specjalnej, współpracuje m.in. z Centrum CBT-EDU, Instytutem Badań w Oświacie, Wydawnictwem &quot;Fraszka Edukacyjna&quot;,</li>
    #                                 <li>Publikuje artykuły o terapeutycznej pracy z dziećmi i młodzieżą w &quot;Głosie Pedagogicznym&quot;.</li>
    #                             </ul>
    #                         </div>

    #                         <strong>mgr Marta Wójcik</strong>
    #                         <div class="biography">
    #                             <ul>
    #                                 <li>Psycholog, trener,</li>
    #                                 <li>Terapeuta w Instytucie Wspierania Rozwoju Dziecka w Gdańsku (IWRD), który wszechstronnie pomaga dzieciom z autyzmem i ich rodzinom. IWRD uzyskał status pierwszej w Polsce i Europie repliki Princeton Child Development Institute w USA (jednej z najlepszych placówek terapeutycznych na świecie),</li>
    #                                 <li>Dyrektor IWRD Niepublicznego Ośrodka Doskonalenia Nauczycieli, konsultant w Niepublicznej Poradni Psychologiczno-Pedagogicznej,</li>
    #                                 <li>Prowadzi zajęcia na Studium Podyplomowym: &quot;Wczesne wspomaganie, edukacja i terapia dzieci i młodzieży z zaburzeniami rozwoju&quot; oraz wykłady i szkolenia z zakresu terapii behawioralnej dzieci z autyzmem dla nauczycieli i terapeutów na terenie całego kraju,</li>
    #                                 <li>Studentka studiów doktoranckich z Analizy Behawioralnej na Oslo and Akershus University College of Applied Sciences (HiOA),</li>
    #                                 <li>Współautorka następujących publikacji:
    #                                     <ol>
    #                                         <li>Budzińska A., Lubomirska A., Wójcik M., Krant, P. J., McClannahan L. (2014). <i>&quot;Use of scripts and scripts-fading procedure and activity schedule to develop spontaneous social interaction in three-year-old girl with autism.&quot;</i> Health Psychology Report, vo. 2(1), 2014</li>
    #                                         <li>Budzinska A., Wojcik M. (2012). <i>&quot;Promoting the generalization of verbal behavior in autistic child.&quot;</i> Acta Neuropsychologica Nr 2 (10)</li>
    #                                         <li>Budzińska A., Wójcik M. (2010). <i>&quot;Zespół Aspergera. Księga pytań i odpowiedzi.&quot;</i> Wydawnictwo Harmonia.</li>
    #                                         <li>Budzińska A., Wójcik M. (2010). <i>&quot;Teaching verbal behaviors to a four-year-old autistic boy using techniques off Applied Behavior Analysis.&quot;</i> Acta Neuropsychologica, vol. 8, no. 2.</li>
    #                                     </ol>

    #                                 </li>
    #                             </ul>
    #                         </div>

    #                     <h2>Media</h2>
    #                     <img class="imgCenter" src="../img/depresja-plakat-big.jpg" />

    #                 """,
    #                 u"""
    #                 <script type="text/javascript">
    #                     markSelected('pomocRodziceKonferencja');
    #                 </script>
    #                 """
    #             ],

    u'pomocGrupoweBystryUmysl.html':
                [
                    u"\"Bystry umysł\" - zajęcia doskonalące koncentrację uwagi dla klas II-IV szkoły podstawowej. <span class='attention'>NOWOŚĆ !</span>",
                    u"""
                        <p>"Bystry umysł" to zajęcia mające na celu rozwijanie procesów poznawczych, szczególnie koncentracji uwagi, a także: pamięci, myślenia logicznego i twórczego oraz umiejętności skutecznego uczenia się.</p>
                    """,
                    u""" 
                        <script type="text/javascript">
                            markSelected('szkPomocGrupoweDobryStart2');
                        </script>
                    """
                ],

    u'pomocGrupoweTerapiaReki.html':
                [
                    u"Terapia ręki dla dzieci 5-7 letnich <span class='attention'>NOWOŚĆ !</span>",
                    u"""<h2>Cele:</h2>
                        <ul>
                            <li>usprawnianie małej motoryki, czyli precyzyjnych ruchów dłoni i palców,</li>
                            <li>dostarczanie wrażeń dotykowych i poznawania dzięki nim różnych kształtów i struktur materiałów oraz nabywanie umiejętności ich rozróżniania.</li>
                        </ul>
                    """,
                    u""" 
                        <script type="text/javascript">
                            markSelected('szkPomocGrupoweTerapiaReki');
                        </script>
                    """
                ],
    u'pomocGrupoweTerapiaReki2.html':
                [
                    u"Terapia ręki dla dzieci 5-7 letnich <span class='attention'>NOWOŚĆ !</span>",
                    u"""<h2>Cele:</h2>
                        <ul>
                            <li>usprawnianie małej motoryki, czyli precyzyjnych ruchów dłoni i palców,</li>
                            <li>dostarczanie wrażeń dotykowych i poznawania dzięki nim różnych kształtów i struktur materiałów oraz nabywanie umiejętności ich rozróżniania.</li>
                        </ul>
                    """,
                    u""" 
                        <script type="text/javascript">
                            markSelected('grupoweTerapiaReki');
                        </script>
                    """
                ],            

    u'pomocDlaNauczycieli.html':
                [
                    u"Pomoc dla nauczycieli",
                    u"""

                            <h2>1. WARSZTATY DLA NAUCZYCIELI</h2>
                            <p>- tematyka wynikająca z zapotrzebowania placówek, na ich pisemny wniosek.</p>

                            <h2>2. UDZIAŁ W RADACH PEDAGOGICZNYCH</h2>
                            <p>- zgodnie z zapotrzebowaniem placówek, na pisemny ich wniosek.</p>

                            <h2>3. PORADY prowadzone przez psychologa, pedagoga lub logopedę</h2>
                            <p>- na terenie poradni, po wcześniejszym umówieniu w sekretariacie poradni.</p>

                            <h2>4. GRUPA ROZWOJU ZAWODOWEGO LOGOPEDÓW PRZEDSZKOLNYCH I SZKOLNYCH</h2>
                            <p>- cykliczne spotkania logopedów pracujących w przedszkolach i szkołach z logopedami białogardzkiej poradni o charakterze szkoleniowym prowadzone na terenie poradni. Mają one na celu wymianę doświadczeń w pracy logopedycznej oraz wspólne ustalanie sposobów postępowania terapeutycznego w celu podniesienia umiejętności wymowy dziecka.</p>
                            <p class='attention' style="font-size: 1.1em;">Pierwsze spotkanie na temat "Jak skutecznie pracować z dzieckiem z sygmatyzmem?" odbędzie się 13.10.2016 roku o godzinie 17:00 w Klubie Nauczyciela na parterze w budynku poradni.</p>

                            <h2 id="sieć_współpracy">5. SIEĆ WSPÓŁPRACY I SAMOKSZTAŁCENIA DLA SOCJOTERAPEUTÓW <span class='attention' style="font-size: 0.4em;">NOWOŚĆ !</span></h2>
                            <p>– cykliczne spotkania dedykowane socjoterapeutom w celu:</p>
                            
                            <ul>
                                <li>wymiany doświadczeń między uczestnikami,</li>
                                <li>analizy "dobrych praktyk" stosowanych przez uczestników,</li>
                                <li>udzielania wsparcia w pracy socjoterapeutycznej,</li>
                                <li>poszerzania kompetencji uczestników,</li>
                                <li>tworzenia nowych rozwiązań na potrzeby szkół uczestników,</li>
                                <li>pogłębiania współpracy między szkołami oraz między szkołami a poradnią.</li>
                            </ul>

                            <p class='attention' style="font-size: 1.1em;">Pierwsze spotkanie organizacyjne odbędzie się <strong>21.10.2016 r.</strong> o godzinie <strong>10:30</strong> w Klubie Nauczyciela na parterze budynku poradni.</p>
                            <p>Prowadzące: Ewa Cieszko-Kowalska – psycholog, socjoterapeuta oraz Anna Politowska-Kowal – pedagog, socjoterapeuta.</p>
                
                            <h2>6. WSPOMAGANIE SZKÓŁ, PRZEDSZKOLI I PLACÓWEK <span class='attention' style="font-size: 0.4em;">NOWOŚĆ !</span></h2>
                            <p>- w zakresie realizacji zadań wychowawczych i opiekuńczych oraz podnoszenia umiejętności pracy z dziećmi, młodzieżą i rodzicami – na ich wniosek w formie uzgodnionej z dyrektorem poradni, w miarę możliwości kadrowych.</p>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('pomocDlaNauczycieli');
                    </script>
                    """
                ],
    u'badanieSłuchu.html':
                [
                    u"Komputerowe badanie słuchu",
                    u"""
                        <p>Badanie słuchu jest przeprowadzane na terenie poradni poprzez komputerowy program "Słyszę".
                        Ma ono charakter przesiewowy, co oznacza,
                        że celem jest wykrycie ewentualnych nieprawidłowości bez określania stopnia ubytku słuchu.
                        Jeśli wynik wyszedłby nieprawidłowy, szczegółowe badania należy następnie przeprowadzić w specjalistycznej placówce.</p>

                        <p>Zapisy na przesiewowe komputerowe badanie słuchu w sekretariacie poradni przez cały rok.</p>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('badaniesluchu');
                    </script>
                    """
                ],
    u'szkPomocGrupoweGrupaWsparcia.html':
                [
                    u"Grupa Wsparcia i Rozwoju Osobistego dla Młodzieży",
                    u"""
                        <h2>Cele</h2>
                            <ul>
                                <li>wzmacnianie poczucia własnej wartości, poznanie swoich mocnych stron i ograniczeń;</li>
                                <li>nauka skutecznej komunikacji - praca nad umiejętnością wyrażania własnego zdania i postawą asertywną;</li>
                                <li>doskonalenie umiejętności wyrażania i rozpoznawania uczuć;</li>
                                <li>doskonalenie umiejętności radzenia sobie w sytuacjach stresogennych;</li>
                                <li>nauka strategii rozwiązywania problemów i podejmowania decyzji;</li>
                                <li>nauka planowania aktywności, rozkładu dnia, przewidywania konsekwencji swoich działań;</li>
                                <li>planowanie i osiąganie ważnych celów życiowych.</li>
                            </ul>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('szkGrupoweGrupaWsparcia');
                    </script>
                    """
                ],
    u'pomocGrupoweLepiejGloskuje.html':
                [
                    u"Zajęcia grupowe dla dzieci 5-letnich \"Lepiej głoskuję, lepiej opowiadam\"",
                    u"""
                        <h2>Cele</h2>

                        <p>Zajęcia grupowe dla dzieci 5-letnich \"Lepiej głoskuję, lepiej opowiadam\" mają na celu odkrywanie języka w jego różnych aspektach poprzez:</p>
                        <ul>
                            <li>rozwój świadomości metafonolofgicznej – czyli dotyczącej dźwiękowej struktury języka (umiejętność dzielenia słów na sylaby, sprawne określanie głoski na początku,
                                na końcu i w środku słowa, dzielenie słów na głoski, różnicowanie głosek o podobnym brzmieniu, dobra spostrzegawczość i uwaga słuchowa),</li>
                            <li>rozwój świadomości metamorfologicznej – czyli bogacenie zasobu słownictwa, wiedzy o sposobach tworzenia wyrazów,</li>
                            <li>rozwój świadomości metasyntaktycznej – czyli wiedzy o budowie zdania, rozpoznawanie części mowy,</li>
                            <li>rozwój świadomości metapragmatycznej – czyli umiejętności bardziej sprawnego używania języka – w tym aktywnego słuchania i rozumienia słuchanego tekstu,
                                umiejętność planowania swoich wypowiedzi, wyrażania swoich myśli, przeżyć i spostrzeżeń.</li>
                        </ul>

                        <p>Najogólniejszym celem zajęć jest dobre przygotowanie dzieci do nauki poprawnego czytania i pisania.</p>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('pomocGrupoweLepiejGloskuje');
                    </script>
                    """
                ],
    u'pomocGrupoweMatematyka.html':
                [
                    u"Matematyka bez trudności dla uczniów klas IV-VI szkoły podstawowej",
                    u"""
                        <h2>Cele</h2>
                        <ul>
                            <li>rozwijanie orientacji przestrzennej i motoryki,</li>
                            <li>rozwijanie koordynacji wzrokowo-słuchowo-ruchowej,</li>
                            <li>ćwiczenie myślenia, pamięci, uwagi i umiejętności matematycznych,</li>
                            <li>kształtowanie pojęć czasowych,</li>
                            <li>ćwiczenie posługiwania się jednostkami długości, masy i objętości,</li>
                            <li>rozwijanie wyobraźni, myślenia, aktywności twórczej i zainteresowań matematyką,</li>
                            <li>rozwijanie umiejętności czytania ze zrozumieniem.</li>
                        </ul>

                        <p>Podczas zajęć wykorzystywane są podręczniki z serii Ortograffiti <em>\"Matematyka bez trudności\"</em> oraz różnorodne gry matematyczne.</p>
                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('szkGrupoweMatematyka');
                    </script>
                    """
                ],
    u'pomocGrupoweZajeciaKorekcyjnoKompensacyjne.html':
                [
                    u"Zajęcia korekcyjno – kompensacyjne",
                    u"""
                        <h2>Cele</h2>
                        <ul>
                            <li>usprawnianie funkcji percepcyjno- motorycznych odpowiedzialnych za naukę czytania i pisania,</li>
                            <li>rozwijanie umiejętności czytania i pisania pod wszystkimi względami,</li>
                            <li>kształtowanie czujności ortograficznej,</li>
                            <li>doskonalenie koncentracji uwagi,</li>
                            <li>wzmacnianie wiary w siebie i swoje umiejętności.</li>
                        </ul>

                        <p>Na zajęciach wykorzystywane są następujące pozycje książkowe:</p>
                        <ul>
                            <li><em>&quot;Ortograffiti z Bratkiem&quot;,</em></li>
                            <li><em>&quot;Czytam z Bratkiem&quot;,</em></li>
                            <li><em>&quot;Ortograffiti&quot;,</em></li>
                            <li><em>&quot;Ćwiczenia korekcyjno-kompensacyjne dla dzieci 6-9-letnich&quot;,</em></li>
                            <li><em>&quot;Zestaw ćwiczeń do zajęć korekcyjno-kompensacyjnych dla dzieci w wieku 10-12 lat&quot;,</em></li>
                            <li><em>&quot;Myślę, rozwiązuję i... wiem! – ćwiczenia korekcyjno-kompensacyjne dla uczniów klas 1–3&quot;,</em></li>
                            <li><em>&quot;Myślę, rozwiązuję i...wiem! – ćwiczenia korekcyjno-kompensacyjne dla uczniów klas 4–6&quot;,</em></li>
                            <li><em>&quot;Kramik – ćwiczenia korekcyjno-kompensacyjne&quot;.</em></li>
                        </ul>

                    """,
                    u"""
                    <script type="text/javascript">
                        markSelected('szkGrupoweKorekcyjnoKompensacyjne');
                    </script>
                    """
                ]




}

