# TEE RATKAISUSI TÄHÄN:
class ListaApuri:

    @classmethod
    def suurin_frekvenssi(cls, lista:list):
        return max(set(lista), key=lista.count)

    @classmethod
    def tuplia(cls, lista: list):
        lista1 = set(lista)
        laskuri = 0
        for alkio in lista1:
            if lista.count(alkio) >= 2:
                laskuri += 1
        return laskuri


if __name__ == "__main__":
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))