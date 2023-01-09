# TEE RATKAISUSI TÄHÄN:
def alkuluvut():
    luku = 2
    while True:
        if luku %luku == 0:
            yield luku
        luku +=1

if __name__ == "__main__":
    luvut = alkuluvut()
    for i in range(8):
        print(next(luvut))