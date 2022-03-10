# print('Halo Dunia1')
# print('Halo Dunia2')
# print('Halo Dunia3')
# print('Halo Dunia4')

# VARIABEL

# nama = 'Bambang'
# print(nama)
# print(type(nama))

# umur = 25
# print(type(umur)) # Int

# nomor_rumah = '14'
# print(type(nomor_rumah)) # String
 
# DATA TYPE

# String
# x = 'Saya sedang belajar Python'
# print(x)

# Numerik
# x = 20 # Integer
# y = 20.5 # Float
# print(type(x))
# print(type(y))

# Boolean
# x = True
# y = False
# print(type(x))
# print(type(y))

# x = true 
# print(type(x)) # Error ditunjukkan dengan garis bawah berwarna merah

# Range
# x = range(8)
# print(x) # output --> range(0, 8)
# print(type(x)) # range

# None
# x = None
# print(x)
# print(type(x))

# Collection data types

# List
# x = ['a', 'b', 'c'] 
# print(x)
# print(type(x)) # list

# x = 'a', 'b', 'c'
# print(x)
# print(type(x)) # Tanpa tanda kurung, terbaca sebagai tuple

# Tuple
# x = ('a', 'b', 'c')
# print(x)
# print(type(x)) # tuple

# Dictionary
# x = {'nama': 'Frances'}
# print(x)
# print(type(x))

# Set 
# x = {'a', 'b', 'c', 'd', 'a'}
# print(x) # output unordered ==> a, b, c, d 
# print(type(x)) 

# Quiz

# angka = ['15']
# print(type(angka)) # list

# Buat dictionary berisi 3 item, dengan key-nya merupakan bahasa Inggris dan value-nya adalah Bahasa Indonesia.
# items = {'sit':'duduk', 'walk':'berjalan', 'sleep':'tidur'}
# print(items)
# print(type(items))

# =============================================================================================================

# ARITHMETIC OPERATIONS

y = 5 + 2       # penjumlahan
y = 5 - 2       # pengurangan
y = 5 * 2       # perkalian
y = 5 ** 2      # pangkat

y = 5 / 2       # pembagian, hasilnya float
y = 5 // 2      # pembagian, hasilnya integer (dibulatkan ke bawah)

# Modulus (sisa dari pembagian)
# # x = 42 % 10
# # print(x) # sisa 2

# x = 25 % 5
# print(x) # sisa 0

# y = 26 % 5
# print(y) # sisa 1

# z = 35 % 7
# print(z) # sisa 0

# x = 100e6
# print(x) # sama dengan 100 * 10^6

# y = 100e-6
# print(y) # sama dengan 100 * 10^-6

# Menggunakan math module
import math

# angka = 142.5

# x = math.ceil(angka) # pembulatan ke atas
# print(x) # 143

# x = math.floor(angka) # pembulatan ke bawah
# print(x) # 142

# x = math.pow(angka, 2) # eksponensial
# print(x) 

# x = math.sqrt(angka) # akar kuadrat
# print(x) 

# x = math.fabs(-205)
# print(x) # return nilai absolut dari angka yang dimasukkan, tipe data menjadi float

# x = math.pi
# print(x) # 3.14......

# x = round(123.5875385733, 2) # untuk membulatkan angka decimal di belakang koma menjadi hanya beberapa angka sesuai kebutuhan
# print(x) # output 123.59

# QUIZ

# Berapa luas lingkaran dengan diameter 10cm? Tampilkan dalam decimal dengan 3 angka di belakang koma.

# Solusi

# diameter = 10
# rad = diameter/2
# luas = math.pi * ((10/2)**2)
# print(round(luas, 3))

# import time
# start_time = time.time()

# diameter = 10
# rad = diameter/2
# luas = math.pi * ((10/2)**2)
# print(round(luas, 3))

# print((time.time() - start_time))


# SOAL TAMBAHAN

# Lakukan hanya dengan operasi matematika

# x = 1234
# y = 5678

# output: 3412 
# output: 7856 

# 3412 % 100 = 12 * 100 = 1200
# 3412 // 100 = 34

angka = int(input('Masukkan 4 angka: '))

head = angka%100 * 100 # 12
tail = angka//100 # 34

print(tail + head)




