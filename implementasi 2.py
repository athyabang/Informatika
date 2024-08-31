#variable names
myname = "Athya"
MyFullName = "Nareswari Athiyya Wahyuningsih" 
my_school = "SMA Sains"
myMOM = "Sulistyani Wahyuningsih" #pascal case
_my_Dad = "Pujianto" #snake case

print (myname)
print (MyFullName)
print (my_school)
print (myMOM)
print (_my_Dad)

#Tipe data angka
harga = 50000 #tipe int
berat = 25.3 #float
jarak = 3e4 #float eksponen

print (harga)
print (berat)
print (jarak)

#Tipe data teks
barang = "kemeja"
ukuran = "M"
alamat = """Karangrejo, Karangnongko, RT 05/RW 28 Tirtomartani, Kalasan, Sleman """
kode_pos = 55571

print (barang, ukuran)
print (alamat)
print (kode_pos)

#Tipe Boolean
name = "Athya"
citizenship = 'Indonesia'
age = 17
high = 168.9
marriage = False
student = True


print ("Nama :", name)
print ("Negara :", citizenship)
print ("Umur :", age)
print ("Tinggi :", high)
if marriage:
    print("Status: menikah")
else:
    print("Status: belum menikah")

if student:
    print("Masih pelajar")
else:
    print("Kerja")

#konversi tipe data
a = 10
b = 3
c = a/b
print (float(c))

#menampilkan output teks
nama = "Nareswari Athiyya"
print ("Hi", nama, "pintar")

# Problem Solvment 1
# Mengumpulkan Input
print ("=================================")
print ('PENUGASAN 1')
print ("=================================")

nama_lengkap = str(input("Masukkan nama lengkap Anda: "))
usia_tahun = int(input("Masukkan usia Anda dalam tahun: "))
tinggi_cm = float(input("Masukkan tinggi badan Anda dalam sentimeter: "))
status_menikah = input("Apakah Anda sudah menikah? (sudah/belum)").lower() == 'sudah'

# Memproses Data
usia_bulan = usia_tahun * 12
tinggi_meter = tinggi_cm / 100

# Menampilkan Output
print("\n--- Ringkasan Informasi ---")
print(f"Nama lengkap: {nama_lengkap}")
print(f"Usia: {usia_tahun} tahun atau {usia_bulan} bulan")
print(f"Tinggi badan: {tinggi_cm} cm atau {tinggi_meter:.2f} m")
print(f"Status pernikahan: {'Sudah menikah' if status_menikah else 'Belum menikah'}")


# Problem Solvment 2
# Kalkulator Mini
print("==================") 
print("PENUGASAN 2") 
print("==================") 
 
print("Calculator mini created by:") 
print("Nareswari Athiyya Wahyuningsih") 
 
print("===============") 
print("pilihan operasi") 
print("1. Tambah") 
print("2. Kurang") 
print("3. Bagi") 
print("4. Kali") 
print("===============") 
 
operasi = int(input("Masukkan pilihan operasi (1/2/3/4)")) 
 
if operasi == 1: 
    x = int (input("Masukkan nilai pertama : ")) 
    y = int (input("Masukkan nilai kedua : ")) 
    z = x + y 
    print("Hasilnya adalah : ", x, "+", y, "=", z) 
    print("=========================") 
 
elif operasi == 2: 
    x = int (input("Masukkan nilai pertama : ")) 
    y = int (input("Masukkan nilai kedua : ")) 
    z = x - y 
    print("Hasilnya adalah : ", x, "-", y, "=", z) 
    print("=========================") 
 
elif operasi == 3: 
    x = float (input("Masukkan nilai pertama : ")) 
    y = float (input("Masukkan nilai kedua : ")) 
    z = x / y 
    print("Hasilnya adalah : ", x, "/", y, "=", z) 
    print("=========================") 
 
elif operasi == 4: 
    x = int (input("Masukkan nilai pertama : ")) 
    y = int (input("Masukkan nilai kedua : ")) 
    z = x * y 
    print("Hasilnya adalah : ", x, "x", y, "=", z) 
    print("=========================")



# Problem Solvment 3
# Meminta pengguna memasukkan nilai awal
print("==================") 
print("PENUGASAN 3") 
print("==================") 

nilai = float(input("Masukkan nilai awal: "))

# Tambahkan 2 ke nilai tersebut
nilai += 2
print(f"Setelah ditambah 2: {nilai}")

# Kurangi nilai tersebut dengan 3
nilai -= 3
print(f"Setelah dikurangi 3: {nilai}")

# Kalikan nilai tersebut dengan 10
nilai *= 10
print(f"Setelah dikalikan 10: {nilai}")

# Bagi nilai tersebut dengan 4
nilai /= 4
print(f"Setelah dibagi 4: {nilai}")

# Hitung pangkat nilai tersebut dengan 10
nilai **= 10
print(f"Setelah dipangkatkan 10: {nilai}")