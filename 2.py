from datetime import*
kode = input('Masukkan Kode Member : ')
nama = input('Masukkan Nama Member : ')
buku = input('Masukkan Judul Buku  : ')
x = datetime.date(datetime.now())
y = x + timedelta(days=7)
print('')

teks = "{}|{}|{}|{}|{}\n".format(kode, nama, buku, x, y)
data = open('d:\Peminjaman Buku.txt', 'w')
data.write(teks)
data.close()
tanya = input("Ulangi input lagi (y/n)? ")
print('')

while tanya == 'y' :
    kode2 = input('Masukkan Kode Member : ')
    nama2 = input('Masukkan Nama Member : ')
    buku2 = input('Masukkan Judul Buku  : ')
    x2 = datetime.date(datetime.now())
    y2 = x2 + timedelta(days=7)
    print('')

    teks2 = "{}|{}|{}|{}|{}\n".format(kode2, nama2, buku2, x2, y2)
    data2 = open('d:\Peminjaman Buku.txt', 'a')
    data2.write(teks2)
    data2.close()
    tanya = input("Ulangi input lagi (y/n)? ")
    print('')
    if tanya == 'n':
        break
