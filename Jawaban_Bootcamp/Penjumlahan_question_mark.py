angka = int(input("Masukkan jumlah angka: ")) 		#asumsi input selalu valid

hasil = int(0)										#set hasil penjumlahan sebagai 0


#lakukan looping sebanyak jumlah angka
for i in range(angka):
  inputTemp = int(input("Masukkan angka ke-" + str(i+1) + ": "))		#minta input dari user untuk "dijumlahkan", asumsi selalu valid
  if inputTemp % 2 == 0:												#bila genap
    hasil += inputTemp														#tambahkan
  else:																	#tapi bila ganjil
    hasil -= inputTemp														#kurangkan
print("Hasil 'penjumlahan' adalah " + str(hasil))						#print hasilnya