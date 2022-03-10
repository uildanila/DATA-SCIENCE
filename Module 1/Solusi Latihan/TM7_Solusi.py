# Soal 1

# Buatlah function dengan input dan output seperti contoh di bawah ini
# [1,3,4,5]         --> ['Ganjil', 'Ganjil', 'Genap', 'Ganjil']
# [22,17,19,20,14]  --> ['Genap', 'Ganjil', 'Ganjil', 'Genap', 'Genap']
# [1,3,5]           --> ['Ganjil', 'Ganjil', 'Ganjil']
# [2,4,6]           --> ['Genap', 'Genap', 'Genap']

# Solusi

# def ganjil_genap(angka) :
#     if(angka % 2 == 0) :
#         return 'Genap'
#     return 'Ganjil'

# def ubah_jadi_ganjil_genap(list_angka) :
#     return list(map(ganjil_genap, list_angka))

# list1 = [1, 3, 4, 5]
# list2 = [22, 17, 19, 20, 14]
# list3 = [1, 3, 5]
# list4 = [2, 4, 6]

# list1 = ubah_jadi_ganjil_genap(list1)
# list2 = ubah_jadi_ganjil_genap(list2)
# list3 = ubah_jadi_ganjil_genap(list3)
# list4 = ubah_jadi_ganjil_genap(list4)

# print(list1)
# print(list2)
# print(list3)
# print(list4)


# Bayu
# def ganjilgenap(angka):
#     listnew = []
#     for i in angka:
#         if i%2 == 0:
#             i = "genap"
#         else:
#             i = "ganjil"
#         listnew.append(i)
#     return listnew

# print(ganjilgenap([11, 12, 14, 15]))

# # =================================================================================================


# Soal 2

# Buatlah sebuah function untuk melakukan filtering pada suatu list berisi gaji karyawan.
# Tampilkan gaji yang tetap berniai di atas 9 juta setelah dikurangi 5% dari gaji tersebut 
list_gaji = [9100000, 9800000, 9500000, 10300000, 9300000]


# Cara 1: regular function
# def melebihi_9juta(gaji):
#     if gaji - (gaji*(5/100)) > 9000000:
#         return True
#     else:
#         return False

# list_gaji = [9100000, 9800000, 9500000, 10300000, 9300000]

# def filter_9juta(fn, my_list):
#     filtering = list(filter(fn, my_list))
#     return filtering

# print(filter_9juta(melebihi_9juta, list_gaji))



# # Cara 2: lambda function
# def filter_9juta(my_list):
#     filtering = list(filter(lambda gaji: gaji-(gaji*(5/100)) > 9000000, my_list))
#     return filtering

# list_gaji = [9100000, 9800000, 9500000, 10300000, 9300000]

# print(filter_9juta(list_gaji))

# # =================================================================================================


# # Soal 3

# Buatlah function yang menerima inputan string serta dapat menghitung jumlah huruf kapital dan huruf kecil
    # yang ada pada string tersebut.

# Contoh: 'Halo Pak Andi, bagaimana kabar Anda pada hari Senin ini?'

# Output:
# - Jumlah huruf kapital: 5
# - Jumlah huruf kecil: 40

# def kecil_besar(str):
#     jumlah = {'kapital':0, 'kecil':0}

#     for i in str:
#         if i.isupper():
#             jumlah['kapital'] += 1
#         elif i.islower():
#             jumlah['kecil'] += 1
#         else:
#             pass
    
#     print(f"Jumlah huruf kapital: {jumlah['kapital']}")
#     print(f"Jumlah huruf kecil: {jumlah['kecil']}")

# kecil_besar('Halo Pak Andi, bagaimana kabar Anda pada hari Senin ini?')

# # =================================================================================================


# # Soal 4

# Buatlah fungsi yang dapat mengubah kalimat yang dimasukkan menjadi kalimat baru yang karakternya hilang sesuai dengan yang di-input-kan.

# Contoh: 
# Input --> saya mau makan
# Karakter yang ingin dihapus --> a
# Output --> 'sy mu mkn'


# def hapus():
#     x = input('masukkan kalimat: ')
#     print(x)
#     y = input('masukkan huruf yang ingin dihapus: ')
#     print(y)
    
#     yang_dihapus = x.split(y)
#     yang_dihapus = ''.join(yang_dihapus)
#     return yang_dihapus

# print(hapus())


# Bayu
# kalimat = str(input("masukkan kalimat: "))
# karakter = str(input("masukkan karakter yang mau dihapus: "))

# def hapus(old, new):
#     lowerold = old.lower()
#     lowernew = new.lower()
#     kalimatbaru = lowerold.replace((lowernew),"")
#     return kalimatbaru

# print(hapus(kalimat, karakter))
