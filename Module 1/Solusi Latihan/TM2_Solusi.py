# # SOAL DARI SLIDE
# # =================================================================

# Soal 1
# Buat input angka dan print apakah angka tersebut bilangan genap atau ganjil.

# angka = int(input('Masukkan angka: '))

# if angka%2 == 0:
#     print(f'{angka} adalah bilangan genap')
# else:
#     print(f'{angka} adalah bilangan ganjil')



# # =================================================================
# Soal 2
# Buat user input untuk massa badan dan tinggi badan.
# Bulatkan IMT 1 angka dibelakang koma

# massa = int(input('Masukkan massa badan: '))
# tinggi = int(input('Masukkan tinggi badan: '))

# imt = massa/(tinggi/100)**2
# imt = round(imt, 1)

# if imt < 18.5:
#     print(f'IMT = {imt}, berat badan kurang')
# elif imt <= 24.9:
#     print(f'IMT = {imt}, berat badan ideal')
# elif imt <= 29.9:
#     print(f'IMT = {imt}, berat badan berlebih')
# elif imt <= 39.9:
#     print(f'IMT = {imt}, berat badan sangat berlebih')
# else:
#     print(f'IMT = {imt}, berat badan obesitas')



# # =================================================================
# Soal 3 

# listA = [True, 13, 'Hello', 2.7] 

# buatlah program untuk mengetahui tipe data dari tiap item dengan menggunakan conditional if
# buat user input berisi index dari listA ('Masukkan index:')
# contoh output:
# - True bertipe data boolean
# - 2.7 bertipe data float

#SOLUSI
# index = int(input('Masukkan index: '))

# listA = [True, 13, 'Hello', 2.7] 

# item = listA[index]
# tipe = type(item)

# print(tipe)

# if tipe == str:
#     print(f'{item} bertipe data string') 
# elif tipe == bool:
#     print(f'{item} bertipe data boolean') 
# elif tipe == int:
#     print(f'{item} bertipe data integer') 
# elif tipe == float:
#     print(f'{item} bertipe data float')

# Cara penulisan lain

# if type(listA[index]) == str:
#     print(f'{listA[index]} bertipe data string') 
# elif type(listA[index]) == bool:
#     print(f'{listA[index]} bertipe data boolean') 
# elif type(listA[index]) == int:
#     print(f'{listA[index]} bertipe data integer') 
# elif type(listA[index]) == float:
#     print(f'{listA[index]} bertipe data float') 




# # =================================================================
# Soal 4
# masukkan angka antara 1-99
# jika x adalah bilangan puluhan, munculkan 'x adalah puluhan'. 
# kemudian jika bilangan puluhan tersebut genap, munculkan 'x adalah bilangan genap'
# kemudian jika bilangan puluhan tersebut ganjil, munculkan 'x adalah bilangan ganjil'
# jika x adalah bilangan satuan, cukup munculkan 'x adalah satuan'
# coba gunakan range()


# x = int(input('Masukkan angka antara 1 hingga 99: '))

# if x in range(10, 100): # 10,11,12,13, ...., 97,98,99
#     print(f'{x} adalah puluhan')

#     if x % 2 == 0:
#         print(f'{x} adalah bilangan genap')
#     else:
#         print(f'{x} adalah bilangan ganjil')

# else:
#     print(f'{x} adalah satuan')



# x = int(input('Masukkan angka 1-99: '))

# if x in range(10, 100, 2): # 10,12,14,....,96,98
#     print(f'{x} adalah puluhan')
#     print(f'{x} adalah bilangan genap')

# elif x in range(11, 100, 2): # 11,13,15,.....,97,99
#     print(f'{x} adalah puluhan')
#     print(f'{x} adalah bilangan ganjil')

# else:
#     print(f'{x} adalah satuan')



# # =================================================================
# Soal 5
# Gunakan user input

# input: masukkan 2 kata: makan hati
# output: hati makan

# kata = input('Masukkan 2 kata: ')

# kata_list = kata.split()

# print(kata_list[1], kata_list[0])

# # =================================================================
# Soal 6
# Gunakan user input

# input = Purwadhika
# output = Puka (2 huruf pertama dan 2 huruf terakhir dari input)

# x = str(input("Masukkan kata: "))

# print(x[:2], x[-2:])

# # =================================================================
# Soal 7
# x = [1, 2, 3, 4, 5]
# output: 1 + 2 + 3 + 4 + 5 = 15

# x = [1, 2, 3, 4, 5]

# print(f'{x[0]} + {x[1]} + {x[2]} + {x[3]} + {x[4]} = {sum(x)}')


# # =================================================================
# Soal 8
# x = '32.054,23'
# # # output = '32,054.23' (koma diganti titik, titik diganti koma)

# list_angka = list(x)
# list_angka[2], list_angka[6] = list_angka[6], list_angka[2]
# print(''.join(list_angka))


# TAKE HOME ASSIGNMENT SOLUTION

# No. 6
harga_apel = 10000
harga_jeruk = 15000
harga_anggur = 20000

jumlah_apel = int(input('Masukkan jumlah apel: '))
jumlah_jeruk = int(input('Masukkan jumlah jeruk: '))
jumlah_anggur = int(input('Masukkan jumlah anggur: '))

# Opsi dibuat variabel
total_harga_apel = jumlah_apel * harga_apel
total_harga_jeruk = jumlah_jeruk * harga_jeruk
total_harga_anggur = jumlah_anggur * harga_anggur

total_belanja = total_harga_apel + total_harga_jeruk + total_harga_anggur

# Opsi langsung dioperasikan di dalam print
print(f'''
        Apel: \t {jumlah_apel} x {harga_apel} = {jumlah_apel*harga_apel}
        Jeruk:\t {jumlah_jeruk} x {harga_jeruk} = {jumlah_jeruk*harga_jeruk}
        Anggur:\t {jumlah_anggur} x {harga_anggur} = {jumlah_anggur*harga_anggur}

        Total belanja: {total_belanja}
        ''')


# No. 3

# jumlah_apel = int(input('Masukkan jumlah apel: '))
# jumlah_jeruk = int(input('Masukkan jumlah jeruk: '))
# jumlah_anggur = int(input('Masukkan jumlah anggur: '))

# # Diketahui harga buah sebagai berikut:
# harga_apel = 10000
# harga_jeruk = 15000
# harga_anggur = 20000

# print(f'''\nDetail Belanja\n
#         Apel: \t {jumlah_apel} x {harga_apel} = {jumlah_apel*harga_apel}
#         Jeruk:\t {jumlah_jeruk} x {harga_jeruk} = {jumlah_jeruk*harga_jeruk}
#         Anggur:\t {jumlah_anggur} x {harga_anggur} = {jumlah_anggur*harga_anggur}
#         ''')

# total_belanja = (jumlah_apel*harga_apel) + (jumlah_jeruk*harga_jeruk) + (jumlah_anggur*harga_anggur)
# print(f'Total belanjaan Anda Rp.{total_belanja}')

# bayar = int(input('Masukkan jumlah uang Anda: '))

# if bayar > total_belanja:
#     print(f'Uang kembalian Anda: {bayar-total_belanja}')
#     print('Terima kasih')
# elif bayar == total_belanja:
#     print('Terima kasih')
# else:
#     print('Transaksi Anda dibatalkan')
#     print(f'Uang Anda kurang: {total_belanja-bayar}')



