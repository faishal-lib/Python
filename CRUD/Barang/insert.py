import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_serba"
)

#Memasukkan data ke tabel yang berada di dalam database
cursor = db.cursor()
sql = "INSERT INTO barang (id_barang, nama_barang, kuantitas, harga_beli, harga_jual) VALUES (%s, %s, %s, %s, %s)"
values = [
    ("", "Kursi Kayu", "50", "75", "100"),
    ("", "Kursi Plastik", "50", "45", "70"),
    ("", "Keramik Marmer", "100", "100", "150")
]

#Meyimpan Perubahan
for val in values:
    cursor.execute(sql,val)
    db.commit()

print("{} Data Telah Ditambahakan Ke Database".format(len(values)))