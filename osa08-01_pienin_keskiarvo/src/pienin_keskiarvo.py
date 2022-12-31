# tee ratkaisu tänne
def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    hlo1 = (henkilo1["tulos1"] + henkilo1["tulos2"] + henkilo1["tulos3"]) / 3
    hlo2 = (henkilo2["tulos1"] + henkilo2["tulos2"] + henkilo2["tulos3"]) / 3
    hlo3 = (henkilo3["tulos1"] + henkilo3["tulos2"] + henkilo3["tulos3"]) / 3

    if hlo1 < hlo2 and hlo1 < hlo3:
        return henkilo1
    if hlo2 < hlo1 and hlo2 < hlo3:
        return henkilo2
    if hlo3 < hlo1 and hlo3 < hlo2:
        return henkilo3


if __name__ == "__main__":
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))