# TEE RATKAISUSI TÄHÄN:
class Lottorivi:
    def __init__(self, kierroksen_numero: int, lista: list):
        self.kierroksen_numero = kierroksen_numero
        self.lista = lista

    def osumien_maara(self, pelattu_rivi: list):
        return len([luku for luku in self.lista if luku in pelattu_rivi])
    
    def osumat_paikoillaan(self, pelattu_rivi):
        return[luku if luku in self.lista else -1 for luku in pelattu_rivi]

if __name__ == "__main__":
    oikea = Lottorivi(8, [1,2,3,10,20,30,33])
    oma_rivi = [1,4,7,10,11,20,30]

    print(oikea.osumat_paikoillaan(oma_rivi))