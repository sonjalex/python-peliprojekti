import random

pelaaja1 = None
# Luokka Tavarat, jonka sisällä määritellään pelaajan mukaan ottamat tavarat
class Tavarat():
    def __init__ (self, nimi):
        self.nimi = nimi

    # Funktio tavarat, pelaaja saa itse määritellä haluaako ottaa matkalle jotain mukaan
    def tavarat():
        # Pelaajan sijainniksi laitetaan koti
        pelaaja1.sijainti = "koti"
        lisätäänkö = input("\nHaluatko lisätä reppuusi jotain matkaa varten? \nPitää muistaa ettei metsässä välttämättä ole toimivaa nettiyhteyttä ja matka olisi muutenkin kivempi taittaa ilman puhelinta! \nVastaa 'kyllä' tai 'ei' ")

        varmistus = "ei" # Alustus
        # Varmistetaan pelaajan päätös olla lisäämättä tavaroita
        while lisätäänkö != "kyllä" and lisätäänkö != "ei":
            lisätäänkö = input("Vastaa 'kyllä' tai 'ei' ")
        if lisätäänkö == "ei":
            print("\nOletko nyt ihan varma? Jos lisättäisiin jotain kuitenkin.. ")
            varmistus = input("Vastaa 'lisätään' tai 'ei' ")
            while varmistus != "ei" and varmistus != "lisätään":
                varmistus = input("Vastaa 'lisätään' tai 'ei' ")
            if varmistus == "lisätään":
                print("Tuo on varmasti parempi valinta!")
            elif varmistus == "ei":
                print("Selvä sitten!")

        # Annetaan pelaajan lisätä haluamansa tavarat reppuun
        if lisätäänkö == "kyllä" or varmistus == "lisätään":
            mukaan = input("\nMitä haluat lisätä reppuusi? (tyhjä lopettaa) ")
            # Poistetaan tyhjän komentorivin aiheuttama lisäys repun sisällöstä
            if mukaan == "":
                if "" in pelaaja1.reppu:
                    pelaaja1.reppu.remove("")
            while mukaan != "":
                print(f"{mukaan} on lisätty reppuun")
                pelaaja1.reppu.append(mukaan)
                mukaan = input("")

    # Funktio kartta, ensimmäinen tavara jota pelaajalle tarjotaan mukaan - tapahtuu vain, jos pelaaja ei ole ottanut karttaa mukaansa
    def kartta():
        if not "kartta" in pelaaja1.reppu:
            print("\nHaluaisit olla matkan ilman puhelintasi, eikä netti välttämättä toimi metsässä - haluatko ottaa alueen kartan mukaasi?")
            vastaus = input("Kyllä vai ei? ")
            kerrat = 0
            while vastaus != "kyllä" and vastaus != "ei" and kerrat < 3:
                kerrat += 1
                # Generoidaan satunnainen reagointi siihen, jos pelaaja ei vastaa kysymykseen halutulla tavalla
                numero = random.randint(1,3)
                if numero == 1:
                    vastaus = input("Ei tuo ollut kysymys :( Syötä kyllä tai ei: ")
                elif numero == 2:
                    vastaus = input("Uskon, että osaat keskittyä sen verran että vastaat 'kyllä' tai 'ei': ")
                elif numero == 3:
                    vastaus = input("Lueppa vähän tarkemmin: 'Syötä kyllä tai ei': ")
            if vastaus == "kyllä":
                print("Hyvä, nyt et ainakaan eksy, jos polut eivät näytäkkään tutuilta!")
                pelaaja1.reppu.append("kartta")
                print("Kartta on lisätty reppuun")
            elif vastaus == "ei":
                print("Muistat varmasti reitin yhtä hyvin kuin oman nimesi - eihän karttaa tarvitse mihinkään!")
            else:
                print("No ei väkisin!")

    # Funktio kasvikirja, toinen tavara jota pelaajalle tarjotaan mukaan - tapahtuu vain, jos pelaaja ei ole ottanut kirjaa mukaansa
    def kasvikirja():
        if not "kasvikirja" in pelaaja1.reppu:
            print("\nHuomaat sivusilmällä kirjan kasveista, tahtoisit olla matkan ilman puhelintasi eikä netti välttämättä toimi -  haluatko ottaa kirjan mukaan?")
            vastaus = input("Kyllä vai ei? ")
            kerrat = 0
            while vastaus != "kyllä" and vastaus != "ei" and kerrat < 3:
                kerrat += 1
                # Generoidaan satunnainen reagointi siihen, jos pelaaja ei vastaa kysymykseen halutulla tavalla
                numero = random.randint(1,3)
                if numero == 1:
                    vastaus = input("Ei tuo ollut kysymys :( Syötä kyllä tai ei: ")
                elif numero == 2:
                    vastaus = input("Uskon, että osaat keskittyä sen verran että vastaat 'kyllä' tai 'ei': ")
                elif numero == 3:
                    vastaus = input("Lueppa vähän tarkemmin: 'Syötä kyllä tai ei': ")
            if vastaus == "kyllä":
                print("Hyvä, kasvikirja kannattaa olla mukana, jotta tunnistat ovatko kasvit myrkyllisiä!")
                pelaaja1.reppu.append("kasvikirja")
                print("Kasvikirja on lisätty reppuun")
            elif vastaus == "ei":
                print("No... jos olet ihan varma!")
            else:
                print("No ei väkisin!")

    # Funktio vesi, kolmas tavara jota pelaajalle tarjotaan mukaan - tapahtuu vain, jos pelaaja ei ole ottanut kirjaa mukaansa
    def vesi():
        # Toteutettu any rakenteella määrittelyn helpottamiseksi
        if not any(tavara in pelaaja1.reppu
            for tavara in ("vettä", "vesipullo", "vesi")):
            print("\nPidemmälle matkalle olisi varmaan hyvä ottaa jotain juotavaa mukaan, eikö totta?")
            vastaus = input("Kyllä vai ei? ")
            kerrat = 0
            while vastaus != "kyllä" and vastaus != "ei" and kerrat < 3:
                kerrat += 1
                # Generoidaan satunnainen reagointi siihen, jos pelaaja ei vastaa kysymykseen halutulla tavalla
                numero = random.randint(1,3)
                if numero == 1:
                    vastaus = input("Ei tuo ollut kysymys :( Syötä kyllä tai ei: ")
                elif numero == 2:
                    vastaus = input("Uskon, että osaat keskittyä sen verran että vastaat 'kyllä' tai 'ei': ")
                elif numero == 3:
                    vastaus = input("Lueppa vähän tarkemmin: 'Syötä kyllä tai ei': ")
            if vastaus == "kyllä":
                # Otetaan huomioon kestävän kehityksen mahdollistava puhdas juomavesi
                print("Lisäät vesipullon reppuusi - ihan fiksu päätös. On etuoikeus asua maassa, jossa on mahdollisuus saada puhdasta juomavettä milloin tahansa")
                pelaaja1.reppu.append("vesipullo")
            elif vastaus == "ei":
                # Otetaan huomioon kestävän kehityksen mahdollistava puhdas juomavesi
                print("Matka ei varmaankaan ole niin pitkä, että vettä olisi pakko ottaa mukaan - on kuitenkin etuoikeus saada puhdasta juomavettä lähes missä vain tilanteessa.")      
            else:
                print("No ei väkisin!")    

        # Jos pelaajan repussa on mitään, käydään tavarat läpi luetellen
        if any(pelaaja1.reppu):
            print("\nRepussasi on")
            for tavara in pelaaja1.reppu:
                print("-", tavara)
            print("Vaikuttaa hyvältä, olet valmis retkellesi!")

        # Jos pelaajan reppu on tyhjä, laitetaan harmitteluviesti
        if not pelaaja1.reppu:
            print("\nReppusi on tyhjä :(")