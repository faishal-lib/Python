import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_serba"
)

#Memasukkan data ke tabel yang berada dalam database
cursor = db.cursor()
sql = "INSERT INTO penjualan (id_penjualan, id_pegawai, id_barang, kuantitas, harga_satuan, jumlah) VALUES (%s, %s, %s, %s, %s, %s)"
values = [
    ("", "8", "8", "5", "2000", "10000" )
]

#Meyimpan Perubahan
for val in values:
    cursor.execute(sql,val)
    db.commit()

print("{} Data Telah Ditambahakan Ke Database".format(len(values)))