# Contoh 1

# x = 100

# def jumlah(angka1, angka2):
#     hasil = angka1 + angka2 + x
#     return hasil

# print(jumlah(11, 3)) # 114 # x merujuk ke variabel x di luar function
# print(hasil) # Error karena variabel hasil adalah local variabel (berada di dalam function)

## ============================================================================================

## GLOBAL VARIABLE

# - Variabel yang didefinisikan di luar function.
# - Global variable memiliki cakupan global, berarti memegang nilai sepanjang program dijalankan.
# - Global variable dapat diakses di seluruh program oleh function yang terdapat dalam program.

# def coba():
#     print(x + 2)
#     return x + 3

# x = 5

# print(coba()) # 7, 8
# print(x)    # 5

## ============================================================================================

## LOCAL VARIABLE

# - Variabel yang didefinisikan di dalam function.
# - Local variabel hanya bisa digunakan di dalam function di mana variabel tersebut didefinisikan.
# - Local variabel akan ada selama function dijalankan, setelahnya, local variable akan hilang secara otomatis.

# def coba():
#     x = 100 # Local variabel
#     print(x + 2)
#     return x + 3

# x = 5 # Global variabel

# print(coba()) # 102, 103
# print(x) # output 5 

## ============================================================================================

# def coba():
#     x = x + 10 # Karena x di local bukan berupa angka, sehingga akan error kalau dijalankan.
#     print(x + 2)
#     return x + 3

# x = 5

# print(coba())
# print(x)

# Solusi 1

# Memberikan local variabel di dalam function

# def coba():
#     x = 5
#     x = x + 10  # Local variabel
#     print(x + 2)
#     return x + 3

# x = 5

# print(coba()) # 17, 18
# print(x) # 5

# Solusi 2

# def coba():
#     global x        # Mengambil nilai x dari global variabel
#     x = x + 10      # x = 5 + 10 = 15
#     print(x + 2)    # 17
#     return x + 3    # 18

# x = 5

# print(coba()) 
# print(x)        # 15 --? nilai x yang awalnya 5 karena di dalam function coba ditambahkan 10, jadi nilainya menjadi 15


## ============================================================================================

## CALL BACK FUNCTION

# - Function yang menerima argumen berupa function lainnya.

# def tambah(angka1, angka2):
#     hasil_tambah = angka1 + angka2
#     return hasil_tambah

# def kurang(angka3, angka4):
#     hasil_kurang = angka3 - angka4
#     return hasil_kurang

# def matematika(fungsi, angka_pertama, angka_kedua):
#     hasil_operasi = fungsi(angka_pertama, angka_kedua)
#     return hasil_operasi

# print(matematika(tambah, 100, 5))
# print(matematika(kurang, 100, 5))


## ============================================================================================

## CALLING OTHER FUNCTION

# - Function yang digunakan di dalam function lainnya.

# def tampilkan(jawaban):
#     print(f'Jawabannya adalah {jawaban}')

# tampilkan(100) # Jawabannya adalah 100

# def perkalian(angka1, angka2):
#     hasil = angka1 * angka2
#     tampilkan(hasil)

# perkalian(8, 10) # Jawabannya adalah 80

## ============================================================================================

## RECURSIVE FUNCTION

# - Sebuah function yang memanggil dirinya sendiri di dalam function tersebut.

# def countdown(counter):
#     print(counter)
#     counter -= 1

#     if counter >= 0:
#         countdown(counter)
#         print(f'counter = {counter}')

# countdown(3)



## ============================================================================================
## LAMBDA FUNCTION 

# - Function tanpa nama.
# - Bisa punya beberapa parameter, tapi kalau expression-nya lebih dari 1, itu lebih pakai regular function.
# - Syntax --> lambda parameter: expression

# kuadrat = lambda angka: angka**2
# print(kuadrat(5)) # 25

# perkalian = lambda angka1, angka2: angka1 * angka2
# print(perkalian(3, 4))     # 12

## ============================================================================================

## MAP

# - Digunakan untuk mengubah nilai atau bentuk dari item yang ada di collection data types, tanpa mengubah jumlah itemnya.

# Cara yang biasa digunakan:
# list1 = [1, 2, 3, 4]

# def kuadrat(angka):
#     return angka ** 2

# list_baru = []

# for i in list1:
#     list_baru.append(kuadrat(i))

# print(list_baru)


# Cara dengan menggunakan map:

# - Syntax --> map(nama function, nama variabel)
# - Hasilnya dalam bentuk map object
# - Kita bisa mengubahnya menjadi bentuk list, agar hasil di terminal menjadi dalam list.

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# def kuadrat(angka1, angka2):
#     return angka1 ** angka2

# print(list(map(kuadrat, list1, list2))) # Menggunakan regular function dengan 2 argumen

# print(list(map(lambda x, y: x ** y, list1, list2))) # Menggunakan lambda function dengan 2 argumen


## ============================================================================================

## LATIHAN MAP

# # Tarif taxi per kilometer adalah 5000
# # Awal buka pintu sudah dikenakan tarif 8000
# # Berapa tarif taxi untuk perjalanan sejauh 1, 2, 3, 4, dan 5 kilometer? Buat dengan lambda function
    # dan built in function map()

# kilometer = [1, 2, 3, 4, 5]

# Menggunakan regular function dan map()

# def tarif(jarak):
#     return 8000 + (5000*jarak)

# print(list(map(tarif, kilometer)))


# Menggunakan lambda function dan map()

# print(list(map(lambda jarak: jarak*5000 + 8000, kilometer)))


# Menggunakan list comprehension

# print([(jarak*5000) + 8000 for jarak in kilometer])

## ============================================================================================

## FILTER

# - Digunakan untuk filtering (memilih) data pada collection data types.
# - Jumlah item dalam list akan berkurang karena difilter, tetap item tidak berubah.

# def genap(angka):
#     if angka%2 == 0:
#         return True
#     else:
#         return False

# print(genap(7)) # False


# Tidak pakai filter (menggunakan looping manual)

# kilometer = [1, 2, 3, 4, 5]
# list_genap = []

# for i in kilometer:
#     if i%2 == 0:
#         list_genap.append(i)

# print(list_genap)


# Filter menggunakan regular function

# def genap(angka):
#     return angka%2 == 0

# print(genap(9)) # False

# print(list(filter(genap, kilometer)))


# Filter menggunakan lambda function

# print(list(filter(lambda angka: angka%2 == 0, kilometer)))


## ============================================================================================

## DOCSTRING

# - Untuk menamabahkan dokumentasi atau penjelasan dari function yang kita buat.
# - Dokumentasi ini dapat dimunculkan dan dibaca orang lain dengan cara --> help(nama_function)

# def genap(angka):
#     '''Function ini digunakan untuk menyeleksi apakah angka yang dimasukkan ke dalam
#     argumen itu angka genap atau bukan. Function ini hanya membutuhkan satu argumen saja.'''
#     return angka%2 == 0

# print(genap(8)) # True
# print(help(genap))

# print(help(print)) # Contoh untuk mengecek dokumentasi built-in function Python

## ============================================================================================

## *args dan **kwargs

# def myfunc(a, b):
#     '''Function ini mengembalikan nilai 5% dari jumlah perkalian kedua parameter'''
#     return sum((a, b)) * 0.05

# print(myfunc(40, 60)) # 5.0

# Contoh 2

# def myfunc(a, b, c=0, d=0, e=0):
#     '''Function ini mengembalikan nilai 5% dari jumlah perkalian kedua parameter'''
#     return sum((a, b, c, d, e)) * 0.05

# print(myfunc(40, 60, 100)) # 10.0

# print(myfunc(40, 60, 100, 100, 200, 300)) # Error karena jumlah argumen yang dimasukkan melebihi jumlah parameter


# Di sinilah *args dapat berguna

# def myfunc(*args):
#     return sum((args)) * 0.05

# print(myfunc(40, 60, 100, 100, 200, 300, 1000, 20000)) # Bisa memasukkan jumlah argumen tak terbatas

## ============================================================================================

# **kwargs (keyword args)

# def myfunc(**kwargs):
#     if 'buah' in kwargs:
#         print(f"Pilihan buah saya adalah {kwargs['buah']}")
#     else:
#         print('Saya tidak menemukan buah pilihan saya.')

# myfunc(buah='apel', sayur='kangkung')

# Nama *args dan **kwargs bisa diubah seperti nama variabel sementara pada looping, tapi lebih baik
    # gunakan default (*args atau **kwargs) saja.


# def myfunc(*args, **kwargs):
#     print(f"Saya mau {args[0]} {kwargs['cemilan']}")

# myfunc(10, 20, 30, cemilan = 'risoles', dessert = 'puding')

# # Urutan penggunaan jika menggunakan *args dan **kwargs secara bersamaan, maka *args berada sebelum **kwargs
# # Penggunaan **kwargs harus mendefinisikan nama parameternya.

# def myfunc(**kwargs, *args):
#     print(f"Saya mau {args[0]} {kwargs['cemilan']}")

# myfunc(cemilan = 'risoles', dessert = 'puding', 10, 20, 30) # Tidak bisa dijalankan, karena invalid syntax (*args berada setelah **kwargs)

# def myfunc(*args, **kwargs):
#     print(f"Saya mau {args[0]} {kwargs['cemilan']}")

# # myfunc(10, 20, 30, cemilan = ['risoles', 'bolu'], dessert = 'puding')

# # myfunc(10, 20, 30, cemilan = 'risoles', cemilan = 'bolu', dessert = 'puding') # Error, argumen yang sama tidak bisa diulang

# myfunc('cemilan', 20, 30, 'risoles', cemilan='puding') # Saya mau cemilan puding 