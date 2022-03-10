# BREAK, CONTINUE, PASS (LOOP CONTROL STATEMENTS)
## ============================================================

# Kita dapat menggunakan break, continue, dan pass statements dalam loop untuk menambah
    # fungsional tambahan dalam bermacam-macam kasus.

# Break --> memberhentikan proses looping
# Continue --> melewati tugas yang ada pada iterasi yang sedang dijalankan, lalu akan kembali ke awal looping (iterasi selanjutnya)
# Pass --> tidak melakukan apa-apa

## ============================================================

# REVIEW MATERI

# Contoh 1

# x = 5

# while x > 0:
#     print(x)
#     x -= 1
# print('SELESAI')


# Contoh 2

# x = 10

# while True:
#     print(x, end=' ')
#     x -= 1
# print('SELESAI') # Output: infinite loop

## ============================================================

# Contoh 1

# kalimat = 'kita sedang belajar control loop statements'

## Contoh untuk continue
# for huruf in kalimat:
#     if huruf == 'o':
#         continue
#     print(huruf)

## Contoh untuk break
# for huruf in kalimat:
#     if huruf == 'd':
#         break
#     print(huruf)

# # Contoh untuk pass
# for huruf in kalimat:
#     pass # Digunakan jika misalnya kita tahu kalau kita perlu menggunakan loop, tapi belum tahu statement-nya


# Contoh 2

# angka = int(input('Masukkan angka: '))

# while True:
#     if angka % 3 == 0 and angka % 5 == 0:
#         print('kelipatan 3 & 5')
#         break
#     elif angka % 3 == 0:
#         print('kelipatan 3')
#         break
#     elif angka % 5 == 0:
#         print('kelipatan 5')
#         break
#     else:
#         print('angka ini bukan merupakan kelipatan 3 dan/atau 5')
#         break


# Contoh 3

# x = 0

# while x < 10:
#     x += 1
#     print(f'Ini adalah angka {x}')

#     if x == 3:
#         print('Angka 3 ketemu!\n')
#         continue
#     elif x == 10:
#         print('Angka sudah tidak kurang dari 10')
#         break

#     print('Angka masih kurang dari 10')
#     print('Lanjutkan proses ke angka selanjutnya')


# Contoh 4

# x = 0

# while x < 10:
#     print('Nilai x saat ini adalah', x)
#     print('Nilai x masih lebih kecil dari 10, menambahkan 1 pada x\n')

#     if x == 3:
#         print('Looping berhenti karena x = 3')
#         break
#     else:
#         print('Lanjutkan proses ke angka selanjutnya\n')
#         x += 1


# Contoh 5
# Break juga bisa digunakan untuk dapat keluar dari looping ketika kondisi untuk keluar dari looping sudah terpenuhi

# while True:
#     inputan_user = input('Masukkan kata: ')
#     if inputan_user.lower() == 'selesai': # Pada contoh ini, kita menyatakan secara eksplisit bahwa looping akan selesai
                                                # ketika inputan user adalah 'selesai'
#         break
#     print(inputan_user)

# print('Looping selesai')


# Contoh 6

# while True:
#     inputan_user = input('Masukkan kata: ')
#     if inputan_user[0].lower() == 'm': # jika kata yang dimasukkan memiliki huruf depan 'm', maka proses looping akan kembali ke awal
#         continue
#     elif inputan_user.lower() == 'selesai': # jika inputan adalah 'selesai', maka looping akan berhenti, dan melanjutkan tugas yang 
#                                                 # ada di luar looping
#         break
#     print(inputan_user) # Hanya akan dijalankan, jika user memasukkan kata selain kata yang huruf depannya 'm'

# print('Looping selesai') # Hanya akan dijalankan, jika user memasukkan kata 'selesai'


# Contoh 7

# x = [1, 2, 3]

# for item in x:
#     pass # jika pass statement tidak dinyatakan, maka akan error ketika kode dijalankan

# print('Akhir dari kode')


# Contoh 8

# kata = 'Purwadhika'

# for huruf in kata:
#     if huruf == 'a':
#         continue
#     print(huruf) # output: Purwdhik --> setiap huruf 'a' akan diabaikan, tidak tercetak di terminal

# for huruf in kata:
#     if huruf == 'a':
#         break
#     print(huruf) # output: Purw --> looping berhenti ketika ketemu huruf 'a'

## ============================================================

# NESTED LOOP
## ============================================================

# Loop di dalam loop.
# Inner loop akan diselesaikan terlebih dahulu sebelum lanjut ke outer loop.
# While loop bisa terdapat for loop di dalamnya, dan juga sebaliknya.

# Contoh analogi makan

# sendok = range(1, 6) # 1 2 3 4 5
# piring = ['nasi', 'lauk', 'sayur', 'sambal']

# for suapan in sendok: # outer loop
#     print(f'Ini adalah suapan ke {suapan}')

#     for isi in piring: # inner loop --> akan diselesaikan terlebih dahulu untuk bisa lanjut ke iterasi outer loop selanjutnya
#         print(isi)
#     print() # Mencetak baris kosong


# Contoh 1

# for i in range(5): # 0 1 2 3 4 
#     for j in range(3): # 0 1 2
#         print(i, end=' ')
#     print() # Ditambah print kosong, untuk pindah baris setelah print i selesai

# i dikerjakan pertama, yaitu 0, lalu loop ke j, lalu minta print i. Lalu, j kembali i, lanjut print lagi.
# Setelah j habis, maka ketika kembali ke i, akan bergeser ke index selanjutnya, dan begitu seterusnya hingga selesai.

# Output:
# 0 0 0
# 1 1 1
# 2 2 2
# 3 3 3
# 4 4 4 


# Contoh 2

# i = 1 # 2
#                 # untuk iterasi pertama:
# while (i <= 5): # i = 1
#     j = 5 # j = 5

#     while (j >= i): # 5 >= 1
#         print(j, end=' ') # kondisi terpenuhi, print j dan ke samping
#         j -= 1 # kurangi 1 untuk j

#     i += 1 # kalau inner loop sudah selesai, masuk looping kedua dengan i ditambah 1
#     print() # untuk enter atau pindah ke baris baru


## ============================================================

# ENUMERATE()

# index_count = 0
# kata = 'semua'

# for i in kata:
#     print(f'Pada index {index_count} hurufnya adalah {i}')
#     index_count += 1

# Enumerate --> mengembalikan dalam bentuk tipe data tuple, dan otomatis ada penambahan 1 index untuk tiap iterasi

# for i in enumerate(kata):
#     print(i)

# Tuple unpacking

# for i, j in enumerate(kata):
#     print(f'Pada index {i} hurufnya adalah {j}')

## ============================================================

# LOOPING DRAWING
## ============================================================

# Menggambar berbagai pola dengan menggunakan kode Python

# Contoh 1
# Menggambar persegi panjang

# baris = 4
# kolom = 8

# for i in range(baris): # baris
#     for j in range(kolom): # kolom
#         print('*', end=' ')
#     print()


# Contoh 2
# Menggambar segitiga siku-siku

# x = int(input('Masukkan tinggi segitiga siku-siku: '))

# for i in range(0, x):  # BARIS 
#     for j in range(0, i): # KOLOM
#         print('*', end=' ')  
#     print()

# ================================================================

# Latihan sesi materi

# 1. 
# Output: 10 8 6 4 2 0

# x = 12

# for i in range(x):
#     x -= 2
#     if x >= 0:
#         print(x, end=' ')


# for i in range(10, -1, -2): # start stop step
#     print(i, end=' ')


# 2.
# Output:
# 1 2 3
# 1 2 3
# 1 2 3

# for i in range(3):
#     for j in range(3):
#         print(j + 1, end=' ')
#     print()

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(j, end=' ')
#     print()
