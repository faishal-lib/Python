import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_serba"
)

#Membuat tabel
cursor = db.cursor()
sql = """CREATE TABLE barang (
    id_barang INT(8) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nama_barang VARCHAR(50) NOT NULL,
    kuantitas INT(8) NOT NULL,
    harga_beli INT(8) NOT NULL,
    harga_jual INT(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
cursor.execute(sql)

#Notif apabila sukses membuat tabel
print("Tabel barang berhasil dibuat")
