'''
Tuan Bas adalah orang yang unik. Dia selalu menyesuaikan warna bajunya dengan tanggal.
Jika hari ini tanggalnya lebih dari 10, dia akan menggunakan baju dengan warna sesuai 
dengan ganjil genapnya tanggal.

Jika tanggal > 10 dan tanggal bernilai ganjil, maka Tuan Bas akan menggunakan baju berwarna biru. 
Jika tanggal > 10 dan tanggal bernilai genap, maka Tuan Bas akan menggunakan baju berwarna merah. 
Jika tanggal <= 10, maka Tuan Bas akan menggunakan baju berwarna hijau.

Buatlah program untuk membantu Tuan Bas dalam memilih baju tiap harinya!

Input : Tanggal hari ini (Asumsi Tuan Bas menggunakan program ini pada bulan Januari, 
tanggal bernilai 1 sampai 31).

Output : Warna baju yang akan dipakai oleh Tuan Bas pada hari ini. 
Jika tanggal < 1 atau tanggal >31, berikan output “Tanggal tidak valid”
'''

# Input tanggal
tanggal = int(input("Masukkan tanggal : "))

# Periksa apakah tanggal valid di bulan Januari
if (tanggal < 1 or tanggal > 31):
    print("Tanggal tidak valid.")

# Periksa apakah tanggal kurang dari sama dengan 10
elif (tanggal <= 10):
    print("Pada hari ini, Tuan Bas akan memakai baju berwarna hijau.")

# Periksa apakah tanggal genap
elif (tanggal % 2 == 0):
    print("Pada hari ini, Tuan Bas akan memakai baju berwarna merah.")

# Sisanya adalah 1 <= tanggal <= 31, tanggal ganjil
else :
    print("Pada hari ini, Tuan Bas akan memakai baju berwarna biru.")


# Perhatikan urutan conditional!
# Bisa pake urutan lain kok asal kondisinya sesuai sama urutannya