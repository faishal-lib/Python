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
    nama_barang = input("Masukkan Nama Barang : ")
    kuantitas = input("Masukkan Kuantitas : ")
    harga_beli = input("Masukkan Harga Beli : ")
    harga_jual = input("Masukkan Harga Jual : ")
    val = (nama_barang, kuantitas, harga_beli, harga_jual)
    cursor = db.cursor()
    sql = "INSERT INTO barang (nama_barang, kuantitas, harga_beli, harga_jual) VALUES (%s, %s, %s, %s )"
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil Ditambahkan".format(cursor.rowcount))

#Fungsi Show Data
def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM barang"
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
    id_barang = input("Pilih ID Barang : ")
    nama_barang = input("Masukkan Nama Barang Baru : ")
    kuantitas = input("Masukkan Kuantitas Baru : ")
    harga_beli = input("Masukkan Harga Beli Baru : ")
    harga_jual = input("Masukkan Harga Jual Baru : ")

    sql = "UPDATE barang SET nama_barang=%s, kuantitas=%s, harga_beli=%s, harga_jual=%s WHERE id_barang=%s"
    val = (nama_barang, kuantitas, harga_beli, harga_jual, id_barang)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil Diperbarui".format(cursor.rowcount))

#Fungsi Hapus Data
def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    id_barang = input("Pilih ID Barang : ")
    sql = "DELETE FROM barang WHERE id_barang=%s"
    val = (id_barang,)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil Dihapus".format(cursor.rowcount))

#Fungsi Menampilkan Menu
def show_menu(db):
    print("")
    print("=== APLIKASI CRUDS PYTHON ===")
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

#Menampilka menu pada saat program dijalankan
if __name__ == "__main__":
    while(True):
        show_menu(db)