#Asumsikan input pangkat benar
#Minta input user
bilangan = float(input("Masukkan bilangan yang ingin dipangkatkan: "))
pangkat = int(input("Masukkan pangkatnya: "))

hasil = float(1)
for i in range(pangkat):
  hasil *= bilangan

print(hasil)