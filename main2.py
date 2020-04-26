# Tubes Daspro
# Last updated : 26/04/20 - 11am

import csv

def display(role) :
    global boolLogin
    if role == 'pemain' :
        print('''
        Pilih apa yang akan pemain lakukan di Willy Wangky ini!
        1. Pencarian Wahana
        2. Pembelian Tiket
        3. Menggunakan Tiket
        4. Refund
        5. Kritik dan Saran
        6. Exit
        7. Report
        ''')
        inp = input('')
        if inp == '1' : searchWahana()
        elif inp == '2' : buyTicket()
        elif inp == '3' : useTicket()
        elif inp == '4' : refund()
        elif inp == '5' : kritik()
        elif inp == '6' : shutdown(); boolLogin = False
        elif inp == '7' : report()

    else :
        print('''
        Berikut yang admin bisa lakukan :
        1. Sign Up User
        2. Pencarian Pemain
        3. Melihat Kritik dan Saran
        4. Menambahkan Wahana Baru
        5. Top Up Saldo
        6. Melihat Riwayat Penggunaan Wahana
        7. Melihat Jumlah Tiket Pemain
        8. Exit
        9. Melihat Wahana Terbaik
        ''')
        inp = input('')
        if inp == '1' : signUp()
        elif inp == '2' : searchPemain()
        elif inp == '3' : lookupKritik()
        elif inp == '4' : addWahana()
        elif inp == '5' : topup()
        elif inp == '6' : history()
        elif inp == '7' : lookupTiket()
        elif inp == '8' : shutdown(); boolLogin = False
        elif inp == '9' : best()


################################################## F01 - Load
# Mengubah csv ke array
def toList(namafile) :
    with open(namafile,'r') as f :
        array = [[] for i in range(100)]
        i = 0
        for row in csv.reader(f) :
            array[i] = row
            i += 1
            if i == 100 : break

    return array

# load file csv dan mengubahnya ke array 2 dimensi.
def load() :
    global fileuser, filewahana, filebeli, fileguna, filemilik, filerefund, filekritik, filereport
    # input nama file
    namafuser = input('Masukkan nama file user: ') or 'user.csv'
    namafwahana = input('Masukkan nama file wahana: ') or 'wahana.csv'
    namafbeli = input('Masukkan nama file pembelian tiket: ') or 'pembeliantiket.csv'
    namafmilik = input('Masukkan nama file kepemilikan tiket: ') or 'kepemilikantiket.csv'
    namafguna = input('Masukkan nama file penggunaan tiket: ') or 'penggunaantiket.csv'
    namafrefund = input('Masukkan nama file refund tiket: ') or 'refundtiket.csv'
    namafkritik = input('Masukkan nama file kritik dan saran: ') or 'kritikdansaran.csv'
    namafreport = 'report.csv'

    # menulis ke array
    fileuser = toList(namafuser)
    filewahana = toList(namafwahana)
    filebeli = toList(namafbeli)
    fileguna = toList(namafguna)
    filemilik = toList(namafmilik)
    filerefund = toList(namafrefund)
    filekritik = toList(namafkritik)
    filereport = toList(namafreport)

    print('file perusahaan Willy Wangky’s Chocolate Factory telah di-load.')

################################################## F02 - Save
# menyimpan array data ke csv
def save() :
    global fileuser, filewahana, filebeli, fileguna, filemilik, filerefund, filekritik, filereport
    # input nama file
    namafuser = input('Masukkan nama file user: ') or 'user.csv'
    namafwahana = input('Masukkan nama file wahana: ') or 'wahana.csv'
    namafbeli = input('Masukkan nama file pembelian tiket: ') or 'pembeliantiket.csv'
    namafmilik = input('Masukkan nama file kepemilikan tiket: ') or 'kepemilikantiket.csv'
    namafguna = input('Masukkan nama file penggunaan tiket: ') or 'penggunaantiket.csv'
    namafrefund = input('Masukkan nama file refund tiket: ') or 'refundtiket.csv'
    namafkritik = input('Masukkan nama file kritik dan saran: ') or 'kritikdansaran.csv'
    namafreport = 'report.csv'

    # menulis ke csv
    with open(namafuser,'w',newline='') as user, open(namafwahana,'w',newline='') as wahana, open(namafbeli,'w',newline='') as beli, open(namafguna,'w',newline='') as guna, open(namafmilik,'w',newline='') as milik, open(namafrefund,'w',newline='') as refund, open(namafkritik,'w',newline='') as kritik, open(namafreport,'w',newline='') as report:
        csv.writer(user).writerows(fileuser)
        csv.writer(wahana).writerows(filewahana)
        csv.writer(beli).writerows(filebeli)
        csv.writer(guna).writerows(fileguna)
        csv.writer(milik).writerows(filemilik)
        csv.writer(refund).writerows(filerefund)
        csv.writer(kritik).writerows(filekritik)
        csv.writer(report).writerows(filereport)

    print('Data berhasil disimpan!')

################################################## F03 - SignUp
# Menambah user ke user.csv. Jika username telah digunakan, akan return error. Asumsi input lainnya benar.
def signUp() :
    global fileuser
    used = False
    
    newUser = ['' for i in range(7)]
    newUser[0] = input('Masukkan nama pemain: ')
    newUser[1] = input('Masukkan tanggal lahir pemain (DD/MM/YYYY): ')
    newUser[2] = input('Masukkan tinggi badan pemain (cm): ')
    newUser[3] = input('Masukkan username pemain: ')
    newUser[4] = encrypt(input('Masukkan password pemain: '))
    newUser[5] = 'pemain'
    newUser[6] = 0
    
    # validasi
    for row in fileuser :
        if row == [] : break
        if newUser[3] == row[3] :
            print('Username telah digunakan.')
            used = True
    # menambahkan user
    if not used :
        i = 0
        for row in fileuser :
            if row == [] :
                fileuser[i] = newUser
                break
            i += 1
        
        print(f'Selamat mejadi pemain, {newUser[0]}! Selamat bermain.')


################################################## F04 - Login
# login aplikasi, akan diulang sampai input benar.
# return data-data user yang telah login untuk digunakan di fungsi lain.
def login() :
    global fileuser
    # input sampai benar
    while True :
        username = input('Masukkan username: ')
        password = encrypt(input('Masukkan password: '))

        # validasi
        for row in fileuser :
            if row == [] : break
            if username == row[3] and password == row[4] :
                print(f'Selamat bersenang-senang, {row[0]}!')
                return (row[1], row[2], row[3], row[5], int(row[6]), True)
        
        print('Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silahkan coba lagi!\n')


################################################## F05 - Pencarian Pemain
# mencari data pemain berdasarkan username
def searchPemain() :
    global fileuser
    searchUsername = input('Masukkan username: ')
    found = False

    # searching
    for row in fileuser :
        if row == [] : break
        if searchUsername == row[3] :
            found = True
            print(f'''
            Nama Pemain : {row[0]}
            Tanggal Lahir Pemain : {row[1]}
            Tinggi Pemain : {row[2]}
            ''')
            break
    if not found :
        print('Pemain tidak ditemukan')


################################################## F06 - Pencarian Wahana
# mencari wahana yang sesuai dengan spesifikasi yang dicari
def searchWahana() :
    global filewahana
    batasUmur = ['','anak-anak','dewasa','semua umur']
    batasTinggi = ['','170','tanpa batasan']

    print('''
    Jenis batasan umur:
    1. Anak-anak (<17 tahun)
    2. Dewasa (>=17 tahun)
    3. Semua umur

    Jenis batasan tinggi badan:
    1. Lebih dari 170 cm
    2. Tanpa Batasan
    ''')

    # input batasan umur dan tinggi, diulang sampai benar
    while True :
        searchBatasUmur = int(input('Batasan umur pemain: '))
        if searchBatasUmur > 0 and searchBatasUmur <= 3 : break
        print('Batasan umur tidak valid!')
    while True :
        searchBatasTinggi = int(input('Batasan tinggi badan: '))
        if searchBatasTinggi > 0 and searchBatasTinggi <= 2 : break
        print('Batasan tinggi tidak valid!')

    print('Hasil pencarian:')

    # searching
    found = False
    for row in filewahana :
        if row == []  : break
        if batasUmur[searchBatasUmur] == row[3] and batasTinggi[searchBatasTinggi] == row[4] :
            print(f'{row[0]} | {row[1]} | {row[2]}')
            found = True
    if not found :
        print('Tidak ada wahana yang sesuai dengan pencarian anda.')


################################################## F07 - Pembelian Tiket
# membeli tiket
def buyTicket() :
    global filemilik, filebeli, filewahana
    global currentUser, currentTL, currentTinggi, currentSaldo
    belitiket = ['' for i in range(4)]
    belitiket[0] = currentUser
    belitiket[1] = input('Masukkan ID wahana: ')
    belitiket[2] = input('Masukkan tanggal hari ini: ')
    belitiket[3] = input('Jumlah tiket yang dibeli: ')

    miliktiket = [belitiket[0], belitiket[1], belitiket[3]]
    katUmur = age(currentTL, belitiket[2])
    found = False

    for row1 in filewahana :
        if row1 == [] : break
        # validasi
        if row1[0] == belitiket[1]:
            found = True
            if validTinggi(currentTinggi, row1[4]) and validUmur(katUmur,row1[3]) :
                if cukupSaldo(currentSaldo, row1[2], belitiket[3]) :
                    # menambahkan tiket ke kepemilikan tiket
                    new = True
                    # menambahkan tiket ke yang telah memiliki tiket sebelumnya
                    for row2 in filemilik :
                        if row2 == [] : break
                        if currentUser == row2[0] and row2[1] == belitiket[1]:
                            row2[2] = int(row2[2]) + int(belitiket[3])
                            new = False

                    # menambahkan tiket baru
                    if new :
                        i = 0
                        for row2 in filemilik :
                            if row2 == []:
                                filemilik[i] = miliktiket
                                break
                            i += 1

                    # menambahkan data ke pembelian data
                    j = 0
                    for row3 in filebeli :
                        if row3 == [] :
                            filebeli[0] = belitiket
                            break
                        j += 1
                    
                    # mengurangi saldo
                    currentSaldo -= (int(row1[2]) * int(belitiket[3]))
                    
                    print(f'Selamat bersenang-senang di {row1[1]}!')
                    break
                else :
                    print('Saldo anda tidak cukup. \nSilakan mengisi saldo anda.')   
            else :
                print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini. \nSilahkan menggunakan wahana lain yang tersedia.')

    if not found :
        print('ID wahana salah.')

# menghitung umur berdasarkan tanggal sekarang dan tanggal lahir
# output kategori usia berdasarkan umur tersebut
def age(TL, crrDate) :
    TLdate = int(TL[:2])
    TLmonth = int(TL[3:5])
    TLyear = int(TL[6:10])
    crrdate = int(crrDate[:2])
    crrmonth = int(crrDate[3:5])
    crryear = int(crrDate[6:10])

    age = crryear - TLyear - ((crrmonth, crrdate) < (TLmonth, TLdate))
    if age >= 17 :
        return 'dewasa'
    else :
        return 'anak-anak'

# menentukan apakah cukup umur untuk menaiki wahana
def validUmur(paramUmur, batasanUmur) :
    if batasanUmur == 'semua umur' :
        return True
    elif batasanUmur == 'dewasa' :
        if paramUmur == 'dewasa' :
            return True
        else : 
            return False
    else :
        if paramUmur == 'anak-anak' :
            return True
        else : 
            return False

# menentukan apakah cukup tinggi untuk menaiki wahana
def validTinggi(paramTinggi, batasanTinggi) :
    if batasanTinggi == 'tanpa batasan' :
        return True
    else :
        if int(paramTinggi) >= 170 :
            return True
        else :
            return False

# menentukan apakah saldo cukup
def cukupSaldo(paramSaldo, hargaTiket, banyakTiket) :
    if int(paramSaldo) >= int(hargaTiket) * int(banyakTiket) :
        return True
    else :
        return False


################################################## F08 - Menggunakkan Tiket
# menggunakkan tiket
def useTicket() :
    global filemilik, fileguna
    global currentUser
    found = False
    gunakanTiket = ['' for i in range(4)]
    gunakanTiket[0] = currentUser
    gunakanTiket[1] = input('Masukkan ID Wahana: ')
    gunakanTiket[2] = input('Masukkan tanggal hari ini: ')
    gunakanTiket[3] = input('Jumlah tiket yang digunakan: ')

    
    for row in filemilik :
        if row == [] : break
        # mencari kepemilikan tiket
        if row[0] == currentUser and row[1] == gunakanTiket[1] :
            found = True
            if (int(row[2]) - int(gunakanTiket[3])) >= 0 :
                # mengurangi jumlah tiket yang dimiliki
                row[2] = int(row[2]) - int(gunakanTiket[3])
                # menambahkan data ke penggunaan wahana
                # menambahkan tiket yang digunakan jika telah ada di fileguna
                for row1 in fileguna :
                    if row1 == [] : break
                    if row1[0] == gunakanTiket[0] and row1[1] == gunakanTiket[1] and row1[2] == gunakanTiket[2] :
                        row1[3] = int(row1[3]) + int(gunakanTiket[3])
                # menambahkan penggunaan baru
                else :
                    i = 0
                    for row1 in fileguna :
                        if row1[0] == [] :
                            fileguna[i] = gunakanTiket
                            break
                        i += 1
                
                print('Terima kasih telah bermain.')
            else :
                print('Anda tidak memiliki cukup tiket.')
        
    if not found :
        print('Anda tidak memiliki tiket atau input ID salah.')


################################################## F09 - Refund
# refund tiket
def refund() :
    global currentSaldo, currentUser
    global filemilik, filerefund, filewahana
    found = False

    arrRefund = ['' for i in range(4)]
    arrRefund[0] = currentUser
    arrRefund[1] = input('Masukkan ID wahana: ')
    arrRefund[2] = input('Masukkan tanggal hari ini: ')
    arrRefund[3] = input('Jumlah tiket yang di-refund: ')

    
    for row1 in filemilik :
        if row1 == [] : break
        # mencari kepemilikan tiket
        if row1[0] == currentUser and row1[1] == arrRefund[1] :
            found = True
            # mengecek apakah tiket yang dimiliki cukup
            if (int(row1[2]) - int(arrRefund[3])) >= 0 :
                # menulis ke array
                row1[2] = int(row1[2]) - int(arrRefund[3])
                for row3 in filerefund :
                    i = 0
                    if row3 == []:
                        filerefund[i] = arrRefund
                        break
                    i += 1

                # menambah saldo
                for row2 in filewahana :
                    if row2[0] == arrRefund[1] :
                        currentSaldo += (int(row2[2]) * int(arrRefund[3]))
                        break
                
                print('Uang refund telah kami berikan kepada akun anda.')
            else :
                print('Anda tidak memiliki cukup tiket.')
        
    if not found :
        print('Anda tidak memiliki tiket atau input ID salah.')


################################################## F10 - Kritik dan Saran
# memasukkan kritik
def kritik() :
    global currentUser, filekritik
    arrKritik = ['' for i in range(4)]
    arrKritik[0] = currentUser
    arrKritik[1] = input('Masukkan ID wahana: ')
    arrKritik[2] = input('Masukkan tanggal pelaporan: ')
    arrKritik[3] = input('Kritik/saran Anda: ')

    # menambahkan ke array
    i = 0
    for row in filekritik :
        if row == []:
            filekritik[i] = arrKritik
            break
        i += 1

    print('Kritik dan saran Anda telah kami terima.')


################################################## F11 - Melihat Kritik dan Saran
# meliihat kritik terurut bedasarkan ID Wahana
def lookupKritik() :
    global filekritik

    print('Kritik dan saran:')
    sortedList = sortA(filekritik)
    for row in sortedList :
        if row == [] : break
        print(f'{row[1]} | {row[2]} | {row[0]} | {row[3]}')

# Mengurutkan kritik secara alfabetis berdasarkan ID Wahana
def sortA(A) :
    l = 0
    for a in A :
        if a == [] : break
        l += 1

    for i in range(l) :
        # mencari minimum
        min_idx = i 
        for j in range(i+1, l):
            if A[min_idx][0][:1] > A[j][0][:1]: 
                min_idx = j 
        # Swap
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


################################################## F12 - Menambahkan Wahana Baru
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

    # Menambahkan ke filewahana
    i = 0
    for row in filewahana :
        if row == [] :
            filewahana[i] = newWahana
            break
        i += 1
    
    print('Info wahana telah ditambahkan!')


################################################## F13 - Top Up Saldo
# Menambahkan saldo ke akun pemain. Asumsi input benar.
def topup() :
    global fileuser
    user = input('Masukkan username: ')
    addSaldo = int(input('Masukkan saldo yang di-top up: '))

    # menambah saldo
    for row in fileuser :
        if row == [] : break
        if user == row[3] :
            row[6] = int(row[6]) + addSaldo
            print(f'Top up berhasil. Saldo {row[0]} bertambah menjadi {row[6]}')


################################################## F14 - Melihat Riwayat Penggunaan Wahana
# Melihat riwayat. Asumsi input benar.
def history() :
    global fileguna
    idwahana = input('Masukkan ID wahana: ')

    print('Riwayat:')
    # output riwayat penggunaan wahana
    for row in fileguna :
        if row == [] : break
        if row[1] == idwahana :
            print(f'{row[2]} | {row[0]} | {row[3]}')


################################################## F15 - Melihat Jumlah Tiket Pemain
# melihat jumlah tiket pemain. Asumsi input benar.
def lookupTiket() :
    global filemilik, filewahana
    user = input('Masukkan username: ')

    print('Riwayat:')
    #output kepemilikan tiker
    for row2 in filemilik :
        if row2 == [] : break
        if user == row2[0]:
            for row1 in filewahana :
                if row1 == [] : break
                if row2[1] == row1[0] :
                    print(row2[1], '|', row1[1], '|', row2[2])


################################################## F16 - Exit
# keluar program
def shutdown() :
    global fileuser
    global currentUser, currentSaldo
    
    # menyimpan saldo ke array
    for row in fileuser :
        if currentUser == row[3] :
            row[6] = currentSaldo
            break

    # konfirmasi penyimpanan
    conf = input('Apakah anda akan melakukan penyimpanan file yang sudah dilakukan (Y/N) ?')
    if conf == 'Y' :
        save()



################################################## B01 - Enkripsi Password
# enkripsi password
def encrypt(words) :
    allchar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    key = 5
    enc = ''
    for i in words :
        n = 0
        for j in allchar :
            if i == j :
                position = n
            else :
                n += 1
        newposition = (position + key)%72
        enc += allchar[newposition]
    return enc


################################################## B02 - Golden Account
def golden() :
    global fileuser
    user = input('Masukkan username yang ingin di-upgrade: ')
    print('Akun anda telah di-upgrade')
    #belum diimplementasikan ke fungsi lainnya

################################################## B03 - Best Wahana
# memberikan daftar 3 wahana berdasarkan jumlah tiket yang terjual
def best() :
    global filebeli, filewahana
    # membuat array kosong arrBest sesuai banyaknya wahana
    l = 0
    for row in filewahana :
        if row == [] : break
        l += 1
    arrBest = ['' for i in range(l)]

    # mengisi arrBest dengan wahana
    i = 0
    for row in filewahana :
        if row == [] : break
        arrBest[i] = [row[0], row[1], 0]
        i += 1

    # menambah jumlah tiket setiap wahana
    for arr in arrBest :
        for row in filebeli :
            if row == [] : break
            if row[1] == arr[0] :
                arr[2] = int(arr[2]) + int(row[3])
    # sorting
    sortB(arrBest)
    # print
    for i in range(3) :
        print(f'{i+1} | {arrBest[i][0]} | {arrBest[i][1]} | {arrBest[i][2]}')

# mengurutkan arrBest dari terbesar
def sortB(A) :
    l = 0
    for a in A :
        l += 1

    for i in range(l) :
        # mencari maximum
        max_idx = i 
        for j in range(i+1, l): 
            if A[max_idx][2] < A[j][2]: 
                max_idx = j 
        # Swap
        A[i], A[max_idx] = A[max_idx], A[i]
    return A


################################################## B04 - Laporan Kehilangan Tiket
# Melaporkan apabila ada kehilangan tiket. Akan mengurangi jumlah tiket yang dimiliki pemain.
# Asumsi input benar
def report() :
    global filemilik
    global filereport
    arrReport = ['' for i in range(4)]
    arrReport[0] = input('Masukkan username: ')
    arrReport[1] = input('Tanggal kehilangan tiket: ')
    arrReport[2] = input('ID Wahana: ')
    arrReport[3] = input('Jumlah tiket yang dihilangkan: ')

    # mengurangi tiket pemain
    for row1 in filemilik :
        if row1 == [] : break
        if row1[0] == arrReport[0] and row1[1] == arrReport[2] :
            row1[2] = int(row1[2]) - int(arrReport[3])
            break

    # menulis ke filereport
    i = 0
    for row2 in filereport :
        if row2 == [] :
            filereport[i] = arrReport
            break
        i += 1

    print('Laporan kehilangan tiket Anda telah direkam.')


# MAIN PROGRAM

load()
currentTL, currentTinggi, currentUser, currentRole, currentSaldo, boolLogin = login()

while boolLogin :
    
    display(currentRole)