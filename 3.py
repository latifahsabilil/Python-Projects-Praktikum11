from datetime import*

def diffDate(x):
    tgl = x.split('-')
    listTgl = []

    for i in tgl:
        listTgl.append(int(i))

    tgl1 = date(listTgl[0], listTgl[1], listTgl[2])
    tgl2 = datetime.date(datetime.now())

    a = tgl1 - tgl2
    b = a.days
    return b

myFile = open('d:\Peminjaman buku.txt', 'r')
file = myFile.readlines()

mKode = input('Masukan Kode Member    : ' )
print('')

for i in range(len(file)):
    if(mKode in file[i]):
        data = file[i].split('|')
        status = 'ada'
        break
    else:
        status = 'tidak ada'
        continue

if(status == 'ada'):
    terlambat = diffDate(data[4])
    denda = 2000*abs(terlambat)
    hrIni = datetime.date(datetime.today())
    print('Data Peminjaman Buku')
    print('Kode Member            : ' , data[0])
    print('Nama Member            : ' , data[1])
    print('Judul Buku             : ' , data[2])
    print('Tanggal Mulai Pinjam   : ', data[3])
    print('Tanggal Maks Peminjaman: ', data[4], end ='')
    print('Tanggal Pengembalian   : ', hrIni)
    if(terlambat >= 0):
        print('Terlambat              :  0 hari')
        print('Denda                  :  Rp 0')
    else:
        print('Terlambat              :  ', abs(terlambat))
        print('Denda                  :  Rp', denda)
else:
    print('Data tidak di temukan')
