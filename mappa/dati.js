/* Mappa «Dove siamo stati» · Nexus APS
   tipo: g = visita in giornata, v = viaggio di più giorni · stato: f = fatto, p = in programma
   luoghi: [nome, lat, lon, paese] */
const S='https://nexusghedi.it/';
const USCITE=[
 // 2027
 {t:'Arkè i5sensi · Dresda, Svizzera Sassone e Praga',d:'2027-03-29',tipo:'v',stato:'p',u:S+'2026/11/05/arke-i5sensi-dresda-svizzera-sassone-praga-2027/',l:[['Dresda',51.0504,13.7373,'Germania'],['Bastei, Svizzera Sassone',50.9620,14.0730,'Germania'],['Praga',50.0875,14.4213,'Repubblica Ceca']]},
 {t:'Tunisia da sentire',d:'2027-02-07',tipo:'v',stato:'p',u:S+'2026/11/05/tunisia-da-sentire-febbraio-2027/',l:[['Tunisi e Sidi Bou Said',36.8700,10.3410,'Tunisia'],['El Jem',35.2964,10.7069,'Tunisia'],['Douz, Sahara',33.4570,9.0200,'Tunisia']]},
 // 2026
 {t:'Milano: Dalí, Verdi e un aperitivo in centro',d:'2026-12-29',tipo:'g',stato:'p',u:S+'2026/11/05/milano-29-dicembre-2026/',l:[['Milano',45.4636,9.1900,'Italia']]},
 {t:'Salento: un risveglio assoluto per i cinque sensi',d:'2026-12-05',tipo:'v',stato:'p',u:S+'2026/11/05/salento-ars-nova-dicembre-2026/',l:[['Lecce',40.3529,18.1743,'Italia'],['Otranto',40.1460,18.4910,'Italia'],['Santa Maria di Leuca',39.7970,18.3580,'Italia'],['Gallipoli',40.0550,17.9920,'Italia'],['Ostuni',40.7290,17.5770,'Italia'],['Martina Franca',40.7050,17.3370,'Italia']]},
 {t:'Arkè i5sensi · Fontanellato e il re dei salumi',d:'2026-11-21',tipo:'g',stato:'p',u:S+'2026/11/05/arke-i5sensi-fontanellato/',l:[['Fontanellato',44.8810,10.1750,'Italia']]},
 {t:'Como e Cernobbio: forme, luci ed eleganza',d:'2026-11-08',tipo:'g',stato:'f',u:S+'2026/11/08/como-cernobbio-8-novembre-2026/',l:[['Como',45.8100,9.0852,'Italia'],['Cernobbio',45.8410,9.0740,'Italia']]},
 {t:'Arkè i5sensi · Acquanegra sul Chiese',d:'2026-10-17',tipo:'g',stato:'f',u:S+'2026/10/17/arke-i5sensi-acquanegra-sul-chiese/',l:[['Acquanegra sul Chiese',45.1636,10.4337,'Italia'],['Canneto sull\'Oglio',45.1510,10.3790,'Italia']]},
 {t:'Arkè i5sensi · L\'anima della Val d\'Arda',d:'2026-09-26',tipo:'g',stato:'f',u:S+'2026/09/26/arke-i5sensi-anima-della-val-darda/',l:[['Chiaravalle della Colomba',44.9310,9.8830,'Italia'],['Castell\'Arquato',44.8520,9.8710,'Italia']]},
 {t:'Sussurri longobardi: Castiglione Olona, Castelseprio e Cairate',d:'2026-09-20',tipo:'g',stato:'f',u:S+'2026/09/08/sussurri-longobardi-castelseprio-cairate/',l:[['Castiglione Olona',45.7520,8.8760,'Italia'],['Castelseprio',45.7210,8.8610,'Italia'],['Cairate',45.6920,8.8740,'Italia']]},
 {t:'Arkè i5sensi · Cremona, non è la solita musica',d:'2026-09-12',tipo:'g',stato:'f',u:S+'2026/09/12/arke-i5sensi-cremona-non-e-la-solita-musica/',l:[['Cremona',45.1335,10.0227,'Italia']]},
 {t:'L\'eleganza del Marchesato di Saluzzo',d:'2026-09-05',tipo:'v',stato:'f',u:S+'2026/08/25/eleganza-marchesato-di-saluzzo-settembre-2026/',l:[['Saluzzo',44.6450,7.4930,'Italia'],['Castello della Manta',44.6160,7.4880,'Italia'],['Abbazia di Staffarda',44.7100,7.4330,'Italia'],['Racconigi',44.7690,7.6760,'Italia']]},
 {t:'Arkè i5sensi: Arte Sella e Castel Pergine',d:'2026-05-17',tipo:'g',stato:'f',u:S+'2026/05/07/arke-i5sensi-arte-sella-castel-pergine/',l:[['Arte Sella',46.0300,11.4200,'Italia'],['Castel Pergine',46.0630,11.2380,'Italia']]},
 {t:'Vista e meraviglia: Viareggio e Torre del Lago Puccini',d:'2026-04-26',tipo:'g',stato:'f',u:S+'2026/04/12/vista-e-meraviglia-viareggio-torre-del-lago/',l:[['Viareggio',43.8659,10.2513,'Italia'],['Torre del Lago Puccini',43.8290,10.2870,'Italia']]},
 {t:'Arkè i5sensi a Collebeato',d:'2026-04-18',tipo:'g',stato:'f',u:S+'2026/04/09/arke-i5sensi-collebeato-tenuta-martinengo/',l:[['Collebeato',45.5830,10.2100,'Italia']]},
 {t:'Arkè i5sensi a Ostiano',d:'2026-03-21',tipo:'g',stato:'f',u:S+'2026/03/12/arke-i5sensi-ostiano-colori-e-sapori/',l:[['Ostiano',45.2210,10.2520,'Italia']]},
 {t:'Arkè e l\'incanto della vista: il Liberty bresciano',d:'2026-02-08',tipo:'g',stato:'f',u:S+'2026/02/08/arke-e-lincanto-della-vistaun-viaggio-nel-liberty-bresciano-con-nexus/',l:[['Brescia',45.5416,10.2118,'Italia']]},
 // 2025
 {t:'Arkè · Colli Euganei: Castello del Catajo',d:'2025-05-18',tipo:'g',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Castello del Catajo',45.2930,11.7870,'Italia']]},
 {t:'Eolie: tra aria e fuoco',d:'2025-05-26',tipo:'v',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Lipari',38.4670,14.9540,'Italia'],['Stromboli',38.7930,15.2110,'Italia'],['Vulcano',38.4040,14.9620,'Italia']]},
 {t:'Arkè · Tavernole sul Mella: il forno fusorio',d:'2025-05-03',tipo:'g',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Tavernole sul Mella',45.7460,10.2390,'Italia']]},
 {t:'Alvernia e Périgord',d:'2025-04-21',tipo:'v',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Clermont-Ferrand',45.7772,3.0870,'Francia'],['Sarlat-la-Canéda',44.8890,1.2160,'Francia']]},
 {t:'Arkè · Gardone Riviera e Calvagese',d:'2025-04-05',tipo:'g',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Gardone Riviera',45.6200,10.5600,'Italia'],['Calvagese della Riviera',45.5340,10.4440,'Italia']]},
 {t:'Arkè · Torbiere del Sebino',d:'2025-03-29',tipo:'g',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Provaglio d\'Iseo',45.6330,10.0420,'Italia']]},
 {t:'Arkè · Asola e Redondesco',d:'2025-03-22',tipo:'g',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Asola',45.2210,10.4130,'Italia'],['Redondesco',45.1660,10.5130,'Italia']]},
 {t:'CERN, Ginevra e Losanna',d:'2025-03-14',tipo:'v',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Ginevra e CERN',46.2340,6.0550,'Svizzera'],['Losanna',46.5197,6.6323,'Svizzera']]},
 {t:'Vietnam e Cambogia',d:'2025-02-26',tipo:'v',stato:'f',u:S+'2024/11/13/viaggio-in-vietnam-e-cambogia/',l:[['Hanoi',21.0285,105.8542,'Vietnam'],['Baia di Ha Long',20.9101,107.1839,'Vietnam'],['Ho Chi Minh',10.7769,106.7009,'Vietnam'],['Siem Reap e Angkor',13.4125,103.8670,'Cambogia']]},
 {t:'Arkè · Milano: Fonderia De Andreis e Fondazione Pomodoro',d:'2025-02-15',tipo:'g',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Milano',45.4636,9.1900,'Italia']]},
 {t:'Arkè · Cremona: pitture di luce e fuoco',d:'2025-02-01',tipo:'g',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Cremona',45.1335,10.0227,'Italia']]},
 {t:'Milano: Niki de Saint Phalle e Binario 21',d:'2025-01-19',tipo:'g',stato:'f',u:S+'2025/01/12/programma-2025/',l:[['Milano',45.4636,9.1900,'Italia']]},
 // 2023
 {t:'Viaggio in Andalusia',d:'2023-04-23',tipo:'v',stato:'f',u:S+'2022/12/11/viaggio-in-andalusia/',l:[['Siviglia',37.3891,-5.9845,'Spagna'],['Cordova',37.8882,-4.7794,'Spagna'],['Granada',37.1773,-3.5986,'Spagna']]},
 {t:'Viaggio in Marocco',d:'2023-02-18',tipo:'v',stato:'f',u:S+'2022/11/15/viaggio-in-marocco-18-26-febbraio-2023/',l:[['Marrakech',31.6295,-7.9811,'Marocco'],['Fès',34.0181,-5.0078,'Marocco']]},
 {t:'Il mondo del marmo di Carrara',d:'2023-03-01',tipo:'g',stato:'f',u:S+'2023/01/26/il-mondo-del-marmo-di-carrara/',l:[['Carrara',44.0790,10.0970,'Italia']]},
 {t:'Bergamo e Brescia Capitale della Cultura 2023',d:'2023-02-01',tipo:'g',stato:'f',u:S+'2023/01/26/bergamo-e-brescia-capitale-della-cultura-2023/',l:[['Bergamo',45.6983,9.6773,'Italia']]},
 // 2022
 {t:'Slovenia, Croazia e laghi di Plitvice',d:'2022-10-29',tipo:'v',stato:'f',u:S+'2022/07/02/viaggio-in-slovenia-e-croazia-e-ai-laghi-di-plitvice/',l:[['Lubiana',46.0569,14.5058,'Slovenia'],['Laghi di Plitvice',44.8654,15.5820,'Croazia']]},
 {t:'Milano: Max Ernst, Castello Sforzesco e Monumentale',d:'2022-11-01',tipo:'g',stato:'f',u:S+'2022/10/27/milano-max-ernst-i-sotterranei-del-castello-sforzesco-e-il-cimitero-monumentale/',l:[['Milano',45.4636,9.1900,'Italia']]},
 {t:'Innsbruck e i Mondi di Cristallo Swarovski',d:'2022-10-02',tipo:'g',stato:'f',u:S+'2022/07/25/innsbruck-con-visita-alla-mostra-un-solo-mondo-il-potere-dei-4-elementi-e-visita-ai-mondi-di-cristallo-swarovski/',l:[['Innsbruck',47.2692,11.4041,'Austria'],['Wattens, Mondi di Cristallo',47.2940,11.6000,'Austria']]},
 {t:'Genova e Staglieno',d:'2022-06-25',tipo:'v',stato:'f',u:S+'2022/06/14/viaggio-a-genova-e-staglieno/',l:[['Genova',44.4056,8.9463,'Italia']]},
 {t:'Amsterdam e le città anseatiche',d:'2022-05-28',tipo:'v',stato:'f',u:S+'2022/04/13/viaggio-ad-amsterdam-e-le-citta-anseatiche-iscrizioni-proprogate-entro-il-7-maggio/',l:[['Amsterdam',52.3676,4.9041,'Paesi Bassi']]},
 // 2020
 {t:'Cipro: il mare d\'amore',d:'2020-02-20',tipo:'v',stato:'f',u:S+'2020/01/31/cipro-il-mare-damore/',l:[['Pafos',34.7720,32.4297,'Cipro'],['Nicosia',35.1856,33.3823,'Cipro']]},
 // 2019
 {t:'Natale a Milano in tram storico',d:'2019-12-29',tipo:'g',stato:'f',u:S+'2019/10/27/natale-a-milano/',l:[['Milano',45.4636,9.1900,'Italia']]},
 {t:'Modena e Sassuolo',d:'2019-10-01',tipo:'g',stato:'f',u:S+'2019/09/09/modena-e-sassuolo/',l:[['Modena',44.6471,10.9252,'Italia'],['Sassuolo',44.5450,10.7850,'Italia']]},
 {t:'Vigevano, la città ideale di Leonardo',d:'2019-06-01',tipo:'g',stato:'f',u:S+'2019/05/07/vigevano-la-citta-ideale-di-leonardo/',l:[['Vigevano',45.3167,8.8597,'Italia']]},
 {t:'Vinci, le terre di Leonardo',d:'2019-05-01',tipo:'v',stato:'f',u:S+'2019/04/08/vinci-le-terre-di-leonardo/',l:[['Vinci',43.7860,10.9260,'Italia']]},
 {t:'Milano: la grazia e la bellezza',d:'2019-04-01',tipo:'g',stato:'f',u:S+'2019/03/10/milano-la-grazia-e-la-bellezza/',l:[['Milano',45.4636,9.1900,'Italia']]},
 {t:'Venezia 500',d:'2019-03-01',tipo:'g',stato:'f',u:S+'2019/02/03/venezia-500/',l:[['Venezia',45.4408,12.3155,'Italia']]},
 {t:'Giordania',d:'2019-03-15',tipo:'v',stato:'f',u:S+'2018/09/25/giordania/',l:[['Amman',31.9539,35.9106,'Giordania'],['Petra',30.3285,35.4444,'Giordania']]},
 // 2018
 {t:'Milano: nuovi e antichi romanticismi',d:'2018-11-15',tipo:'g',stato:'f',u:S+'2018/10/18/milano-nuovi-e-antichi-romanticismi/',l:[['Milano',45.4636,9.1900,'Italia']]},
 {t:'Viaggio in Baviera',d:'2018-11-01',tipo:'v',stato:'f',u:S+'2018/09/01/viaggio-in-baviera-1-4-novembre-2018/',l:[['Monaco di Baviera',48.1351,11.5820,'Germania'],['Neuschwanstein',47.5576,10.7498,'Germania']]},
 {t:'Padova, città degli affreschi',d:'2018-09-23',tipo:'g',stato:'f',u:S+'2018/05/30/padova-citta-degli-affreschi-23-settembre-2018/',l:[['Padova',45.4064,11.8768,'Italia']]},
 {t:'Roma: Caravaggio e Bernini',d:'2018-09-08',tipo:'v',stato:'f',u:S+'2018/05/11/roma-08-09-settembre-2018/',l:[['Roma',41.9028,12.4964,'Italia']]},
 {t:'Tiziano e la Pinacoteca Tosio Martinengo',d:'2018-06-17',tipo:'g',stato:'f',u:S+'2018/05/20/tiziano-e-pinacoteca-tosio-martinengo-17-giugno-2018/',l:[['Brescia',45.5416,10.2118,'Italia']]},
 {t:'Ravenna e la mostra di Forlì',d:'2018-03-01',tipo:'g',stato:'f',u:S+'2018/02/07/ravenna-e-visita-alla-mostra-di-forli-leterno-e-il-tempo-tra-michelangelo-e-caravaggio/',l:[['Ravenna',44.4184,12.2035,'Italia'],['Forlì',44.2227,12.0407,'Italia']]},
 {t:'Malta in 3C: cavalieri, Caravaggio e carnevale',d:'2018-02-10',tipo:'v',stato:'f',u:S+'2017/10/22/malta-in-3c/',l:[['La Valletta',35.8989,14.5146,'Malta']]},
 {t:'Milano: mostra di Frida Kahlo',d:'2018-02-01',tipo:'g',stato:'f',u:S+'2018/01/19/milano-mostra-frida-kahlo/',l:[['Milano',45.4636,9.1900,'Italia']]},
 // 2017
 {t:'I tesori di Napoli e le luci di Salerno',d:'2017-12-06',tipo:'v',stato:'f',u:S+'2017/10/05/i-tesori-di-napoli-e-le-luci-di-salerno/',l:[['Napoli',40.8518,14.2681,'Italia'],['Ercolano',40.8060,14.3480,'Italia'],['Salerno',40.6824,14.7681,'Italia']]},
 {t:'Milano: Dentro Caravaggio',d:'2017-11-01',tipo:'g',stato:'f',u:S+'2017/10/05/dentro-caravaggio/',l:[['Milano',45.4636,9.1900,'Italia']]},
 {t:'Messico e Guatemala',d:'2017-03-01',tipo:'v',stato:'f',u:S+'2017/03/13/racconti-di-viaggio/',l:[['Città del Messico',19.4326,-99.1332,'Messico'],['San Cristóbal de las Casas',16.7370,-92.6376,'Messico'],['Antigua Guatemala',14.5586,-90.7295,'Guatemala'],['Tikal',17.2220,-89.6237,'Guatemala']]},
 {t:'Matera e la Puglia',d:'2017-04-01',tipo:'v',stato:'f',u:S+'2017/02/07/matera-e-la-puglia/',l:[['Matera',40.6664,16.6043,'Italia'],['Alberobello',40.7840,17.2370,'Italia'],['Bari',41.1171,16.8719,'Italia']]},
 {t:'Bologna: Dalí Experience e la città',d:'2017-02-15',tipo:'g',stato:'f',u:S+'2017/02/01/bologna-visita-alla-mostra-dali-experience-e-alla-citta/',l:[['Bologna',44.4949,11.3426,'Italia']]},
 {t:'La Santa Russia: San Pietroburgo, Mosca e l\'Anello d\'Oro',d:'2017-04-20',tipo:'v',stato:'f',u:S+'2016/10/29/la-santa-russia-san-pietroburgo-mosca-e-lanello-doro/',l:[['San Pietroburgo',59.9311,30.3609,'Russia'],['Mosca',55.7558,37.6173,'Russia'],['Sergiev Posad, Anello d\'Oro',56.3100,38.1300,'Russia']]},
 {t:'Sicilia nel cuore del Barocco',d:'2017-05-01',tipo:'v',stato:'f',u:S+'2016/10/29/sicilia-nel-cuore-del-barocco/',l:[['Noto',36.8910,15.0700,'Italia'],['Ragusa',36.9250,14.7300,'Italia'],['Siracusa',37.0755,15.2866,'Italia']]},
 // 2016
 {t:'Nei luoghi di Tommaso d\'Aquino: Fossanova e la riviera di Ulisse',d:'2016-12-08',tipo:'v',stato:'f',u:S+'2016/10/04/viaggio-di-dicembre-nei-luoghi-di-tommaso-daquino-labbazia-di-fossanova-e-la-riviera-di-ulisse/',l:[['Abbazia di Fossanova',41.4400,13.1980,'Italia'],['Sperlonga',41.2600,13.4330,'Italia'],['Gaeta',41.2130,13.5710,'Italia']]},
 {t:'Firenze: i luoghi della carità',d:'2016-09-18',tipo:'g',stato:'f',u:S+'2016/07/13/firenze-i-luoghi-della-carita-domenica-18-settembre-2016/',l:[['Firenze',43.7696,11.2558,'Italia']]},
 {t:'L\'Abbazia di Monteveglio e la Rocchetta Mattei',d:'2016-05-15',tipo:'g',stato:'f',u:S+'2016/04/06/l-abbazia-di-monterveglio-e-la-rocchetta-mattei/',l:[['Monteveglio',44.4700,11.1000,'Italia'],['Rocchetta Mattei',44.2720,11.0300,'Italia']]},
 {t:'Germania: sulle orme di Carlo Magno',d:'2016-04-23',tipo:'v',stato:'f',u:S+'2016/02/05/viaggio-in-germania-sulle-orme-di-carlo-magno-le-cattedrali-della-germania-imperiale/',l:[['Aquisgrana',50.7753,6.0839,'Germania'],['Colonia',50.9375,6.9603,'Germania'],['Magonza',49.9929,8.2473,'Germania'],['Worms',49.6341,8.3507,'Germania'],['Spira',49.3173,8.4412,'Germania']]},
 {t:'Le capitali baltiche: Riga, Tallinn e Helsinki',d:'2016-02-06',tipo:'v',stato:'f',u:S+'2015/12/18/nuova-proposta-viaggio-di-febbraio/',l:[['Riga',56.9496,24.1052,'Lettonia'],['Tallinn',59.4370,24.7536,'Estonia'],['Helsinki',60.1699,24.9384,'Finlandia']]},
 // 2015
 {t:'Aosta: i cammini sacri e il castello di Issogne',d:'2015-09-15',tipo:'v',stato:'f',u:S+'2015/08/14/viaggio-ad-aosta-i-cammini-sacri-il-castello-di-issogne/',l:[['Aosta',45.7372,7.3201,'Italia'],['Castello di Issogne',45.6550,7.6870,'Italia']]},
 {t:'Asti, Vicoforte e Mondovì',d:'2015-05-15',tipo:'v',stato:'f',u:S+'2015/04/08/viaggio-ad-asti-vicoforte-e-mondovi/',l:[['Asti',44.9008,8.2064,'Italia'],['Vicoforte',44.3640,7.8630,'Italia'],['Mondovì',44.3900,7.8180,'Italia']]},
 {t:'Portogallo: il Cammino Portoghese',d:'2015-04-25',tipo:'v',stato:'f',u:S+'2015/01/14/viaggio-in-portogallo/',l:[['Lisbona',38.7223,-9.1393,'Portogallo'],['Fátima',39.6300,-8.6700,'Portogallo'],['Porto',41.1579,-8.6291,'Portogallo'],['Braga',41.5450,-8.4260,'Portogallo']]},
 {t:'Parigi',d:'2015-02-15',tipo:'v',stato:'f',u:S+'2014/11/21/parigi-iscrizioni-entro-il-15-dicembre/',l:[['Parigi',48.8566,2.3522,'Francia']]},
 // 2014
 {t:'Milano: due mostre di Chagall',d:'2014-12-27',tipo:'g',stato:'f',u:S+'2014/11/01/milano-mostre-di-chagall-27-dicembre-2014/',l:[['Milano',45.4636,9.1900,'Italia']]},
 {t:'Ciociaria: sui passi di San Benedetto',d:'2014-12-06',tipo:'v',stato:'f',u:S+'2014/10/19/viaggio-in-ciociaria-sui-passi-di-san-benedetto/',l:[['Montecassino',41.4900,13.8140,'Italia'],['Subiaco',41.9250,13.0940,'Italia']]},
 {t:'Avila e Santiago di Compostela',d:'2014-04-25',tipo:'v',stato:'f',u:S+'2013/11/12/viaggi-di-primavera-2/',l:[['Avila',40.6560,-4.6810,'Spagna'],['Santiago di Compostela',42.8782,-8.5448,'Spagna']]},
 {t:'Istanbul',d:'2014-03-01',tipo:'v',stato:'f',u:S+'2013/09/18/viaggio-culturale-a-istanbul/',l:[['Istanbul',41.0082,28.9784,'Turchia']]},
 {t:'Brescia: 100 dipinti a Palazzo Martinengo',d:'2014-02-20',tipo:'g',stato:'f',u:S+'2014/02/09/mostra-100-dipinti-a-brescia-palazzo-martinengo-aperte-le-prenotazioni/',l:[['Brescia',45.5416,10.2118,'Italia']]},
 // 2013
 {t:'Polonia: i luoghi di Giovanni Paolo II',d:'2013-04-25',tipo:'v',stato:'f',u:S+'2013/01/02/viaggio-in-polonia/',l:[['Cracovia',50.0647,19.9450,'Polonia'],['Wadowice',49.8830,19.4930,'Polonia'],['Auschwitz-Birkenau',50.0260,19.2040,'Polonia'],['Częstochowa',50.8120,19.1200,'Polonia']]},
 {t:'San Fruttuoso e il santuario di Montallegro',d:'2013-04-14',tipo:'g',stato:'f',u:S+'2013/03/28/viaggio-a-san-fruttuoso-e-monteallegro/',l:[['San Fruttuoso',44.3160,9.1750,'Italia'],['Santuario di Montallegro',44.3600,9.2500,'Italia']]},
 // 2012
 {t:'Sulle orme di San Carlo Borromeo',d:'2012-06-23',tipo:'g',stato:'f',u:S+'2012/05/25/in-viaggio-con-nexus-23-giugno-sulle-orme-di-san-carlo-borromeo/',l:[['Arona',45.7580,8.5560,'Italia']]},
 {t:'Romania: i monasteri della Bucovina',d:'2012-04-25',tipo:'v',stato:'f',u:S+'2012/01/26/in-viaggio-con-nexus-2/',l:[['Monasteri della Bucovina',47.7700,25.7100,'Romania'],['Brașov',45.6427,25.5887,'Romania']]},
 // 2011
 {t:'Andalusia',d:'2011-04-25',tipo:'v',stato:'f',u:S+'2011/02/03/viaggio-parrocchiale-in-andalusia/',l:[['Siviglia',37.3891,-5.9845,'Spagna'],['Granada',37.1773,-3.5986,'Spagna']]},
 {t:'Varallo e il Sacro Monte',d:'2011-03-01',tipo:'g',stato:'f',u:S+'2011/02/06/visita-a-varallo/',l:[['Sacro Monte di Varallo',45.8180,8.2570,'Italia']]}
];
