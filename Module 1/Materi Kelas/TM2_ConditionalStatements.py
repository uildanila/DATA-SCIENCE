# BOOLEAN

# Tipe data yang hanya terdiri dari True dan False

# print(True)
# print(False)

## =============================================================

# COMPARISON OPERATORS

# print(5 > 3) # True
# print(4 >= 3) # True
# print(5 < 3) # False
# print(5 <= 3) # False
# print(3 <= 3) # True
# print(5 != 3) # True
# print(5 == 3) # False

## =============================================================

# LOGICAL OPERATORS (AND, OR, NOT)

# and
# Semua kondisi harus True untuk menghasilkan output True
# Jika salah satu ada yang False, maka hasilnya akan False

# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False

# or
# Minimal ada satu kondisi yang bernilai True, maka outputnya akan menjadi True
# Jika semua kondisi bernilai False, maka outputnya akan menjadi False

# print(True or True) # True
# print(True or False) # True
# print(False or False) # False

# not
# Untuk mengembalikan nilai kebalikannya

# print(not True) # False
# print(not False) # True

## =============================================================

# CONDITIONAL STATEMENTS

# Program akan melakukan suatu tugas, jika suatu kondisi terpenuhi.

# IF STATEMENT
# - Jika kondisi terpenuhi (True), maka tugas dijalankan oleh program dan sebaliknya jika bernilai False

# umur = 17

# if umur >= 18:
#     print(f'Umur Anda adalah {umur} tahun')
#     print(f'Silakan mendaftar')


# IF ELSE
# - Jika kondisi terpenuhi pada if (bernilai True), maka tugas di if statements dijalankan
# - Jika kondisi tidak terpenuhi pada if (bernilai False), maka tugas di else statements yang dijalankan

# if umur >= 18:
#     print(f'Umur Anda adalah {umur} tahun')
#     print(f'Silakan mendaftar')
# else:
#     print('Silakan coba kembali')


# IF ELIF ELSE
# - Jika kondisi terpenuhi pada if (bernilai True), maka tugas di if statements dijalankan
# - Jika kondisi tidak terpenuhi pada if (bernilai False), maka tugas di elif statements dijalankan
# - Jika kondisi tidak terpenuhi pada elif (bernilai False), maka tugas di else statements dijalankan

nilai = 90

if nilai >= 90:
    print('Nilai Anda A')
elif nilai >= 70:
    print('Nilai Anda B')
elif nilai >= 50:
    print('Nilai Anda C')
else:
    print('Anda tidak lulus')