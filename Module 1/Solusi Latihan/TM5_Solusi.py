# # 1. 

# # Temukan angka minimum dan maksimum pada list berikut:

# list_angka = [31, 5, 1, 7, 88, 42]

# # Output:
# # Angka minimum = 1
# # Angka maksimum = 88

# angka_minimum = list_angka[0]
# angka_maksimum = list_angka[0]

# for angka in list_angka: 
#     if(angka < angka_minimum):
#         angka_minimum = angka
#     elif(angka > angka_maksimum):
#         angka_maksimum = angka

# print(f'Angka minimum = {angka_minimum}')
# print(f'Angka maksimum = {angka_maksimum}')


# # 2.

# # Urutkan angka pada list berikut dari yang terkecil hingga terbesar tanpa menggunakan method sort!

# list_angka = [31, 5, 1, 7, 88, 42, 202, 29]

# # Output
# # list_angka_sorted = [1, 5, 7, 29, 31, 42, 88, 202]

# print(f'List angka sebelum diurutkan = {list_angka}')

# for i in range(len(list_angka)):
#     for j in range(i+1, len(list_angka)):
#         if(list_angka[i] > list_angka[j]):
#             list_angka[i], list_angka[j] = list_angka[j], list_angka[i]
        
# print(f'List angka setelah diurutkan = {list_angka}')


# # 3.

# kalimat = str(input('Masukkan kalimat: '))
# kata = {}
    
# for word in kalimat.lower().split():
#     if word in kata.keys():
#         kata[word] += 1 # Tambahkan 1 value pada key word di dictionary kata
#     else:
#         kata[word] = 1 # Buat key baru dengan value 1 pada dictionary kata
    
# for keys, val in kata.items():
#     print(f'Jumlah kata {keys.capitalize()} ada sebanyak {val}')


# # 4.

# valid = True
# while valid:
#     user1 = str.title(input('Masukkan 5 film kesukaan Anda, dipisahkan dengan tanda koma: '))
    
#     user1_list = user1.split(', ')
#     user1_len = len(user1_list)

#     user2 = str.title(input('Masukkan 5 film kesukaan teman Anda, dipisahkan dengan tanda koma: '))

#     user2_list = user2.split(', ')
#     user2_len = len(user2_list)

#     if user1_len and user2_len == 5:
#         print(f'5 film kesukaan Anda adalah {user1}')
#         print(f'5 film kesukaan teman Anda adalah {user2}')

#         valid = False
#     elif user1_len and user2_len > 5:
#         print("Anda memasukkan lebih dari 5 judul film")
#     else:
#         print('Anda memasukkan kurang dari 5 judul film')

# # Solusi lain

# user1 = str.title(input('Masukkan 5 film kesukaan Anda, dipisahkan dengan tanda koma: '))
# user1_list = user1.split(', ')

# user2 = str.title(input('Masukkan 5 film kesukaan teman Anda, dipisahkan dengan tanda koma: '))
# user2_list = user2.split(', ')

# set1 = set(user1_list)
# set2 = set(user2_list)

# kesamaan = set1.intersection(set2)

# jumlah = len(kesamaan)

# if jumlah == 5:
#     print('Kesukaan film kalian yang sama sebesar 100%')
# elif jumlah == 4:
#     print('Kesukaan film kalian yang sama sebesar 80%')
# elif jumlah == 3:
#     print('Kesukaan film kalian yang sama sebesar 60%')
# elif jumlah == 2:
#     print('Kesukaan film kalian yang sama sebesar 40%')
# elif jumlah == 1:
#     print('Kesukaan film kalian yang sama sebesar 20%')    
# else:
#     print('Kalian tidak memiliki kesukaan film yang sama')


# # 5.

# pembagian = [angka for angka in range(1, 101) if True in [True for pembagi in range(2, 10) if angka % pembagi == 0]]
# print(pembagian)
# print(len(pembagian))

# # # Cara for loop
# pembagian2 = []

# for i in range(1, 101):
#     for j in range(2, 10):
#         if i % j == 0:
#             pembagian2.append(i)

# pembagian2 = set(pembagian2)

# print(list(pembagian2))

# print(len(pembagian2))

# # 6.

# kalimat = 'Kemarin dari jam 2 hingga 3.30 siang saya bertemu dengan 10 orang di 4 tempat berbeda'
# kata = kalimat.split()
# hasil = [angka for angka in kata if not angka.isalpha()]
# print(hasil)



# # # 7.

list_buah = [
    ['Apel', 20, 10000],
    ['Jeruk', 15, 15000],
    ['Anggur', 25, 20000]
]

cart = []

while True:
    pilihan_menu = input('''
        Selamat Datang di Pasar Buah

        List Menu:
        1. Menampilkan Daftar Buah
        2. Menambah Buah
        3. Menghapus Buah
        4. Membeli Buah
        5. Keluar Program

        Masukkan angka menu yang ingin dijalankan: ''')

    if(pilihan_menu == '1'):

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')
        
        for i in range(len(list_buah)):
            print(f'{i}\t| {list_buah[i][0]}  \t| {list_buah[i][1]}\t| {list_buah[i][2]}')

    elif(pilihan_menu == '2'):

        nama_buah = input('Masukkan nama buah: ').capitalize()
        stok_buah = int(input('Masukkan stok buah: '))
        harga_buah = int(input('Masukkan harga buah: '))
        
        list_buah.append([nama_buah, stok_buah, harga_buah])
        
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')
        
        for i in range(len(list_buah)):
            print(f'{i}\t| {list_buah[i][0]}  \t| {list_buah[i][1]}\t| {list_buah[i][2]}')

    elif(pilihan_menu == '3'):

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')
        
        for i in range(len(list_buah)):
            print(f'{i}\t| {list_buah[i][0]}  \t| {list_buah[i][1]}\t| {list_buah[i][2]}')

        index_buah = int(input('Masukkan index buah yang ingin dihapus: '))
        
        del list_buah[index_buah]

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')
        
        for i in range(len(list_buah)):
            print(f'{i}\t| {list_buah[i][0]}  \t| {list_buah[i][1]}\t| {list_buah[i][2]}')


    elif(pilihan_menu == '4'):

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')

        for i in range(len(list_buah)):
            print(f'{i}\t| {list_buah[i][0]}  \t| {list_buah[i][1]}\t| {list_buah[i][2]}')
        
        while True:
            index_buah = int(input('Masukkan index buah yang ingin dibeli: '))
            jumlah_buah = int(input('Masukkan jumlah yang ingin dibeli: '))
            
            if(jumlah_buah > list_buah[index_buah][1]):
                print(f'Stok tidak cukup, sisa stok {list_buah[index_buah][0]} adalah {list_buah[index_buah][1]}')
            else:
                cart.append([list_buah[index_buah][0], jumlah_buah, list_buah[index_buah][2], index_buah])
            
            for item in cart:
                list_buah[item[3]][1] -= jumlah_buah
            
            print('Isi Cart:')
            print('Nama\t| Jumlah\t| Harga')
            
            for item in cart:
                print(f'{item[0]}\t| {item[1]}\t\t| {item[2]}')

            break

        while True:
            checker = input('Mau beli yang lain? (Ya/Tidak) = ')

            if(checker == 'ya'):
                index_buah = int(input('Masukkan index buah yang ingin dibeli: '))
                print(f'Sisa stok {list_buah[index_buah][0]} adalah {list_buah[index_buah][1]}.')

                if(list_buah[index_buah][1] == 0):
                    print('Maaf, stok buah yang dipilih sedang kosong. Silakan pilih buah yang lain jika mau.')
                    continue
                else:
                    jumlah_buah_tambahan = int(input('Masukkan jumlah yang ingin dibeli: '))
                    

                if(jumlah_buah_tambahan > list_buah[index_buah][1]):
                    print(f'Stok tidak cukup, masukkan jumlah yang sesuai dengan sisa stok.')
                else:
                    cart.append([list_buah[index_buah][0], jumlah_buah_tambahan, list_buah[index_buah][2], index_buah]) 
                    list_buah[index_buah][1] -= jumlah_buah_tambahan
            
            else:
                break

            
        print('Daftar Belanja:')
        print('Nama\t| Jumlah\t| Harga\t| Total Harga')
        total_harga = 0

        for item in cart:
            print(f'{item[0]}\t| {item[1]}\t| {item[2]}\t\t| {item[1] * item[2]}')
            total_harga += item[1] * item[2]    
        
        while True:
            print(f'Total yang harus dibayar = {total_harga}')
            if total_harga != 0:
                jumlah_uang = int(input('Masukkan jumlah uang: '))

                if(jumlah_uang > total_harga):
                    kembali = jumlah_uang - total_harga
                    print(f'Terima kasih \n\nUang kembalian Anda: {kembali}')
                    cart.clear()
                    break
            
                elif(jumlah_uang == total_harga):
                    print('Terima kasih')
                    cart.clear()
                    break
            
                else:
                    kekurangan = total_harga - jumlah_uang
                    print(f'Uang Anda kurang sebesar {kekurangan}')

            else:
                print(f'Terima kasih telah berkunjung.')
                break
            
            
                
    elif(pilihan_menu == '5'):
        break



# # # 8.

list_buah = [
    {
        'nama': 'Apel',
        'stok': 20,
        'harga': 10000
    },
    {
        'nama': 'Jeruk',
        'stok': 15,
        'harga': 15000
    },
    {
        'nama': 'Anggur',
        'stok': 25,
        'harga': 20000
    }
]

cart = []

while True:
    pilihan_menu = input('''
        Selamat Datang di Pasar Buah

        List Menu:
        1. Menampilkan Daftar Buah
        2. Menambah Buah
        3. Menghapus Buah
        4. Membeli Buah
        5. Keluar Program

        Masukkan angka menu yang ingin dijalankan: ''')

    if(pilihan_menu == '1'):

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')
        
        for i in range(len(list_buah)):
            print(f"{i}\t| {list_buah[i]['nama']}   \t| {list_buah[i]['stok']}\t| {list_buah[i]['harga']}")

    elif(pilihan_menu == '2'):

        nama_buah = str(input('Masukkan nama buah: ').capitalize())
        stok_buah = int(input('Masukkan stok buah: '))
        harga_buah = int(input('Masukkan harga buah: '))
        
        for i in range(len(list_buah)):
            if nama_buah in (list_buah[i]['nama']) and harga_buah == (list_buah[i]['harga']):
                list_buah[i]['stok'] += stok_buah
                break
            elif nama_buah in (list_buah[i]['nama']) and harga_buah != (list_buah[i]['harga']):
                list_buah.append({
                    'nama': nama_buah,
                    'stok': stok_buah,
                    'harga': harga_buah
                })
                break

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')
        
        for i in range(len(list_buah)):
            print(f"{i}\t| {list_buah[i]['nama']}   \t| {list_buah[i]['stok']}\t| {list_buah[i]['harga']}")

    elif(pilihan_menu == '3'):

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')
        
        for i in range(len(list_buah)):
            print(f"{i}\t| {list_buah[i]['nama']}   \t| {list_buah[i]['stok']}\t| {list_buah[i]['harga']}")
        
        index_buah = int(input('Masukkan index buah yang ingin dihapus: '))
        del list_buah[index_buah]
        
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')
        
        for i in range(len(list_buah)):
            print(f"{i}\t| {list_buah[i]['nama']}   \t| {list_buah[i]['stok']}\t| {list_buah[i]['harga']}")

    elif(pilihan_menu == '4'):

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stok\t| Harga')
        
        for i in range(len(list_buah)):
            print(f"{i}\t| {list_buah[i]['nama']}   \t| {list_buah[i]['stok']}\t| {list_buah[i]['harga']}")
        
        while True:
            index_buah = int(input('Masukkan index buah yang ingin dibeli: '))
            jumlah_buah = int(input('Masukkan jumlah yang ingin dibeli: '))
            
            if(jumlah_buah > list_buah[index_buah]['stok']):
                print(f"Stok tidak cukup. Stok {list_buah[index_buah]['nama']} tersisa {list_buah[index_buah]['stok']} buah")
            else:
                cart.append({
                    'nama': list_buah[index_buah]['nama'], 
                    'jumlah': jumlah_buah, 
                    'harga': list_buah[index_buah]['harga'], 
                    'index': index_buah
                })

            for item in cart:
                    list_buah[item['index']]['stok'] -= item['jumlah']

            print('Isi Cart:')
            print(f'Nama\t| Jumlah\t| Harga')

            for item in cart:
                print(f"{item['nama']}\t| {item['jumlah']}\t\t| {item['harga']}")

            break

        while True:
            checker = input('Mau beli yang lain? (Ya/Tidak) = ')
            
            if(checker == 'ya'):
                index_buah = int(input('Masukkan index buah yang ingin dibeli: '))
                print(f"Sisa stok {list_buah[index_buah]['nama']} adalah {list_buah[index_buah]['stok']}.")

                if(list_buah[index_buah]['stok'] == 0):
                    print('Maaf, stok buah yang dipilih sedang kosong. Silakan pilih buah yang lain jika mau.')
                    continue
                else:
                    jumlah_buah_tambahan = int(input('Masukkan jumlah yang ingin dibeli: '))
                    

                if(jumlah_buah_tambahan > list_buah[index_buah]['stok']):
                    print(f'Stok tidak cukup, masukkan jumlah yang sesuai dengan sisa stok.')
                else:
                    cart.append([list_buah[index_buah]['nama'], jumlah_buah_tambahan, list_buah[index_buah]['harga'], index_buah]) 
                    list_buah[index_buah]['stok'] -= jumlah_buah_tambahan
            
            else:
                break

        print('Daftar Belanja:')
        print('Nama\t| Jumlah\t| Harga\t| Total Harga')
        
        total_harga = 0
        
        for item in cart:
            print(f"{item['nama']}\t| {item['jumlah']}\t\t| {item['harga']}\t| {item['jumlah'] * item['harga']}")
            total_harga += item['jumlah'] * item['harga']    
        
        while True:
            print(f'Total yang harus dibayar = {total_harga}')
            if total_harga != 0:
                jumlah_uang = int(input('Masukkan jumlah uang: '))
            
                if(jumlah_uang > total_harga):
                    kembali = jumlah_uang - total_harga
                    print(f'Terima kasih \n\nUang kembalian Anda: {kembali}')
                    cart.clear()
                    break
            
                elif(jumlah_uang == total_harga):
                    print('Terima kasih')
                    cart.clear()
                    break
            
                else:
                    kekurangan = total_harga - jumlah_uang
                    print(f'Uang Anda kurang sebesar {kekurangan}')

            else:
                print(f'Terima kasih telah berkunjung.')
                break
                
    elif(pilihan_menu == '5'):
        break
    
