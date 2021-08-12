'''
Tuan Bas sedang melihat sepupunya, Haru, belajar sistem koordinat kartesian. 
Setelah itu, Tuan Bas mempunyai ide untuk membantu Haru dalam belajar memahami 
sistem koordinat kartesian yang terbagi menjadi 4 kuadran, 2 sumbu, dan sebuah titik pusat. 
Bantulah Tuan Bas dalam membuat program untuk membantu Haru!

Program menerima input koordinat sebuah titik (x,y) kemudian memberikan output letak titik tersebut
•	Jika x dan y bernilai 0, titik terletak pada titik pusat.
•	Jika x bernilai 0, titik terletak pada sumbu-y.
•	Jika y bernilai 0, titik terletak pada sumbu-x.
•	Jika x dan y bernilai bukan 0, tentukan kuadrannya! 

Input :
Baris pertama berisi nilai x
Baris kedua berisi nilai y

Output :
Letak titik tersebut
'''

# Input koordinat titik
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

# Periksa apakah titik berada di titik pusat
if (x == 0 and y == 0):
    print("(" + str(x) + "," + str(y) + ") ada di titik pusat.")

# Periksa apakah titik berada di sumbu-y
elif (x == 0):
    print("(" + str(x) + "," + str(y) + ") ada di sumbu-y.")

# Periksa apakah titik berada di sumbu-x
elif (y == 0):
    print("(" + str(x) + "," + str(y) + ") ada di sumbu-x.")

# Periksa apakah titik berada di kuadran 1
elif (y > 0 and x > 0):
    print("(" + str(x) + "," + str(y) + ") ada di kuadran 1.")

# Periksa apakah titik berada di kuadran 2
elif (y > 0 and x < 0):
    print("(" + str(x) + "," + str(y) + ") ada di kuadran 2.")

# Periksa apakah titik berada di kuadran 3
elif (y < 0 and x < 0):
    print("(" + str(x) + "," + str(y) + ") ada di kuadran 3.")

# Periksa apakah titik berada di kuadran 4
elif (y < 0 and x > 0):
    print("(" + str(x) + "," + str(y) + ") ada di kuadran 4.")

# elif yang terakhir dapat diganti menjadi else saja

# Perhatikan urutan conditional!
# Bisa pake urutan lain kok asal kondisinya sesuai sama urutannya