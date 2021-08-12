'''
Suatu hari, Tuan Bas bersama Tuan Tian mengunjungi sebuah taman kanak-kanak (TK).
Di sana, mereka akan membagikan biskuit yang dibawa dari rumah masing-masing. 
Tentukan apakah setiap anak di sana mendapat jumlah biskuit yang sama.

Input : 
Baris pertama berisi biskuit dari Tuan Bas
Baris kedua berisi biskuit dari Tuan Tian
Baris ketiga berisi jumlah anak di TK tersebut
(asumsi semua input selalu valid)

Output :
Pernyataan apakah setiap anak mendapat biskuit yang sama
'''

# Input jumlah biskuit dan jumlah anak
biskuit_tuan_bas = int(input("Jumlah biskuit dari Tuan Bas : "))
biskuit_tuan_tian = int(input("Jumlah biskuit dari Tuan Tian : "))
jumlah_anak = int(input("Jumlah anak di TK : "))

# Jumlahkan biskuit Tuan Bas dengan Biskuit Tuan Tian
jumlah_biskuit = biskuit_tuan_bas + biskuit_tuan_tian

# Periksa apakah jumlah biskuit dapat dibagi habis oleh jumlah anak
if (jumlah_biskuit % jumlah_anak == 0):
    print("Setiap anak akan mendapat biskuit dengan jumlah sama.")
else :
    print("Setiap anak tidak akan mendapat biskuit dengan jumlah sama.")

