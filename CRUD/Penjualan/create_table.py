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
sql = """CREATE TABLE pembelian (
    id_pembelian INT(8) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    id_pegawai INT(8) NOT NULL,
    id_barang INT(8) NOT NULL,
    waktu timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
    kuantitas INT(11) NOT NULL,
    harga_satuan INT(11) NOT NULL,
    jumlah INT(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;    
"""
cursor.execute(sql)

#Notif apabila sukses membuat tabel
print("Tabel Penjualan berhasil dibuat")
