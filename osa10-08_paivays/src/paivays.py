# TEE RATKAISUSI TÄHÄN:
class Paivays(self, paiva: int, kk: int, vuosi: int):
    self.__paiva = paiva
    self.__kk = kk
    self.__vuosi = vuosi

    def __lt__(self, toinen: Paivays):
        return 

if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(28, 12, 1985)
    p3 = Paivays(28, 12, 1985)

    print(p1)
    print(p2)
    print(p1 == p2)
    print(p1 != p2)
    print(p1 == p3)
    print(p1 < p2)
    print(p1 > p2)
