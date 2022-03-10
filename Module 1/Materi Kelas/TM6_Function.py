## FUNCTION

# - Function adalah sebuah blok kode terorganisir yang dapat menerima input dan mengeluarkan output, serta dapat digunakan
#     berulang kali.
# - Jika suatu proses dilakukan berulang kali, makan kita bisa gunakan function.
# - Function bisa digunakan di banyak tempat berbeda, agar kita tidak perlu copy paste kode yang sama berulang kali.
# - Function secara umum punya input dan output.
# - Built in function adalah function bawaan dari Python.
# - Function bisa digunakan oleh orang lain, tanpa harus orang tersebut mengetahui bagaimana proses di dalam function-nya.
#     (Gunakan docstring untuk menjelaskan apa gunanya function yang kita buat).


# REGULAR FUNCTION

# Membuat function
# def kali(angka1, angka2):         # def nama_function(parameter, parameter):
#     return angka1 * angka2          #    return return_value

# Memanggil function
# print(kali(5, 7))

# Lambda function
# x = lambda angka1, angka2: angka1 * angka2
# print(x(2, 4)) # Masukkan ke variabel, lalu panggil variabel besert argumennya.

## ==================================================================================

# Function tanpa input dan output

# def salam():
#     print('Selamat pagi')
#     print('Semoga hari Anda menyenangkan')

# salam()

# Latihan

# Buat function untuk menampilkan teks di bawah ini:
# Output:

# Halo, selamat datang di toko A.
# Jam operasional:
# - Senin - Jumat: 08.00 - 21.00
# - Sabtu - Minggu: Libur
# Pesanan dikirim setiap jam 3 sore, lewat dari itu, pesanan akan dikirim di hari kerja berikutnya.

# def online_shop():
#     print(f'''Halo, selama datang di toko A.
#     Jam operasional:
#     - Senin - Jumat: 08.00 - 21.00
#     - Sabtu - Minggu: Libur
#     Pesanan dikirim setiap jam 3 sore, lewat dari itu, pesanan akan dikirim di hari kerja berikutnya.
#     ''')

# online_shop()

## ==================================================================================

# Function dengan input tapi tanpa output

# Syntax
# def nama_function(parameter)

# def perkenalan(nama, umur):
#     print(f'Halo, nama saya {nama} dan umur saya {umur} tahun.')
#     print('Senang berkenalan dengan kalian.')

# nama_function(argumen, argumen)
# perkenalan('Andi', 29)

# Bisa tidak berurutan, tapi harus disebutkan nama parameternya.
# perkenalan(umur=28, nama='Budi')


# Latihan

# Buatlah function bernama 'oscar' dengan parameter berupa nama actor, film, dan tahunnya.

# Contoh output:
# Pemenang aktor terbaik tahun 2016 adalah Leonardo DiCaprio pada film 'The Revenant'.

# def oscar(nama_actor, film, tahunnya):
#     print(f'Pemenang aktor terbaik tahun {tahunnya} adalah {nama_actor} pada film {film}')

# oscar(tahunnya=2016, nama_actor='Leonardo DiCaprio', film='The Revenant')

## ==================================================================================

# Function dengan input dan output

# def kuadrat(angka):         
#     hasil = angka ** 2
#     return hasil 

# print(kuadrat(8)) # return value berupa integer


# def tambah(angka1, angka2):
#     return angka1 + angka2

# print(tambah(100, 200))


# def kuadrat(angka):
#     hasil = angka ** 2
#     print(hasil)

# print(kuadrat(5))
# print(kuadrat(2) * tambah(2, 3)) # Error karena kuadrat(2) adalah NoneType karena ter-print 2x
                                    # Agar tidak error, ubah print(hasil) jadi return(hasil)


# Latihan

# Buatlah function untuk menghitung luas lingkaran dengan parameter radius.

# import math

# def luas(rad):
#     hasil = math.pi * (rad**2)
#     return hasil

# print(luas(3))

## ==================================================================================

# Default Parameter

# Jika tidak memasukkan argumen saat function dipanggil, function-nya sudah memiliki nilai default
    # untuk parameter tersebut.

# def tambah(angka1=0, angka2=100):
#     return angka1 + angka2

# print(tambah(9)) # 109
# print(tambah(9, 10)) # 19


# def perkenalan(nama='Unknown', umur=0):
#     if (nama != 'Unknown') and (umur > 0):
#         print(f'Halo, nama saya {nama} dan umur saya {umur} tahun')
#     elif (nama != 'Unknown') and (umur == 0):
#         print(f'Halo, nama saya {nama}')
#     elif (nama == 'Unknown') and (umur > 0):
#         print(f'Halo, umur saya {umur} tahun, dan saya tidak mau menyebutkan nama')
#     else:
#         print('Saya tidak mau memperkenalkan diri')

# perkenalan()
# perkenalan('Alex', 25)
# perkenalan(umur=25, nama='Andi')
# perkenalan('Budi')
# perkenalan(30) # Akan masuk ke kondisi elif pertama
# perkenalan(umur=30) # Akan masuk ke kondisi elif kedua
# perkenalan('Andi', '30') # Error, karena argumen umur dimasukkan sebagai string
