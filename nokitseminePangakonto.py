# ÜLESANNE: defineerige uus klass, see peaks kirjeldama/defineerima pangakonto
class Pangakonto:
    # luua init meetod, nagu tegime õpilane.py failis
    # see võiks kirjeldada pangakonto olulisi omadusi - kontonumber, bilanss, omanikuNimi
    #klassil võiks olla ka omadus, mis suurendab bilansi omadust mingi arvu võrra

# Lisaks:  Võiks luua ühe objekti sellest klassist mingite väärtustega.

            # # Võiks selle loodud objekti bilanssi suurendada


    def __init__(self, nimi, number, bilanss, hoius):
        self.omanikuNimi = nimi
        self.kontoNumber = number
        self.kontoSeis = bilanss
        self.reservHoius = hoius

    def suurendaBilanssi(self):
        self.kontoSeis  = self.kontoSeis + 500

    def suurendaHoiust(self):
        self.reservHoius = self.reservHoius + 50

konto1 = Pangakonto ("Mari", "EE123456789", 200, 1000)
konto2 = Pangakonto ("Mari", "EE123456789", 200, 1000)

UusKonto = Pangakonto("Jüri", "EE987654321", 1000, 300)

##### SEE ON MARI KONTO VÄLJAVÕTE
print(konto1.omanikuNimi)
print(konto1.kontoNumber)
print(konto1.kontoSeis)
konto1.suurendaBilanssi()
print(konto1.kontoSeis)
konto1.suurendaHoiust()
print(konto1.reservHoius)
print(konto2.omanikuNimi + "  ", konto2.kontoNumber + "  ", konto2.reservHoius)
konto2.suurendaHoiust()
print(konto2.reservHoius)

### SEE ON JÕRI KONTO VÄLJAVÕTE
print (UusKonto.omanikuNimi)
UusKonto.suurendaHoiust()
print(UusKonto.reservHoius)


