M = int(input('Jumlah garis: '))

listGaris = [] 
for i in range(M):
    x1,y1,x2,y2 = input('Garis ke-' + str(i+1) + ': ').split(',')
    x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
    m = (y2-y1)/(x2-x1)
    c = y1 - m*x1
    listGaris.append((m,c))

print()

N = int(input('Jumlah titik uji: '))

onLineCount = 0
for i in range(N):
    x,y = input('Titik ke-' + str(i+1) + ': ').split(',')
    x,y = int(x), int(y)

    onLine = False
    k = 0
    while (not onLine) and (k < M):
        m,c = listGaris[k][0], listGaris[k][1]
        if (y == m*x + c):
            onLine = True
            onLineCount += 1
        else:
            k += 1

print()

print('Jumlah titik uji yang berada pada garis:', onLineCount)
