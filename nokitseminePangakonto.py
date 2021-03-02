# ÜLESANNE: defineerige uus klass, see peaks kirjeldama/defineerima pangakonto
class Pangakonto:
    # luua init meetod, nagu tegime õpilane.py failis
    # see võiks kirjeldada pangakonto olulisi omadusi - kontonumber, bilanss, omanikuNimi
    #klassil võiks olla ka omadus, mis suurendab bilansi omadust mingi arvu võrra
    def __init__(self, nimi, number, bilanss):
        self.omanikuNimi = nimi
        self.kontoNumber = number
        self.kontoSeis = bilanss

    def suurendaBilanssi(self):
        self.kontoSeis  = self.kontoSeis + 500

konto1 = Pangakonto ("Mari", "EE123456789", 200)

print(konto1.omanikuNimi)
print(konto1.kontoNumber)
print(konto1.kontoSeis)
konto1.suurendaBilanssi()
print(konto1.kontoSeis)
