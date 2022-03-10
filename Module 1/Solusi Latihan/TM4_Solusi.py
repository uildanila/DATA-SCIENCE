# 1

# Output 
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# 13 14 15

# for i in range(1, 16, 3): # output --> 1, 4, 7, 10, 13)
#     for j in range(3):
#         print(i, end = ' ')
#         i += 1
#     print() # metode start: stop: step nya range

# Solusi lain

# x = 0 
# for i in range(5): # jumlah baris yang diperlukan
#     for j in range(0, 3): # jumlah kolom yang diperlukan
#         x += 1
#         print(x, end = ' ')
#     print()
    
# x = 1
# for i in range(5): # 0 1 2 3 4 --> ini yang buat print 5 baris ke bawah # BARIS
#     for j in range(3): # 0 1 2 --> ini yang buat ngeprint 3 kali ke samping # KOLOM
#         print(x, end = ' ') # print x dulu, lalu spasi ke samping
#         x += 1 # lalu looping x + 1 setelahnya
#     print() # ini untuk print ke bawah setelah ada 3 kolom, atau setelah loop j selesai 3x


# 2.

# Output
# 9 8 7
# 6 5 4
# 3 2 1

# x = 10

# for i in range(3):
#     for j in range(3):
#         x -= 1
#         print(x, end = ' ')
#     print()


# 3. 

# * * * * *
# * * * *
# * * *
# * *
# *

# baris = 5

# for i in range(baris + 1, 0, -1): # baris
#     for j in range(0, i - 1): # kolom
#         print('*', end = ' ')
#     print()


# 4.

# * * * * *
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *


# baris = 5

# for i in range(baris + 1, 1, -1): # baris
#     for j in range(0, i - 1): # kolom
#         print('*', end = ' ')
#     print()

# for i in range(1, baris): # baris
#     for j in range(0, i + 1): # kolom
#         print('*', end = ' ')
#     print()


# Cara lain
# stars = ''
# size = 5

# for i in range(size) :
#     for j in range(size - i) :
#         stars += '* '
#     stars += '\n'

# for i in range(1, size) :
#     for j in range(i + 1) :
#         stars += '* '
#     stars += '\n'

# print(stars)


# 5. 

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *

ketupat = ''
size = 5

for i in range(size) :
    for j in range(size - i) : # Akan diselesaikan lebih dahulu
        ketupat += '  '
    for k in range(i * 2 + 1) :
        ketupat += '* '
    ketupat += '\n'

for i in range(1, size) :
    for j in range(i + 1) :
        ketupat += '  '
    for k in range((size * 2) - (i * 2) - 1) :
        ketupat += '* '
    ketupat += '\n'

print(ketupat)


# 6. App Market

# harga_apel = 10000
# harga_jeruk = 15000
# harga_anggur = 20000

# stock_apel = 5
# stock_jeruk = 7
# stock_anggur = 6

# while(True):
#     jumlah_apel = int(input('Masukkan jumlah apel: '))
#     if(jumlah_apel > stock_apel):
#         print(f'Jumlah yang dimasukkan terlalu banyak \nStock apel tinggal: {str(stock_apel)}')
#     else:
#         break
# while(True):
#     jumlah_jeruk = int(input('Masukkan jumlah jeruk: '))
#     if(jumlah_jeruk > stock_jeruk):
#         print(f'Jumlah yang dimasukkan terlalu banyak \nStock jeruk tinggal: {str(stock_jeruk)}')
#     else:
#         break
# while(True) :
#     jumlah_anggur = int(input('Masukkan jumlah anggur: '))
#     if(jumlah_anggur > stock_anggur):
#         print(f'Jumlah yang dimasukkan terlalu banyak \nStock anggur tinggal: {str(stock_anggur)}')
#     else:
#         break

# total_harga_apel = jumlah_apel * harga_apel
# total_harga_jeruk = jumlah_jeruk * harga_jeruk
# total_harga_anggur = jumlah_anggur * harga_anggur
# total_harga = total_harga_anggur + total_harga_apel + total_harga_jeruk

# print(f'''
#     Detail Belanja

#     Apel: {jumlah_apel} x {harga_apel} = {total_harga_apel}
#     Jeruk: {jumlah_jeruk} x {harga_jeruk} = {total_harga_jeruk}
#     Anggur: {jumlah_anggur} x {harga_anggur} = {total_harga_anggur}

#     Total: {total_harga}
#     ''')

# while(True) :
#     jumlah_uang = int(input('Masukkan jumlah uang: '))

#     if(jumlah_uang > total_harga):
#         kembali = jumlah_uang - total_harga
#         print(f'Terima kasih \n\nUang kembalian Anda: {kembali}')
#         break
#     elif(jumlah_uang == total_harga):
#         print('Terima kasih')
#         break
#     else:
#         kekurangan = total_harga - jumlah_uang
#         print(f'Uang Anda kurang sebesar {kekurangan}')

# Untuk contoh for loop seperti ini:
# for i in range(5):
#     print(i)

# # Yang terjadi di balik for loop
# iter_obj = iter(range(5))

# while True:
#     try:
#         i = next(iter_obj)
#         print(i)
#     except StopIteration:
#         break