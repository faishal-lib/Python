import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

#Notif apabila berhasil terkoneksi
if db.is_connected():
    print("Berhasil Terkoneksi ke Database")