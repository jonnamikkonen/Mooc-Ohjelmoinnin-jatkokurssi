# TEE RATKAISUSI TÄHÄN:
class Auto:
    def __init__(self):
        self.__sisalto = 0
        self.__km = 0

    def tankkaa(self):
        self.__sisalto = 60

    def aja(self, km: int):
        if km > self.__sisalto:
            km = self.__sisalto
        self.__km += km
        self.__sisalto -= km

    def __str__(self):
        return f"Auto: ajettu {self.__km} km, bensaa {self.__sisalto} litraa"

if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)