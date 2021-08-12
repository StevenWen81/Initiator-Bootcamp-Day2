N = int(input('Jumlah hari: '))

daftarBuku = []
daftarHalaman = []

for i in range(N):
    buku, halaman = input('Hari ke-' + str(i+1) + ': ').split(', ')
    halaman = int(halaman)
    
    Found = False
    j = 0
    while (not Found) and (j < len(daftarBuku)):
        if (buku == daftarBuku[j]):
            Found = True
            indexBuku = j
        else:
            j+=1

    if Found:
        daftarHalaman[j] += halaman
    else:
        daftarBuku.append(buku)
        daftarHalaman.append(halaman)

halamanTerbanyak = 0
bukuFavorit = True
for i in range(len(daftarHalaman)):
    if (daftarHalaman[i] > halamanTerbanyak):
        halamanTerbanyak = daftarHalaman[i]
        indexHalamanTerbanyak = i
        bukuFavorit = True
    elif (daftarHalaman[i] == halamanTerbanyak):
        bukuFavorit = False

if bukuFavorit:
    print('Buku favorit:', daftarBuku[indexHalamanTerbanyak])
else:
    print('Buku favorit: tidak ada')
        
                                      

