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
    id_pegawai = input("Masukkan ID Pegawai : ")
    id_barang = input("Masukkan ID Barang : ")
    kuantitas = input("Masukkan Kuantitas : ")
    harga_satuan = input("Masukkan Harga Satuan : ")
    jumlah = input("Masukkan Jumlah : ")

    val = (id_pegawai, id_barang, kuantitas, harga_satuan, jumlah)
    cursor = db.cursor()
    sql = "INSERT INTO pembelian (id_pegawai, id_barang, kuantitas, harga_satuan, jumlah) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil Ditambahkan".format(cursor.rowcount))

#Fungsi Show Data
def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM pembelian"
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
    id_pembelian = input("Pilih ID Pembelian : ")
    id_pegawai = input("Masukkan ID Pegawai Baru : ")
    id_barang = input("Masukkan ID Barang Baru : ")
    kuantitas = input("Masukkan Kuantitas Baru : ")
    harga_satuan = input("Masukkan Harga Satuan Baru : ")
    jumlah = input("Masukkan Jumlah Baru : ")

    sql = "UPDATE pembelian SET id_pegawai=%s, id_barang=%s, kuantitas=%s, harga_satuan=%s, jumlah=%s WHERE id_pembelian=%s"
    val = (id_pegawai, id_barang, kuantitas, harga_satuan, jumlah, id_pembelian)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil Diperbarui".format(cursor.rowcount))

#Fungsi Hapus Data
def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    id_pembelian = input("Pilih ID Pembelian : ")
    sql = "DELETE FROM pembelian WHERE id_pembelian=%s"
    val = (id_pembelian,)
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