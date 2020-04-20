# Tubes Daspro F-1, F-3, F-4, F-12
# Muhammad Iqbal Sigid
# Last edit: 20/4/2020

import csv

# Mengubah csv ke array
def toList(namafile) :
    with open(namafile, 'r') as f :
        j = 0
        for i in csv.reader(f) :
            j += 1
    with open(namafile,'r') as f :
        array = ['' for i in range(j)]
        i = 0
        for row in csv.reader(f) :
            array[i] = row
            i += 1

    return array


# load file csv dan mengubahnya ke array 2 dimensi.
def load() :
    global fileuser, filewahana, filebeli, fileguna, filemilik, filerefund, filekritik

    namafuser = input('Masukkan nama file user: ')
    namafwahana = input('Masukkan nama file wahana: ')
    namafbeli = input('Masukkan nama file pembelian tiket: ')
    namafmilik = input('Masukkan nama file kepemilikan tiket: ')
    namafguna = input('Masukkan nama file penggunaan tiket: ')
    namafrefund = input('Masukkan nama file refund tiket: ')
    namafkritik = input('Masukkan nama file kritik dan saran: ')

    fileuser = toList(namafuser)
    filewahana = toList(namafwahana)
    filebeli = toList(namafbeli)
    fileguna = toList(namafguna)
    filemilik = toList(namafmilik)
    filerefund = toList(namafrefund)
    filekritik = toList(namafkritik)
        
# login aplikasi, akan diulang sampai input benar.
# return data-data user yang telah login untuk digunakan di fungsi lain.
def login() :
    global fileuser

    while True :
        username = input('Masukkan username: ')
        password = input('Masukkan password: ')

        for row in fileuser :
            if username == row[3] and password == row[4] :
                print(f'Selamat bersenang-senang, {row[0]}!')
                return (row[1], row[2], row[3], row[5], int(row[6]), True)
        else :
            print('Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silahkan coba lagi!\n')

# Menambah user ke user.csv. Jika username telah digunakan, akan return error. Asumsi input lainnya benar.
def signUp() :
    global fileuser

    used = False
    newUser = ['' for i in range(7)]
    newUser[0] = input('Masukkan nama pemain: ')
    newUser[1] = input('Masukkan tanggal lahir pemain (DD/MM/YYYY): ')
    newUser[2] = input('Masukkan tinggi badan pemain (cm): ')
    newUser[3] = input('Masukkan username pemain: ')
    newUser[4] = input('Masukkan password pemain: ')
    newUser[5] = 'pemain'
    newUser[6] = 0
    
    for row in fileuser :
        if newUser[3] == row[3] :
            print('Username telah digunakan.')
            used = True
    if not used :
        fileuser = fileuser + [newUser]
        print(f'Selamat mejadi pemain, {newUser[0]}! Selamat bermain.')

# Menambah wahana ke wahana.csv. Asumsi input benar.
def addWahana() :
    global filewahana

    print('Masukkan informasi wahana yang ditambahakan:')
    newWahana = ['' for i in range(5)]
    newWahana[0] = input('Masukkan ID wahana (AAANNN): ')
    newWahana[1] = input('Masukkan nama wahana: ')
    newWahana[2] = input('Masukkan harga tiket: ')
    newWahana[3] = input('Batasan umur (anak-anak/dewasa/semua umur): ')
    newWahana[4] = input('Batasan tinggi badan (cm): ')

    filewahana = filewahana + [newWahana]
    
    print('Info wahana telah ditambahkan!')


load()
currentTL, currentTinggi, currentUser, currentRole, currentSaldo, boolLogin = login()
