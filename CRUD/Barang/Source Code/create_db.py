import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

#Command untuk membuat database baru
cursor = db.cursor()
cursor.execute("CREATE DATABASE toko_serba")

#Notif apabila berhasil membuat database
print("Database Berhail Dibuat")