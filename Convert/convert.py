s = (input("masukkan data yang ingin di convert menjadi biner:\n"))
hasil = (' '.join(format(ord(x), 'b') for x in s))
print("hasil dari convert" ,hasil)%