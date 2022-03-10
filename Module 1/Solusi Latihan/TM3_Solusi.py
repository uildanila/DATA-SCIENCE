# 1. Buat algoritma untuk menentukan apakah suatu bilangan adalah bilangan prima

# Misal:

# masukkan angka: 7
# 7 adalah bilangan prima

# masukkan angka: 12
# 12 bukan merupakan bilangan prima


# angka = int(input('Masukkan angka: '))

# if angka > 1:
#     for i in range(2, angka):
#         if (angka % i) == 0:
#             print(f'{angka} bukan merupakan bilangan prima')
#             break
#     else:
#         print(f'{angka} merupakan bilangan prima')
# else:
#     print(f'{angka} bukan merupakan bilangan prima')

    

# 2. 

# Dari list berikut: [12, 15, 1, 7, 4, 100]

# Buat algoritma untuk mencari angka tertinggi di dalam list tanpa menggunakan fungsi max atau sort

list_angka = [12, 15, 1, 7, 4, 100]

angka_tertinggi = list_angka[0] # 100

for angka in list_angka:
    if angka > angka_tertinggi: # 100 > 15??
        angka_tertinggi = angka # iterasi pertama = 12, iterasi kedua angka = 15 > 12? YA

print(angka_tertinggi) # 100


# 3. 

# Buat while loop untuk mencari angka 13 di antara angka 1-100
# Ketika angka 13 ketemu, print 'angka 13 ditemukan'


# x = 1
# dicari = 13

# while x <= 100:
#     print(x)

#     if x == dicari:
#         print(f'angka {x} ditemukan')
#         break
#     x += 1


# 4. 

# Buat looping dengan output:
# ini bilangan ganjil [1, 3, 5, 7, 9]
# ini bilangan genap [2, 4, 6, 8, 10]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ganjil = []
list_genap = []

for i in input_list: 
    if i % 2 == 0:
        list_genap.append(i)
    else:
        list_ganjil.append(i)

print('ini bilangan ganjil', list_ganjil)
print('ini bilangan genap', list_genap)


# 5.

# Gunakan looping untuk membuat list yang berisikan huruf depan dari setiap kata pada kalimat di bawah ini
# Lalu gabungkan setiap huruf depan menjadi satu kata!

kalimat = 'Buatlah list yang berisikan huruf depan dari setiap kata pada kalimat ini'

hasil = []

for kata in kalimat.split():
    hasil.append(kata[0])
print(''.join(hasil))



        


    


    

    
    