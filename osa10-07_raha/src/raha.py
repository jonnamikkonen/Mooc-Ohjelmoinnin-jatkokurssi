# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):    
        return f"{self.__eurot}.{self.__sentit:02d} eur"
 
    @property
    def __sentit(self):
        return (self.__eurot * 100) + self.__sentit
 
    def __aseta_arvo(self, sentteja: int):
        self.__eurot = sentteja // 100
        self.__sentit = sentteja - self.__eurot * 100
 
    def __eq__(self, toinen: "Raha"):
        return self.__sentit() == toinen.__sentit()

    def __lt__(self, toinen: "Raha"):
        return self.__sentit() < toinen.__sentit()
 
    def __gt__(self, toinen: "Raha"):
        return self.__sentit() > toinen.__sentit()
 
    def __add__(self, toinen: "Raha"):
        summa = __aseta_arvo(self.__sentit() + toinen.__sentit())
        return summa
 
    def __sub__(self, toinen: "Raha"):
        erotus = self.__sentit() - toinen.__sentit()
        if erotus < 0:
            raise ValueError("Erotuksen tulos on negatiivinen!")
        else:
            return erotus

if __name__ == "__main__":
    e1 = Raha(4, 5)
    e2 = Raha(2, 95)

    raha1 = Raha(15, 95)
    raha2 = Raha(1, 55)

    e3 = e1 + e2
    print(e3)

    e4 = raha1 + raha1
    print(e4)


    e5 = raha1-raha2
    print(e5)
