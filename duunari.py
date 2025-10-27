class Työntekijä:

    def __init__(self, etunimi, sukunimi):
        self.nimi = etunimi
        self.sukunimi = sukunimi
        self.palkka = 0

    def tee_töitä(self):
        while True:
            print("Teen iloisesti töitä")

    def get_tiedot(self):
        return f"Nimi: {self.nimi} {self.sukunimi}"

    def tulosta_tiedot(self):
        print(self.get_tiedot())

class Tuntityöntekijä(Työntekijä):

    def __init__(self, etunimi, sukunimi, palkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = palkka

    def mene_kahvitauolle(self):
        self.kahvitauko = True

    def pois_kahvitauolta(self):
        self.kahvitauko = False

    def get_tiedot(self):
        return f"{super().get_tiedot()}, Tuntipalkka {self.tuntipalkka}"

class Toimari(Työntekijä):

    def __init__(self, palkka):
        self.palkka = palkka * 25
        #super().__init__("Santeri")
        self.nimi = "Nimi"

    def tee_töitä(self):
        print("Päivän työt tehty")


# Alla oleva koodi on pääohjelmaa, ylläolevat on luokkamäärityksiä

duunari = Tuntityöntekijä("Juha", "Sukunimi", 20)
duunari.tulosta_tiedot()
duunari.mene_kahvitauolle()
print(f"{duunari.nimi} on kahvitauolla: {duunari.kahvitauko}")
#print("Nimi")
#print(duunari.nimi)
#print("Name")
#print(duunari.name)

#duunari.tee_töitä()

employee = Työntekijä("Aino", "Sukunimi")
employee.tulosta_tiedot()
#print(employee.nimi)
#print(employee.name)

toimari = Toimari(10000)
toimari.tee_töitä()
print(f"Toimarin nimi {toimari.nimi}")
print(f"Toimarin palkka {toimari.palkka}")

toimari2 = Toimari(1000)
print(f"Toimarin nimi {toimari2.nimi}")
print(f"Toimarin palkka {toimari2.palkka}")

toimari3 = Toimari(100)
print(f"Toimarin nimi {toimari3.nimi}")
print(f"Toimarin palkka {toimari3.palkka}")


class Elevator:

    def __init__(self, alin, ylin):
        self.bottom_floor = alin
        self.top_floor = ylin
        self.current_floor = alin

    def floor_up(self):
        self.current_floor = self.current_floor + 1

    def floor_down(self):
        self.current_floor = self.current_floor - 1

    def go_to_floor(self, kerros):
        while True:
            if self.current_floor == kerros:
                break

            if self.current_floor > kerros:
                self.floor_down()
            if self.current_floor < kerros:
                self.floor_up()