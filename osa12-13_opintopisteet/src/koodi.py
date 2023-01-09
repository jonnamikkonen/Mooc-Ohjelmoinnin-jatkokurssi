from functools import reduce

class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"

# Tee ratkaisusi tähän:
from functools import reduce

def kaikkien_opintopisteiden_summa(suoritukset: list):
    return reduce(lambda opintopisteet, kurssi: opintopisteet + kurssi.opintopisteet, suoritukset, 0)

def hyvaksyttyjen_opintopisteiden_summa(suoritukset: list):
    hyvaksytyt = filter(lambda x: x.arvosana >= 1, suoritukset)
    return reduce(lambda opintopisteet, hyvaksytyt: opintopisteet + hyvaksytyt.opintopisteet, hyvaksytyt, 0)

def keskiarvo(suoritukset: list):
    hyvaksytyt = list(filter(lambda x: x.arvosana >= 1, suoritukset))
    return reduce(lambda arvosana, hyvaksytyt: arvosana + hyvaksytyt.arvosana, hyvaksytyt, 0)/len(hyvaksytyt)

if __name__ == "__main__":
    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = keskiarvo([s1, s2, s3])
    print(summa)