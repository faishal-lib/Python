import mysql.connector

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_serba"
)

#Memasukkan data ke tabel yang berada di dalam database
cursor = db.cursor()
sql = "INSERT INTO pegawai (id_pegawai, nama_pegawai, no_hp) VALUES (%s, %s, %s)"
values = [
    ("", "Saber", "8990326125"),
    ("", "Dominic", "85157146226"),
    ("", "Brian", "87811652432")
]

#Meyimpan Perubahan
for val in values:
    cursor.execute(sql,val)
    db.commit()

print("{} Data Telah Ditambahakan Ke Database".format(len(values)))