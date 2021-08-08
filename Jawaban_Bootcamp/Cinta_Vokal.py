'''
Soal

Tuan Wes merupakan pecinta huruf vokal (a, e, i, o, dan u).
Akhir-akhir ini  Tuan Wes sedang sibuk membaca artikel. 
Biasanya Tuan Wes tetap menghitung berapa banyak huruf 
vokal yang terdapat dalam artikel yang ia baca. Hari ini 
Tuan Wes sangat sibuk. Akan tetapi, Tuan Wes tetap ingin 
tahu ada berapa banyak huruf vokal yang terdapat dalam 
artikel yang ia baca. Bisakah kamu sebagai seorang programmer 
membantu Tuan Wes untuk membuatkan program yang berfungsi 
untuk menghitung jumlah huruf vokal dalam suatu artikel

(Asumsikan semua huruf pada artikel tidak mengandung huruf kapital) 

Test Case 1:
Masukkan judul artikel: ini adalah artikel 
Jumlah huruf vokal pada artikel adalah: 6 

Test Case 2:
Masukkan judul artikel: bootcamp initator keren abis 
Jumlah huruf vokal pada artikel adalah: 12 

'''

# Algoritma
# ---------

# Terima inputan pengguna berupa judul artikel
artikel = str(input("Masukkan judul artikel: "))

# Deklarasikan variabel yang berfungsi untuk
# menghitung jumlah huruf vokal pada judul artikel
jlh_vokal = 0

# Lakukan looping untuk mengecek tiap karakter dalam judul artikel
for i in artikel:
    # Lakukan pengecekan huruf vokal
    if ( i=='a' or i=='e' or i=='i' or i=='o' or i=='u'): # Syarat huruf vokal
        jlh_vokal += 1
    else: # Bukan huruf vokal
        jlh_vokal += 0
        
# Outputkan hasil jumlah huruf vokal yang diperoleh
print("Jumlah huruf vokal pada artikel adalah: " + str(jlh_vokal))
        