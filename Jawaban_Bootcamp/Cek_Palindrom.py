'''
Soal

Tuan Wes sedang membaca KBBI dan melihat ada beberapa
kata yang bersifat palindrom, yaitu kata yang sama
apabila dibaca dari depan maupun dari belakang.

Namun, karena Tuan Wes telah membaca KBBI dalam waktu
yang lama, ia mulai malas untuk membaca kata yang ia 
temui dari belakang. Oleh karena itu, bantulah Tuan Wes
untuk membuat program yang mengecek apakah sebuah kata 
merupakan sebuah kata palindrom atau bukan.

Test Case 1: 
Masukkan kata: rotator 
Kata tersebut merupakan kata palindrom. 

Test Case 2: 
Masukkan kata: bootcamp 
Kata tersebut bukan kata palindrom. 
'''

# Algoritma
# ---------

# Terima Masukkan Pengguna
kata = str(input("Masukkan kata: "))

# Deklarasikan variabel yang akan digunakan 
#untuk melakukan pengecekan palindrom
check = ""

# Lakukan pembalikan kata
for i in kata:
    check = i + check
    
# Lakukan pengecekan untuk mengecek apabila
# kata yang diinput sama apabila dibaca dari
# depan maupun dibaca dari belakang
if (kata == check):
    print("Kata tersebut merupakan kata palindrom.")
else:
    print("Kata tersebut bukan kata palindrom.")
