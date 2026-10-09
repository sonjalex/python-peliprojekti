import random
import json

from luokat import Pelaaja, Tavarat, Reitit
from luokat import tavarat as tavarat_moduuli
from luokat import reitit as reitit_moduuli

# Pääohjelma

def lue_intro():
    try:
        with open("intro.txt", "r", encoding="utf-8") as tiedosto:
            intro = tiedosto.read()
        return intro
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")
    except IOError:
        print("Tiedoston käsittelyssä tapahtui virhe.")

def tallenna(pelaaja1):
    tallennus = {
        "nimi": pelaaja1.nimi,
        "ikä": pelaaja1.ikä,
        "reppu": pelaaja1.reppu,
        "sijainti": pelaaja1.sijainti
    }
    with open("pelaaja.json", "w", encoding="utf-8") as tiedosto:
        json.dump(tallennus, tiedosto, ensure_ascii=False, indent=4) # Näyttää ääkköset ja muotoilee tallennuksen

def lataa():
    try:
        with open("pelaaja.json", "r", encoding="utf-8") as tiedosto:
            data = json.load(tiedosto)

        pelaaja1 = Pelaaja(data["nimi"], data["ikä"])
        pelaaja1.reppu = data["reppu"]
        pelaaja1.sijainti = data["sijainti"]
        return pelaaja1
    except FileNotFoundError:
        print("Tallennusta ei löytynyt")
        return None
    except json.JSONDecodeError:
        print("Tallennus on tyhjä\nAloita uusi peli")
        return None

def pelaa():
    # Pelaajaa ei tallenneta pelkästään pelaa funktioon
    global pelaaja1

    peli = True

    while peli:
        if pelaaja1.sijainti == "oikea":
            Reitit.oikea()
            tallenna(pelaaja1)
        elif pelaaja1.sijainti == "vasen":
            Reitit.vasen()
            tallenna(pelaaja1)
        elif pelaaja1.sijainti == "marjat":
            Reitit.marjat()
            tallenna(pelaaja1)
            break
        elif pelaaja1.sijainti in ("loppu", "käänny"):
            Reitit.loppu()
            tallenna(pelaaja1)
            break
        elif pelaaja1.sijainti == "valmis":
            tallenna(pelaaja1)
            break

        else:
            peli = False

def aloita_peli():
    # Pelaajaa ei tallenneta pelkästään aloita_peli funktioon
    global pelaaja1
    # Peli aloitetaan kysymällä pelaajan nimi ja ikä
    nimi = input("Anna nimesi: ")
    print(f"Hei, {nimi}")
    while True:
        try:
            ikä = int(input("Syötä ikäsi: "))
            break
        except ValueError:
            print("Virhe: Syötä kokonaisluku")
    print(f"Olet {ikä} vuotias.")

    # Pelaajan iän ollessa vähemmmän kuin 12 peli sulkeutuu
    if ikä < 12:
        print("Olet liian nuori, sinun pitää olla vähintään 12 vuotias pelataksesi peliä")
        exit()
    else:
        print(f"Hei {nimi}!")
        # Jos pelaajan ikä on vähintään 12, luetaan pelin intro
        print(lue_intro())
        # Tallennetaan pelaajan nimi ja ikä luokkaan Pelaaja
        pelaaja1 = Pelaaja(nimi, ikä)

        tavarat_moduuli.pelaaja1 = pelaaja1
        reitit_moduuli.pelaaja1 = pelaaja1

        Tavarat.tavarat()
        tallenna(pelaaja1)
        Tavarat.kartta()
        tallenna(pelaaja1)
        Tavarat.kasvikirja()
        tallenna(pelaaja1)
        Tavarat.vesi()
        tallenna(pelaaja1)
        Reitit.reittivalinta()
        tallenna(pelaaja1)

        pelaa()

def jatka():
    # Pelaajaa ei tallenneta pelkästään jatka funktioon
    global pelaaja1

    # Ladataan tallennetut tiedot
    pelaaja1 = lataa()

    if pelaaja1 is None:
        print("Tallennusta ei löytynyt")
        return

    tavarat_moduuli.pelaaja1 = pelaaja1
    reitit_moduuli.pelaaja1 = pelaaja1

    print(f"\nHei, {pelaaja1.nimi}! Älä unohda reppuasi! {pelaaja1.reppu}")

    if pelaaja1.sijainti == "koti":
        print("Olet vielä kotona!")
        Tavarat.tavarat()
        tallenna(pelaaja1)
        Tavarat.kartta()
        tallenna(pelaaja1)
        Tavarat.kasvikirja()
        tallenna(pelaaja1)
        Tavarat.vesi()
        tallenna(pelaaja1)
        Reitit.reittivalinta()
        tallenna(pelaaja1)
    
    pelaa()

def ohjeet():
    try:
        with open("ohjeet.txt", "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())
    except FileNotFoundError:
        print("Tiedostoa ei löyty")

    input("\nPaina 'enter' palataksesi päävalikkoon.")

def päävalikko():
    while True:
        print("\nTervetuloa metsäseikkailupeliin!\n1. Aloita peli\n2. Jatka peliä\n3. Ohjeet\n4. Sulje peli")

        valinta = input("'1-4': ")

        if valinta == "1":
            aloita_peli()
        elif valinta == "2":
            jatka()
        elif valinta == "3":
            ohjeet()
        elif valinta == "4":
            break
        else:
            print("Virhe")

if __name__ == "__main__":
    päävalikko()