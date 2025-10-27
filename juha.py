


class Elukka:
    def __init__(self):
        self.jalat = 4
        self.dna = "ATGCAACAGCATTTGAA"
        self.tee_tietokantahaku()

    def tee_tietokantahaku(self):
        # ... mysql haku
        return [(1, "tulos"), (2, "nimi")]


class Ihminen(Elukka):
    def __init__(self):
        super().__init__()
        self.jalat = 2
        self.peukalot = True

    def tee_tietokantahaku(self):
        # Jos halutaan perittyä tee_tietokantahaku() metodia kutsua myös
        data = super().tee_tietokantahaku()

        for item in data:
            # haet item['id'] perusteella toisesta taulusta
            break # break vain esimerkin vuoksi tässä
        return True

class Henkilö(Ihminen):
    def __init__(self, nimi):
        super().__init__()
        self.nimi = nimi

    def set_eksistentiaalinen_kriisi(self, kriisi):
        self.eksistentiaalinen_kriisi = kriisi

    def mene_töihin(self):
        self.töissä = True

    def tulosta_tiedot(self):
        print(self.jalat)
        print(self.dna)
        print(self.peukalot)
        print(self.nimi)
        print(self.eksistentiaalinen_kriisi)

juha = Henkilö("Juha")
juha.set_eksistentiaalinen_kriisi(True)
juha.tulosta_tiedot()
