def main():
    print("Program konversi Suhu dari Celcius")
    C = int(input("Masukkan Suhu dalam Celcius: "))
    X = input("konversi e K/R/F: ")
    konversi(C, X)

def konversi(C, X):
    if X.title() == "K":
        K = C + 273
        print("%d Celcius itu %d Kelvin" % (C, K))
    elif X.title() == "R":
        R = (4/5) * C
        print("%d Celcius itu %d Reamur" % (C, R))
    elif X.title() == "F":
        F = ((9/5) * C) + 32
        print("%d Celcius itu %d Fahrenheit" % (C, F))
    else:
        print("ERROR!")
    konfirmasi()

def konfirmasi():
    while True:
        ulang = input("Apakah anda ingin mengulangi?(y/t): ")
        if ulang.title() == "Y":
            main()
        else:
            print('TAMAT')
        break
if __name__ == '__main__':
    main()