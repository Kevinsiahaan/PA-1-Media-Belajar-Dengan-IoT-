s = (input("masukkan karakter yang ingin di convert:\n"))
data = print(' '.join(format(ord(x), 'b') for x in s))