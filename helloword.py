#Penulisan String
print("Hello Athya!")
print('''Ayo belajar Python dari Nol''')

#Penulisan blok program
if 5 > 2:
  print("Five is greater than two!")
  
#Penulisan case
my_variable_name = "Athya " #snake case
MyVariableName = "Wahyu" #pascal case

print (my_variable_name + MyVariableName)

  
#Variabel 1
x = 9
y = "Gasiwa"

print(x)
print(y)

#Variabel 2
N = "Athya"
T = "Computer Science" 
U = 2025
print(N, T, U)

#Variable umur
umur = input("masukan umur: ")
if int(umur) < 25:
    keterangan = 'masih muda'
else: 
    keterangan = 'sudah tua'
 
print('athya memasukan umur {}, artinya athya {}'.format(umur, keterangan))


#Komentar
#Bisa menggunakan pagar
'''Bisa menggunakan petik'''
"""
This is a comment
written in
more than just one line
"""