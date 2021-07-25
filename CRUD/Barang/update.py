import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_serba"
)

cursor = db.cursor()
sql = "UPDATE barang SET kuantitas=%s, harga_beli=%s WHERE id_barang=%s"
val = ("15", "140", "5")
cursor.execute(sql, val)

db.commit()

print("{} Data Diupdate".format(cursor.rowcount))