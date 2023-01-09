# Tee ratkaisusi tähän:
class Sarja:
    def __init__(self, nimi: str, kaudet: int, genre: list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genre = genre
        self.arvostelu = []

    def __str__(self):
        genret = ", ".join(self.genre)
        if self.arvostelu:
            return f"{self.nimi} ({self.kaudet} esityskautta) \ngenret: {genret} \narvosteluja {len(self.arvostelu)}, keskiarvo {sum(self.arvostelu)/len(self.arvostelu):.1f} pistettä"
        
        return f"{self.nimi} ({self.kaudet} esityskautta) \ngenret: {genret} \nei arvosteluja"
    
    def arvostele(self, arvosana: int):
        if arvosana >= 0:
            self.arvostelu.append(arvosana)

    def keskiarvo(self):
        return sum(self.arvostelu) / len(self.arvostelu)
    
def arvosana_vahintaan(arvosana: float, sarjat: list):
    lista = []
    for sarja in sarjat:
        if arvosana <= sarja.keskiarvo():
            lista.append(sarja)
    return lista

def sisaltaa_genren(genre: str, sarjat: list):
    lista = []
    for sarja in sarjat:
        if genre in sarja.genre:
            lista.append(sarja)
    return lista

if __name__ == "__main__":
    dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)
