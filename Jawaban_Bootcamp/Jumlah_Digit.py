'''
Soal

Hitunglah jumlah digit dari sebuah angka misalkan N

(Asumsikan N bernilai positif)

Test Case 1:
Masukkan nilai N: 165
Jumlah digit angka tersebut adalah 12

Test Case 2:
Masukkan nilai N: 2021
Jumlah digit angka tersebut adalah 5

'''

# Algoritma
# ---------

# Terima angka dari pengguna
N = int(input("Masukkan nilai N: "))

# Deklarasi variabel untuk membantu penghitungan
helper = 0

# Deklarasi variabel untuk menyimpan jumlah digit
sum_dgt = 0

# Lakukan looping untuk mengecek angka satu per satu
while ( N>0 ):
    helper = N % 10 # Ambil digit terakhir
    sum_dgt += helper
    N //= 10 # Hilangkan digit terakhir
    
print("Jumlah digit angka tersebut adalah " + str(sum_dgt))

'''
Ilustrasi
Input => 19
19 % 10 => 9
19 // 10 = 1
'''
