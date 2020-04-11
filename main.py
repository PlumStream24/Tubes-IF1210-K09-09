import csv
from tempfile import NamedTemporaryFile
import shutil
import operator
from os import remove

def load() :
    fileuser = input('Masukkan nama file user: ')
    filewahana = input('Masukkan nama file wahana: ')
    filepembeliantiket = input('Masukkan nama file pembelian tiket: ')
    filekepemilikantiket = input('Masukkan nama file kepemilikan tiket: ')
    filepenggunaantiket = input('Masukkan nama file penggunaan tiket: ')
    filerefundtiket = input('Masukkan nama file refund tiket: ')
    filekritikdansaran = input('Masukkan nama file kritik dan saran: ')

    shutil.copy(fileuser, 'temp_user.csv')
    shutil.copy(filewahana, 'temp_wahana.csv')
    shutil.copy(filepembeliantiket, 'temp_pembeliantiket.csv')
    shutil.copy(filepenggunaantiket, 'temp_penggunaantiket.csv')
    shutil.copy(filekepemilikantiket, 'temp_kepemilikantiket.csv')
    shutil.copy(filerefundtiket ,'temp_refundtiket.csv')
    shutil.copy(filekritikdansaran, 'temp_kritikdansaran.csv')


def save() :
    fileuser = input('Masukkan nama file user: ')
    filewahana = input('Masukkan nama file wahana: ')
    filepembeliantiket = input('Masukkan nama file pembelian tiket: ')
    filekepemilikantiket = input('Masukkan nama file kepemilikan tiket: ')
    filepenggunaantiket = input('Masukkan nama file penggunaan tiket: ')
    filerefundtiket = input('Masukkan nama file refund tiket: ')
    filekritikdansaran = input('Masukkan nama file kritik dan saran: ')


    shutil.move('temp_user.csv', fileuser)
    shutil.move('temp_wahana.csv', filewahana)
    shutil.move('temp_pembeliantiket.csv', filepembeliantiket)
    shutil.move('temp_penggunaantiket.csv', filepenggunaantiket)
    shutil.move('temp_kepemilikantiket.csv',filekepemilikantiket)
    shutil.move('temp_refundtiket.csv', filerefundtiket)
    shutil.move('temp_kritikdansaran.csv', filekritikdansaran)



def signup() :
    used = False
    newInput = ['' for i in range(7)]
    newInput[0] = input('Masukkan nama pemain: ')
    newInput[1] = input('Masukkan tanggal lahir pemain: ')
    newInput[2] = input('Masukkan tinggi badan pemain: ')
    newInput[3] = input('Masukkan username pemain: ')
    newInput[4] = input('Masukkan password pemain: ')
    newInput[5] = 'pemain'
    newInput[6] = 0

    with open('temp_user.csv','r') as csvfile :
        for row in csv.reader(csvfile) :
            if newInput[3] == row[3] :
                print('Username telah digunakan.')
                used = True
    if not used :
        with open('temp_user.csv', 'a', newline='') as csvfile:
            writecsv = csv.writer(csvfile)
            writecsv.writerow(newInput)
            print(f'Selamat mejadi pemain, {newInput[0]}! Selamat bermain.')
        

def login() :
    while True :
        username = input('Masukkan username: ')
        password = input('Masukkan password: ')
        
        with open('temp_user.csv') as csvfile:
            readcsv = csv.reader(csvfile)
            for row in readcsv :
                if username == row[3] and password == row[4] :
                    print(f'Selamat bersenang-senang, {row[0]}!')
                    return (row[1], row[2], row[3], row[5], int(row[6]), True)
            else :
                print('Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silahkan coba lagi!\n')


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
        ''')
        inp = input('')
        if inp == '1' : searchWahana()
        elif inp == '2' : buyTicket()
        elif inp == '3' : useTicket()
        elif inp == '4' : refund()
        elif inp == '5' : kritik()
        elif inp == '6' : shutdown(); boolLogin = False

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
        ''')
        inp = input('')
        if inp == '1' : signup()
        elif inp == '2' : searchPemain()
        elif inp == '3' : lookupKritik()
        elif inp == '4' : addWahana()
        elif inp == '5' : topup()
        elif inp == '6' : history()
        elif inp == '7' : lookupTiket()
        elif inp == '8' : shutdown(); boolLogin = False


def searchPemain() :
    searchUsername = input('Masukkan username: ')

    with open('temp_user.csv') as csvfile:
        readcsv = csv.reader(csvfile)
        for row in readcsv :
            if searchUsername == row[3] :
                print(f'''
                Nama Pemain : {row[0]}
                Tanggal Lahir Pemain : {row[1]}
                Tinggi Pemain : {row[2]}
                ''')
                break
        else :
            print('Pemain tidak ditemukan')


def searchWahana() :
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

    while True :
        searchBatasUmur = int(input('Batasan umur pemain: '))
        if searchBatasUmur >= 0 and searchBatasUmur <= 3 : break
        print('Batasan umur tidak valid!')
    while True :
        searchBatasTinggi = int(input('Batasan tinggi badan: '))
        if searchBatasTinggi >=0 and searchBatasTinggi <= 2 : break
        print('Batasan tinggi tidak valid!')

    print('Hasil pencarian:')

    with open('temp_wahana.csv') as csvfile:
        readcsv = csv.reader(csvfile)
        for row in readcsv :
            found = False
            if batasUmur[searchBatasUmur] == row[3] and batasTinggi[searchBatasTinggi] == row[4] :
                print(f'{row[0]} | {row[1]} | {row[2]}')
                found = True
        if not found :
            print('Tidak ada wahana yang sesuai dengan pencarian anda.')


def addWahana() :
    print('Masukkan informasi wahana yang ditambahakan:')
    newWahana = ['' for i in range(5)]
    newWahana[0] = input('Masukkan ID wahana: ')
    newWahana[1] = input('Masukkan nama wahana: ')
    newWahana[2] = input('Masukkan harga tiket :')
    newWahana[3] = input('Batasan umur: ')
    newWahana[4] = input('Batasan tinggi badan: ')

    with open('temp_wahana.csv','a',newline='') as csvfile :
        writecsv = csv.writer(csvfile)
        writecsv.writerow(newWahana)
    
    print('Info wahana telah ditambahkan!')


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


def buyTicket() :
    global currentUser
    global currentTL
    global currentTinggi
    global currentSaldo
    belitiket = ['' for i in range(4)]
    belitiket[0] = currentUser
    belitiket[1] = input('Masukkan ID wahana: ')
    belitiket[2] = input('Masukkan tanggal hari ini: ')
    belitiket[3] = input('Jumlah tiket yang dibeli: ')

    miliktiket = belitiket.copy()
    del miliktiket[2]
    katUmur = age(currentTL, belitiket[2])
    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')
    
    with open('temp_wahana.csv','r') as wahana, open('temp_pembeliantiket.csv','a', newline='') as pembelian :
        for row1 in csv.reader(wahana) :
            if row1[0] == belitiket[1]:
                if validTinggi(currentTinggi, row1[4]) and validUmur(katUmur,row1[3]) :
                    if cukupSaldo(currentSaldo, row1[2], belitiket[3]) :
                        with open('temp_kepemilikantiket.csv','r') as milik, tempfile :
                            new = True
                            for row2 in csv.reader(milik) :
                                if currentUser == row2[0] and row2[1] == belitiket[1]:
                                    row2[2] = int(row2[2]) + int(belitiket[3])
                                    csv.writer(tempfile).writerow(row2)
                                    new = False
                                else :
                                    csv.writer(tempfile).writerow(row2)
                            if new :
                                csv.writer(tempfile).writerow(miliktiket)
                        shutil.move(tempfile.name, 'temp_kepemilikantiket.csv')
                        csv.writer(pembelian).writerow(belitiket)
                        currentSaldo -= (int(row1[2]) * int(belitiket[3]))
                        print(f'Selamat bersenang-senang di {row1[1]}!')
                        break
                    else :
                        print('Saldo anda tidak cukup. \nSilakan mengisi saldo anda.')   
                else :
                    print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini. \nSilahkan menggunakan wahana lain yang tersedia.')



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

def validTinggi(paramTinggi, batasanTinggi) :
    if batasanTinggi == 'tanpa batasan' :
        return True
    else :
        if int(paramTinggi) >= 170 :
            return True
        else :
            return False

def cukupSaldo(paramSaldo, hargaTiket, banyakTiket) :
    if int(paramSaldo) >= int(hargaTiket) * int(banyakTiket) :
        return True
    else :
        return False


def useTicket() :
    found = False
    global currentUser
    gunakanTiket = ['' for i in range(4)]
    gunakanTiket[0] = currentUser
    gunakanTiket[1] = input('Masukkan ID Wahana: ')
    gunakanTiket[2] = input('Masukkan tanggal hari ini: ')
    gunakanTiket[3] = input('Jumlah tiket yang digunakan: ')

    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')

    with open('temp_kepemilikantiket.csv','r') as inp, open('temp_penggunaantiket.csv','a', newline='') as out, tempfile :
        writecsv = csv.writer(tempfile)
        for row in csv.reader(inp) :
            if row[0] == currentUser and row[1] == gunakanTiket[1] :
                found = True
                row[2] = int(row[2]) - int(gunakanTiket[3])
                if row[2] >= 0 :
                    csv.writer(out).writerow(gunakanTiket)
                    if row[2] > 0 :
                        writecsv.writerow(row)
                    else : #row[2] == 0
                        continue
                    print('Terima kasih telah bermain.')
                else :
                    print('Anda tidak memiliki cukup tiket.')
            else :
                writecsv.writerow(row)
        if not found :
            print('Anda tidak memiliki tiket atau input ID salah.')

    shutil.move(tempfile.name, 'temp_kepemilikantiket.csv')



def refund() :
    global currentSaldo
    global currentUser
    found = False
    arrRefund = ['' for i in range(4)]
    arrRefund[0] = currentUser
    arrRefund[1] = input('Masukkan ID wahana: ')
    arrRefund[2] = input('Masukkan tanggal hari ini: ')
    arrRefund[3] = input('Jumlah tiket yang di-refund: ')

    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')

    with open('temp_kepemilikantiket.csv','r') as inp, open('temp_wahana.csv', 'r') as data, open('temp_refundtiket.csv', 'a', newline='') as out, tempfile :
        for row1 in csv.reader(inp) :
            if row1[0] == currentUser and row1[1] == arrRefund[1] :
                found = True
                row1[2] = int(row1[2]) - int(arrRefund[3])
                if row1[2] >= 0 :
                    csv.writer(out).writerow(arrRefund)
                    for row2 in csv.reader(data) :
                        if row2[0] == arrRefund[1] :
                            currentSaldo += (int(row2[2]) * int(arrRefund[3]))
                    if row1[2] > 0 :
                        csv.writer(tempfile).writerow(row1)
                    else : #row1[2] == 0
                        continue
                    print('Uang refund telah kami berikan kepada akun anda.')
                else :
                    print('Anda tidak memiliki cukup tiket.')
            else :
                csv.writer(tempfile).writerow(row1)
        if not found :
            print('Anda tidak memiliki tiket atau input ID salah.')

    shutil.move(tempfile.name, 'temp_kepemilikantiket.csv')
   
def kritik() :
    global currentUser
    arrKritik = ['' for i in range(4)]
    arrKritik[0] = currentUser
    arrKritik[1] = input('Masukkan ID wahana: ')
    arrKritik[2] = input('Masukkan tanggal pelaporan: ')
    arrKritik[3] = input('Kritik/saran Anda: ')

    with open('temp_kritikdansaran.csv','a', newline='') as out :
        csv.writer(out).writerow(arrKritik)

def topup() :
    user = input('Masukkan username: ')
    addSaldo = int(input('Masukkan saldo yang di-top up: '))

    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')

    with open('temp_user.csv','r') as datauser, tempfile :
        for row in csv.reader(datauser) :
            if user == row[3] :
                row[6] = int(row[6]) + addSaldo
            csv.writer(tempfile).writerow(row)
    shutil.move(tempfile.name, 'temp_user.csv')
    
    with open('temp_user.csv','r') as datauser :
        for row in csv.reader(datauser) :
            if user == row[3] :
                print(f'Top up berhasil. Saldo {row[0]} bertambah menjadi {row[6]}')

def lookupKritik() :
    print('Kritik dan saran:')
    with open('temp_kritikdansaran.csv', 'r') as data :
        tabel = [line for line in csv.reader(data)]
    tabel.sort(key=operator.itemgetter(1))
    with open('temp_kritikdansaran.csv','w', newline='') as data :
        csv.writer(data).writerows(tabel)
    with open('temp_kritikdansaran.csv','r') as data :
        for row in csv.reader(data) :
            print(f'{row[1]} | {row[2]} | {row[0]} | {row[3]}')


def lookupTiket() :
    user = input('Masukkan username: ')
    with open('temp_kepemilikantiket.csv','r') as data, open('temp_wahana.csv','r') as listwahana :
        for row2 in csv.reader(data) :
            if user == row2[0]:
                for row1 in csv.reader(listwahana) :
                    if row2[1] == row1[0] :
                        print(row2[1], '|', row1[1], '|', row2[2])


def history() :
    idwahana = input('Masukkan ID wahana: ')
    with open('temp_penggunaantiket.csv','r') as data :
        for row in csv.reader(data) :
            if row[1] == idwahana :
                print(f'{row[2]} | {row[0]} | {row[3]}')


def shutdown() :
    global currentUser
    global currentSaldo
    tempfile = tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')

    with open('temp_user.csv', 'r') as data, tempfile :
        for row in csv.reader(data) :
            if currentUser == row[3] :
                row[6] = currentSaldo
                csv.writer(tempfile).writerow(row)
            else :
                csv.writer(tempfile).writerow(row)
    shutil.move(tempfile.name, 'temp_user.csv')

    conf = input('Apakah anda akan melakukan penyimpanan file yang sudah dilakukan (Y/N) ?')
    if conf == 'Y' :
        save()
    elif conf == 'N' :
        remove('temp_user.csv')
        remove('temp_wahana.csv')
        remove('temp_pembeliantiket.csv')
        remove('temp_penggunaantiket.csv')
        remove('temp_kepemilikantiket.csv')
        remove('temp_refundtiket.csv')
        remove('temp_kritikdansaran.csv')


# main program

load()
currentTL, currentTinggi, currentUser, currentRole, currentSaldo, boolLogin = login()

while boolLogin :
    display(currentRole)
