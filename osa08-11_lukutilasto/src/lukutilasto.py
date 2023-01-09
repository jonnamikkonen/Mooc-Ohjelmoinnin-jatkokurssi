# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.luvut = []

    def lisaa_luku(self, luku:int):
        self.luvut.append(luku)

    def lukujen_maara(self):
        return len(self.luvut)

    def summa(self):
        return sum(self.luvut)

    def keskiarvo(self):
        if len(self.luvut) > 0:
            return float(sum(self.luvut)/len(self.luvut))

luvut = Lukutilasto()
parilliset = Lukutilasto()
parittomat = Lukutilasto()

print("Anna lukuja: ")
while True:
    luku = int(input())
    if luku == -1:
        break
    if luku % 2 == 0:
        parilliset.lisaa_luku(luku)
    else:
        parittomat.lisaa_luku(luku)
    luvut.lisaa_luku(luku)
        
print(f"Summa: {luvut.summa()}")
print(f"Keskiarvo: {luvut.keskiarvo()}")
print(f"Parillisten summa: {parilliset.summa()}")
print(f"Parittomien summa: {parittomat.summa()}")
    