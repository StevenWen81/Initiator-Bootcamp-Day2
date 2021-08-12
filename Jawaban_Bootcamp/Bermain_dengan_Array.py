N = int(input('Panjang list = '))

listElemen = [0 for i in range(N)]

for i in range(N):
    listElemen[i] = int(input('Elemen ke-' + str(i+1) + ' = '))


listSetelahPerkalian = [0 for i in range((N+1)//2)]

for i in range(N//2):
    listSetelahPerkalian[i] = listElemen[-(2*i+1)] * listElemen[-(2*i+2)]

if (N % 2 == 1):
    listSetelahPerkalian[-1] = listElemen[0]


hasilOperasi = 0

for i in range(len(listSetelahPerkalian)):
    if (i % 2 == 0):
        hasilOperasi += listSetelahPerkalian[i]
    else:
        hasilOperasi -= listSetelahPerkalian[i]

print('Hasil operasi =', hasilOperasi)


