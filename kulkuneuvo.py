class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus


class Urheiluväline:
    def __init__(self, paino):
        self.paino = paino


class Polkupyörä(Urheiluväline, Kulkuneuvo):
    def __init__(self, nopeus, paino, vaihteet):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluväline.__init__(self, paino)
        self.vaihteet = vaihteet

    def kulje(self):
        print("Mennään lujaa")


pp = Polkupyörä(45, 18.7, 3)
print(pp.vaihteet)
print(pp.nopeus)
print(pp.paino)
pp.kulje()