'''
Soal

Pada saat istirahat, Tuan Wes merasa sangat bosan
sehingga ia pun mengambil 3 pensil dengan panjang
a, b dan c. Tuan Wes pun mencoba membentuk segitiga
dengan 3 pensil tersebut. Akan tetapi, ia tidak tau
kenapa terkadang 3 pensil tersebut tidak dapat 
membentuk segitiga.

Oleh karena itu, Anda diminta untuk membuat
sebuah program yang dapat menentukan dengan pasti
apakah 3 pensil tersebut dapat membentuk segitiga
atau tidak.

Test Case 1:
Masukkan panjang pensil a: 1
Masukkan panjang pensil b: 2
Masukkan panjang pensil c: 3
Ketiga pensil tersebut tidak dapat membentuk segitiga.

Test Case 2:
Masukkan panjang pensil a: 3
Masukkan panjang pensil b: 4
Masukkan panjang pensil c: 5
Ketiga pensil tersebut dapat membentuk segitiga.

'''

# Algoritma
# ---------

# Terima input 3 buah pensil
a = int(input("Masukkan panjang pensil a: "))
b = int(input("Masukkan panjang pensil b: "))
c = int(input("Masukkan panjang pensil c: "))

# Cek syarat pembentuk segitiga
if (a+b>c and a+c>b and b+c>a):
    print("Ketiga pensil tersebut dapat membentuk segitiga.")
else: # Apabila syarat tidak dipenuhi
    print("Ketiga pensil tersebut tidak dapat membentuk segitiga.")
