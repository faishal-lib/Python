import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_serba"
)

#Mengubah Data Pegawai Dengan Mencari Nomer Index
cursor = db.cursor()
sql = "UPDATE pegawai SET nama_pegawai=%s, no_hp=%s WHERE id_pegawai=%s"
val = ("Johan", "12345678", "2")
cursor.execute(sql, val)

#Menyimpan Perubahan
db.commit()

print("{} Data Diupdate".format(cursor.rowcount))