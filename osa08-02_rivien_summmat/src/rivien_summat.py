# tee ratkaisu tänne
def rivien_summat(matriisi: list):
    summa = matriisi
    i = 0
    for rivi in matriisi:
        rivi.append(sum(rivi))
        summa[i] = rivi
        i += 1
   
    
if __name__ == "__main__":
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)