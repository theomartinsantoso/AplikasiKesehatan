def bmi():
    print ("")
    print ('--------------------------------------------')
    print ('Selamat Datang di Program Indeks Massa Tubuh')
    print ('--------------------------------------------')
    nama = raw_input('Masukkan Nama Kamu : ')
    berat = input('Masukkan Berat (kg) = ')
    tinggi = float(input('Masukkan Tinggi (m) = '))

    bmi = berat / (tinggi * tinggi)

    print 'Indeks Massa Tubuh : ', bmi

    if bmi < 18.5:
        print ('Kategori : Kurus')
        print ("")
        print 'Hai %s !' %nama
        kurus()
    elif bmi < 25:
        print ('Kategori : Normal')
        print ("")
        print 'Hai %s !' %nama
        normal()
    elif bmi < 30:
        print ('Kategori : Kelebihan Berat')
        print ("")
        print 'Hai %s !' %nama
        kelebihan()
    else:
        print ('Kategori: Kegemukan')
        print ("")
        print 'Hai %s !' %nama
        kegemukan()

def login():
    username = raw_input("Username : ")
    password = raw_input("Password : ")
    if username == "theo" and password == "12345":
        menu()
    elif username == "admin" and password == "admin":
        menu()
    else:
        print "LOGIN GAGAL"
        login()

def menu():
    print ("")
    print ("-----------------------------------")
    print ("SELAMAT DATANG DI PROGRAM KESEHATAN")
    print ("-----------------------------------")
    print (" 1. Program Indeks Massa Tubuh")
    print (" 2. Program Kebutuhan Kalori")
    print (" 3. Program Detak Jantung")
    print (" 4. Informasi")
    print (" 5. Exit")
    print ("-----------------------------------")
    takon = input("Masukkan Pilihan (1-5) : ")
    if takon == 1:
        bmi()
    elif takon == 2:
        bmr()
    elif takon == 3:
        jantung()
    elif takon == 4:
        info()
    elif takon == 5:
        exit()
    else:
        print ("Pilihan Tidak Tersedia")
        menu()

def tanyamenu() :
    print ("")
    tanya = raw_input("Kembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit()
    else:
        print "Salah Input"
        tanyamenu()

def kegemukan():
    print ('Kamu termasuk gemuk atau memiliki berat badan berlebih')
    print ('jika angka BMI Kamu berada antara angka 23 sampai 24,9.')
    print ('Bagaimana cara menurunkan berat badan? Untuk menurunkan berat badan,')
    print ('Kamu harus mengonsumsi makanan dan minuman dengan jumlah kalori')
    print ('yang lebih kecil dari kebutuhan kalori harian Kamu.')
    print ("")
    tanyamenu()
    
def kurus():
    print ('Kamu termasuk kurus atau memiliki berat badan kurang,')
    print ('jika angka BMI Kamu berada di bawah 18,5.')
    print ('Bagaimana cara menambah berat badan? Jika Anda ingin menaikkan berat badan,')
    print ('Kamu perlu mengonsumsi makanan dan minuman dengan jumlah kalori')
    print ('yang lebih besar dari kebutuhan kalori harian Kamu.')
    print ("")
    tanyamenu()

def normal():
    print ('Berat badan Kamu bisa dikatakan ideal.')
    print ('jika angka BMI Kamu berada antara angka 18,5 sampai 22,9.')
    print ('Bagaimana cara menjaga agar berat badan tetap ideal? Kamu perlu mengonsumsi')
    print ('makanan dan minuman sesuai dengan kebutuhan kalori harian Kamu,')
    print ('untuk mempertahankan berat badan ideal seperti sekarang.')
    print ("")
    tanyamenu()

def kelebihan():
    print ('Kamu termasuk obesitas atau memiliki berat badan berlebih yang berat,')
    print ('jika angka BMI Kamu berada di antara 25 sampai 29,9.')
    print ('Untuk menurunkan berat badan, Kamu harus mengonsumsi makanan dan minuman')
    print ('dengan jumlah kalori yang lebih kecil dari kebutuhan kalori harian Kamu.')
    print ("")
    tanyamenu()

def bmr():
    print ("")
    print ("------------------------------------------")
    print ("Selamat Datang di Program Kebutuhan Kalori")
    print ("------------------------------------------")
    tinggi = float(input("Masukkan Tinggi(m) : "))
    berat = float(input("Masukkan Berat (kg) : "))
    usia = int(input("Masukkan Usia (tahun) : "))
    print (" Jenis Kelamin  ")
    print ("----------------")
    print (" Laki-Laki = L ")
    print (" Perempuan = P ")
    gender = raw_input ("Masukkan (L/P) : ")
    if (gender == "L") or (gender == "Laki") or (gender == "l"):
        BMR = 66.5 + (13.75 * berat) + (5.003 * tinggi ) - (6.755 * usia)
        print  "Kebutuhan Kalori Kamu adalah %s kal" %BMR
        print ("Itu adalah jumlah kalori MINIMAL setiap hari,")
        print ("supaya tubuh organ tubuh kamu bisa berfungsi.")
        tanyamenu()
    elif (gender == "P") or (gender == "Perempuan") or (gender == "p"):
        BMR = 655.1 + (9.563 * berat) + (1.850 * tinggi) - (4.676 * usia)
        print  "Kebutuhan Kalori Kamu adalah %s kal" %BMR
        print ("Itu adalah jumlah kalori MINIMAL setiap hari,")
        print ("supaya tubuh organ tubuh kamu bisa berfungsi.")
        tanyamenu()
    else:
        print("Inputan Salah!")
        bmr()

def jantung():
    print ("")
    print ("---------------------------------------")
    print ("Selamat Datang di Program Detak Jantung")
    print ("---------------------------------------")
    usia = int(input("Masukkan Usia (tahun) : "))
    print (" Jenis Kelamin  ")
    print ("----------------")
    print (" Laki-Laki = L ")
    print (" Perempuan = P ")
    gender = raw_input ("Masukkan (L/P) : ")
    if (gender == "L") or (gender == "Laki") or (gender == "l"):
        jantung =  210 - (usia *0.7)
        print "Detak jantung MAKSIMAL kamu adalah %s detakan permenit" %jantung
        tanyamenu()
    elif (gender == "P") or (gender == "Perempuan") or (gender == "p"):
        jantung = 200 - (usia *0.7)
        print "Detak jantung MAKSIMAL kamu adalah %s detakan permenit" %jantung
        tanyamenu()
    else:
        print ("Inputan Salah!")
        jantung()
    

def info():
    print ("")
    print ("Created by Theo Martin Santoso")
    print ("NPM : 57418046")
    print ("UNIVERSITAS GUNADARMA")

login()
menu()
    
