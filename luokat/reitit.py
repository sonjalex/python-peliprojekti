import random

pelaaja1 = None

# Luokka reitit, jossa käydään läpi pelaajan ensimmäinen reittivalinta sekä lopulta valittu polku, oikea tai vasen
class Reitit:
    def __init__(self, pelaaja):
        self.pelaaja = pelaaja

    # Funktio reittivalinta, jossa pelaaja päättää kummalle polulle lähtee
    def reittivalinta():
        # Pelaajan sijainniksi merkitään metsä
        pelaaja1.sijainti = "metsä"
        print("\nSaavut Menninkäisten metsäreitille. Päivä näyttää kauniilta ja on täydellinen sää pienelle seikkailulle.")
        # Jos pelaajan repussa on kartta, annetaan hänelle valinta katsoa reittiä siitä
        if "kartta" in pelaaja1.reppu:
            katsotaanko = input("\nEdessäsi on kyltti kahdesta eri reitistä, vasemmalta löytyy Hömppäreitti ja oikealta Kuurupiilopolku.\nMuistat ottaneesi kartan reppuun mukaan, haluatko katsoa karttaa? Vastaa 'kyllä' tai 'ei' ")
            while katsotaanko != "kyllä" and katsotaanko != "ei":
                katsotaanko = input("Joudut nyt kuitenkin valitsemaan, että pääset eteenpäin! Katsotaanko karttaa? 'kyllä' / 'ei' ")
            if katsotaanko == "kyllä":
                print("\nKaivat kartan repustasi tutkien sitä hetken. Kartan mukaan vasemman polun Hömppäreitti on helpompi ja oikealle on vaativampi Kuurupiilopolku kokeneemmille patikoijille.")
                suunta = input("\nKumpaan suuntaan haluat mennä, vasempaan helpommalle reitille vai oikeaan vaativammalle reitille? 'vasen / 'oikea' ")
                while suunta != "vasen" and suunta != "oikea":
                    suunta = input("Syötä: 'vasen' tai 'oikea': ")
                if suunta == "vasen":
                    print("\nKävelet kohti Hömppäreittiä, seikkailu voi alkaa!")
                elif suunta == "oikea":
                    print("\nKävelet kohti Kuurupiilopolkua, toivottavasti osaat asiasi - seikkailu voi alkaa!")
            elif katsotaanko == "ei":
                suunta = input("\nOnneksi sinulla on mahtava suuntavaisto! Menetkö vasemmalle Hömppäreitille vai oikealle Kuurupiilopolulle? 'vasen / 'oikea' ")
                while suunta != "vasen" and suunta != "oikea":
                    suunta = input("Syötä: 'vasen' tai 'oikea': ")
                if suunta == "vasen":
                    print("\nKävelet kohti Hömppäreittiä, seikkailu voi alkaa!")
                elif suunta == "oikea":
                    print("\nKävelet kohti Kuurupiilopolkua, seikkailu voi alkaa!")
        # Pelaajalla ei ole karttaa ja hänen pitää sokeasti valita oma reittinsä
        if "kartta" not in pelaaja1.reppu:
            suunta = input("\nEdessäsi on kyltti kahdesta eri reitistä, muistat ettet ottanut karttaa mukaan retkelle.. \nKumpaan suuntaan haluat mennä, vasemmalle vievälle Hömppäreitille vai oikealle kohti Kuurupiilopolkua? 'vasen / 'oikea' ")
            while suunta != "vasen" and suunta != "oikea":
                suunta = input("Syötä: 'vasen' tai 'oikea': ")
            if suunta == "vasen":
                print("\nKävelet kohti Hömppäreittiä, seikkailu voi alkaa!")
            elif suunta == "oikea":
                print("\nKävelet kohti Kuurupiilopolkua, seikkailu voi alkaa!")
        if suunta == "vasen":
            # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
            pelaaja1.sijainti = "vasen"
            Reitit.vasen()
        else:
            # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
            pelaaja1.sijainti = "oikea"
            Reitit.oikea()

    # Funktio oikea, johon siirrytään kun pelaajan reittivalinta on oikea poulku - myös sijainti muutetaan
    def oikea():
        if pelaaja1.sijainti == "oikea":
            pass
        # Vaihtoehdot pelaajalle, jolla on kartta mukana
        if "kartta" in pelaaja1.reppu:
            print("\nHetken käveltyäsi huomaat kuinka jyrkkä ja vaikeakulkuinen valitsemasi reitti on.\n'En oikein tiedä miksi edes valitsin tämän', jupiset mielessäsi jatkaen matkaa: 'Ei tässä takaisinkaan päin viitsi kääntyä.'")
            print("\nKuulet korvissasi kovan kohinan ja jatkaessasi pidemmälle edessäsi siintää koski.")
            valinta = input("Mitä nyt? Käännytkö takaisin vai jatkatko matkaa? 'jatka' / 'käänny' ")
            while valinta != "jatka" and valinta != "käänny":
                valinta = input("'jatka' / 'käänny' ")
            if valinta == "käänny":
                # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                pelaaja1.sijainti = "käänny"
                Reitit.loppu()
            if valinta == "jatka":
                print("\nAlat ottamaan harppauksia kohti koskea - ylitse et pääse, mutta voit jatkaa matkaasi kosken viertä pitkin.\nNäet sivusilmällä marjapensaan ja kuulet kuinka vatsasi pitää meteliä.")
                # Valinnainen vaihtoehto pelaajalle, jolla on kasvikirja mukana
                if "kasvikirja" in pelaaja1.reppu:
                    print("\nMarjat näyttävät ihan puolukoilta, mutta koskaan ei voi olla liian varma!")
                    valinta = input("Muistat ottaneesi kasvikirjan mukaan, haluatko vilkaista sitä? 'kyllä' / 'ei' ")
                    if valinta == "ei":
                        print("\nOtat ison kourallisen marjoja ja heivaat ne suuhusi ajattelematta sen enempää. Nyt jaksaa jatkaa matkaa!")
                        # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                        pelaaja1.sijainti = "marjat"
                        Reitit.marjat()
                    elif valinta == "kyllä" and "vesipullo" in pelaaja1.reppu:
                        print("\nLöydät kasvikirjasta identtisen marjan joka on myrkyllinen - hyvä että tarkistit! Otat repustasi vesipullon ja otat siitä kunnon huikan. Nyt on hyvä jatkaa matkaa!")
                        # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                        pelaaja1.sijainti = "loppu"
                        Reitit.loppu()
                    elif valinta == "kyllä" and "vesipullo" not in pelaaja1.reppu:
                        print("\nLöydät kasvikirjasta identtisen marjan joka on myrkyllinen - hyvä että tarkistit! Nouset ylös ja jatkat matkaasi.")
                        # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                        pelaaja1.sijainti = "loppu"
                        Reitit.loppu()
                # Valinnainen vaihtoehto pelaajalle, jolla ei ole kasvikirjaa mukana
                elif "kasvikirja" not in pelaaja1.reppu:
                    print("\nMarjat näyttävät ihan puolukoilta")
                    valinta = input("Pitäisikö maistaa muutama? 'kyllä' / 'ei' ")
        # Vaihtoehto pelaajalle, jolla ei ole karttaa mukana
        elif "kartta" not in pelaaja1.reppu:
            print("\nHetken käveltyäsi huomaat kuinka jyrkkä ja vaikeakulkuinen valitsemasi reitti on.\n'Olisi varmaan pitänyt ottaa kartta mukaan', jupiset mielessäsi jatkaen matkaa: 'Ei tässä takaisinkaan päin viitsi kääntyä.'")
            print("\nKuulet korvissasi kovan kohinan ja jatkaessasi pidemmälle edessäsi siintää koski.")
            valinta = input("Mitä nyt? Käännynkö takaisin vai jatkanko matkaa? 'jatka' / 'käänny' ")
            while valinta != "jatka" and valinta != "käänny":
                valinta = input("'jatka' / 'käänny' ")
            if valinta == "käänny":
                # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                pelaaja1.sijainti = "käänny"
                Reitit.loppu()
            if valinta == "jatka":
                print("\nAlat ottamaan harppauksia kohti koskea - ylitse et pääse, mutta voit jatkaa matkaasi kosken viertä pitkin.\nNäet sivusilmällä marjapensaan ja kuulet kuinka vatsasi pitää meteliä.")
                # Valinnainen vaihtoehto pelaajalle, jolla on kasvikirja mukana
                if "kasvikirja" in pelaaja1.reppu:
                    print("Marjat näyttävät ihan puolukoilta, mutta koskaan ei voi olla liian varma!")
                    valinta = input("Muistat ottaneesi kasvikirjan mukaan, haluatko vilkaista sitä? 'kyllä' / 'ei' ")
                    if valinta == "ei":
                        print("Otat ison kourallisen marjoja ja heivaat ne suuhusi ajattelematta sen enempää. Nyt jaksaa jatkaa matkaa!")
                        # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                        pelaaja1.sijainti = "marjat"
                        Reitit.marjat()
                    elif valinta == "kyllä" and "vesipullo" in pelaaja1.reppu:
                        print("Löydät kasvikirjasta identtisen marjan joka on myrkyllinen - hyvä että tarkistit! Otat repustasi vesipullon ja otat siitä kunnon huikan. Nyt on hyvä jatkaa matkaa!")
                        # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                        pelaaja1.sijainti = "loppu"
                        Reitit.loppu()
                    elif valinta == "kyllä" and "vesipullo" not in pelaaja1.reppu:
                        print("Löydät kasvikirjasta identtisen marjan joka on myrkyllinen - hyvä että tarkistit! Nouset ylös ja jatkat matkaasi.")
                        # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                        pelaaja1.sijainti = "loppu"
                        Reitit.loppu()
                # Valinnainen vaihtoehto pelaajalle, jolla on kasvikirja mukana
                elif "kasvikirja" not in pelaaja1.reppu:
                    print("Marjat näyttävät ihan puolukoilta.")
                    valinta = input("Pitäisikö maistaa muutama? 'kyllä' / 'ei' ")
                    while valinta != "kyllä" and valinta != "ei":
                        valinta = input("'kyllä' / 'ei' ")
                    if valinta == "kyllä":
                        print("Otat ison kourallisen marjoja ja heivaat ne suuhusi ajattelematta sen enempää. Nyt jaksaa jatkaa matkaa!")
                        # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                        pelaaja1.sijainti = "marjat"
                        Reitit.marjat()
                    elif valinta == "ei":
                        print("Jätät marjat odottamaan seuraavaa matkailijaa ja jatkat kivikkoista reittiä eteenpäin")
                        pelaaja1.sijainti = "loppu"
                        return
                        

    # Funktio marjat, johon pelaaja siirretään, jos hän on syönyt marjoja tietämättä ovatko ne myrkyllisiä
    def marjat():
        # Arvotaan tulos marjasta, tuleeko pelaajalle huono olo
        heitä = input("Heitä noppaa painamalla 'enter'! ")
        while heitä != "":
            heitä = input("Paina 'enter' näppäintä. ")
        else:
            luku = random.randint(1,6)
            print(f"Heitit luvun {luku}, katsotaan mitä onni tuo tullessaan!")
            if 1 <= luku <= 3:
                print("\nVaeltaessasi polkua eteenpäin alat tuntea itsesi huonovointiseksi. Marjat eivät tainneetkaan olla niin hyvä idea... \nJoudut ottamaan puhelimen esille ja soittamaan ystäväsi apuun päästäksesi pois metsästä.\nTänään sinun oli tarkoitus siivota metsän takaista rantaviivaa roskista ystäviesti kanssa, huonovointisuuden takia joudut kuitenkin peruuttamaan suunnitelman.\nEnsi kerralla otat omat eväät mukaan...")
                print("")
                # Tulostetaan lopputeksti
                print(lue_lopputeksti())
                # Vaihdetaan pelaajan sijainti ja siirretään loppuun
                pelaaja1.sijainti = "valmis"
                # Valinta sulkea peli tai mennä päävalikkoon
                valinta = input("\nPaina 'P' palataksesti päävalikkoon tai 'E' sulkeaksesi pelin: ")
                if valinta == "p":
                    pelaaja1.sijainti = "koti"
                    return
                elif valinta == "e":
                    exit()
                else:
                    print("Virhe")
            if 4 <= luku <= 6:
                print("\nIkuisuudelta tuntuneen matkan jälkeen pääset vihdoin määränpäähäsi - aiemmin tunnetusti kauniille rannalle, jolle on vuosien saatossa alkanut huuhtoutua veden mukana paljon erilaista roskaa.\nPaikalle on kokoontunut joukko muitakin ihmisiä puhdistamaan rantaviivaa kaikenlaisesta roskasta.\nTällainen teko voi vaikuttaa mitättömältä suuremmassa skaalassa, mutta vesistöjen roskista siivoaminen on tärkeä osa luonnon säilymistä.")
                print("")
                # Tulostetaan lopputeksti
                print(lue_lopputeksti())
                # Vaihdetaan pelaajan sijainti ja siirretään loppuun
                pelaaja1.sijainti = "valmis"
                # Valinta sulkea peli tai mennä päävalikkoon
                valinta = input("\nPaina 'P' palataksesti päävalikkoon tai 'E' sulkeaksesi pelin: ")
                if valinta == "p":
                    pelaaja1.sijainti = "koti"
                    return
                elif valinta == "e":
                    exit()
                else:
                    print("Virhe")

    # Funktio loppu johon siirretään pelaajat, jotka eivät syöneet marjoja ja päättivät kääntyä kosken kohdalla pois
    def loppu():
        if pelaaja1.sijainti == "loppu":
        # Kosken kohdalla kääntynyt pelaaja saadaan funktioon käyttämällä pelaajan sijaintia
            print("\nIkuisuudelta tuntuneen matkan jälkeen pääset vihdoin määränpäähäsi - aiemmin tunnetusti kauniille rannalle, jolle on vuosien saatossa alkanut huuhtoutua veden mukana paljon erilaista roskaa.\nPaikalle on kokoontunut joukko muitakin ihmisiä puhdistamaan rantaviivaa kaikenlaisesta roskasta.\nTällainen teko voi vaikuttaa mitättömältä suuremmassa skaalassa, mutta vesistöjen roskista siivoaminen on tärkeä osa luonnon säilymistä.")
            print("")
            # Tulostetaan lopputeksti
            print(lue_lopputeksti())
            # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
            pelaaja1.sijainti = "valmis"
            # Valinta sulkea peli tai mennä päävalikkoon
            valinta = input("\nPaina 'P' palataksesti päävalikkoon tai 'E' sulkeaksesi pelin: ")
            if valinta == "p":
                pelaaja1.sijainti = "koti"
                return
            elif valinta == "e":
                exit()
            else:
                print("Virhe")
        if pelaaja1.sijainti == "käänny":
            print("Kosken vierestä kävely ei vaikuta lainkaan turvalliselta, joten käännyt ympäri kohti aiempaa reittiä.\nIkuisuudelta tuntuvan ajan jälkeen alat kyseenalaistaa omaa suuntavaistoasi.\nMissä oikein olet? Mihin olet menossa? Mistä olet tulossa?")
            # Jos pelaajalla on kartta repussaan hän löytää helposti takaisin kylteille
            if "kartta" in pelaaja1.reppu:
                print("\nOtat kartan esille ja vilkuilet sitä hämmentyneenä yrittäen ymmärtää missä olet.\nPitkän pähkäilyn jälkeen ymmärrät missä olet ja pääset vihdoin takaisin kylteille huokaisten helpotuksesta.")
                # Vaihdetaan pelaajan sijainti ja siirretään seuraavaan osaan
                pelaaja1.sijainti = "vasen"
                Reitit.vasen()
                return
            # Jos pelaajalla ei ole karttaa
            elif "kartta" not in pelaaja1.reppu:
                print("\nJuurikin sinun tuuriasi, se ainoa kerta kun karttaa ei ole mukana eksyt ihan totaalisesti. \nKaivat puhelimen taskusta - akku on loppu, niimpä tietenkin.")
                valinta = input("Ympäriltäsi lähtee neljä eri polkua, mihin suuntaan haluat lähteä? 'p' (pohjoinen), 'e' (etelä), 'i' (itä), 'l' (länsi)" )
                while valinta != "i" and valinta != "p" and valinta != "l" and valinta != "e":
                    valinta = input("Valitse ilmansuunta: 'p' (pohjoinen), 'e' (etelä), 'i' (itä), 'l' (länsi) ")
                if valinta == "l" or valinta == "e":
                    print("\nHarpot eteenpäin yrittäen löytää tietä ulos metsästä - pitkän ja kivisen kamppailun jälkeen voit vain todeta olevasi todellisen eksyksissä.\nSinulla ja ystävilläsi oli tänään tarkoitus mennä siivoamaan metsän takana olevaa rantaviivaa sinne huuhtoutuneista roskista.\nJoudut kuitenkin unohtamaan suunnitelman, koska jäit metsään loukkuun.")
                    print("")
                    # Tulostetaan lopputeksti
                    print(lue_lopputeksti())
                    # Vaihdetaan pelaajan sijainti ja siirretään loppuun
                    pelaaja1.sijainti = "valmis"
                    # Valinta sulkea peli tai mennä päävalikkoon
                    valinta = input("\nPaina 'P' palataksesti päävalikkoon tai 'E' sulkeaksesi pelin: ")
                    if valinta == "p":
                        pelaaja1.sijainti = "koti"
                        return
                    elif valinta == "e":
                        exit()
                    else:
                        print("Virhe")
                elif valinta == "i":
                    print("\nPitkän vaelluksen jälkeen löydät kuin löydätkin sinne mihin alunperin halusitkin!\nAiemmin tunnetusti kauniille rannalle, jolle on vuosien saatossa alkanut huuhtoutua veden mukana paljon erilaista roskaa.\nPaikalle on kokoontunut joukko muitakin ihmisiä puhdistamaan rantaviivaa kaikenlaisesta roskasta.\nTällainen teko voi vaikuttaa mitättömältä suuremmassa skaalassa, mutta vesistöjen roskista siivoaminen on tärkeä osa luonnon säilymistä.")
                    print("")
                    # Tulostetaan lopputeksti
                    print(lue_lopputeksti())
                    # Vaihdetaan pelaajan sijainti ja siirretään loppuun
                    pelaaja1.sijainti = "valmis"
                    # Valinta sulkea peli tai mennä päävalikkoon
                    valinta = input("\nPaina 'P' palataksesti päävalikkoon tai 'E' sulkeaksesi pelin: ")
                    if valinta == "p":
                        pelaaja1.sijainti = "koti"
                        return
                    elif valinta == "e":
                        exit()
                    else:
                        print("Virhe")
                elif valinta == "p":
                    print("\nTodella pitkältä tuntuneen matkan jälkeen pääset kuin pääsetkin takaisin kylteille jotka veivät sinut pahamaisen Kuurupiilopolun suuntaan.\nHömppäreitti ei valitettavasti kuulosta yhtään sen paremmalta, joten päätät lähteä kotiin.\nTarkoituksenasi oli mennä ystäviesti kanssa siivoamaan metsän takaa löytyvää rantaviivaa, mutta tämän päivän koitoksen jälkeen se voi odottaa päivän tai pari.")
                    print("")
                    # Tulostetaan lopputeksti
                    print(lue_lopputeksti())
                    # Vaihdetaan pelaajan sijainti ja siirretään loppuun
                    pelaaja1.sijainti = "valmis"
                    # Valinta sulkea peli tai mennä päävalikkoon
                    valinta = input("\nPaina 'P' palataksesti päävalikkoon tai 'E' sulkeaksesi pelin: ")
                    if valinta == "p":
                        pelaaja1.sijainti = "koti"
                        return
                    elif valinta == "e":
                        exit()
                    else:
                        print("Virhe")

    # Funktio vasen johon siirrytään, kun pelaajan reittivalinta on vasen polku - myös sijainti muutetaan
    def vasen():
        if pelaaja1.sijainti == "vasen":
            print("\nMatkan varrella näet paljon erilaisia eläimiä ja jopa muutama patikoiva ihminen tulee sinua vastaan.\nNäät sivusilmällä peuran metsän laidalla - halusit olla ilman puhelinta, mutta tästä on saatava kuva!\n")
            heitä = input("Heitä noppaa painamalla enter ")
            while heitä != "":
                heitä = input("Paina enter näppäintä! ")
            else:
                luku = random.randint(1,6)
                print(f"Heitit luvun {luku}! Katsotaan onko onni puolellasi")
                if 1 <= luku <= 3:
                    print("\nOtat hitaasti puhelimen taskustasi ja hiivit kohti peuraa. Päästessäsi lähemmäs nappaat siitä ihan täydellisen kuvan!\nJatkat matkaasi Hömppäreittiä pitkin kunnes saavut metsän takana olevalle rantaviivalle.\nAiemmin tunnetusti kauniille rannalla, jolle on vuosien saatossa alkanut huuhtoutua veden mukana paljon erilaista roskaa.\nPaikalle on kokoontunut joukko muitakin ihmisiä puhdistamaan rantaviivaa kaikenlaisesta roskasta.\nTällainen teko voi vaikuttaa mitättömältä suuremmassa skaalassa, mutta vesistöjen roskista siivoaminen on tärkeä osa luonnon säilymistä.")
                    print("")
                    # Tulostetaan lopputeksti
                    print(lue_lopputeksti())
                    # Vaihdetaan pelaajan sijainti ja siirretään loppuun
                    pelaaja1.sijainti = "valmis"
                    # Valinta sulkea peli tai mennä päävalikkoon
                    valinta = input("\nPaina 'P' palataksesti päävalikkoon tai 'E' sulkeaksesi pelin: ")
                    if valinta == "p":
                        pelaaja1.sijainti = "koti"
                        return
                    elif valinta == "e":
                        exit()
                    else:
                        print("Virhe")
                elif 4 <= luku <= 6:
                    print("\nOtat hitaasti puhelimen taskustasi ja lähdet kohti peuraa.\nJaloissasi on kuitenkin juuri mihin kompastut epähuomiossasi. Huudahdat säikähdyksestä ja peura juoksee karkuun - kuva jäi saamatta :(\nJatkat kuitenkin matkaasi Hömppäreittiä pitkin hetkellisesti ontuen kunnes saavut metsän takana olevalle rantaviivalle.\nAiemmin tunnetusti kauniille rannalle, jolle on vuosien saatossa alkanut huuhtoutua veden mukana paljon erilaista roskaa.\nPaikalle on kokoontunut joukko muitakin ihmisiä puhdistamaan rantaviivaa kaikenlaisesta roskasta.\nTällainen teko voi vaikuttaa mitättömältä suuremmassa skaalassa, mutta vesistöjen roskista siivoaminen on tärkeä osa luonnon säilymistä.")
                    print("")
                    # Tulostetaan lopputeksti
                    print(lue_lopputeksti())
                    # Vaihdetaan pelaajan sijainti ja siirretään loppuun
                    pelaaja1.sijainti = "valmis"
                    # Valinta sulkea peli tai mennä päävalikkoon
                    valinta = input("\nPaina 'P' palataksesti päävalikkoon tai 'E' sulkeaksesi pelin: ")
                    if valinta == "p":
                        pelaaja1.sijainti = "koti"
                        return
                    elif valinta == "e":
                        exit()
                    else:
                        print("Virhe")

def lue_lopputeksti():
    try:
        with open("lopputeksti.txt", "r", encoding="utf-8") as tiedosto:
            lopputeksti = tiedosto.read()
        return lopputeksti
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")
    except IOError:
        print("Tiedoston käsittelyssä tapahtui virhe.")