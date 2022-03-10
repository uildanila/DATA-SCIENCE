# CASTING (Mengubah tipe data)

# a = '123' # string
# print(a)
# print(type(a))

# # Ubah tipe data menjadi int & float
# b = int(a)
# print(b)
# print(type(b))

# c = float(b)
# print(c)
# print(type(c))

## =========================================================

# d = 33.7 # float
# print(d)
# print(type(d))

# e = int(d) # integer
# print(e)
# print(type(e))

# f = str(e)
# print(f)
# print(type(f))

## =========================================================

# g = '12.5' # string
# print(g)
# print(type(g))

# h = float(g) # float
# print(h)
# print(type(h))

# i = int(g) # Error karena nilai awalnya adalah float
# print(i)
# print(type(i))

# j = True # bernilai 1, False bernilai 0
# print(j)
# print(type(j))

# k = int(j)
# print(k)

# l = float(j)
# print(l)

## ===============================================================================

# USER INPUT
# Secara default menghasilkan string

# student = input('Nama saya adalah: ')
# print('Nama yang kamu tulis di atas adalah', student)

# jumlah = int(input('Masukkan jumlah buku: '))
# print('Jumlah buku yang kamu masukkan adalah', jumlah)

## ===============================================================================

# PENGGUNAAN TANDA KUTIP PADA STRING

# kutip_satu = 'ini pakai kutip satu'

# kutip_dua = "ini pakai kutip dua"

# kutip_tiga = '''
#                 ini di dalam kutip tiga
#                 ini juga di dalam kutip tiga dan ada 'tanda' lain
#                 '''
# print(kutip_satu)
# print(kutip_dua)
# print(kutip_tiga)

## ===============================================================================

# ESCAPE CHARACTER (back slash)

# escape_kutip = "Saya sedang belajar \"Python\" di Purwadhika"
# print(escape_kutip)

# escape_baris_baru = 'ini baris 1 \n ini baris 2'
# print(escape_baris_baru)

## ===============================================================================

# STRING FUNCTION & METHOD

kata = 'This is Python'

# panjang_string = len(kata)
# print(panjang_string)

# cari_index = kata.index('Python')
# print(cari_index)

# splitting = kata.split(' ') # memisahkan string dengan suatu karakter (' ' berarti spasi)
# print(splitting)

# splitting2 = kata.split('i') # memisahkan string berdasarkan karakter 'i'
# print(splitting2)

# jadi_huruf_kecil = kata.lower()
# print(jadi_huruf_kecil)

# jadi_huruf_kapital = kata.upper()
# print(jadi_huruf_kapital)

# huruf_pertama_kapital = kata.capitalize()
# print(huruf_pertama_kapital)

# titel = kata.title() # Mengubah semua huruf depan menjadi kapital
# print(titel)

## ===============================================================================

# STRING SLICING

# kalimat = 'hari ini saya menonton "Spiderman" di bioskop'

# print(kalimat[1]) # a
# print(kalimat[0:4]) # hari
# print(kalimat[:7]) # hari in
# print(kalimat[6:]) # ni saya menonton "Spiderman" di bioskop

# print(kalimat[-4]) # negative indexing, dimulai dari kanan (-1)
# print(kalimat[-5:-2]) # osk
# print(kalimat[-2:-5]) # tidak error, tapi tidak ada hasil apa-apa
# print(kalimat[:]) # keluar semua yang ada di string

# print(kalimat[:-5]) # hari ini saya menonton "Spiderman" di bi
# print(kalimat[::3]) # hinsaennSdm"iik

## ===============================================================================

# STRING CONCATENATION (Menyambungkan beberapa string)

# depan = 'Michael'
# belakang = 'Jordan'

# # print(depan + ' ' + belakang)

# nomor_punggung = belakang + (' ') + str(23)
# print(nomor_punggung)

## ===============================================================================

# STRING FORMAT

# teks = 'Umur saya' + str(19) + 'Tahun'
# print(teks)

# FORMAT METHOD

# umur = 19
# teks = 'Umur saya {} tahun'
# print(teks.format(umur))

# print('saya membeli {} apel, {} jeruk, {} mangga'.format(7, 4, 6))
# print('saya membeli {a} apel, {b} jeruk, {c} mangga'.format(a = 7, b = 4, c = 6))
# print('saya membeli {c} apel, {a} jeruk, {c} mangga'.format(a = 7, b = 4, c = 6))

# f-String METHOD

# umur = 19
# print(f'Umur saya {umur} tahun')

# FLOAT FORMATTING

# nama = 'Steven'
# umur = 2200/34

# print(f'Nama saya {nama}, umur {umur} tahun')
# print(f'Nama saya {nama}, umur {umur:.2f} tahun') # syntax-nya --> nama_variable:.jumlahAngkaDiBelakangKomaf

## ===============================================================================

# CHECK STRING

# kalimat = 'Saya belajar Python'

# print('aja' in kalimat) # True
# print('aja' not in kalimat) # False
# print('aji' not in kalimat) # True
# print(int('Pyr' in kalimat)) # False # Kalau mau output 0/1, tambah int di depan.

## ===============================================================================

# STRING METHOD TAMBAHAN

# kalimat = 'Saya belajar data science'

# print(kalimat.count('a')) # Menghitung jumlah karakter yang diinginkan. Harus memasukkan parameter

# print(kalimat.endswith('ce')) # True
# print(kalimat.endswith('ya', 0, 4)) # True

# print(kalimat.isalnum()) # False karena ada spasi. Mengembalikan True jika hanya mengandung alfabet dan numerik.

# print(kalimat.isalpha()) # False karena ada spasi. Mengembalikan True jika hanya mengandung alfabet.

# print(kalimat.islower()) # False karena ada huruf kapital

# print(kalimat.isspace()) # False. Mengembalikan True jika semua karakter adalah whitespace

# print(kalimat.isupper()) # False. Mengembalikan True jika semua karakter huruf kapital

# print(kalimat.replace('a', 'A')) # Mengganti karakter
# print(kalimat.replace('a', 'A', 2)) # Mengganti karakter hanya sesuai dengan jumlah yang diinginkan

