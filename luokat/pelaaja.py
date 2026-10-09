# Luokka Pelaaja, johon määritellään pelaajan nimi, ikä, repun sisältö sekä pelaajan alkuperäinen sijainti
class Pelaaja():
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä
        self.reppu = []
        self.sijainti = "koti"