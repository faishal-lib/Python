import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_serba"
)

#Fungsi menampilkan beberapa data (Sebagai contoh Menampilkan 4 Data)
cursor = db.cursor()
sql = "SELECT * FROM barang"
cursor.execute(sql)

results = cursor.fetchmany(4)

for data in results:
  print(data)