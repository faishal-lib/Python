import mysql.connector
import os

#Konfigurasi letak host, username dan password database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_serba"
)

#Fungsi Insert Data
def insert_data(db):
    nama_pegawai = input("Masukkan Nama Pegawai : ")
    no_hp = input("Masukkan No HP : ")

    val = (nama_pegawai, no_hp)
    cursor = db.cursor()
    sql = "INSERT INTO pegawai (nama_pegawai, no_hp) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil Ditambahkan".format(cursor.rowcount))

#Fungsi Show Data
def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM pegawai"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak Ada Data")
    else:
        for data in results:
            print(data)


#Fungsi Memperbarui Data
def update_data(db):
    cursor = db.cursor()
    show_data(db)
    id_pegawai = input("Pilih ID Pegawai : ")
    nama_pegawai = input("Masukkan Nama Pegawai Baru : ")
    no_hp = input("Masukkan No HP Baru : ")

    sql = "UPDATE pegawai SET nama_pegawai=%s, no_hp=%s WHERE id_pegawai=%s"
    val = (nama_pegawai, no_hp, id_pegawai)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil Diperbarui".format(cursor.rowcount))

#Fungsi Hapus Data
def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    id_pegawai = input("Pilih ID Pegawai : ")
    sql = "DELETE FROM pegawai WHERE id_pegawai=%s"
    val = (id_pegawai,)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil Dihapus".format(cursor.rowcount))

#Fungsi Menampilkan Menu
def show_menu(db):
    print("")
    print("=== APLIKASI CRUD PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih Menu : ")

    #clear screen
    os.system('cls')
        
    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu Tidak Ditemukan!")

#Menampilkan menu pada saat program dijalankan
if __name__ == "__main__":
    while(True):
        show_menu(db)