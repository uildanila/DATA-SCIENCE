# COLLECTION DATA TYPES
## ===================================================================

# LIST

# - Dapat menyimpan berbagai jenis tipe data (string, integer, boolean, list, tuple, dll.) secara bersamaan.
# - Dapat memiliki data yang sama nilainya atau duplikat.
# - Kita dapat mengubah elemen yang ada di dalam suatu list.append
# - Ditandai dengan tanda []

# Syntax

# contoh_list = ['Halo', 1, 10, 100, True]
# index:           0     1   2   3     4
# negative index: -5    -4  -3  -2    -1

# Kita dapat mengakses element pada sua list melakukan indexing.

# print(contoh_list[0])
# print(contoh_list[1])
# print(contoh_list[2])
# print(contoh_list[-3])
# print(contoh_list[-5])


# Akses data menggunakan range of index (slicing)

# contoh_list = ['Halo', 1, 10, 100, True]
# index:           0     1   2   3     4
# negative index: -5    -4  -3  -2    -1

# print(contoh_list[-4: -1]) # [1, 10, 100]
# print(contoh_list[-5: 2]) # ['Halo', 1]
# print(contoh_list[2:]) # [10, 100, True]
# print(contoh_list[:2]) # ['Halo', 1]


# Mengubah data pada List

# contoh_list = ['Halo', 1, 10, 100, True]

# contoh_list[1] = 'Purwadhika'
# print(contoh_list) # ['Halo', 'Purwadhika', 10, 100, True]

# contoh_list.replace(10, 20) # function replace hanya untuk string


# Menambah data pada List (append() dan insert())

# contoh_list.append('Hai') 
# print(contoh_list) # ['Halo', 1, 10, 100, True, 'Hai']

# contoh_list.insert(4, False)
# print(contoh_list) # ['Halo', 1, 10, 100, False, True]


# Menghapus data pada List

# contoh_list = ['Halo', 'Hai', 1, 10, 100, 'Hai', True]

# contoh_list.remove('Hai')
# print(contoh_list) # Hanya menghapus 'Hai' pertama (index 1)

# contoh_list.pop()
# print(contoh_list) # Menghapus item terakhir

# del contoh_list[1] 
# print(contoh_list) # Menghapus sesuai nomor index yang didefinisikan

# contoh_list.clear()
# print(contoh_list) # Menghapus semua item pada List --> []


# Looping pada List

# contoh_list = ['Halo', 'Hai', 1, 10, 100, 'Hai', True]

# for i in contoh_list:
#     print(i)


# Mengecek jika suatu item berada di list

# contoh_list = ['Halo', 'Hai', 1, 10, 100, 'Hai', True]

# if 'Halo' in contoh_list:
#     print('Ada')
# else:
#     print('Tidak ada')


# Mengecek banyaknya jumlah item pada suatu List

# contoh_list = ['Halo', 'Hai', 1, 10, 100, 'Hai', True]
# print(len(contoh_list)) # 7


# Cara duplikasi suatu List

# contoh_list = ['Halo', 'Hai', 1, 10, 100, 'Hai', True]

# list_baru = contoh_list
# list_baru[1] = 200000

# list_baru2 = contoh_list.copy()
# list_baru2[2] = 'Bandung'

# print(list_baru) # ['Halo', 200000, 1, 10, 100, 'Hai', True]
# print(contoh_list) # ['Halo', 'Hai', 1, 10, 100, 'Hai', True]
# print()
# print(list_baru2) # ['Halo', 200000, 'Bandung', 10, 100, 'Hai', True]
# print(contoh_list) # ['Halo', 'Hai', 1, 10, 100, 'Hai', True]

# Kalau kita punya list lain:
# contoh_list2 = [1, 2, 3, 4]

# contoh_list[0] = contoh_list2[1]
# print(contoh_list) # Mengubah item pada satu list dengan item dari list lainnya

# contoh_list.append(contoh_list2)
# print(contoh_list) # Menambahkan item sesuai dengan tipe data yang ditambahkan

# contoh_list.extend(contoh_list2)
# print(contoh_list) # Menambahkan item ke dalam list yang outputnya menjadi hanya 1 list saja

# Indexing list di dalam list
# print(contoh_list[-1][2]) # 3 
# print(contoh_list[7][0]) # 1


# List Concatenation (Menggabungkan beberapa List)

# contoh_list = ['Halo', 1, 10, 100, True]
# list_baru = [9, 8, 6, 4]
# list_lain = ['Surabaya', 500000]

# # list_gabungan = contoh_list + list_baru
# list_gabungan = list_baru + contoh_list
# print(list_gabungan) # Urutan output sesuai dengan urutan list yang dituliskan

# list_gabungan.extend(list_lain)
# print(list_gabungan) # List yang ditambahkan akan menyatu dengan list utama


# Mencari index pada List

# nama = ['Andi', 'Budi', 'Caca', 'Dedi', 'Erika']
# cari_index = nama.index('Caca')

# print(cari_index) # 2

# cari_index2 = nama.index('Eno')
# print(cari_index2) # Error, karena tidak ada 'Eno' di dalam List


# Sorting

# nama = ['Andi', 'Rudi', 'Tata', 'Boni']
# nama.sort()
# print(nama) # Diurutkan sesuai dengan alphabet

# # Kalau ada alphabet huruf kecil
# nama = ['Andi', 'Rudi', 'Tata', 'Boni', 'ayu']
# nama.sort()
# print(nama) # ['Andi', 'Boni', 'Rudi', 'Tata', 'ayu'] --> Huruf kapital diurutkan terlebih dahulu


# Reverse

# nama = ['Andi', 'Rudi', 'Tata', 'Boni']
# nama.reverse()
# print(nama) # Hanya dibalik urutan berdasarkan index saja, bukan berdasarkan alphabet


# 2D List

# benda = [
#     ['pulpen_biru', 'pulpen_merah'],
#     ['bola_futsal', 'bola_tenis', 'bola_basket'],
#     ['piring', 'sendok']
# ]

# print(benda[2]) # ['piring', 'sendok']
# print(benda[1][2]) # ['bola_basket'] 


# 3D List

# Input: 
# 3 x 3 x 3

# Output:
# [[['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']],
#  [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']],
#  [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]]


# Input:
# 5 x 3 x 2

# Output:
# [[['#', '#', '#', '#', '#'],
#   ['#', '#', '#', '#', '#'],
#   ['#', '#', '#', '#', '#']],
#  [['#', '#', '#', '#', '#'],
#   ['#', '#', '#', '#', '#'],
#   ['#', '#', '#', '#', '#']]]


# List Comprehension

# - Cara cepat untuk membuat sebuah list yang basis logikanya berasal dari for loop.
# - Jika kode yang mau dituliskan ternyata cukup kompleks, seperti terdapat if else
    # condition, maka lebih baik gunakan for loop, untuk readability yang lebih baik.

# Contoh 1
# contoh_string = 'Halo'
# contoh_list = []

# Cara for loop
# for huruf in contoh_string:
#     contoh_list.append(huruf)
# print(contoh_list)

# Bandingkan dengan menggunakan list comprehension
# contoh_listcomp = [i for i in contoh_string] # nama temporary variabel bisa apa saja
# print(contoh_listcomp)

# Contoh 2
# kalimat = [i for i in 'kalimat']
# print(kalimat)

# Contoh 3
# angka = [x for x in range(10)]
# print(angka)

# Contoh 4
# kuadrat = [x**2 for x in range(10)]
# print(kuadrat)

# Contoh 5
# Menambahkan if statement pada list comprehension

# contoh_if = [x for x in range(11) if x%2 == 0]
# print(contoh_if)

# Contoh 6
# Nestep loop

# mylist = []

# # For loop
# for x in [2, 4, 6]:
#     for y in [100, 200, 400]:
#         mylist.append(x*y)

# print(mylist) # []

# # List comprehension
# mylistcompre = [x*y for x in [2, 4, 6] for y in [100, 200, 400]]
# print(mylistcompre)

## ===================================================================

# TUPLE

# - Mirip seperti list, dapat menyimpan banyak value dengan berbagai tipe data,
#     tetapi item tidak dapat diubah setelah dibuat.
# - Dapat di-indexing.
# - Ditandai dengan ()

# Syntax

# contoh_tuple = ('Halo', 1, 10, 100, True)

# Indexing
# print(contoh_tuple[0]) # Halo

# Negative indexing
# print(contoh_tuple[-1]) # True


# Slicing
# print(contoh_tuple[-4: -1]) # (1, 10, 100)


# Mengubah data pada Tuple
# contoh_tuple = ('Halo', 1, 10, 100, True)
# contoh_tuple[1] = 100 
# print(contoh_tuple) # Error

# Agar tidak error, kita bisa menyiasatinya dengan mengubah tuple ke dalam list,
    # lalu diubah ke tuple lagi.

# list_contoh = list(contoh_tuple)
# list_contoh[1] = 100
# contoh_tuple = tuple(list_contoh)
# print(contoh_tuple)


# Looping pada tuple

# contoh_tuple = ('Halo', 1, 10, 100, True)

# for i in contoh_tuple:
#     print(i)


# Cek jika item ada pada tuple

# contoh_tuple = ('Halo', 1, 2, 4, True)

# if 'Halo' in contoh_tuple:
#     print('Ada')
# else:
#     print('Tidak ditemukan')


# Cek jumlah item pada tuple

# contoh_tuple = ('Halo', 1, 2, 4, True)

# print(len(contoh_tuple)) # 5


# Cara membuat tuple hanya dengan 1 item
# Harus tambahkan koma di akhir sebelum kurung tutup

# tuple1 = ('halo',)
# print(tuple1) # ('halo')
# print(len(tuple1)) # 1
# print(type(tuple1)) # <class 'tuple'>

# Jika tidak memakai koma di akhir, tidak akan menjadi tuple
# tuple2 = ('halo')
# print(tuple2) # 'halo'
# print(type(tuple2)) # <class 'str'>


# Tuple concatenating

# contoh_tuple = ('Halo', 1, 2, 4, True)
# tuple_tambah = (5, 6, False)

# tuple_gabungan = contoh_tuple + tuple_tambah
# print(tuple_gabungan) # ('Halo', 1, 2, 4, True, 5, 6, False)


# Mencari index pada tuple

# nama_tuple = ('edi', 'bambang', 'septi', 'lodri')
# cari_tuple = nama_tuple.index('septi')

# print(cari_tuple) # 2

# cari_tuple2 = nama_tuple.index('kyu')
# print(cari_tuple2) # Error


# Nested tuple

# benda = (
#     ('ayam', 'kucing'),
#     ('jam', 'celana'),
#     ('meja', 'kursi')
# )

# benda[1] # ('jam', 'celana')
# benda[1][1] # 'celana'

## ===================================================================

# # DICTIONARY

# # - Kontainer yang bisa menampung banyak value dengan beragam tipe data, tetapi bersifat tidak berurutan.
# # - Ditandai {}
# # - Memiliki key dan value, di mana key berupa kata kunci unik dan berfungsi mirip seperti index pada list.append
# # - Indexing menggunakan nama key.
# # - Gunakan Dictionary bila ingin menyimpan data yang lebih dari 1, tetapi saat data tersebut tidak memiliki 
# #     pola atau tipe data yang sama tetapi berhubungan satu dengan yang lainnya.

# # Syntax

# dictionary1 = {'key1': 'value1'}

# print(dictionary1) # {'key1': 'value1'}
# print(dictionary1['key1']) # value1
# print(dictionary1[1]) # Error, karena tidak bisa indexing dictionary dengan menggunakan angka index.

# for key in dictionary1:
#     print(key)
#     print(dictionary1[key])


# # Membuat Dictionary

# # Cara 1
# dict1 = {
#     'nama': 'Andi',
#     'usia': 25,
#     'pekerjaan': 'Data Scientist'
# }

# # print(dict1)

# # Cara 2 (Menggunakan built in function dict())
# dict2 = dict(nama='Budi', usia='26', pekerjaan='Data Analyst')
# print(dict2)


# # Mengakses data pada dictionary

# dict1 = {
#     'nama': 'Andi',
#     'usia': 25,
#     'pekerjaan': 'Data Analyst',
#     'menikah': False
# }

# print(dict1['nama']) # Andi
# print(dict1.get('menikah')) # False


# # Mengubah data

# dict1 = {
#     'nama': 'Andi',
#     'usia': 25,
#     'pekerjaan': 'Data Analyst'
# }

# dict1['usia'] = 27
# print(dict1)


# # Menambah data

# dict1 = {
#     'nama': 'Andi',
#     'usia': 25,
#     'pekerjaan': 'Data Analyst'
# }

# dict1['kelamin'] = 'Pria'
# print(dict1)


# # Menghapus data

# dict1 = {
#     'nama': 'Andi',
#     'usia': 25,
#     'pekerjaan': 'Data Analyst',
#     'menikah': False
# }

# del dict1['usia']
# dict1.pop('nama')
# dict1.popitem() # Menghapus item terakhir

# print(dict1)

# dict1.clear() # Mengosongkan dictionary
# print(dict1) # {}


# # Looping pada dictionary

# dict1 = {
#     'nama': 'Andi',
#     'usia': 25,
#     'pekerjaan': 'Data Analyst',
#     'menikah': False
# }

# # Loop langsung pada dictionary
# for key in dict1:
#     print(f'{key} = {dict1[key]}')

# # Loop pada data yang dihasilkan oleh method keys 
# for key in dict1.keys():
#     print(f'{key} = {dict1[key]}')

# # Loop pada data yang dihasilkan oleh method values
# for val in dict1.values():
#     print(val)

# # Loop pada data yang dihasilkan oleh method items
# for key, val in dict1.items():
#     print(f'{key} = {val}')


# # Cek jika key ada pada dictionary

# dict1 = {
#     'nama': 'Andi',
#     'usia': 25,
#     'pekerjaan': 'Data Analyst',
#     'menikah': False
# }

# if 'usia' in dict1:
#     print('Ada key usia')
# else:
#     print('Tidak ditemukan')


# # Cek jumlah key value pairs pada dictionary

# dict1 = {
#     'nama': 'Andi',
#     'usia': 25,
#     'pekerjaan': 'Data Analyst',
#     'menikah': False
# }

# print(len(dict1)) # 4


# # Cara copy dictionary

# dict1 = {
#     'nama': 'Andi',
#     'usia': 25,
#     'pekerjaan': 'Data Analyst',
#     'menikah': False
# }

# dict_baru = dict1
# dict_baru['nama'] = 'Brodi'

# dict_baru2 = dict1.copy()
# dict_baru2['usia'] = 29

# print(dict_baru) # {'nama': 'Brodi', 'usia': 25, 'pekerjaan': 'Data Analyst', 'menikah': False}
# print(dict_baru2) # {'nama': 'Brodi', 'usia': 29, 'pekerjaan': 'Data Analyst', 'menikah': False}
# print(dict1) # {'nama': 'Brodi', 'usia': 25, 'pekerjaan': 'Data Analyst', 'menikah': False}


# # Nested dictionary

# makanan = {
#     'pembuka':{
#         'nama':'Sup',
#         'harga':20000
#     },
#     'main_course':{
#         'nama':'Nasi goreng',
#         'harga':40000
#     },
#     'penutup':{
#         'nama':'Puding',
#         'harga':15000
#     }
# }

# makanan['pembuka'] # {'nama':'Sup', 'harga':20000}
# makanan['penutup']['nama'] # 'Puding

## ===================================================================

# # TM6

# SET

# - Dapat digunakan untuk menyimpan banyak value dengan berbagai tipe data.
# - Pada set, setiap value adalah unik, tidak ada perulangan atau duplikat, dan bersifat unordered.
# - Ditandai dengan {}
# - Set bisa digunakan untuk memfilter data duplikat.
# - Kita tidak bisa melakukan indexing pada set karena sifatnya unorderd, tapi bisa diiterasi melalui looping.


# Syntax


# my_set = {'Spiderman', 'Iron Man', 'The Avenger', 'Spiderman'}
# print(my_set)

# print(my_set[0]) # Error, tidak bisa indexing

# for i in my_set:
#     print(i) # Output akan acak tiap kali run 


# Membuat set dari list, tuple, dictionary

# list1 = ['Budi', 2, 2, 'Cici', 'Budi']
# tuple1 = (False, 1, 'Andi', False)
# dict1 = {
#     'nama': 'Budi',
#     'usia': 24
# }

# set_list1 = set(list1)
# set_tuple1 = set(tuple1)
# set_dict1 = set(dict1)
# set_dict_val = set(dict1.values())

# print(set_list1)
# print(set_tuple1)
# print(set_dict1)
# print(set_dict_val)


# Akses data pada set

# my_set = {'Spiderman', 'Iron Man', 'The Avenger', 'Spiderman 3'}

# for item in my_set:
#     print(item)


# Cek jika item pada set

# my_set = {'Spiderman', 'Iron Man', 'The Avenger', 'Spiderman 3'}

# if 'Iron Man' in my_set:
#     print('Ada')
# else:
#     print('Tidak ada')


# Menambah data pada set

# my_set = {'Spiderman', 'Iron Man', 'The Avenger', 'Spiderman'}

# # my_set.add('Hulk')
# # print(my_set)

# my_set.update({'Iron Man', 'Ant Man'})
# print(my_set) # Iron Man tidak akan ditambahkan pada set karena sudah ada sebelumnya. Hanya Ant Man saja yang ditambahkan.



# Menghapus data pada set

# my_set = {'Spiderman', 'Iron Man', 'The Avenger', 'Spiderman 3'}

# my_set.remove('Spiderman 3')
# print(my_set)

# my_set.discard('Spiderman')
# print(my_set)

# my_set.pop()
# print(my_set) # Akan menghapus 1 item secara random

# my_set.clear()
# print(my_set) # Output: set()


# Menghitung jumlah item pada set

# my_set = {'Spiderman', 'Iron Man', 'The Avenger', 'Spiderman'}
# print(len(my_set)) # Output: 3. Hanya menghitung data unik


# JOIN SETS

# set_movie1 = {'The Avengers', 'Iron Man', 'Hulk'}
# set_movie2 = {'Titanic', 'Hulk'}

# # Menggabungkan semua data dari beberapa sets
# set_gabungan = set_movie1.union(set_movie2) # Full outer join
# print(set_gabungan)

# # Mencari perbedaan pada 2 sets berbeda
# set_movie1 = {'The Avengers', 'Iron Man', 'Hulk'}
# set_movie2 = {'Titanic', 'Hulk'}

# set_movie3 = set_movie1.difference(set_movie2)
# print(set_movie3)

# set_movie1.difference_update(set_movie2)
# print(set_movie1) # Menampilkan item yang hanya dimiliki oleh set_movie1

# # Mencari perbedaan simetris antara 2 sets
# set_movie1 = {'The Avengers', 'Iron Man', 'Hulk'}
# set_movie2 = {'Titanic', 'Hulk'}

# set_movie3 = set_movie1.symmetric_difference(set_movie2)
# print(set_movie3) # Menampilkan item yang tidak dimiliki antar set
# print(set_movie1)

# set_movie1.symmetric_difference_update(set_movie2)
# print(set_movie1) # Sama saja hasilnya

# # Mencari intersection antara 2 sets
# set_movie1 = {'The Avengers', 'Iron Man', 'Hulk'}
# set_movie2 = {'Titanic', 'Hulk'}

# set_movie3 = set_movie1.intersection(set_movie2)
# print(set_movie3) # Menampilkan item yang sama-sama dimiliki antar set

# set_movie1.intersection_update(set_movie2)
# print(set_movie1) # Sama saja hasilnya


# # Cek disjoint, subset, dan superset

# my_set = {'Spiderman', 'Iron Man 3', 'The Avenger'}
# my_set2 = {'Spiderman', 'Iron Man 3', 'The Avenger', 'Spiderman 2', 'Wonder Woman'}

# print(my_set.isdisjoint(my_set2)) # Melihat apakah kedua set tidak berhubungan. Output False karena set 1 dan set 2 memiliki beberapa elemen yang sama
# print(my_set.issubset(my_set2)) # Melihat apakah set pertama merupakan subset dari set kedua, output True
# print(my_set.issuperset(my_set2)) # Melihat apakah set pertama merupakan superset dari set kedua, output False

# # Superset memiliki semua data yang ada di subset, dan juga data selain itu.
# # Subset: semua datanya dimiliki oleh superset. Jadi, seperti lingkaran kecil di dalam lingkaran besar.


# ZIP

# - Menggabungkan collection data types menjadi tuple yang berpasangan.
# - Misalnya, item pertama pada list1 akan dipasangkan dengan item pertama pada list2.
# - Return-nya berupa tuple.

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# zip(list1, list2) # Hanya menunjukkan memory location

# for item in zip(list1, list2):
#     print(item)

# Unpacking
# for i, j in zip(list1, list2):
#     print(i) # 1, 2, 3
#     print(j) # a, b, c


# Bagaimana kalau jumlah item tidak sama?
# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c']

# for item in zip(list1, list2):
#     print(item) # 4 tidak akan masuk ke output karena tidak memiliki pasangan.