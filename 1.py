from datetime import *

def diffDate(x):
    tgl = x.split('-')
    listTgl = []
    
    for i in tgl:
        listTgl.append(int(i))
    
    tgl1= date(listTgl[0], listTgl[1], listTgl[2])
    tgl2 = datetime.date(datetime.now())
    selisih = tgl1 - tgl2
    hasil = selisih.days
    return hasil
hAkhir = diffDate('2021-1-18')
print('Selisih harinya adalah {} hari'.format(hAkhir))
