import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_serba"
)

#Mengubah Data pembelian Dengan Mencari Nomer Index
cursor = db.cursor()
sql = "UPDATE pembelian SET id_pegawai=%s, id_barang=%s, kuantitas=%s, harga_satuan=%s, jumlah=%s WHERE id_pembelian=%s"
val = ("4", "1", "2" , "200000", "400000", "1")
cursor.execute(sql, val)

#Menyimpan Perubahan
db.commit()

print("{} Data Diupdate".format(cursor.rowcount))