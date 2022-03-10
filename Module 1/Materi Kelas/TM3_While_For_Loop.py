# LOOPING STATEMENTS
## =================================================================

# Looping digunakan untuk mengeksekusi kode secara berulang, sehingga kode menjadi lebih efisien.

# 2 tipe looping:

# While loop --> looping berdasarkan suatu kondisi, mirip dengan if statement, hanya saja terdapat iterasi/perulangan
    # hingga kondisi yang diinginkan tidak terpenuhi lagi, dengan kata lain looping akan berhenti.

# For loop --> looping dalam jumlah tertentu yang jumlah iterasinya sudah didefinisikan di awal.

## =================================================================

# Cara konvensional
# print('Halo, siapa nama kamu?')
# print('Halo, siapa nama kamu?')
# print('Halo, siapa nama kamu?')
# print('Halo, siapa nama kamu?')
# print('Halo, siapa nama kamu?')

# WHILE LOOP

# Contoh 1

x = 0 # Fungsi akan mulai dari 0 karena kita define x = 0

# while (x < 5):
#     print('Halo, siapa nama kamu?')
#     x += 1 # compound assignment operation, sama dengan x = x+1, yang awalnya x=0, akan ditambah 1
#             # menjadi x=1 dan seterusnya hingga kondisi tidak terpenuhi. Lalu looping akan berhenti.

# Kode compound assignment operator pada while loop sangatlah penting. Kalau tidak ada, maka akan terjadi
    # infinite loop, di mana looping akan terus berulang pada nilai yang sama.

# Jika terjadi infinite loop, pada vscode, cukup klik di terminal, lalu tekan ctrl+c untuk terminate infinite loop-nya.


# Contoh 2

# x = 0

# while (x < 10):
#     print(x, end=' ') # End untuk mengakhiri looping dengan printing ke samping
#                         # ' ' berarti spasi, bisa diisi karakter lain. Bisa juga '', berarti print ke samping tanpa spasi.
#     x += 2


# Contoh 3

# x = -100

# while (x < -10):
#     print(x, end= ' ')
#     x += 1 # Outputnya akan  -100 sampai -11


# Contoh 4

# while x < 10:
#     print('Nilai x saat ini adalah: ', x)
#     print('Nilai x masih lebih kecil dari 10, tambahkan 1 ke x')
#     x += 1


# Contoh 5
# Menambahkan else statement

# while x < 10:
#     print('Nilai x saat ini adalah: ', x)
#     print('Nilai x masih lebih kecil dari 10, tambahkan 1 ke x')
#     x += 1

# else:
#     print('x sudah tidak lagi kurang dari 10')

## =================================================================

# FOR LOOP

# Contoh 1

# for kalimat in range(5): # 0, 1, 2, 3, 4
#     print('Halo, siapa nama kamu?')

# range() function menghasilkan sequence numbers
# Secara default mulai dari 0, meningkat sebanyak 1, dan berhenti sebelum angka yang didefinisikan


# Contoh 2

# for i in range(0, 12, 3): # start, stop, step
#     print(i) # i adalah variabel untuk memanggil semua elemen dalam range

# for i in range(12, 3): # start, stop, step
#     print(i) # tidak akan error, tapi tidak ada output apa-apa. Nilai start harus didefinisikan kalau tidak
#                 # menggunakan default step (increment)


# Contoh 3

# angka = [1, 2, 3, 4, 5, 6]

# for i in angka:
#     print(i, end='') # 123456

# for i in angka:
#     if i % 2 == 1:
#         print(i, end='') # 135


# Contoh 4

# for i in range(11):
#     if i % 2 == 1:
#         print(i)
#     else:
#         print('Angka genap')


# Contoh 5
# For loop dengan list (salah satu collection data types)
# Kita juga bisa mengalkulasi kumpulan angka dengan for loop

# daftar_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 0
# output --> 55

# Solusi 1 (Nila)
# for angka in range(0, len(daftar_angka)+1):
#     total += angka
# print(total)

# for angka in range(0, len(daftar_angka)): # 0 1 2 3 4 5 6 7 8 9
#     total = total + daftar_angka[angka] 
# print(total)


# Contoh 6
# list1 = ['Apel', 'Jeruk', 'Mangga']

# # output --> Apel, Jeruk, Mangga

# for i in range(len(list1)):
#     print(list1[i])


# Contoh 7
# Kita juga dapat menggunakan for loop untuk string
# Setiap elemen pada string akan diiterasi

# for huruf in 'Ini adalah sebuah string':
#     print(huruf)


# Contoh 8
# For loop pada tuple (collection data type)

# tuple1 = [(2, 4), (3, 6), (4, 8)]

# for tup in tuple1:
#     print(tup) # output (2, 4) (3, 6) (4, 8)

# Bagaimana jika kita hanya ingin mengambil item pertama atau kedua dari tiap tuple?

# for tup in tuple1:
#     print(tup[0]) # output 2, 3, 4

# Tuple unpacking
# for t1, t2 in tuple1:
#     print(t1) # output 2, 3, 4


# Contoh 9
# For loop pada dictionary (salah satu collection data types)

# dict1 = {'n1': 1, 'n2':2, 'n3':3}

# for item in dict1:
#     print(item) # output -->  n1 n2 n3

# Bagaimana kalau kita ingin mengambil nilai value dari tiap key saja?
# Output --> 1 2 3

# for item in dict1:
#     print(item[1]) # output --> 1 2 3

# Cara lain
# Dictionary unpacking
# for key, value in dict1.items():
#     print(value) # output --> 1, 2, 3

## =================================================================

# SPEED, SPACE, and MAINTAINABILITY

# SPEED --> seberapa cepat kode ketika dieksekusi

# print('halo dunia') # 10000 kali --> ini lebih cepat 

# for i in range(10000):
#     print('halo dunia') # lebih lambah karena banyak step yang perlu diselesaikan: cek range sampai 10000, baru print


# SPACE --> seberapa besar memori yang akan digunakan ketika kode disimpan. Lebih kecil berarti lebih baik.

# print('halo dunia') # 10000 kali --> membutuhkan space lebih besar pada ROM atau harddisk

# for i in range(10000): # membutuhkan space lebih besar pada RAM karena lebih banyak instruksi yang dikerjakan
#     print('halo dunia')


# MAINTAINABILITY --> seberapa mudah kode untuk di-maintain, misal jika ada bug ada kita mau update kode.

# print('halo dunia')
# print('halo dunia')
# print('halo dunia')
# print('halo dunia')

# x = 'halo dunia' 
# print(x) # mudah dimaintain
# print(x)
# print(x)

# for i in range(4): # Lebih mudah dimaintain
#     print(x)

# Dalam menuliskan kode, harus dipikirkan speed, space, dan maintainability secara seimbang sesuai kebutuhan

## =================================================================

# import this # Guideline untuk menyusun kode
# print(this)

## =================================================================

# LATIHAN

# 1. kalimat = 'Kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat ini'

# - for loop
# - split()
# - indexing
# - conditional statement

# kalimat = 'Kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat ini'

# for kata in kalimat.lower().split():
#     if kata[0] == 'k':
#         print(kata)
#     else:
#         print('kata tidak berawalan huruf k')

# Output = kamu, kata, k, kalimat


# 2. Dari angka 1 hingga 50, tampilkan angka yang dapat dibagi 3!

# for angka in range(1, 51):
#     if angka % 3 == 0:
#         print(angka)

# 3. kalimat = 'Tampilkan kata yang memiliki jumlah karakter berjumlah genap pada kalimat ini'

# Tampilkan kata yang memiliki jumlah karakter berjumlah genap!

# for kata in kalimat.split():
#     if len(kata) % 2 == 0:
#         print(f'{kata} adalah kata yang memiliki karakter berjumlah genap.')


# 4. Buatlah program yang menampilkan integer dari 1 hingga 100 dengan spesifikasi:
        # - Jika angka merupakan kelipatan 3, maka print 'kelipatan 3'
        # - Jika angka merupakan kelipatan 5, maka print 'kelipatan 5'
        # - Jika angka merupakan kelipatan 3 dan 5, maka print 'kelipatan 3 & 5'

    # Gunakan user input!

# for angka in range(1, 101):
#     if angka % 3 == 0 and angka % 5 == 0:
#         print('kelipatan 3 & 5')
#     elif angka % 3 == 0:
#         print('kelipatan 3')
#     elif angka % 5 == 0:
#         print('kelipatan 5')
#     else:
#         print(angka)

# Dengan while loop
angka = int(input('Masukkan angka: '))

while True:
    if angka % 3 == 0 and angka % 5 == 0:
        print('kelipatan 3 & 5')
        break
    elif angka % 3 == 0:
        print('kelipatan 3')
        break
    elif angka % 5 == 0:
        print('kelipatan 5')
        break
    else:
        print('angka ini bukan merupakan kelipatan 3 dan/atau 5')
        break