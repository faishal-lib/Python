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
sql = """CREATE TABLE pegawai (
    id_pegawai INT(8) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nama_pegawai VARCHAR(30) NOT NULL,
    no_hp INT(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;    
"""
cursor.execute(sql)

#Notif apabila sukses membuat tabel
print("Tabel Pegawai berhasil dibuat")
