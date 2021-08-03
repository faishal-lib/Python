import mysql.connector
import os


#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_serba"
)

#clear screen
os.system('cls')

#Fungsi menampilkan semua data
print("")
print("======================= Data Barang =======================")
print("")
print("Waktu - Kuantitas Jual - Harga Jual - ID Barang -  Nama Barang - Kuantitas - Harga Beli - Harga Jual - ID Pegawai - Nama Pegawai - No HP ")
cursor = db.cursor()
sql = "SELECT penjualan.date, penjualan.kuantitas, penjualan.id_barang, barang.nama_barang, barang.kuantitas, barang.harga_beli, barang.harga_jual, pegawai.id_pegawai, pegawai.nama_pegawai, pegawai.no_hp FROM penjualan INNER JOIN pegawai ON penjualan.id_pegawai = pegawai.id_pegawai INNER JOIN barang ON penjualan.id_barang = barang.id_barang"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)
