import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_serba"
)

#Fungsi Hapus Data (Sebagai contoh menghapus data yang memiliki ID 3)
cursor = db.cursor()
sql = "DELETE FROM pegawai WHERE id_pegawai=%s"
val = ("2",)
cursor.execute(sql, val)

db.commit()

print("{} Data Dihapus".format(cursor.rowcount))