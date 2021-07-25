import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_serba"
)

#Fungsi menampilkan semua data
cursor = db.cursor()
sql = "SELECT * FROM barang"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)