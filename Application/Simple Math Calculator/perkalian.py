print ("Simple Math Calculator (X)" +"\n")

bil1 = input("Input Bilangan 1 : ")
bil2 = input("Input Bilangan 2 : ")

# Integer (int) perlu dideklarasikan khusus operasi aritmatika input
hasil = (int(bil1)* int(bil2))

# String (str) perlu didkelarasikan supaya tidak error ketika melakukan print 2 tipe data yg berbeda (int dan str)
# Error yg terjadi : TypeError: 'str' object is not callable
print ("Hasil Perkalian : " +str(hasil))