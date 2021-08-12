#Dengan asumsi jumlah ronde merupakan bilangan bulat positif, minta masukan user
ronde = int(input("Masukkan jumlah ronde: "))

#Set skor Tuan Haco dan Tuan Maar 0
skorHaco = int(0)
skorMaar = int(0)


#Ulangi dengan jumlah ronde
for i in range(ronde):
  #minta input gerakan kedua tuan
  #asumsikan input selalu benar, alias antara g atau k atau b
  gerakanHaco = str(input("Masukkan gerakan Tuan Haco ke " + str(i+1) + ": "))
  gerakanMaar = str(input("Masukkan gerakan Tuan Maar ke " + str(i+1) + ": "))
  
  #cek gerakan
  #KAMUS GERAKAN:  ’B’ mengalahkan ’G’, ’G’ mengalahkan ’K’, dan ’K’ mengalahkan ’B’. 
  if gerakanHaco == "B" and gerakanMaar == "G":
    skorHaco += 1
  elif gerakanHaco == "G" and gerakanMaar == "K":
    skorHaco += 1
  elif gerakanHaco == "K" and gerakanMaar == "B":
    skorHaco += 1
  elif gerakanMaar == "B" and gerakanHaco == "G":
    skorMaar += 1
  elif gerakanMaar == "G" and gerakanHaco == "K":
    skorMaar += 1
  elif gerakanMaar == "K" and gerakanHaco == "B":
    skorMaar += 1


#Print pemenangnya berdasarkan skornya.
if skorMaar > skorHaco:
  print("\nPemenangnya adalah Tuan Maar!")
elif skorHaco > skorMaar:
  print("\nPemenangnya adalah Tuan Haco!")
else:
  print("\nTidak ada pemenang, permainan berakhir seri")