angka1 = int(input("Masukkan Angka Pertama : "))
angka2 = int(input("Masukkan Angka Kedua : "))
print("Operator : \n1.Penjumlahan \n2.Pengurangan\n"
        "3.Perkalian \n4. Pembagian")
pilih = int(input("Masukkan Operator : "))
if pilih == 1:
    tambah = angka1+angka2
    print("Hasilnya Ini Nih ",tambah)
elif pilih == 2:
    kurang = angka1-angka2
    print("Hasilnya Ini Nih ", kurang)
elif pilih == 3:
    kali = angka1*angka2
    print("Hasilnya Ini Nih ", kali)
elif pilih == 4:
    bagi = angka1/angka2
    print("Hasilnya Ini Nih ", bagi)
else:
    print("Operator yang anda masukkan tidak ada disini mwehehehehe")                   








































