class Koira:
    luotu_lkm = 0

    def __init__(self, nimi, ikä, ääni="vuh vuh", jalkojen_lkm=4):
        self.ikä = ikä
        self.rotu = "Koira"
        self.nimi = nimi
        self.ääni = ääni
        self.jalkojen_määrä = jalkojen_lkm
        Koira.luotu_lkm = Koira.luotu_lkm + 1

    def hauku(self):
        print(f"Koira {self.nimi} haukkuu: {self.ääni}")
        print(f"Minulla on {self.jalkojen_määrä} jalkaa")

    def hauku_kertaa(self, n):
        for i in range(n):
            self.hauku()

koira = Koira("Musti", 40)
koira2 = Koira("Rekku", 1)
koira3 = Koira("Muro", 1, "vuh", "on jalat")
koira4 = Koira("Piski", 1, "piu piu", 3)
"""
koira.hauku()
koira3.hauku()
koira4.hauku_kertaa(4)
"""
koira2 = koira

print(koira.nimi)

koira2.nimi = "toisen koiran nimi"

print(koira.nimi)

#print(Koira.luotu_lkm)

koira3.rotu = "kissa"

#print(koira.nimi)
#print(koira2.nimi)
