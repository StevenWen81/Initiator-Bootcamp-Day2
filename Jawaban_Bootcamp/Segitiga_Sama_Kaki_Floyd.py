#Asumsi input selalu benar
baris = int(input("Masukkan jumlah baris: "))


temp = int(1) 		#inisiasi temp, yaitu angka yang akan diprint untuk membentuk segitiganya

#lakukan looping untuk membuat satu sisi segitiga 
for i in range(1 , ((baris // 2) + 1) if baris % 2 == 0 else ((baris // 2) + 2)):
  for j in range(1, i+1):
    print(temp, end=" ")			#print temp
    temp += 1						#tambahkan temp dengan 1
  print("")					#end line, ganti baris berikutnya

#lakukan looping untuk sisi segitiga satunya lagi
if baris != 1:
  for i in range(baris//2, 0, -1):
    for j in range(1, i+1):
      print(temp, end=" ")
      temp += 1
    print("")