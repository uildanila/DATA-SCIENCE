# Soal dari slide untuk session Function

# # =================================================================================================

# # Soal 1

# # Tarif taxi per kilometer adalah 5000
# # Awal buka pintu sudah dikenakan tarif 8000
# # Berapa tarif taxi untuk perjalanan sejauh 1, 2, 3, 4, dan 5 kilometer?

# kilometer = [1, 2, 3, 4, 5]

# # -----------------------------------------
# # Menggunakan lambda
# list(map(lambda x: (x*5000) + 8000, kilometer))

# # -----------------------------------------
# # Menggunakan List Comprehension 
# [(x*5000) + 8000 for x in kilometer]

# # -----------------------------------------
# # Menggunakan regular function 
# def tarif(list_jarak):
    
#     total = []
#     for x in list_jarak:
#         jarak = (x*5000) + 8000
#         total.append(jarak)

#     return total

# print(tarif(kilometer))




# # =================================================================================================
# # Soal 2

# # Buat function dengan parameter yang akan diisi dengan argumen berupa sebuah kalimat, contoh
# # Argumen: teh cukup murah
# # Output: teh pukuc harum

# # Syarat: 
# # Hanya kata yg memiliki panjang lebih dari 3 huruf yang dibalik
# # Input hanya berupa huruf dan spasi, tanpa tanda baca

# # Sugestion: pakai looping string dan list
# # Pakai conditional if
 
# # ----------------------------------
# # Cara 1
# def terbalik(kalimat):
#     list_kalimat = kalimat.split(' ') # teh, cukup, murah

#     for i in list_kalimat:  # 0 1 2 --> teh, cukup, murah --> karena hanya ada 3 kata             
#         for j in range(len(i)): #  0 1 2             
#             terbalik = i[len(i)-1-j]  #  teh[3-1-0] = teh[2] --> h
#             biasa = i[j]    # teh[0] --> t              
            
#             if len(i) > 3:
#                 print(terbalik, end='')
#             else:
#                 print(biasa, end='')
#         print(' ', end='')              

# terbalik('teh cukup murah')

# # # ----------------------------------
# # # Cara 2
# def kebalik(kalimat):
#     list_kalimat = kalimat.split(' ')

#     for i in list_kalimat:
#         if len(i) > 3:
#             print(i[::-1], end=' ')     
#         else:
#             print(i, end=' ')

# kebalik('pagi ini lumayan panas')





# # =================================================================================================
# # Soal 3

# Buat algoritma untuk memutar list di dalam list yang berukuran 3x3 satu kali searah jarum jam.
# Misal:

# Input
# [[1,2,3],   
# [4,5,6],
# [7,8,9]]

# Output
# [[7,4,1],   [2][0]  [1][0]  [0][0]
# [8,5,2],    [2][1]  [1][1]  [0][1]
# [9,6,3]]    [2][2]  [1][2]  [0][2]


# Solusi

list1 = [[1,2,3],       # 0 0   0 1     0 2
         [4,5,6],       # 1 0   1 1     1 2
         [7,8,9]]       # 2 0   2 1     2 2


# def rotasi(x): # buat fungsi bernama rotasi
#     list2 = [] # digunakan untuk menampung keseluruhan item yang dirotasi
    
#     for i in range(0, 3):    
#         list3 = []             
#         for j in range(2, -1, -1):    
#             list2.append(x[j][i]) # hanya dapat menampung item untuk tiap iterasi i. Jika masuk ke nilai i selanjutnya, maka list3 akan kosong kembali

#         list2.append(list3)

#     return list2 # jika fungsi rotasi dijalankan, maka akan ngeprint isi list3 (list1 yang telah berputar)

# print(rotasi(list1)) # fungsi rotasi digunakan pada list1



# # =================================================================================================
# # Soal 4

# Jika parameter sebuah fungsi adalah integer n, return True jika n ada pada range +-10 dari 100 atau 200.

# Contoh output:

# plus_minus(90) --> True
# plus_minus(150) --> False
# plus_minus(104) --> True

# def plus_minus(angka):
#     return (abs(100-angka) <= 10) or (abs(200-angka) <=10)

# print(plus_minus(90))
# print(plus_minus(150)) 
# print(plus_minus(104))



# # =================================================================================================
# # Soal 5

# Buat function yang dapat mengecek sebuah angka apakah dalam range angka yang diberikan atau tidak.

# Contoh output:

# dalam_range(21, 10, 100) --> Output: True. 
    # Parameter pertama adalah angka yang ingin dicari apakah dalam range atau tidak.

# def dalam_range(angka, bawah, atas):
#     if angka in range(bawah, atas):
#         print(f'{angka} ada dalam range')
#     else:
#         print(f'{angka} berada di luar range')

# print(dalam_range(21, 1, 10))

    
