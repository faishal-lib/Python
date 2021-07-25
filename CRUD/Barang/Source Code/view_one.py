import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_serba"
)

#Fungsi menampilkan 1 Data (Sebagai contoh menampilkan 1 data pertama)
cursor = db.cursor()
sql = "SELECT * FROM barang"
cursor.execute(sql)

result = cursor.fetchone()

print(result)