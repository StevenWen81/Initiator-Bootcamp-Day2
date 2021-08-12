'''
Tuan Bas bekerja di perusahaan ShiroKuro. Perusahaan tersebut memiliki 
jam kerja yang berbeda setiap harinya seperti pada tabel berikut

Hari	Jam Kerja
Senin	08.00-13.00
Selasa	08.00-13.00
Rabu	08.00-13.00
Kamis	10.00-17.00
Jumat	08.00-11.00
Sabtu	Libur
Minggu	Libur

Buatlah program yang membantu Tuan Bas dalam memberi tahu waktu kerjanya setiap hari.

Input : Nama hari (tanpa spasi dan huruf pertama selalu kapital). 
Output : Waktu kerja Tuan Bas. Jika input tidak valid, program tidak menampilkan apa-apa
'''

# Input hari
hari = input("Masukkan hari : ")

# Cek hari
if (hari == "Senin" or hari == "Selasa" or hari == "Rabu"):
    print("Pada hari ini, Tuan Bas akan bekerja pada jam 08.00-11.00.")
elif (hari == "Kamis"):
    print("Pada hari ini, Tuan Bas akan bekerja pada jam 10.00-17.00.")
elif (hari == "Jumat"):
    print("Pada hari ini, Tuan Bas akan bekerja pada jam 08.00-11.00.")
elif (hari == "Sabtu" or hari == "Minggu") :
    print("Pada hari ini, Tuan Bas libur")