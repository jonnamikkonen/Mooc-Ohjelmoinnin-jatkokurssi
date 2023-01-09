# TEE RATKAISUSI TÄHÄN:
def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    with open(tiedoston_nimi) as tiedosto:
        tiedosto.read()
        return {sana: tiedoston_nimi.count(sana) for sana in tiedoston_nimi if tiedoston_nimi.count(sana) >= raja}

if __name__ == "__main__":
    print(yleisimmat_sanat("comprehensions.txt", 3))