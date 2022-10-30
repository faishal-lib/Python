print ("Simple Math Calculator (+)" +"\n")

bil1 = input("Input Bilangan 1 : ")
bil2 = input("Input Bilangan 2 : ")

# Integer (int) perlu dideklarasikan khusus operasi aritmatika input
# Jika tidak, Input sebelumnya hanya akan digabungkan (tidak dijumlahkan)
# Misal : 6+6 = 66 bukan 12
hasil = (int(bil1)+ int(bil2))

# String (str) perlu didkelarasikan supaya tidak error ketika melakukan print
# Error yg terjadi : TypeError: 'str' object is not callable
print ("Hasil Penjumlahan : " +str(hasil))