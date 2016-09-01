#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Romek'

from template import Template

class Artykuly(Template):
    def __init__(self, templateFile, destinationFolder):
        Template.__init__(self,templateFile, destinationFolder)
        self.database = {
            "article001.html": [
                u"""Ciekawa książka - \"Myślenie obrazami\"""",
                u""" <p class="author">autor: Małgorzata Weiszewska - neurologopeda</p>
                    <hr />
                    <div style="float: left; padding: 20px 20px 20px 10px;"><img class="img-responsive" src="../img/article01mini.png" /></div><p>Pani Iwona pożyczyła mi ciekawą książkę - "MYŚLENIE OBRAZAMI" Temple Grandin.</p>
                    <p>Książka jest dość niezwykła, ponieważ  nie zdarza się często, że autorem jest osoba autystyczna. Mamy więc możliwość zajrzenia do trochę innego świata. Świata wysoko funkcjonującej osoby z autyzmem. Autorką jest żyjąca w Ameryce Temple Grandin –doktor Wydziału Nauk o Zwierzętach Uniwersytetu w Illinois. Jako inżynier zaprojektowała ponad 30% urządzeń stosowanych do hodowli bydła w USA. Walczy o humanitarne i empatyczne traktowanie tych zwierząt, szczególnie w czasie uboju. Duże wrażenie robi jej inteligencja, precyzja z jaką nazywa i opisuje swoje przeżycia. Jest osobą bardzo aktywną – pracuje zawodowo, bierze udział w konferencjach, prowadzi wykłady dotyczące życia osób z autyzmem oraz zmaga się z trudnościami  i szczególnymi uzdolnieniami jakimi dysponuje.</p>
                    <p>Uważa, że od urodzenia jej układ nerwowy znajduje się w stanie nieustannego lęku  i niepokoju – niezależnie od otaczających ją okoliczności. Stan nadmiernego pobudzenia organizmu jest jak trwanie w ciągłej czujności  kogoś kto w każdej chwili gotów jest rzucić się do ucieczki przed nieistniejącym drapieżnikiem. Układ nerwowy jest jakby  biologicznie nastawiony na ucieczkę. Drobne napięcia życia codziennego – to powód do napadów lęku. W dzieciństwie przytłaczały ją zapachy, dźwięki, doznania dotykowe. Z powodu chaosu i przerażenia – nie była zdolna do kontaktu z ludźmi. Krzyczała i kiwała się. Jakość jej życia poprawiła się dzięki temu, że coraz lepiej rozumiała mowę i dzięki farmakoterapii. Długotrwała farmakoterapia stosowana musi być jednak bardzo ostrożnie. Duże znaczenie ma odpowiedni dobór dawki długotrwale przyjmowanych leków.</p>
                    <p>Wiele osób autystycznych zauważa, że dominującym w ich życiu uczuciem jest  - lęk. Niektórzy mówią wręcz o przerażeniu  jakie może odczuwać osoba  ścigana.  Osoby z zaburzeniami autystycznymi próbują zmniejszać poziom lęku  poprzez zachowywanie w swoim otoczeniu wszystkiego  w niezmienionym stanie.  U Temple Grandin ogromny lęk zaczął się dopiero w okresie dojrzewania, u innych osób pojawia się już we wczesnym dzieciństwie. Jedna z nich wspomina, że przez pierwszych 5-6 lat życia towarzyszyło jej przerażenie w najczystszej postaci. Pomocne może być wtedy długotrwałe przyjmowanie leków antydepresyjnych w dobrze dobranych, nie za wysokich dawkach.</p>
                    <p>Temple Grandin jest bardzo inteligentną osobą, wnikliwym naukowcem. Uważa jednak, że   do tej pory nie wie, czym są złożone uczucia w związkach międzyludzkich. A jest już dojrzałym człowiekiem. Rozumie tylko te najprostsze- lęk, gniew, szczęście, smutek. Według  najnowszych badań prawdopodobną przyczyną tego  może być uszkodzenie jąder migdałowatych w mózgu. Powoduje  ono trudności z oceną cudzych intencji i  trudności w radzeniu sobie w sytuacjach społecznych.</p>
                    <p>Dzieci autystyczne często interesują się nadmiernie określonymi rzeczami. Zachowania te noszą nazwę fiksacji. Mogą dotyczyć np. dinozaurów, liczenia itp. Tego rodzaju zainteresowania warto wykorzystać jako zachętę do  nauki. Na przykład dziwaczne obsesje Temple  Grandin nauczycielowi nauk przyrodniczych udało się  skierować na drogę kariery naukowej. Fiksacje warto także uwzględniać  przy wyborze zawodu, gdy jest taka możliwość. Lepszy jest wolontariat związany z tym, co się lubi, niż oderwana od tego praca za pieniądze. Grandin zauważa, że w życiu zawodowym, trudność osobom autystycznym sprawia wielozadaniowość. Na przykład kasjer który lubi liczyć - musi nie tylko dobrze wydawać resztę , ale też rozmawiać z ludźmi. Dziedziną, w której wysoko funkcjonujące osoby autystyczne nieźle sobie radzą jest informatyka. Niemożność rozszyfrowania wyrazu twarzy drugiej osoby czy jej intencji w wirtualnym świecie nie musi być problemem.</p>
                    <hr/>"""
            ],
            "article002.html": [
                u"""Czy z niemowlakiem do logopedy?""",
                u"""<p class="author">autor: Maria Jonko - neurologopeda</p>
                    <hr />
                    <img class="imgCenter img-responsive" src="../img/article02.jpg" />
                    <p>Początek roku szkolnego to czas, gdy do naszej placówki zgłasza się znaczna ilość rodziców ze swoimi pociechami do logopedów z uwagi na rożne problemy z prawidłowym mówieniem. Często jest zadawane pytanie kiedy należy zgłosić się na badanie logopedyczne. Tu odpowiadam, że już z niemowlakiem i tutaj to stwierdzenie  z pewnością budzi zdumienie wielu rodziców, jednak rozwój mowy nie zaczyna się w chwili, gdy dziecko zaczyna mówić pełnymi zdaniami. Wiadomym pozostaje fakt, iż dziecko rozwija się w łonie matki i tam też nabywa różnych umiejętności. Dziecko jeszcze przed urodzeniem ćwiczy istotne dla rozwoju umiejętności, jak np. ssanie kciuka będące zapowiedzią późniejszego ssania  z piersi mamy lub butelki.</p>
                    <p>Co można zbadać u niemowlaka? Logopeda jest  jednym z tych specjalistów, który na podstawie badania jest w stanie w dużej mierze przewidzieć rozwój dziecka, bowiem prawidłowo wyrażone odruchy i funkcje układu ustno-twarzowego są podwaliną właściwej artykulacji, czyli mowy.  Podczas badania sprawdza  i ocenia się różne odruchy.  Po co sprawdza się takie odruchy- można postawić pytanie. Jakość odruchów jest dowodem dojrzewania układu nerwowego dziecka. Wygórowany odruch ssania (mamy nazywają to "gryzieniem") uniemożliwia ssanie piersi (sprawia mamie ból) zbyt słaby natomiast uniemożliwia pobieranie pokarmu. Podobnie zbyt silny odruch wypychania języka znacznie utrudnia karmienie. Część odruchów zanika robiąc miejsce następnym ważnym odruchom, tak na przykład odruch kąsania ustępuje odruchowi żucia, który prócz właściwości pokarmowych gwarantuje płynność ruchów mownych na późniejszym etapie rozwoju. Ocenie  logopedy  podlega także sposób oddychania niemowlaka. Oddychanie buzią szczególnie po katarze może przejść w nawykowe, czego skutkiem jest osłabienie napięcia mięśniowego, przerost migdałków, szybkie podrażnienie błony śluzowej jamy ustnej, co prowadzi do powstawania częstych infekcji górnych dróg oddechowych. Błędem jest długie karmienie dziecka przetartymi pokarmami. Maluchy już od 6 miesiąca powinny gryźć i żuć np. skórkę od chleba, biszkopty lub chrupki. Jeśli zaniedbamy to dziecko może w przyszłości seplenić lub mieć problemy z głoskami „r”, „l”, „sz”, „ż”, „cz” i „dż”.</p>
                    <p>Jeśli Państwo zauważycie, że Wasze roczne dziecko porozumiewa się tylko za pomocą gestów lub sylab, np. „da”, „to” a nie używa innych słów, nie rozumie prostych poleceń, np.”idź do mamy”, śpi z otwartymi ustami -to warto poradzić się logopedy, aby w razie występujących trudności wcześnie reagować i pomóc naszemu maluszkowi je przezwyciężyć. Służymy Państwu w tym zakresie pomocą logopedyczną w Poradni Psychologiczno-Pedagogicznej w Białogardzie przy ulicy Dworcowej 2, na spotkanie można się umówić osobiście w sekretariacie lub telefonicznie.</p>
                    <hr/>"""
            ],
            "article003.html": [
                u"""Domowy logopeda - czyli jak doskonalić mowę przedszkolaka?""",
                u"""<p class="author">autor: Maria Jonko - neurologopeda</p>
                    <hr />
                    <p>Największą liczbę moich pacjentów w Poradni Psychologiczno-Pedagogicznej w Białogardzie stanowią dzieci przedszkolne w okresie kształtowania się swoistej mowy dziecięcej.  Rola rodzica w rozwoju mowy dziecka jest nieoceniona. Logopeda w gabinecie pokazuje dziecku ćwiczenia, ucząc je poprawnej wymowy. Rodzic, jako domowy logopeda powinien codziennie i systematycznie pracować z dzieckiem, utrwalając wyuczone ćwiczenia. Wszystkich rodziców zachęcam do częstego rozmawiania i słuchania dzieci – nie tylko tego co, ale i jak mówią. Powinniśmy jak najwięcej mówić do malucha, opowiadać o tym co robią, pokazywać i nazywać przedmioty znajdujące się w jego otoczeniu. Mówimy poprawnie nie zdrabniając słów.</p>
                    <p>Pomiędzy drugim a trzecim rokiem życia powstają zdania.  Jest to bardzo oczekiwany przez rodziców etap rozwoju mowy. Zdarza się (niestety coraz częściej), że dziecko w tym wieku wymawia tylko kilka słów lub głosek, nazywając nimi wszystko, co go otacza. Towarzyszy temu silna gestykulacja i inne zachowania niewerbalne. Jest to problem, z którym rodzic koniecznie powinien udać się do logopedy.</p>
                    <p>Staramy się zachęcać dziecko do zabaw logopedycznych, tak długo, jak to możliwe, najlepiej przez cały okres przedszkolny. Celem rodzica jako domowego logopedy jest nauczyć dziecko koncentracji uwagi na sygnałach słuchowych i analizowaniu tego, co „wpada do ucha”. Oswajanie z dźwiękami to wstęp do nauki mówienia. Pokazujmy maluchowi  ilustracje czy figurki zwierząt, razem dopasowujmy do nich dźwięki, nakłońmy, by  je powtarzało. Możemy grać na bębenku, klaskać, stukać o blat stołu, a potem prosząc o powtórzenie usłyszanej melodii. Ćwiczymy rozumienie wypowiedzi i zapamiętywanie. Dziecko, które w lot łapie, co się do niego mówi, szybciej uczy się budować własne wypowiedzi – a o to chodzi. Bawmy się np. w szukanie skarbów. Wkładamy do woreczka lub pudełka zabawki. Każdą nazywamy, powtarzamy dwa razy. Prosimy: „Daj mi lalkę i misia”, „Daj mi lalkę, misia i klocek”. Zadanie utrudniamy, dodając kolejne. Rozwijamy i poszerzamy słownictwo. Zachęcamy malca do myślenia. Pomagajmy tworzyć własne wypowiedzi, zadając mu dodatkowe pytania: „Co robi?”, „Jaki jest?”, „Gdzie jest?”, itp. Dzięki temu maluch zacznie składać poznane słowa w proste zdania. Trenujemy poprawne oddychanie bawiąc się np. w „Łąkę w pokoju”, wytnijmy z papieru kwiaty, rozłóżmy na dywanie, wąchajmy je.  Gimnastykujemy cały aparat mowy, bawiąc się wspólnie z dzieckiem np. „W porządki w buzi”. Róbmy wesołe i smutne miny.</p>
                    <p>Jeśli widzimy, że mówienie sprawia dziecku poważny problem, nie czekajmy i udajmy się do logopedy! Zapraszamy do naszej Poradni Psychologiczno-Pedagogicznej w Białogardzie przy ul. Dworcowej 2 w celu umówienia terminu wizyty osobiście lub telefonicznie.</p>
                    <hr/>"""
            ],
            "article004.html": [
                u"""Jak wspierać dziecko nieśmiałe?""",
                u"""<p class="author">autor: Ewa Cieszko-Kowalska – psycholog</p>
                    <hr />
                    <img class="img-responsive imgCenter" src="../img/article04.jpg" />
                    <ol>
                        <li><strong>Baw się z dzieckiem</strong> wykorzystując m.in.:
                            <ul>
                                <li>gry planszowe;</li>
                                <li>techniki plastyczne (np. wycinanki, wydzieranki, farby, kredki, kolorowani, plastelina, orgiami, witraże, masa solna, malowanie palcami);</li>
                                <li>rebusy, krzyżówki, labirynty odpowiednie do wieku;</li>
                                <li>czytanie książek, ich opowiadanie;</li>
                                <li>obrazki do ich opisu i przewidywania, co się dalej stanie;</li>
                                <li>śpiew, muzykę taniec dla zwiększenia relaksacji;</li>
                                <li>zabawy ruchowe;</li>
                                <li>odgrywanie scenek z bajek, filmów;</li>
                                <li>zabawy w teatr np. z kukiełkami, pacynkami;</li>
                                <li>recytowanie wierszy, czytanie dialogów na role z odpowiednią intonacją.</li>
                            </ul>
                        </li>
                        <li><strong>Przyjrzyj się specyfice nieśmiałości swojego dziecka.</strong> Zwróć uwagę, czy twoje dziecko jest nieśmiałe w kontakcie z  jedną osobą czy w grupie; czy tylko w nowych, nieznanych czy wszystkich sytuacjach społecznych; czy dziecko ma zahamowania tylko w bardzo określonych sytuacjach (np. telefonowanie, jedzenie w miejscu publicznym, zabawa) czy we wszystkich. Zbadanie specyfiki trudności społecznych dziecka pozwoli określić, jakich umiejętności powinno ćwiczyć.</li>
                        <li><strong>Modeluj pewność siebie w sytuacjach społecznych.</strong> Modelowanie to najbardziej naturalny sposób uczenia się u dzieci. Zatem:
                            <ul>
                                <li>pierwszy mów: „Dzień dobry” znajomym i przedstawiaj się;</li>
                                <li>bądź przyjazny do ludzi;</li>
                                <li>praw innym komplementy;</li>
                                <li>pomagaj innym, gdy widzisz taką potrzebę;</li>
                                <li>podejmuj ryzyko i komentuj, jak to ważne (np. „Myślałam, że będzie trudniej”, „Myślałem, że pójdzie mi lepiej, ale przynajmniej wiem co robić następnym razem”).</li>
                            </ul>
                        </li>
                        <li><strong>Ćwicz w domu sytuacje społeczne trudne dla dziecka</strong> (uścisk ręki, patrzenie w oczy, rozmowy z innymi dziećmi i dorosłymi, przedstawianie się itp.)</li>
                        <li><strong>Unikaj</strong>
                            <ul>
                                <li>publicznego ośmieszania dziecka;</li>
                                <li>publicznego krytykowania ludzi;</li>
                                <li>poniżania siebie, gdy Ci coś nie wyjdzie;</li>
                                <li>poniżania dziecka, gdy mu coś nie wyjdzie.</li>
                            </ul>
                        </li>
                        <li><strong>Ucz umiejętności społecznych jak najwcześniej</strong>
                            <ul>
                                <li>organizuj spotkania z innymi dziećmi w domach;</li>
                                <li>ucz, jak wchodzić w grupę i jak z niej wychodzić;</li>
                                <li>tłumacz, na czym polega przyjaźń;</li>
                                <li>całą rodziną ćwiczcie bycie w dobrym kontakcie (uśmiechanie się, komplementowanie wzajemne, uściski rąk);</li>
                                <li>proponuj zabawy w ćwiczenie zachowań społecznych poza domem, np. w proszenie o pomoc w sklepie, pytanie o drogę, zakupy w lokalnym sklepie, uśmiechanie się do ludzi, mówienie „dzień dobry” itp.</li>
                            </ul>
                            <p>Warto zwrócić uwagę, jaką zmianę może przynieść dziecku nauczenie go tak prostego zachowania jak uśmiechanie się!</p>
                        </li>

                        <li><strong>Ucz, że istnieje więcej niż jeden sposób patrzenia na sprawy, więcej niż jedno rozwiązanie problemu</strong>
                            <ul>
                                <li>Porażka uczy, czego mamy nie robić, by osiągnąć to, co chcemy.</li>
                                <li>Ucz dziecko poszukiwania rozwiązań, aż znajdzie właściwe (ćwicz w sytuacjach życia codziennego).</li>
                            </ul>
                        </li>

                        <li><strong>Zachęcaj do zmian małymi kroczkami</strong>
                            <p>Duże kroki mogą bardzo zniechęcić nieśmiałych. Metoda głębokiej wody (np. wysłanie dziecka na obóz) jest dobra tylko wtedy, gdy jesteś pewny pozytywnego rezultatu.  Gdy nie – pozwól dziecku wchodzić wolno!</p><p>Najpewniejszym sposobem pokonania nieśmiałości u dzieci jest pozwolenie im na robienie tak małych kroczków, by częściej doświadczały sukcesu niż porażki, a jest to najbardziej prawdopodobne w zadaniach, w których są dobre.</p>
                        </li>

                        <li><strong>Pomóż dziecku odkryć zdolności i umiejętności, które czynią go wyjątkowym</strong>
                            <p>Rozpoznaj zdolności dziecka – najpierw te, które może realizować w samotności. Następnie, stopniowo, pozwól mu się wykazać najpierw w gronie wspierających dorosłych, a potem wśród rówieśników.</p>
                        </li>

                        <li><strong>Pomóż dziecku nauczyć się radzić sobie z emocjami</strong>
                                <p>Słuchaj dziecka z empatią, staraj się pomóc w rozpoznaniu jego emocji. Nie krytykuj i nie oceniaj za odczuwanie konkretnych uczuć. Pomagaj w znalezieniu sposobów radzenia sobie z nieprzyjemnymi emocjami.</p>
                        </li>

                        <li><strong>Ucz tolerancji i szacunku dla innych</strong> Nieśmiałe dzieci są zwykle bardzo krytyczne wobec siebie i innych. Dlatego pokazuj, że ludzie nie muszą być idealni, by być wartościowymi. Im więcej okazujesz wyrozumiałości w stosunku do innych, tym bardziej dzieci będą wyrozumiałe wobec siebie... (i Ciebie).</li>

                        <li><strong>Rozumnie używaj etykietki „nieśmiały”</strong>
                            <ul>
                                <li>Zawsze łącz nieśmiałość z czymś pozytywnym („Jesteś nieśmiałym dzieckiem, jak wielu wybitnych ludzi – Einstein, Kidman, Hanks, J. Roberts”); </li>
                                <li>Nie używaj nieśmiałości jako wymówki dla dziecka, by nie musiało próbować;</li>
                                <li>Podkreślaj inne ważne cechy dziecka, w które naprawdę wierzysz;</li>
                                <li>Nie używaj etykietki, gdy nie jesteś absolutnie przekonany, że będzie to miało pozytywny efekt.</li>
                            </ul>
                        </li>

                        <li><strong>Używaj uśmiechu</strong> (szerzej: POCZUCIA HUMORU) jako sposobu na zwiększenie dystansu do własnych problemów i jako dobrej techniki na rozładowanie napięć w kontaktach z ludźmi.</li>


                        <li><strong>Podkreślaj jak najczęściej mocne strony nieśmiałego dziecka</strong>, koncentruj się na jego zaletach, stosuj pochwały opisowe bez oceniania.</li>

                        <li><strong>Zachęcaj do nauki tańca W PARZE lub uprawiania dowolnego sportu zespołowego.</strong></li>
                    </ol>

                    <div style="text-align: center; font-weight: bold;">
                    ROZMAWIAJ, SŁUCHAJ, WSPIERAJ I KOCHAJ NIEŚMIAŁE DZIECKO ZA TO, KIM ONO JEST, A  NIE ZA TO, JAK ŚMIAŁYM CHCESZ, ABY SIĘ STAŁO !
                    </div>

                    <br />
                    <p>Opracowała Ewa Cieszko-Kowalska na podstawie książki „Jak przezwyciężyć nieśmiałość i lęk przed otoczeniem?” M.Antony, R.Swinson, Sensus 2007</p>


                    <div class="note">
                        <h3>Apel:</h3>
                        Nauczycielu możesz pomóc nieśmiałemu uczniowi, jeżeli będziesz stosował zasady podane poniżej:
                        <ol>
                            <li>Traktuj nieśmiałość jako dość powszechną cechę charakteru i wyrażaj się  o niej tylko w pozytywnym kontekście.</li>
                            <li>Nie zapominaj o istnieniu nieśmiałych dzieci w klasie, ale i nie wyróżniaj ich.</li>
                            <li>Daj nieśmiałemu dziecku zadania do wykonania, do których samo by się nie zgłosiło (np. wytarcie tablicy, zamknięcie klasy po lekcjach, rozdanie klasówek, zebranie informacji od innych uczniów na jakiś temat), by umożliwić mu doświadczanie coraz większego poczucia kompetencji.</li>
                            <li>Podkreślaj jego sukcesy, zalety, mocne strony i pokazuj osiągnięcia.</li>
                            <li>Zachęcaj do wypowiadania się na forum grupy poprzez zadawanie pytań pomocniczych życzliwie ukierunkowujących dziecko; pozostawiaj mu więcej czasu do namysłu.</li>
                            <li>Rozbudzaj jego zainteresowania, które może dzielić z kolegami z klasy.</li>
                            <li>Pomóż nauczyć go, jak inicjować kontakt z drugą osobą poprzez zajęcia grupowe, w parach.</li>
                            <li>Obniżaj jego napięcie emocjonalne poprzez indywidualne rozmowy nastawione na  wysłuchanie, zrozumienie sytuacji oraz nazywanie emocji.</li>
                            <li>Udzielaj wskazówek rodzicom, aby potrafili pomóc swojemu dziecku</li>
                            <li>Nagradzaj nawet małe postępy dziecka.</li>
                            <li>Zwracaj uwagę na dokuczanie nieśmiałemu dziecku w grupie czy w klasie i natychmiast interweniuj.</li>
                        </ol>
                    </div>
                    <hr/>"""
            ],
            "article005.html": [
                u"""Jak wspierać dziecko w pokonywaniu trudności w czytaniu i pisaniu?""",
                u"""<p class="author">autor: Anna Politowska–Kowal - pedagog</p>
                    <hr />
                        <div style="float: left; padding: 20px 20px 20px 10px;"><img img-responsive src="../img/article05.jpg" /></div>
                        <p>Już we wczesnym dzieciństwie można zaobserwować pierwsze symptomy zapowiadające ryzyko dysleksji (specyficznych trudności w czytaniu i pisaniu). Dzieci z ryzykiem dysleksji później zaczynają chodzić  i biegać, mają trudności z układaniem klocków, rysowaniem i samodzielnym ubieraniem się. Mowa u takich dzieci również może rozwijać się wolniej. Na etapie przedszkolnym nie lubią zabaw manipulacyjnych, mają trudności z układaniem puzzli, wykonywaniem prac plastycznych, jazdą na rowerze, wykonywaniem ćwiczeń ruchowych. Nie słyszą rymów i nie potrafią ich tworzyć, nie pamiętają wierszyków, trudności sprawia im dzielenie słów na sylaby, wymienianie słów na wskazaną głoskę. <strong>Należy pamiętać, że nie każde dziecko ryzyka dysleksji musi stać się uczniem z dysleksją.</strong></p>
                        <p>Symptomy ryzyka dysleksji mogą nasilać się na początku nauki w szkole. Dzieci wolniej zapamiętują litery, mylą litery podobne wzrokowo np. o-a, b-d itp., piszą litery i cyfry w lustrzanym odbiciu,  mają trudności ze składaniem głosek w słowa, podczas pisania mogą gubić litery w wyrazach. Są to tylko niektóre trudności jakie możemy zauważyć u takich dzieci. Dziecko może również zauważyć, że jest gorsze od swoich rówieśników. Już w klasie pierwszej pojawiają się dzieci, które nie lubią chodzić do szkoły. Może pojawić się utrata wiary w siebie i chęci do nauki. Jeżeli szybko nie pomożemy dziecku, objawy będą się rozszerzać, a niepowodzenia pogłębiać.</p>
                        <p><strong>Zalecenia do pracy z dzieckiem z trudnościami w czytaniu i pisaniu na terenie domu:</strong></p>
                        <ol>
                            <li>Dobrze jest ustalić stałe godziny pracy, dostosowane do indywidualnych możliwości dziecka z uwzględnieniem przerw.</li>
                            <li>Przygotowanie miejsca pracy, czyli zrobienie porządku na biurku i ułożenie pod ręką wszystkich rzeczy potrzebnych do odrabiania lekcji.</li>
                            <li>Należy zwrócić uwagę na ułożenie ciała, wysokość krzesła dostosować do wysokości biurka i wzrostu dziecka, zadbać o dobre oświetlenie oraz spokój /wyłączenie radia, TV, zajęcie zabawą młodsze dzieci.</li>
                            <li>Jak wiadomo, czytać można się nauczyć tylko czytając. Trening czytania powinien odbywać się codziennie (15-20 min), także podczas dni wolnych od nauki, bowiem przerwy negatywnie wpływają na już opanowane umiejętności. Warto dzieci uczyć czytać metodą sylabową, wówczas szybciej może ona opanować umiejętność czytania całościowego. Początkowo można ułatwić czytanie wybierając pozycje książkowe do ćwiczeń, gdzie sylaby w wyrazach wyróżnione są kolorami. Po odczytaniu wyrazu sylabami należy zmierzać do czytania całościowego. Od początku należy wyrabiać umiejętność rozumienia tego, co się czyta. U dzieci z trudnościami w czytaniu powinno się preferować czytanie głośne, które daje możliwość kontroli poziomu czytania. Niekiedy należy pomóc dziecku w  przejściu z etapu głośnego czytania do cichego. Można to zrobić w następującej kolejności: czytanie głośne, szeptem, a potem czytanie wzrokiem  z „wyłączonym” głosem. W początkowej nauce czytania dziecko może sobie pomóc przesuwając palec, wskaźnik lub linijkę pod tekstem. Ważne jest motywowanie dziecka do czytania poprzez ukazywanie korzyści z czytania i wykorzystywania tej umiejętności do czegoś praktycznego np. odczytania instrukcji do gry. </li>
                            <li>Podobnie jak czytanie, pisanie jest jedną z podstawowych umiejętności nabywanych przez człowieka. Jedną z zauważanych trudności w pisaniu jest niski poziom graficzny pisma. Ćwiczenia w kaligraficznym pisaniu potrzebne są zwłaszcza dziecku, które ma słabszą sprawność grafomotoryczną i koordynację ruchową. Ćwiczenia w pisaniu obejmują: utrwalenie miejsca rozpoczynania pisania litery, ćwiczenia w pisaniu po śladzie, w pisaniu według wzoru liter z zachowaniem właściwego  kierunku pisania, ćwiczenia utrwalające sposób łączenia liter. Od początku nauki pisania należy zwracać uwagę na to, by dziecko umieszczało znak diakrytyczny (czyli kropkę lub kreskę, która jest elementem danej litery) w trakcie pisania litery, a nie po napisaniu wyrazu lub zdania, bo przyczynia się to do opuszczania drobnych elementów liter.</li>
                            <li>Na etapie edukacji wczesnoszkolnej pojawiają się także trudności z opanowaniem poprawnej pisowni (błędy ortograficzne, przestawianie i opuszczanie liter, mylenie liter podobnych graficznie np. o-a, b-d). Ortografii należy uczyć dzieci angażując wszystkie zmysły oraz stosując zabawowe formy nauki: żartobliwe skojarzenia, wierszyki  i rymowanki ortograficzne, kalambury. Ważne jest, aby często powracać do pisowni tych samych wyrazów, aby w ten sposób je utrwalać. Powinno się też stopniowo wdrażać dziecko do samokontroli zapisu (samodzielnie sprawdza ze wzorem), do dokonywania poprawy błędnie napisanego wyrazu (zmazanie gumką, zamalowanie korektorem) oraz do posługiwania się słownikiem ortograficznym.</li>
                        </ol>

                        <p>Rodzicu jeśli obserwujesz, że dziecko ma trudności z nauką  umiejętności czytania i pisania wówczas po zasięgnięciu opinii wychowawcy warto zgłosić je na badania  do Poradni Psychologiczno- Pedagogicznej w Białogardzie. Pozwoli to na określenie przyczyn trudności w pisaniu i czytaniu, zaproponowanie mu odpowiedniej do jego potrzeb pomocy w formie dodatkowych zajęć oraz udzielenie szczegółowych zaleceń do pracy  z dzieckiem. Na badanie dziecko do poradni zgłaszają  rodzice, poprzez złożenie do sekretariatu poradni wniosku o przeprowadzenie badań psychologiczno- pedagogicznych wraz z załączoną opinią ze szkoły. Na terenie poradni prowadzimy specjalistyczne zajęcia: Metoda Dobrego Startu, korekcyjno- kompensacyjne, rozwijające funkcje słuchowe, stymulujące rozwój wszystkich funkcji, aby dzieci mogły przezwyciężyć swoje problemy i nauczyć się czytać i pisać. Zapraszamy do skorzystania z naszej pomocy: Poradnia Psychologiczno- Pedagogiczna w Białogardzie, ul. Dworcowa 2, telefon: 94 312 25 96  lub 515 082 620.</p>

                        <p>Opracowano na podstawie książek: M. Bogdanowicz, A. Adryjanek, M. Różyńska „Uczeń z dysleksją w domu” oraz M. Bogdanowicz, A. Adryjanek „Uczeń z dysleksją w szkole”.</p>
                    <hr/>"""
            ],
            "article006.html": [
                u"Kiedy milczenie nie jest złotem...",
                u"""<p class="author">autor: Małgorzata Weiszewska - neurologopeda</p>
                    <hr />
                    <img class="img-responsive imgCenter" src="../img/article06.jpg" />

                    <p>Umiejętność mówienia w rozwoju ludzkości pojawiła się dość niedawno. Umożliwia przekazywanie i odbieranie informacji między członkami społeczności. Mówiąc, posługujemy się słowami.</p>
                    <p>Jednakże, porozumiewając się między sobą, używamy też innych form – są to odpowiednie gesty, pasująca do sytuacji mimika, zmieniający się ton głosu. Oznacza to, że posługujemy się językiem. Jest to szersze pojęcie, niż mówienie. Umiejętność posługiwania się językiem stanowi podstawę rozwoju poznawczego i społecznego. Kiedy potrafimy coś nazwać – łatwiej nam tworzyć pojęcia, myśleć abstrakcyjnie, dogadać się z mamą.</p>
                    <p>Pierwszym w naszym życiu sposobem komunikacji jest krzyk noworodka. Około 3. tygodnia życia pojawia się ważny komunikat emocjonalny - uśmiech dziecka. Kolejny przekaz to wodzenie wzrokiem za matką; później - głużenie (od 2 do 4 miesiąca życia) i gaworzenie (3-6 miesiąc życia). Dwuletnie dziecko próbuje już budować proste zdania z 2 słów. W słowniku trzylatka może znajdować się 400 do 1000 słów, a u pięciolatka – nawet do 2000. Dzieci 5-7 –letnie zazwyczaj potrafią już swobodnie  porozumiewać się z otoczeniem. Zdarza się jednak, że dzieci posługują się zasobem słów poniżej norm wiekowych lub mają inne trudności w komunikacji - należy wtedy sprawdzić słuch dziecka oraz aparat głosowo-artykulacyjny.</p>
                    <p>Kolejnym etapem diagnozy jest ocena rozwoju umysłowego i potencjalnych możliwości poprzez obserwację zachowań dziecka i testy psychologiczne oparte na skalach bezsłownych. Prawidłowa diagnoza specyficznych zaburzeń rozwoju mowy wcale nie jest łatwa. Tymczasem, wczesne podjęcie odpowiedniej terapii umożliwia pełniejsze wykorzystanie potencjalnych możliwości dziecka – a tym samym poprawia jego funkcjonowanie.</p>
                    <p>Specyficzne zaburzenia rozwoju mowy i języka opisane są w Międzynarodowej Klasyfikacji Chorób (ICD-10):</p>
                    <p><strong>F80. 0 – zaburzenia artykulacji</strong> – zdarzające się bardzo często, oraz rzadziej występujące:</p>
                    <p><strong>F80. 1 – zaburzenia ekspresji mowy</strong> - Dzieci z tym zaburzeniem w wieku lat 3-5 nie potrafią tworzyć i powtarzać słów, <strong>ale dokonują prób porozumiewania się</strong> poprzez: gestykulację, rysunki, mimikę. Nawiązują kontakt emocjonalny z otoczeniem. Obserwacja zachowania, ocena zainteresowań oraz wyniki testów bezsłownych wskazują, że dzieci te nie są upośledzone umysłowo. W miarę dorastania pogłębiają się ich trudności w komunikacji pozasłownej, przekazy stają się nieczytelne, a zasób zrozumiałych dla otoczenia słów za mały aby wyrazić swoje potrzeby, przemyślenia. Powoduje to nowe problemy związane z niemożnością realizacji zadań wpisanych w kolejne etapy życia człowieka.</p>
                    <p><strong>F80. 2 – zaburzenia rozumienia mowy</strong> - Rozumienie mowy u tych dzieci jest znacznie poniżej ich rozwoju umysłowego - występuje ono w bardzo ograniczonym zakresie lub nie ma go wcale. Dzieci te potrafią odbierać z otoczenia i oceniać dźwięki niezwiązane z mową człowieka. W wieku 2-3 lat nie spełniają poleceń – okazuje się, że ich nie rozumieją. Inaczej dzieje się, gdy polecenia te rodzic przekazuje bez użycia słów – np. przy pomocy rysunków lub gestów, przy czym ważnym czynnikiem jest to, czy dziecko zainteresowane jest otoczeniem. Jego zabawy świadczą o prawidłowości możliwości poznawczych.</p>
                    <p>Dzieci te potrzebują relacji z otoczeniem i nawiązują je tak, jak potrafią - poprzez rysunki i gesty. Z czasem jednak problemy z porozumiewaniem mogą prowadzić do osamotnienia, dziwnych zachowań czy wybuchów gniewu.</p>
                    <p>Zaburzenia rozwoju mowy występują także w autyzmie. Profesor Hanna Jaklewicz  uważa, że rozwój mowy  przebiega inaczej u dzieci z wczesną i późną postacią autyzmu. We wczesnej postaci –zaburzenia komunikacji występują już w okresie niemowlęcym – obserwuje się brak kontaktu wzrokowego, brak reakcji na obecność matki, zatrzymanie rozwoju mowy zazwyczaj na etapie gaworzenia. U dzieci z późną postacią autyzmu – do 2-3 roku życia rozwój mowy jest prawidłowy. Później - wraz z narastaniem spirali objawów autyzmu - następuje regres w rozwoju mowy. Około 5-7 roku życia często zauważa się znaczny postęp w rozwoju mowy i języka. Jest to jednak mowa charakterystyczna - zazwyczaj nie służy ona do komunikowania się. Nie towarzyszą jej zwykle gesty i mimika. Umiejętność prowadzenia dyskursu jest ograniczona. Z powodu problemów z rozumieniem relacji międzyludzkich i  przyjmowaniem perspektywy innych osób utrzymują się problemy z używaniem zaimka „ja”. Bardzo charakterystyczna jest echolalia – czyli zaburzenie myślenia, objawiające się jako niepotrzebne powtarzanie słów lub zwrotów wypowiedzianych przez inne osoby - bezpośrednia lub odwleczona.</p>
                    <p><strong>Podstawą określenia rodzaju zaburzeń mowy, jakie ma dziecko, jest ocena funkcji, jaką spełnia język, którym się ono posługuje.</strong></p>
                    <p>U dzieci ze specyficznymi zaburzeniami mowy, gesty, mimika, postawa ciała, reakcje emocjonalne, czy wreszcie kontakt wzrokowy służą próbom nawiązywania kontaktu z otoczeniem. Dzieci autystyczne, aż do momentu „wychodzenia z autyzmu” zazwyczaj nie wykorzystują języka do komunikacji.</p>

                    <hr/>"""
            ],
            "article007.html": [
                u"Kilka słów o autyzmie",
                u"""<p class="author">autor: Marta Hewelt - pedagog</p>
                    <img class="img-responsive imgCenter" src="../img/article007.jpg">
                        <p>Autyzm to całościowe zaburzenie rozwoju, co oznacza, że u dzieci nim dotkniętych obserwuje się objawy nieprawidłowego funkcjonowania we wszystkich obszarach rozwoju.  Charakterystyczne dla autyzmu są zaburzenia relacji społecznych, kontaktu, porozumiewania się, trudności z podporządkowaniem się regułom społecznym wynikające z braku ich zrozumienia, które pojawiają się już we wczesnym dzieciństwie (przed 3 rokiem życia).</p>
                        <p>Autyzm występuje w zależności od przyjętych kryteriów diagnostycznych u około 5-20 dzieci na 10.000 urodzin, trzy razy częściej u chłopców niż u dziewczynek. Przyczyny powstawania zaburzenia nie są jeszcze dostatecznie wyjaśnione, jednakże wyniki wielu badań zdają się potwierdzać hipotezę o jego organicznym podłożu. Zaburzenia autystyczne mają bardzo zróżnicowany charakter i nie tworzą jednolitego obrazu co do symptomatologii i głębokości zaburzeń. Z tego powodu w literaturze światowej używa się określenia „spektrum zaburzeń autystycznych”. Bardzo trudno jest podać pełny i jednolity opis dzieci z autyzmem, gdyż reprezentują one zróżnicowany poziom zachowań i funkcjonowania. Nasilenie poszczególnych objawów może być skrajnie silne, lub czasem (niestety znacznie rzadziej) bardzo dyskretne i ledwo zauważalne. Dlatego też diagnoza autyzmu opiera się na stwierdzeniu obecności charakterystycznych zachowań związanych z tym zaburzeniem. Przeprowadza ją zespół diagnostyczny lub lekarz psychiatra w oparciu o kryteria diagnostyczne wg klasyfikacji ICD-10 lub na DSM-IV ( klasyfikacja zaburzeń psychicznych Amerykańskiego Towarzystwa Psychiatrycznego ). Zanim jednak dziecko trafi do specjalisty, to rodzice muszą zauważyć sygnały świadczące o tym, że ich pociecha rozwija się inaczej niż jej rówieśnicy.</p>
                        <p>Powodami do niepokoju powinny stać się objawy takie jak:</p>
                        <ul>
                            <li>brak reakcji dopasowywania swego ciała do osoby, która przytula, bierze na ręce,</li>
                            <li>nie nawiązywanie kontaktu wzrokowego,</li>
                            <li>brak więzi emocjonalnej z rodzicami, nie chwalenie się własnymi wytworami lub interesującymi przedmiotami,</li>
                            <li>brak szukania pocieszenia u swoich rodziców,</li>
                            <li>zubożona ekspresja twarzy,</li>
                            <li>brak zainteresowania prostymi zabawami opartymi na interakcjach społecznych (np. zabawa w „a kuku”),</li>
                            <li>brak zdolności naśladowczych, dziecko nie jest zainteresowane czynnościami, które wykonują inni i nie naśladuje ich,</li>
                            <li>silnie przywiązanie do przedmiotów martwych, takich jak kamienie, małe zabawki, pudełka oraz wykazywanie dużego zaniepokojenia w przypadku zabrania im tego przedmiotu,</li>
                            <li>niezdolność do zabawy z rówieśnikami,</li>
                            <li>brak samodzielności w zakresie wykonywania prostych czynności samoobsługi,</li>
                            <li>niewłaściwe wykorzystywanie przedmiotów, schematyczne i powtarzające się czynności związane z przedmiotami np. układanie klocków według kształtów, burzenie i ponowne układanie, wprowadzanie przedmiotów w ruch wirowy,</li>
                            <li>powtarzające się stereotypowe czynności takie jak: machanie rączkami, kręcenie się w kółko, chodzenie na palcach, wpatrywanie się we własne paluszki,</li>
                            <li>nadmiar takich cech, jak agresja, autoagresja, stymulacje, autostymulacje, napady wściekłości, labilność nastrojów, zachowania nieadekwatne do sytuacji;</li>
                            <li>brak strachu jako odpowiedź na realne niebezpieczeństwo lub nadmierna bojaźliwość wynikająca z kontaktu z niegroźnymi obiektami;</li>
                            <li>brak reakcji na własne imię, przy prawidłowej reakcji – na przykład – na szelest papierka od czekolady;</li>
                            <li>wymaganie niezmienności otoczenia, protest przy próbie – na przykład – przestawienia mebli, zmianie trasy spaceru;</li>
                            <li>ograniczony wachlarz pokarmów, sprzeciw przy próbie wprowadzania nowych pokarmów;</li>
                            <li>brak rozwoju mowy, przy jednoczesnym nie występowaniu innych form komunikacji, na przykład za pomocą gestów lub opóźniony jej rozwój;</li>
                            <li>utrata umiejętności mowy pojawiająca się najczęściej pomiędzy 18 a 30 miesiącem życia;</li>
                            <li>występowanie echolalii (powtarzanie słów lub fraz usłyszanych wcześniej);</li>
                            <li>odwracanie zaimków;</li>
                            <li>niezwykłe reagowanie na bodźce sensoryczne (np. brak reakcji na własne imię lub nagłe hałasy, a zatykanie uszu, krzyk na dźwięk dartej gazety, odgłosu włączonej pralki, obsesja podążania wzorem za ułożonymi wzorami z płytek podłogowych, dostrzeganie interesującego przedmiotu z odległości wielu metrów, wpatrywanie się uważnie w wiatrak wentylatora, okno, spłukiwaną toaletę; nadwrażliwość na dotyk  itp.)</li>
                        </ul>
                        <p>Gdzie szukać pomocy?</p>
                        <p>Do najbardziej znanych poradni diagnozujących autyzm w  naszej okolicy zalicza się:</p>
                        <div class="note" style="width: 60%; margin: 0 auto; text-align: center; padding: 10px;">
                            Szczecińskie Stowarzyszenie Pomocy Autystom<br />
                            ul. Lutyków 24<br />
                            70-876 Szczecin<br /><br />
                            tel./fax 91 46 13 205<br />
                            kom. 502 337 808<br />
                            <a href="mailto:osrodek@autyzmrazem.pl">email: osrodek@autyzmrazem.pl</a><br />
                            <a href="http://www.autyzmrazem.pl">www.autyzmrazem.pl</a><br /><br />

                            <p>Brak możliwości wizyt na NFZ</p>
                            <p>Wizyta prywatna: Koszt całej diagnozy wynosi 240 zł. Najczęściej do jej postawienia potrzebne są od 1 do 2 wizyty trwających ok 1 godzinę i 20 minut. Eksperci opracowują również indywidualny plant terapii oraz prowadzą różnego rodzaju zajęcia. 1 godzina zajęć kosztuje 60 złotych, 45 minut zajęć - 50 złotych. Na wizytę dzieci umawiane są na bieżąco.</p>
                        </div>
                        <br />
                        <div class="note" style="width: 60%; margin: 0 auto; text-align: center; padding: 10px;">
                            NZOZ Poradnia dla Osób z Autyzmem, Ośrodek Rehabilitacji Dziennej, Specjalny Ośrodek Szkolno-Terapeutyczny dla Dzieci i Młodzieży z Autyzmem<br />
                            ul. Chopina 42<br />
                            80-268 Gdańsk<br /><br />
                            tel. 058 520-38-30<br />
                            faks 058 520-38-31<br />
                            <a href="mailto:poradniaaut@wp.pl">email: poradniaaut@wp.pl</a><br />
                            kontakt: dr Elżbieta Mazur<br /><br />

                            <p>Wizyta na NFZ: bez skierowania lekarza rodzinnego, należy okazać ubezpieczenie dziecka. Czas oczekiwania ok. 2 miesiące. Poradnia zajmuje się diagnozą, nie opracowuje indywidualnych planów terapii. Odbywają się najczęściej cztery wizyty (czasami jest ich mniej, a czasami więcej – w zależności od potrzeb) i obejmują spotkania z lekarzem i psychologiem. Czas jednej wizyty to około 2 godziny.</p>
                            <p>Brak możliwości wizyt prywatnych.</p>
                        </div>
                        <br />
                        <p>Drodzy Rodzice!</p>
                        <p>Jeśli zauważyliście, że Wasze dziecko nie rozwija się prawidłowo, jeśli macie wątpliwości dotyczące jego rozwoju umysłowego czy rozwoju mowy lub jeśli  lekarz stwierdził nieprawidłowy rozwój, wady wrodzone lub inne upośledzenia, skontaktujcie się z <strong>Poradnią Psychologiczno-Pedagogiczną w Białogardzie</strong> ul. Dworcowa 2, tel: 0-94 312-25-96. W poradni istnieje możliwość uzyskania porady, przeprowadzenia specjalistycznych badań diagnostycznych oraz objęcia dzieci terapią  psychologiczną,pedagogiczną i logopedyczną. Szczegółowe informacje  można uzyskać poprzez osobisty lub telefoniczny kontakt z sekretariatem poradni.</p><hr />
                """
            ],
            "article008.html": [
                u"Zanim dziecko zacznie naukę w szkole, czyli jak przygotowywać dziecko do nauki czytania i pisania?",
                u"""<p class="author">autor: Anna Politowska-Kowal - pedagog</p>
                    <img class="img-responsive imgCenter" src="../img/article08.jpg" />
                    <p>Czytanie i pisanie są zaliczane do podstawowych umiejętności człowieka. Są to skomplikowane i złożone procesy, w które zaangażowane są funkcje wzrokowe, słuchowe, ruchowe i
                    wzajemna ich współpraca. Aby dziecko mogło nauczyć się czytać i pisać musi być do tego przygotowane przez rodziców i nauczycieli przedszkola. Właśnie rodzice są pierwszymi i
                    najważniejszymi nauczycielami swoich dzieci. <strong>Dlatego też Rodzicu, zanim Twoje dziecko rozpocznie edukację szkolną warto zadbać o to aby:</strong></p>
                    <ul>
                        <li>już od najmłodszych lat miało zapewniony kontakt z książką dostosowaną do jego wieku; natomiast rodzic czytając dziecku książeczki może pokazywać ilustracje,
                        zachęcać do mówienia na temat tego, co widzi na obrazkach, wyjaśniać znaczenie nieznanych słów,</li>
                        <li>rozwijać sprawność ruchową dziecka poprzez ćwiczenia  utrzymywania równowagi, stania i skakania na jednej nodze, chodzenia po narysowanej linii,
                        powtarzania sekwencji ruchowych, maszerowania w rytm muzyki, jazdy na rowerze oraz zabawy ruchowe na świeżym powietrzu, </li>
                        <li>doskonalić funkcje wzrokowe dziecka poprzez dobieranie jednakowych obrazków, układanie zabawek według koloru, kształtu itp., układanie puzzli,
                        uzupełnianie brakujących elementów na obrazkach, zagadki i łamigłówki obrazkowe np. labirynty, domina obrazkowe, budowanie konstrukcji z  klocki, gry typu „memory”,</li>
                        <li>rozwijać funkcje słuchowe poprzez wysłuchiwanie odgłosów w domu np. mikser, kapanie wody z kranu i  na spacerze np. warczenie silnika samochodu, szum drzew, śpiew ptaków,
                        naśladowanie zwierząt, układanie rymów, nauka prostych wierszyków, piosenek, wymyślanie historyjek, zapamiętywanie i powtarzanie zdań; ciągów cyfr i wyrazów, liczenie wyrazów
                        w zdaniu, dzielenie słów na sylaby, wyszukiwanie słów zaczynających się lub kończących na  daną głoskę, ćwiczenia głoskowania krótkich słów,</li>
                        <li>rozwijać sprawność manualną i grafomotoryczną (pamiętając o tym, że zabawy usprawniające zaczynamy  od najprostszych ćwiczeń) poprzez rysowanie patykiem
                        na piasku, rysowanie na tackach z piaskiem czy kaszą,  mazanie zmoczonym palcem w farbie po papierze, odciskanie zamalowanej farbą dłoni, malowanie farbami grubym
                        pędzlem, wycinanie, wyklejanie, wydzieranie, rysowanie wg. szablonu (przy takich zajęciach dziecko rozluźnia mięśnie ręki i ma wrażenie, że się bawi, a nie rysuje),</li>
                        <li>od początku ćwiczeń grafomotorycznych należy starać się wyrabiać u dziecka kierunek pisania od lewej do prawej strony, wskazując mu drogę rysowania szlaczków, kreślenia linii pionowych
                        (z góry w dół) i poziomych (z lewej do prawej), rysowania po śladzie, kończenia szlaczków, odwzorowywania rysunków zgodnie ze wzorem; należy zwrócić uwagę, aby dziecko posługiwało się
                        przy rysowaniu i innych czynnościach zawsze tą samą ręką oraz należy kształtować prawidłowy chwyt  kredki czy ołówka (narzędzie pisarskie trzymane jest przez trzy palce: kciuk, palec
                        wskazujący, palec środkowy).</li>
                    </ul>
                    <p>Najkorzystniej dla dziecka zaczynającego naukę w klasie pierwszej szkoły podstawowej jest być gotowym do nauki czytania i pisania, bo w dużej mierze decydować to będzie o jego powodzeniu w
                    edukacji. Aby się dowiedzieć czy dziecko jest gotowe do rozpoczęcia tej nauki warto się zgłosić do Poradni Psychologiczno- Pedagogicznej w Białogardzie, gdzie zostanie przeprowadzone badanie
                    w tym kierunku. Jak wiemy z naszych doświadczeń niektóre dzieci mają z tym problem.</p>
                    <hr />

                """
            ],
            "article009.html": [
                u"Wczesne wspomaganie rozwoju dziecka – czym jest i dla kogo?",
                u"""<p class="author">autor: Alicja Gudańska-Walkowska - psycholog</p>
                <img class="img-responsive imgCenter" src="../img/article09.jpg" />
                <p>W trosce o pomoc i pełniejszy rozwój dzieci z różnego rodzaju niepełnosprawnością Ministerstwo Edukacji Narodowej i Sportu w 2005 r. wydało rozporządzenie w sprawie organizowania
                wczesnego wspomagania rozwoju dzieci. Rozporządzenie to zapewnia dzieciom niepełnosprawnym bezpłatną, kompleksową i profesjonalną pomoc.</p>
                <p>WWRD organizowane jest dla dzieci niepełnosprawnych, posiadających  opinię o potrzebie wczesnego  wspomagania,  wydaną  przez poradnię  psychologiczno-pedagogiczną.
                Wczesne wspomaganie może być organizowane w przedszkolach i w szkołach podstawowych, w tym również w szkołach i przedszkolach specjalnych, a także
                w specjalnych ośrodkach szkolno-wychowawczych oraz publicznych i niepublicznych poradniach psychologiczno-pedagogicznych.</p>
                <p>Wczesne wspomaganie rozwoju dziecka dzięki interdyscyplinarnemu podejściu umożliwia objęcie pomocą zarówno dziecka jak i jego rodziny. Intensywne
                i wielokierunkowe działania mają na celu stymulowanie  rozwoju psychoruchowego, społecznego i  emocjonalnego dziecka od  chwili  wykrycia niepełnosprawności  do podjęcia  przez nie nauki w szkole.
                Zajęcia te prowadzą, zależnie od potrzeb dziecka, m.in.: logopeda, psycholog, pedagog. Wymiar godzin przysługujących jednemu dziecku jest określony przepisami i wynosi łącznie od 4 do 8 godzin
                w miesiącu. Rozpatrując to w kontekście potrzeb np. dziecka z autyzmem to niewiele, gdyż najlepsze efekty u tych dzieci uzyskuje się pracując z nimi 40 godzin w tygodniu.</p>
                <p>Od 2008r. na terenie Poradni Psychologiczno-Pedagogicznej w Białogardzie prowadzone jest Wczesne Wspomaganie Rozwoju Dziecka. Do tej pory tą formą pomocy objętych było około 30 dzieci.</p>
                <p>Dzieci posiadające opinię o potrzebie wczesnego wspomagania uczestniczą zarówno w zajęciach indywidualnych ze specjalistami jak i w grupowych – w których uczestniczą również ich rodzice. Dodatkowo od 2010 roku na terenie poradni organizowane są spotkania dla rodziców dzieci o zaburzonym rozwoju, których celem jest: kształtowanie właściwych postaw i zachowań rodziny względem niepełnosprawnego dziecka, wzmacnianie więzi emocjonalnych w rodzinie oraz udzielanie instruktażu w zakresie właściwego postępowania
                z dzieckiem.</p>
                <p>Pomimo ograniczonego czasu u dzieci objętych zajęciami zauważa się postępy. U niektórych maluchów, dzięki stymulacji, rozwój psychoruchowy obecnie nie odbiega od normy wiekowej, inne dzieci
                zdecydowanie lepiej funkcjonują np. są mniej agresywne, nauczyły się nawiązywać kontakt z otoczeniem. Niektórzy z naszych podopiecznych obecnie uczęszczają już do szkoły.</p>
                <p>Zajęcia WWRD odbywają się w specjalnie do tego przygotowanej sali. Maluchy bardzo lubią zabawy z chustą czy na materacach, dużym zainteresowaniem cieszy się specjalny tunel. Dyrekcja Poradni stara się by doposażyć tą salę jednakże brak funduszy to ogranicza.
                Z tego też względu szukamy sponsorów chętnych wesprzeć nas w tych działaniach.</p>

                <div class="note" style="width: 60%; margin: 0 auto; text-align: center; padding: 10px; margin-bottom: 10px;">
                  Nr konta: 72 1240 3666 1111 0000 4344 7880 <br />z dopiskiem: na wyposażenie sali wwrd.
                </div>

                <p><strong>I na zakończenie prośba / apel do rodziców:</strong></p>
                <p>Jeśli macie jakiekolwiek wątpliwości czy rozwój Waszego dziecka przebiega prawidłowo skontaktujcie się z najbliższą poradnią psychologiczno-pedagogiczną. Tam uzyskacie poradę, diagnozę, a także –
                jeśli będzie zachodziła taka potrzeba – opinię o potrzebie wczesnego wspomagania rozwoju.</p>
                <hr />
                """
            ],
            "article010.html": [
                u"System Żetonowy",
                u"""<p class="author">autor: Alicja Gudańska-Walkowska - psycholog</p>
                <img class="img-responsive imgCenter" src="../img/article10.jpg" />
                <p>Wszyscy – zarówno dzieci jak i dorośli jesteśmy bardzo podatni na nagrody – to one informują nas czego oczekuje od nas otoczenie. Dzieci nagradzane za jakieś zachowanie zachowują się w ten sposób częściej, dorośli otrzymujący premię w pracy –
                wiedzą co muszą robić by znów ją otrzymać.</p>
                <p>Chcąc wpłynąć na zmianę zachowania u danej osoby stosujemy szereg tzw. wzmocnień. Wzmocnieniem jest każda nasza reakcja, która zwiększa siłę zachowania
                i prawdopodobieństwo ponownego wystąpienia tego zachowania u określonej osoby.
                Istnieje szereg rodzajów wzmocnień – wzmocnienia rzeczowe (np. lizak, zabawka itp.), społeczne (np. pochwała, zwrócenie uwagi itp.), dotyczące przywilejów, aktywności (np. zwolnienie z czegoś,
                przyzwolenie na coś), oraz wzmocnienia symboliczne – żetonowe, na których skupimy się w tym artykule.</p>
                <p>Jest kilka podstawowych zasad, które należy przestrzegać by zastosowane wzmocnienia odnosiły prawidłowy skutek. Po pierwsze: niezbędne jest określenie skutecznego wzmocnienia ponieważ, nigdy nie da się stwierdzić, że jakieś wydarzenie jest wzmocnieniem,
                dopóki się go nie wypróbuje i nie zobaczy jego efektów. Po drugie to co jest wzmocnieniem dla jednej osoby dla drugiej nie musi nim być. Po trzecie – aby wzmocnienie było skuteczne, musi następować natychmiast po zachowaniu, które jest wzmacniane.</p>
                <p>Wzmocnienia symboliczne - żetonowe są jednym z zastępczych rodzajów wzmocnień. Wzmocnienia symboliczne, są to konkretne przedmioty (buźki, plusy, magnesy, guziki itp.), które można wymienić na określone wcześniej wzmocnienia rzeczowe lub związane
                z przywilejami.</p>
                <p>Lecz jak prawidłowo stosować "system żetonowy?"</p>
                <p>Po pierwsze należy określić jakie zachowanie docelowe chcemy uzyskać.  Wybieramy zachowanie, które aktualnie sprawia naszemu dziecku trudność np. nasze dziecko nie chce myć zębów, więc zachowaniem które będziemy nagradzać będzie mycie zębów.
                W drugim kroku wybieramy „żetony”, które dziecko będzie zbierać, np. stempelki, guziki itp. – ważne by było to coś czego nie da się podrobić i by było łatwo dostępne).</p>
                <p>Następnie określamy „nagrodę” – przedmiot, przywilej, na który będziemy wymieniać nasze żetony – musi być to coś atrakcyjnego dla dziecka, coś na czym mu bardzo zależy (coś co jest sprawdzonym wzmocnieniem i będzie dostępne tylko jako nagroda za
                zdobycie żetonów – choć nie musi to być wcale coś wielkiego czy drogiego).</p>
                <p>Ostatnim krokiem jest zaplanowanie systemu wymiany – czyli określenie ile żetonów dziecko musi zdobyć by uzyskać nagrodę, jak długo będzie je zbierać, kiedy nastąpi wymiana. Wszystkie te kwestie trzeba jasno określić i poinformować o tym dziecko.
                Gdy dziecko jest starsze samo może nam podpowiedzieć na jakiej nagrodzie by mu zależało – co wzmocni jego motywację do zmiany zachowania.</p>
                <p>Żeby „gospodarka żetonowa” przyniosła nam pozytywne efekty należy pamiętać, by nagradzać żetonem pożądane zachowanie natychmiast po jego wystąpieniu. Ponadto nagroda powinna być dostępna tylko poprzez żetony a wymagania tak dostosowane by każdy mógł
                zyskać żeton. Ważna jest też okresowa zmiana menu „nagród” oraz zmiana ilości żetonów potrzebnych by zyskać nagrodę. Początkowo dziecko otrzymuje „nagrodę” za mniejszą ilość żetonów – częściej nagradzamy, z czasem jak dane zachowanie występuje częściej
                określamy większą ilość potrzebnych żetonów by uzyskać „nagrodę” (o każdej zmianie informujemy dziecko). A gdy wzmacniane przez nas zachowanie staje się częścią zachowania naszego dziecka wycofujemy się z nagradzania „żetonami” ale nadal nagradzamy np.
                poprzez pochwałę słowną.</p>
                <p>System żetonowy sprawdza się tylko i wyłącznie wtedy, gdy jesteśmy bardzo konsekwentni. Proces zmiany zachowania nie zachodzi od razu, jak sama nazwa wskazuje jest to proces, i u każdej osoby przebiegać on może w różnym tempie. Najważniejsze to nie
                poddawać się i konsekwentnie dążyć do założonego celu. Niekiedy w trakcie może okazać się iż wybrane przez nas wzmocnienie wcale nie spełnia swojej funkcji – np. nasze dziecko zmieniło upodobanie (chciało iść do kina ale teraz chce iść na kulki) jeżeli
                jest to wymiana równo wartościowa możemy się na nią zgodzić.</p>
                <p>I na zakończenie trzeba podkreślić, iż w systemie żetonowym nie ma punktów ujemnych, smutnych buziek itp. Nagradzamy każde poprawne zachowanie, jeśli ono nie występuje dziecko nie dostaje żadnego żetonu. Ponadto nie wolno odbierać punktów, które do tej
                pory dziecko otrzymało – w końcu zasłużyło sobie na nie, a o wszelkich zmianach zasad muszą zostać poinformowane dwie strony.</p>
                <hr />

                """
            ],
            "article011.html": [
                u"Przykłady ćwiczeń i zabaw dla dzieci w wieku przedszkolnym",
                u"""<p class="author">autorki: Anna Politowska-Kowal – pedagog i Ewa Cieszko-Kowalska – psycholog</p>
                <img class="img-responsive imgCenter" src="../img/article011.png" />
                <h2>I. Zabawy pogłębiające więzi rodzica z dzieckiem</h2>
                <ul>
                    <li>masażyki z wykorzystaniem wierszyków np. "Płynęła sobie rzeczka...",</li>
                    <li>przytulanie,  gilgotanie, kołysanie,</li>
                    <li>"koguciki"- kucnijcie naprzeciw siebie, wyciągnijcie przed siebie obie dłonie i podskakując starajcie się odepchnąć,</li>
                    <li>pizza - na plecach dziecka "ugnieść ciasto, nakłuj je widelcem, posmaruj oliwą, posyp serem, upiecz, a na końcu schrup z zachwytem",</li>
                    <li>winda- stojąc podnieś dziecko na ręce, przytul, a następnie delikatnie spuść na dół- dziecko zjeżdża po ciele rodzica,</li>
                    <li>raczkowanie - pochodźcie na czworakach, chwytajcie się za stopy, przepychajcie, przechodźcie pod lub nad sobą.</li>
                </ul>
                <p>zabawy z kocykiem:</p>
                <ul>
                    <li>naleśnik - zwiń dziecko w kocyk, delikatnie turlaj je po podłodze;</li>
                    <li>kółka, zygzaki- poproś, by dziecko położyło się na kocyku. Chwyć za koc i ciągnij delikatnie po podłodze; wykonuj zygzaki, koła itp.;</li>
                    <li>hamak - chwyćcie koc za rogi i delikatnie bujajcie dziecko.</li>
                </ul>

                <h2>II. Zabawy grafomotoryczne</h2>
                <p>Usprawnianie grafomotoryczne zaczynamy od najprostszych ćwiczeń:</p>
                <ul>
                    <li>rysowanie patykiem na piasku,</li>
                    <li>mazanie zmoczonym palcem w farbie po papierze,</li>
                    <li>odciskanie zamalowanej farbą dłoni, stóp,</li>
                    <li>obrysowywanie dłoni i stóp,</li>
                    <li>"malowanki- niespodzianki" pod nieobecność dziecka rysuje się coś świecą, dziecko pokrywa farbą kartkę,</li>
                    <li>wycinanki, wyklejanki, wydzieranki,</li>
                    <li>rysowanie wg. szablonu.</li>
                </ul>
                <p>Przy takich zajęciach dziecko rozluźnia mięśnie i ma wrażenie, że się bawi, a nie rysuje.</p>

                <p><strong>Ćwiczenia kształtujące nawyki ruchowe związane z kierunkiem pisania</strong> - od początku wyrabiamy u dziecka kierunek pisania od lewej do prawej strony, wskazujemy mu drogę:</p>
                <ul>
                    <li>rysowanie szlaczków rozpoczynamy od lewej strony,</li>
                    <li>kreślenie linii pionowych (z góry w dół) i poziomych (z lewej do prawej),</li>
                    <li>ćwiczenia w rysowaniu okręgów i spirali w obu kierunkach,</li>
                    <li>zamalowywanie obrazków, kalkowanie, łączenie kropek, rysowanie po śladzie, kończenie szlaczków, odwzorowywanie rysunków zgodnie ze wzorem, rysowanie na tackach z piaskiem czy kaszą.</li>
                </ul>

                <h2>III. Zabawy usprawniające funkcje wzrokowe</h2>
                <ul>
                    <li>dobieranie jednakowych obrazków, układanie zabawek według koloru, kształtu itp.,</li>
                    <li>układanie puzzli,</li>
                    <li>uzupełnianie brakujących elementów na obrazkach,</li>
                    <li>zagadki i łamigłówki obrazkowe np. labirynty, domina obrazkowe, literowe, układanki, klocki,</li>
                    <li>zapamiętywanie jak największej ilości elementów na obrazku, przedmiotów w pokoju,</li>
                    <li>gra "memory",</li>
                    <li>dla starszych przedszkolaków: wyszukiwanie takich samych liter.</li>
                </ul>


                <h2>IV. Zabawy usprawniające funkcje słuchowe</h2>
                <ul>
                    <li>wysłuchiwanie odgłosów w domu np. pralka, mikser, kapanie wody z kranu,</li>
                    <li>wysłuchiwanie odgłosów na spacerze np. warczenie silnika samochodu, szum drzew, śpiew ptaków,</li>
                    <li>słuchanie, naśladowanie  zwierząt i jednoczesne odnajdywanie na obrazku,</li>
                    <li>szukanie rymów i ich wystukiwanie / klaskanie,</li>
                    <li>nauka prostych wierszyków, piosenek,</li>
                    <li>wymyślanie historyjek np. z wykorzystaniem instrumentów muzycznych.</li>
                    <li>zapamiętywanie i powtarzanie zdań; ciągów cyfr i wyrazów,</li>
                    <li>dla starszych przedszkolaków: podział zdań na wyrazy, liczenie wyrazów, wyodrębnianie sylab w słowach, wyszukiwanie wyrazów zaczynających się lub kończących na daną głoskę.</li>
                </ul>

                <h2>V. Zabawy wzbogacające słownictwo i myślenie</h2>
                <ul>
                    <li>opowiadanie historyjek na podstawie obrazków,</li>
                    <li>opis obrazków,</li>
                    <li>kończenie zdań,</li>
                    <li>wymienianie nazw kolorów, zwierząt, kwiatów, pór roku itp.;</li>
                    <li>zachęcanie dziecka do wypowiadania się na temat codziennych wydarzeń;</li>
                    <li>wprowadzanie nowych pojęć z otaczającego świata,</li>
                    <li>wyciąganie wniosków na podstawie obrazków, bajek; zastanawianie się „co by było, gdyby…”,</li>
                    <li>rozwijanie umiejętności matematycznych typu: liczenie, przeliczanie, porównywanie liczebności zbiorów z wykorzystaniem praktycznych sytuacji dnia codziennego np. porównywanie zawartości dwóch pudełek, przeliczanie patyczków, rozróżnianie prawej/lewej strony,</li>
                    <li>dla starszych przedszkolaków: znajdowanie podobieństw między pojęciami np. pies i lew mają 4 łapy, ogon, sierść i są zwierzętami.</li>
                </ul>

                <h2>Polecana literatura</h2>
                <ul>
                    <li>M. Bogdanowicz <span style="font-style: italic">"W co się bawić z dziećmi"</span> książka + płyta CD</li>
                    <li>M. Bogdanowicz <span style="font-style: italic">"Przytulanki, czyli wierszyki na dziecięce masażyki"</span> książka + płyta CD</li>
                    <li>M. Bogdanowicz <span style="font-style: italic">"Metoda Dobrego Startu", "Od wierszyka do rysunku"</span>  dla dzieci 3-4 letnich oraz dla 5-letnich</li>
                    <li>C. Rose, G. Dryden, Seria książeczek  <span style="font-style: italic">"Zabawy fundamentalne 1"</span> (0-2 lat) i <span style="font-style: italic">"Zabawy fundamentalne 2"</span> (2-6 lat) np. "KOCHAM, LUBIĘ, SZANUJĘ"</li>
                    <li>M. Molicka <span style="font-style: italic">"Bajki terapeutyczne"</span></li>
                    <li>E. Lenka, <span style="font-style: italic">"Teczka 3-4-5 latka"</span> książka z wierszykami + karty pracy, wyd. Olesiejuk</li>
                    <li>J. Silberg <span style="font-style: italic">"Zabawy umysłowe dla dzieci, 125 gier i zabaw dla dzieci od roku do trzech lat"</span></li>
                </ul>

                <div class="note"><p><strong>Co jest na łące?</strong></p>
                <p>CO BĘDZIE POTRZEBNE: zielony i biały papier, różnokolorowa włóczka lub nitka, wata, nożyczki, klej biurowy; gałązki, liście, kwiaty zebrane na spacerze; obrazki lub zdjęcia owadów, kwiatów, zwierząt,
                które można spotkać na  łące (można je powycinać ze starych czasopism, zdjęć, gazet).</p>
                <p>Arkusz białego papieru posłuży jako tło, z zielonego wytnij pasek, który po przyklejeniu na biały arkusz stanie się „podstawą”  łąki. Ponacinaj pasek jednej strony – tworzyć  będzie
                wówczas wrażenie trawy na  łące. Do tak przygotowanej  łąki przyklejać możecie kolejne elementy (powycinane owady i zwierzęta, prawdziwe kawałki roślin). Części papierowe wystarczy przymocować
                klejem biurowym, natomiast zebrane podczas spaceru gałązki, kwiatki, liście – taśmą klejącą albo plasteliną. Zachęcaj dziecko do korzystania z wielu materiałów, np. z kawałka waty zróbcie chmury,
                a z żółtej włóczki słońce. Niektóre części łąki można też narysować.</p>
                <p>Wykorzystując tę metodę możecie się pobawić w budowanie miasta, poznawanie morskiego życia, a wycinając z gazet części ubrań – stworzyć  własną, tematyczną(na plaży, na nartach) rewię mody.</p>

                <p>KORZYŚCI Z ZABAWY: jest to dla dziecka ciekawy sposób łączenia różnych plastycznych czynności; w przyjemny sposób przekazujemy dziecku wiedzę na temat jego
                otoczenia; w zależności od tematu obrazka dziecko wzbogaca swój słownik.</p></div>

                <div class="note"><p><strong>Koloro–węcho–smaki</strong></p>
                <p>CO BĘDZIE POTRZEBNE: nieprzezroczyste kubeczki, różne produkty spożywcze (cytryna, cukier, jabłko, kawałek chleba, truskawki, maliny, buraki, brukselka itp.)</p>
                <p>Kilka (2, 3) wybranych produktów połóż na stole przed dzieckiem, tak,  żeby je widziało. Następnie przykryj je kubeczkami. Grając w tę grę po raz  pierwszy możesz mówić po kolei, jaki produkt
                przykrywasz. Następnie spytaj go, pod którym kubeczkiem ukryta jest np. cytryna? Gdy maluch wybierze kubeczek sprawdźcie, czy prawidłowo odgadł. W miarę jak będzie nabierał wprawy, dodaj czwarty kubeczek
                i sprawdź, czy tym razem też zapamięta lokalizację produktów. Ciekawość dziecka jest na tyle duża, że z chęcią  będzie sprawdzać jak smakuje i pachnie ukryty produkt. Jest to dobra okazja do nauki rozpoznawania
                kolorów, smaków, zapachów. Zamieńcie się rolami, pozwól dziecku pozakrywać przedmioty i zgadnij, gdzie co jest! Bardziej zaawansowaną wersją tej zabawy jest gra w odnajdywanie par. Przygotuj po dwa,
                takie same produkty i zakryj kubeczkami. Odkryjcie jeden dowolny kubeczek. Zadaniem dziecka jest odnalezienie pasującego produktu.</p>

                <p>KORZYŚCI Z ZABAWY: wiczy pamięć, koncentrację oraz rozwija samokontrolę u dziecka; zachęca do używania różnych zmysłów; może być urozmaiceniem posiłku.</p></div>

                <div class="note"><p><strong>Czarodziejski koc</strong></p>
                <p>CO BĘDZIE POTRZEBNE: kocyk</p>
                <p>Przy pomocy kocyka można bawić się z dzieckiem na wiele sposobów. Jednym z nich jest zabawa w detektywa. Ukryj pod kocem jeden z przedmiotów, które zna dziecko. Zadaniem małego detektywa jest
                odgadnięcie, na podstawie samego kształtu, co koc przykrywa. Zamieńcie się rolami. Teraz Ty spróbuj odgadnąć, co maluch ukrył pod kocem. Gdy sam się ukryje, możesz "odgadywać", jakie części jego
                ciała wyczuwasz. Oprócz miłego masażu, ogromną frajdę dziecku będzie sprawiać fakt, że tak mocno się  głowisz nad odgadnięciem. Pamiętaj, żeby kocyk był na tyle cienki, by delikatne rączki dziecka
                mogły wyczuć kształt pod nim ukryty.</p>
                <p>Większość dzieci lubi też bawić się w "naleśnik". Cała zabawa polega na byciu zawijanym i odwijanym przez opiekuna. Lubią się też zawijać przytulone do bliskiej
                osoby. Zwróć uwagę, aby głowa dziecka nie była zakryta i mógł obserwować, co się z nim dzieje. W miarę możliwości starajcie się utrzymywać kontakt wzrokowy.</p>
                <p>Kocyk można też wykorzystać jako domową wersję samochodu. Ciągnąc koc z pasażerem – lalką po podłodze możecie przemierzać wymyślone ulice w Waszym domu. Prawdopodobnie maluch też będzie
                chciał być wożony. Jego mięśnie nie są tak stabilne jak osoby dorosłej, więc może mieć trudności z utrzymaniem się na kocu. Powolutku ruszaj Wasz pojazd, żeby maluch nie przewrócił się do tyłu.</p>

                <p>WSKAZÓWKA: przy tej okazji możesz pokazać dziecku zasadę czerwonego i zielonego światła. Jako światła mogą posłużyć kartki w odpowiednim kolorze.</p>
                <p>KORZYŚCI Z ZABAWY: możliwość aktywnego spędzania czasu, wpajanie pierwszych zasad ruchu drogowego, pogłębianie kontaktu z dzieckiem.</p></div><hr />
                """
            ],
            "article012.html": [
                u"Kiedy nic się nie chce...",
                u"""<p class="author">autorki: Maria Jonko - pedagog-neurologopeda i Ewa Cieszko-Kowalska – psycholog</p>
                <img class="img-responsive imgCenter" src="../img/article12.jpg" />

                            <hr />

                            <p class="indent">Depresja często jest pomijana w kontekście dzieci i nastolatków, a niestety coraz częściej spotykamy się z tym problemem. Każde dziecko jest oczywiście czasami smutne, nic mu się nie chce, choć przedszkolaki wydają się niemal ciągle szczęśliwe. Zdarza się jednak, że nawet one, podobnie jak dorośli, doświadczają depresji.</p>
                            <p>Według Międzynarodowej Klasyfikacji Chorób ICD-10 depresja umieszczona jest jako zaburzenia  nastroju (afektywne), w ramach których wyróżnia się m.in.:</p>
                            <ul>
                                <li><strong>F31:</strong> Zaburzenia afektywne dwubiegunowe charakteryzujące się występowaniem dwóch lub więcej epizodów chorobowych z wyraźnie zaburzonym nastrojem i aktywnością w postaci podwyższenia nastroju, wzmożonej energii i aktywności (hipomania lub mania) lub obniżenia nastroju oraz energii i aktywności (depresja).</li>
                                <li><strong>F32:</strong> Epizod depresyjny - pacjent cierpi z powodu obniżenia nastroju, ubytku energii, zmniejszenia aktywności. Zmniejszone jest odczuwanie przyjemności, zakres zainteresowań i koncentracja są obniżone, często pojawia się znaczne zmęczenie, nawet po małym wysiłku. Sen jest zwykle zaburzony, apetyt obniżony. Samoocena i pewność siebie są niemal zawsze zmniejszone. Obniżenie nastroju nie ulega większym zmianom w kolejnych dniach, jest niezależne od bieżących wydarzeń, mogą mu towarzyszyć tzw. objawy somatyczne: utrata zainteresowania przyjemnością i obniżenie zdolności do jej przeżywania, wczesne budzenie się (kilka godzin wcześniej niż zwykle), narastanie depresji w godzinach porannych, wyraźne zahamowanie psychoruchowe, pobudzenie ruchowe, utrata apetytu, ubytek masy ciała.</li>
                                <li><strong>F33:</strong> Zaburzenia depresyjne nawracające.</li>
                            </ul>

                            <p>Objawy, które powinny nas zaniepokoić, dotyczą 3 głównych obszarów:</p>
                            <ul>
                                  <li>obniżonego nastroju,</li>
                                  <li>zmniejszonej aktywności psychicznej i motorycznej,</li>
                                  <li>oznak somatycznych (biologicznych).</li>
                              </ul>

                            <br>
                            <p>Można pomyśleć, że zachowanie syna czy córki wynika z temperamentu a nie ze schorzenia. Niemniej jednak, zainteresowanie rodziców powinny wzbudzić:</p>
                            <ul>
                                <li>nagła zmiana zachowania i funkcjonowania dziecka,</li>
                                <li>dominujący smutek w postawie ciała i wyrazie twarzy bądź demonstrowanie złości i wrogości wobec otoczenia,</li>
                                <li>nadmierny niepokój, lęk, czego efektem może być pobudzenie psychoruchowe (np. wiercenie się na krześle, niemożność skupienia się na jednej czynności),</li>
                                <li>wycofywanie się lub ograniczanie kontaktów towarzyskich,</li>
                                <li>poczucie znudzenia i zniechęcenia, co przekłada się na ograniczenie lub zaniechanie czynności sprawiających przyjemność czy obowiązków,</li>
                                <li>niska samoocena,</li>
                                <li>kłopoty ze snem, łaknieniem,</li>
                                <li>trudności z koncentracją uwagi i zapamiętywaniem, co prowadzi do pogorszenia wyników szkolnych,</li>
                                <li>skargi na różnorodne bóle,</li>
                                <li>działania autoagresywne np. samookaleczenia,</li>
                                <li>myśli samobójcze, fantazje o śmierci, próby samobójcze. </li>
                            </ul>

                            <p>Często depresja nieleczona u mniejszych dzieci nasila się w okresie dojrzewania. A im dłużej zwlekamy z leczeniem, tym ciężej ją potem wyleczyć. Alarmująco dużo przypadków depresji notuje się głównie w grupie gimnazjalistów i licealistów.</p>
                            <blockquote>
                                Tak opisują swój stan nastolatkowie doświadczający depresji zanim zaczęli się leczyć - <i>&quot;Mgła, szarość, ciężka kołdra, spod której nie sposób się wydobyć. Najchętniej wcale nie wstawałoby się z łóżka. Na samą myśl o szkole boli brzuch. Poranny prysznic jest wysiłkiem niczym wejście na wysoką górę. Strach&quot;.</i> I myśli: <i>&quot;Jestem do niczego, nic mi nie wychodzi, boję się, nie chcę nikogo widzieć, nic mi się nie chce&quot;</i>.
                            </blockquote>

                            <p>Naturalny etap zmian w życiu każdego nastolatka powoduje, że cienka granica między zwykłym przejściowym przygnębieniem a przedłużającym się okresem smutku połączonym z innymi objawami, jeśli nie zostaje na czas rozpoznany jako depresja, rozwija się - powodując spustoszenie w organizmie i psychice młodego człowieka. Ostatecznym, tragicznym następstwem może być także samobójstwo.</p>

                            <p>Aby ustrzec nastolatka przed tego typu konsekwencjami należy wcześnie interweniować. Ciągle jeszcze pokutuje obawa, że korzystanie z profesjonalnej pomocy psychologiczno-psychiatrycznej daje nam lub naszym dzieciom etykietkę osób nieradzących sobie, słabych, aspołecznych. Wiemy, że należy dbać o zęby, systematycznie robić badania kontrolne, a niechętnie dbamy o higienę psychiczną. Tym czasem udanie się po pomoc, to objaw dojrzałości i dbałości o siebie i swoich bliskich. Wszyscy rodzice zaniepokojeni stanem psychicznym swoich dzieci, mogą zwrócić się bez skierowania do psychiatry czy do naszej Poradni Psychologiczno-Pedagogicznej.</p>

                            <hr />
                """
            ],
            "article013.html": [
                u"Nadpobudliwość psychoruchowa u dzieci",
                u"""<p class="author">autor: Małgorzata Lis - pedagog</p>
                <img class="img-responsive imgCenter" src="../img/article13.jpg" />

                            <hr />
                            <p>Pozwólcie Państwo, że przedstawię problem dzieci nadpobudliwych psychoruchowo, które zarówno w szkole jak i w domu sprawiają dość dużo kłopotów. Są nadmiernie ruchliwe, łatwo się denerwują, gubią
                            swoje rzeczy, pracują chaotycznie, nie potrafią się skupić, nie doprowadzają wykonywanych przez siebie zadań do końca, są nieposłuszne. Mają także problemy z zasypianiem ale zdarza się też, że
                            dokuczają innym dzieciom. Na terenie szkoły sprawiają problemy, chodzą po klasie, przeszkadzają innym, robią ciągle bałagan i nie potrafią usiedzieć na miejscu. Tak dzieci z objawami nadpobudliwości
                            psychoruchowej są określane przez rodziców, nauczycieli.Nie znaczy to, że im samym jest z tym dobrze i są one za to głównie odpowiedzialne. Bardzo często borykają się z wieloma kłopotami. Mają trudności w nauce,
                            ich rówieśnicy nie chcą się z nimi bawić i czują się odizolowane. Wiele rzeczy nie udaje im się zrobić i boleśnie przeżywają swoje różne porażki. Próbują zmienić swoje zachowanie, ale im się to nie udaje.
                            Brak efektów podejmowanych wysiłków w celu zmiany zachowania dodatkowo jeszcze utrwala ich niską samoocenę i poczucie izolacji i niezrozumienia.</p>
                            <p>Dlaczego tak się dzieje? Czym jest nadpobudliwość opisana wyżej widoczna w zachowaniach i funkcjonowaniu dziecka? Definicje są różne. Jedna z nich brzmi <i>\"nadpobudliwość psychoruchowa rozumiana
                            medycznie oznacza zespół nadpobudliwości psychoruchowej, czyli zespół hiperkinetyczny będący schorzeniem mającym charakterystyczne objawy i wymagającym odpowiedniego leczenia\"</i>. Mówiąc prościej
                            nadpobudliwość to \"odmienna praca mózgu\", która uniemożliwia dziecku kontrolowanie swojego zachowania, a także kontrolowanie uwagi i ruchu. Rozumując w taki sposób można stwierdzić, że nadpobudliwość
                            jest pewną stałą cechą, która zmienia się wraz z wiekiem dziecka. Schorzenie to częściej dotyka chłopców. Nie jest też niczym nowym. Mówi się o nim już od ponad 100 lat, z tym, że zmieniały się tylko
                            nazwy. Według najnowszych badań <i>\"nadpobudliwość jest jednostką chorobową, która wymaga leczenia farmakologicznego, odpowiedniej terapii dziecka, jego rodziny, a także psychoedukacji\"</i>. A więc
                            aby pomóc swojemu dziecku należy zacząć od przeprowadzenia specjalistycznej diagnozy lekarza pediatry, neurologa, psychiatry i badań psychologiczno – pedagogicznych. Właściwa diagnoza umożliwi dobranie
                            właściwej formy pomocy i zrozumienia problemu dziecka.</p>
                            <hr />
                """
            ],
            "article014.html": [
                u"Samookaleczenia – moda czy coś więcej?",
                u"""<p class="author">autor: Marzena Jakubowska - psycholog</p>
                <img class="img-responsive imgCenter" src="../img/article14.jpg" />

                            <hr />
                            <p class="indent">Myślę, że w ostatnich latach wiele osób w sposób bezpośredni lub pośredni zetknęło się
                            z pojęciem samookaleczania się. Być może ktoś słyszał o tym w telewizji, radiu, czytał
                            w internecie. Być może opowiadała o tym znajoma z pracy, może dzielił się tym
                            zmartwieniem ktoś z rodziny, a może i my sami ze zdziwieniem i przerażeniem odkryliśmy
                            na rękach swojego dziecka dziwne zadrapania, rany lub blizny. Jedno jest pewne nikt kto
                            z tym zjawiskiem się spotkał, nie pozostaje wobec niego obojętny, a samo słowo
                            <strong>"samookaleczenia"</strong> budzi u większości osób silne emocje, takie jak niepokój, lęk, szok,
                            przerażenie. Co więc sprawia, że tak wielu nastolatków zadaje sobie ból nacinając swoje ciało
                            za pośrednictwem żyletki, ostrza temperówki lub do krwi rani skórę czubkiem cyrkla? Czy
                            chodzi tu tylko o swoistą modę, która jak plaga rozprzestrzenia się wśród młodzieży, czy też
                            korzenie tego zjawiska sięgają gdzieś głębiej?</p>

                            <p>Jako psycholog pracujący z dziećmi i młodzieżą szczególnie w ostatnich latach często słyszę
                            podobne pytania zadawane przez przerażonych rodziców.</p><blockquote>Najważniejsze w tym miejscu jest
                            wyjaśnienie, że istotą samouszkodzeń, które zalicza się do aktów autoagresji jest przerwanie
                            bólu emocjonalnego.</blockquote><p>Zadawanie sobie bólu fizycznego ma więc na celu <strong>odwrócenie lub przekierowanie
                            uwagi</strong> danej osoby z jej cierpienia psychicznego na cierpienie cielesne. W związku z tym
                            bardzo wiele dzieci, które się samookaleczają (większość, z którymi się spotkałam to
                            nastolatki, ale zdarzały się i dzieci 10-letnie) – w rozmowie podkreśla, że robią to, gdy są
                            zdenerwowane lub przeżywają  trudne sytuacje np. mają problemy w nauce, pokłócili się z
                            rodzicami, dokuczają im rówieśnicy, rozstali się z sympatią itp.  Zadając sobie ból przez ten
                            krótki moment przestają myśleć o swoich problemach i czują chwilową ulgę. Ta ulga i swoiste
                            znieczulenie psychiczne, którego doświadczają poprzez ból fizyczny, pozwala porównać
                            samookaleczanie się do <strong>"tabletki przeciwbólowej"</strong>, która jednak działa bardzo krótko i od
                            działania której szybko można się uzależnić.  Potem jednak – po chwili ulgi – najczęściej
                            przychodzi poczucie winy, wstyd i lęk (np. Co powiedzą rodzice, jeśli się o tym dowiedzą?),
                            a napięcie emocjonalne i stres jeszcze się u takiej osoby potęgują.</p>

                            <blockquote>W efekcie nastolatek nie dość, że nadal przeżywa swoje dotychczasowe zmartwienia (które
                            przez sam fakt samookaleczenia nie ulegają przecież rozwiązaniu), to jeszcze dodatkowo dźwigać
                            musi swoisty ciężar poczucia winy wynikający z ukrywanego przed bliskimi swoistego "sekretu".</blockquote>

                            <p>Rodzi się więc pytanie - Co w zachowaniu młodego człowieka sygnalizować może powyższy problem
                            i budzić niepokój bliskich? Często objawia się to: tendencją do izolowania się od najbliższych
                            zarówno w sensie psychicznym (np. poprzez niechęć do rozmowy), jak i w fizycznym np. poprzez
                            zamykanie się w swoim pokoju, w łazience (gdyż tylko w ukryciu można nadal w ten sposób "radzić
                            sobie ze stresem”), unikaniem sytuacji przebierania się przy bliskich, noszenia ubrań
                            odsłaniających ręce, nogi (by zapobiec ujawnieniu ran i blizn), wzmożoną drażliwością, huśtawkami
                            nastroju lub obniżonym nastrojem. W tym miejscu nasuwa się szereg kolejnych pytań: Czy
                            każdy nastolatek, który tego spróbuje, popadnie w swoiste uzależnienie i będzie to robić nałogowo?
                            Czy samookaleczenia mogą oznaczać symptomy depresji lub stanowić pierwszy krok do samobójstwa?
                            Czy problem ten dotyczy tylko dzieci i młodzieży, które przeżyły silne traumatyczne
                            doświadczenia lub przejawiających problemy natury psychicznej? I chyba najważniejsze
                            spośród nich: <strong>Jak pomóc nastolatkowi z takim problemem?</strong></p>

                            <p>Odpowiedzi na powyższe pytania nie uda się zawrzeć w krótkim artykule. Wszystkich dotkniętych
                            tym problemem i poszukujących pomocy – rodziców, opiekunów i młodzież zapraszamy do kontaktu
                            ze specjalistami Poradni Psychologiczno-Pedagogicznej w Białogardzie, gdzie podczas
                            konsultacji i szczegółowej diagnozy ustalimy najbardziej adekwatne do potrzeb danej osoby
                            formy pomocy i wsparcia.</p>

                            <hr />
                """
            ]
        }