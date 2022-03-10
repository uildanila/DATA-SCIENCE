# Exercise

# # SOAL DARI SLIDE
# # ===================================================================

# Soal 1

# x = 4
# y = 3
# z = 2

# w = ((x+y*z)/(x*y))**2
# print(w)


# # ===================================================================
# Soal 2

# angka = input('Silakan masukkan angka berapapun: ')
# kuadrat = int(angka)**2

# print(f'Kuadrat dari {angka} = {str(kuadrat)}')
# print('Kuadrat dari', angka, '=', str(kuadrat))
# print('Kuadrat dari ' + angka + ' = ' + str(kuadrat))



# # ===================================================================
# Soal 3

# Buat sebuah user input 'Masukkan jumlah hari: 485'
# Kemudian print hasilnya dalam bentuk 
# '485 hari terdiri dari 1 tahun 4 bulan 0 minggu 5 hari'

# Cara 1
# x = int(input('Masukkan jumlah hari: '))
# print(x)
# tahun = x // 360
# bulan = (x % 360) // 30
# minggu = (x % 30) // 7
# hari = x - (tahun * 360) - (bulan * 30) - (minggu * 7)
# print(f'{x} hari terdiri dari {tahun} tahun {bulan} bulan {minggu} minggu {hari} hari')

# import math

# x = input("Silahkan Masukkan Jumlah Hari: ")
# y = int(x)
# print("%d hari" %y)

# p = y%360
# q = p%30
# r = q%7

# tahun = (math.floor(y/360))
# bulan = (math.floor(p/30))
# minggu = (math.floor(q/7))
# hari = r
# print("%d tahun, %d bulan, %d minggu, %d hari" %(tahun, bulan, minggu, hari))


# Cara 2
# x = int(input('Masukkan jumlah hari: '))
# tahun = x // 360          # dibagi hari dlm setahun, pembulatan ke bawah
# sisa_hari = x % 360        # dibagi kelipatan 360, sisanya adalah sisa_hari
# bulan = sisa_hari //30     # sisa hari dari tahun dibagi 30, pembulatan ke bawah
# sisa_hari2 = sisa_hari % 30 # sisa hari dari tahun dibagi kelipatan 30, sisanya adalah sisa_hari2
# minggu = sisa_hari2 // 7   # sisa hari dari bulan dibagi 7, pembulatan ke bawah
# sisa_hari3 = sisa_hari2 % 7 # sisa hari dari bulan dibagi kelipatan 30, sisanya adalah sisa_hari2
# hari = sisa_hari3          # sisa hari dari minggu adalah jumlah hari itu sendiri 
# print(f'{x} hari terdiri dari {tahun} tahun {bulan} bulan {minggu} minggu {hari} hari')



# # ===================================================================
# Soal 4

# Saat ini total usia Andi dan Budi adalah 49 tahun
# Rasio usia Andi dan Budi adalah 0.4
# Berapa usia Andi dan Budi 2 tahun lagi


# total_umur = 49
# rasio_andi = 4
# rasio_budi = 10
# rasio_total = 14

# umur_andi = total_umur * (rasio_andi/rasio_total)
# umur_budi = total_umur * (rasio_budi/rasio_total)

# print(f'''
# Umur Andi sekarang adalah {umur_andi} tahun.
# Umur Budi sekarang adalah {umur_budi} tahun.
# ''')

# print(f'''
# Umur Andi 2 tahun lagi adalah {umur_andi + 2} tahun.
# Umur Budi 2 tahun lagi adalah {umur_budi + 2} tahun.
# ''')


# # ===================================================================

# Soal 5

# Jarak mobil A dan B adalah 120 km
# A berjalan 60 km/h dari timur
# B berjalan 40 km/h dari barat
# A dan B start pada pukul 09.00
# Jam berapa A dan B bertabrakan?

# jarak = 120      # satuan km
# kecepatan_A = 60/3600   # km/detik
# kecepatan_B = 40/3600   # km/detik
# start = 9        # jam

# # Setiap 3600 detik, mobil akan saling mendekat 100 km
# # Setiap 1 detik, mobil akan saling mendekat 1.66 km 

# jarak_per_detik = kecepatan_A + kecepatan_B
# print('Jarak per detik saling mendekat', jarak_per_detik)

# # Untuk terjadi tabrakan, artinya jarak total saling mendekat harus 120 km
# detik_tabrakan = jarak / jarak_per_detik
# print(f'Tabrakan terjadi {detik_tabrakan} detik setelah start')

# # Dinyatakan dalam jam menit detik
# jam = int(detik_tabrakan // 3600)
# menit = int((detik_tabrakan % 3600) // 60)
# detik = int(detik_tabrakan % 60)

# menit = int((detik_tabrakan - jam*3600) // 60)

# print(f'Tabarakan terjadi pukul {start+jam}:{menit}:{detik}')

# Solusi lain
xAB = 120
# A = 60
# B = 40
# start = 9

# waktu = (xAB / (A + B)) * 60
# print(waktu, 'menit')

# waktu_tabrakan = 10.12
# print(f'Tabrakan terjadi pada pukul {waktu_tabrakan}')


# Breakdown

# Gerak Lurus Beraturan (GLB)
# Apabila sebuah benda bergerak menempuh jarak s dalam rentang waktu t. 
# Maka, kecepatan perpindahan benda tersebut dari titik awal ke titik akhir dapat dirumuskan sebagai berikut:

# v = s/t
# s = v*t
# t = s/v

# jarak = 120 km
# kecepatan A = 60 km/jam
# kecepatan B = 40 km/jam

# (v1*t) + (v2*t) = s
# (v1 + v2)*t = 120

# (60+40)t = 120
# 100t = 120
# t = 120km/100km/jam
# t = 1.2 jam

# 1.2 jam = 1 jam + 0.2 jam

# 0.2 jam = berapa menit?
# 0.2 * 60 = 12 menit

# 1.2 jam = 72 menit

# start jam 9.00

# tabrakan jam 9.00 + 72 menit = 10.12

# # ===================================================================
# Soal 6

# jmlApel = int(input('Masukkan jumlah apel: '))
# jmlJeruk = int(input('Masukkan jumlah jeruk: '))
# jmlAnggur = int(input('Masukkan jumlah anggur: '))

# # Diketahui harga buah sebagai berikut:
# hargaApel = 10000
# hargaJeruk = 15000
# hargaAnggur = 20000

# print('Detail Belanja')

# print(f'Apel: \t {jmlApel} x {hargaApel} = {jmlApel*hargaApel}')
# print(f'Jeruk: \t {jmlJeruk} x {hargaJeruk} = {jmlJeruk*hargaJeruk}')
# print(f'Anggur:\t {jmlAnggur} x {hargaAnggur} = {jmlAnggur*hargaAnggur}')

# totalBelanja = (jmlApel*hargaApel) + (jmlJeruk*hargaJeruk) + (jmlAnggur*hargaAnggur)
# print(f'Total belanjaan Anda Rp.{totalBelanja}')



# # SOAL BIKINAN
# # ===================================================================
# Soal 7
# Seorang karyawan memiliki gaji 10 juta rupiah ditahun 2021
# Tahun 2022, gaji naik 25%
# Pajak penghasilan pertahun adalah 12%
# Berapa gaji dia bulan Januari 2022 ini?
# Berapa gaji total 2021 setelah dipotong pajak dalam setahun
# Berapa gaji total 2022 setelah dipotong pajak dalam setahun

# gaji = 10000000

# naik_gaji = gaji + ((25/100)*gaji)
# gaji_bersih1 = (gaji - ((12/100)*gaji))*12
# gaji_bersih2 = (naik_gaji - ((12/100)*gaji))*12

# print(f'Gaji bulan depan sebesar Rp{naik_gaji:,}')
# print(f'Gaji total 2021 setelah dipotong pajak dalam setahun adalah Rp{gaji_bersih1:,}')
# print(f'Gaji total 2022 setelah dipotong pajak dalam setahun adalah Rp{gaji_bersih2:,}')




# # ===================================================================
# Soal 8
# # input: masukkan 4 angka: 1234
# # output 3412 (lakukan hanya dengan operasi matematika)

# number = int(input('Masukkan 4 digit angka: '))
# a = number/100  # 12.34
# b = number//100 # 12
# c = a-b         # 0.34
# d = c*10000     # 3400
# e = round(d+b)  # 3412
# print(f'Output: {e}')

# # CARA MODULO
# number = int(input('Masukkan 4 digit angka: '))
# head = number%100 * 100   
# tail = number//100
# print(head+tail)