## DAY 1

# Berbeda dengan Python, syntax pada MySQL tidak case sensitive.

## DATA DEFINITION LANGUAGE (DDL)

# DDL berhubungan dengan database schemas dan deskripsinya mengenai bagaimana data tersimpan di database.alter

# Contoh DDL:
	# CREATE - membuat database beserta objeknya (table, index, views, store procedure).
    # ALTER - mengubah struktur pada database (misal: menambah kolom pada suatu tabel).
    # DROP - menghapus objek dari database, dan juga menghapus database itu sendiri.
    # TRUNCATE - menghapus semua data dari tabel, tapi tidak dengan tabelnya.
    # COMMENT - menambah komentar ke data dictionary.
    # RENAME - menamai ulang objek.

## DATA MANIPULATION LANGUAGE (DML)

# DML berhubungan dengan manipulasi data pada tabel.

# Contoh DML:
	# SELECT - mengambil data dari tabel.
    # INSERT - menambahkan data ke tabel.
    # UPDATE - update data yang sudah ada pada tabel.
    # DELETE - menghapus data dari tabel.
    
## =======================================================================================================================

## CREATE DATABASE AND TABLE STATEMENT

# Mengecek ada database apa saja pada local server
SHOW DATABASES;

# Membuat database
CREATE DATABASE seller;

# Menggunakan database
USE seller;

# Menghapus database
DROP DATABASE seller;


# Membuat tabel pada database
CREATE TABLE person (PersonID int,
					LastName varchar(255),
                    FirstName varchar(255),
                    Address varchar(255)
                    );

# Mengecek tabel pada database
SHOW TABLES;

# Mengecek semua kolom pada tabel
SELECT * FROM person;

# Membuat tabel baru dari kolom pada tabel yang sudah ada
CREATE TABLE people AS
SELECT PersonID, LastName
FROM person;

SELECT * FROM people;

## =======================================================================================================================

## SELECT TABLE STATEMENT

# SELECT digunakan untuk mengakses data dari suatu database.
# Syntax --> SELECT nama_kolom FROM nama_tabel;

# Menggunakan database world
USE world;

# Mengecek ada tabel apa saja di database world
SHOW TABLES;

# Mengakses seluruh data pada tabel city
SELECT * FROM city;

# Mengakses hanya beberapa kolom saja dari tabel city
SELECT Name, District, Population
FROM city;

## =======================================================================================================================

## DISTINCT, LIMIT, COUNT, AVG, SUM

# DISTINCT

# SELECT DISTINCT digunakan untuk mengeluarkan data unik pada suatu kolom tertentu.
# Syntax --> SELECT DISTINCT nama_kolom
			# FROM nama_tabel;

# Menampilkan data nama kota yang unik pada tabel city
SELECT DISTINCT Name 
FROM city;

# Menampilkan nama district yang unik pada tabel city
SELECT DISTINCT District
FROM city;

## =======================================================================================================================

# LIMIT

# LIMIT digunakan untuk membatasi jumlah baris yang akan dimunculkan di output.
# Syntax --> SELECT nama_kolom
			# FROM nama_tabel
			# LIMIT 5;
            
# Menampilkan hanya 5 baris teratas pada tabel city
SELECT * FROM city
LIMIT 5;

# Menampilkan hanya 4 baris teratas dengan kolom tertentu saja pada tabel city
SELECT Name, CountryCode
FROM city
LIMIT 4;

## =======================================================================================================================

# COUNT

# Count digunakan untuk menghitung jumlah data pada kolom tertentu.
# Syntax --> SELECT COUNT(nama_kolom)
			# FROM nama_tabel;
            
# Menghitung jumlah district pada tabel city
SELECT COUNT(DISTRICT)
FROM city;

# Menghitung jumlah continent pada tabel country
SELECT COUNT(Continent)
FROM country;

## =======================================================================================================================

# AVG

# AVG digunakan untuk menghitung nilai rata-rata pada kolom yang berisi nilai numerikal. 
# Syntax --> SELECT AVG(nama_kolom)
			# FROM nama_tabel;
            
# Menghitung rata-rata populasi dari kolom Population pada tabel city
SELECT AVG(Population)
FROM city;

# Menghitung rata-rata usia harapan hidup pada tabel country
SELECT AVG(LifeExpectancy)
FROM country;

SELECT * FROM country LIMIT 3;

## =======================================================================================================================

# SUM

# SUM digunakan untuk menghitung jumlah data pada kolom yang berisi nilai numerikal.
# Syntax --> SELECT SUM(nama_kolom)
			# FROM nama_tabel;
            
# Menghitung total populasi pada tabel city
SELECT SUM(Population)
FROM city;

# Menghitung jumlah name pada tabel city
SELECT SUM(Name)
FROM city; -- Output 0 karena kolom name tidak berisi numerik. 

## =======================================================================================================================

## INSERT STATEMENT

# INSERT INTO digunakan untuk memasukkan atau menambahkan data baru ke dalam tabel.
# Caranya ada 2:
		# 1. Memasukkan nama kolom dan nilainya secara spesifik. 
				# Syntax --> INSERT INTO nama_tabel (nama_kolom1, nama_kolom2, ...)
							# VALUES (value1, value2, ...) 
                            
		# 2. Kita diasumsika akan mengisi data pada seluruh kolom di tabel.
				# Syntax --> INSERT INTO nama_tabel
							# VALUES (value1, value2, ...)
                            
# Contoh cara pertama

# Memasukkan data baru ke tabel person pada database seller

USE seller;
SHOW TABLES;
SELECT * FROM person;

INSERT INTO person (PersonID, LastName, FirstName, Address)
VALUES (01, 'Sardi', 'Andi', 'Jl. ABC');

INSERT INTO person (PersonID, LastName, FirstName)
VALUES (03, 'Ari', 'Ramdhan'); # Bisa input data sesuai dengan nama kolom yang didefinisikan. Jika ada kolom yang tidak diinput datanya, akan ditampilkan sebagai Null.

# Contoh cara kedua

INSERT INTO person
VALUES (02, 'Arika', 'Ratni', 'Jl. BSD');

INSERT INTO person
VALUES (03, 'Ari', 'Ramdhan'); # Tidak bisa input data, karena jumlah value yang dimasukkan kurang dari jumlah kolom yang ada.

## =======================================================================================================================

## WHERE STATEMENT

# WHERE digunakan untuk mem-filter atau membatasi data yang ingin dicari.
# WHERE akan menampilkan data sesuai dengan kondisi yang diminta oleh pengguna.
# Jika ada lebih dari 1 kondisi, bisa dihubungkan dengan AND atau OR. 

# Syntax --> SELECT nama_kolom1, nama_kolom2, ...
			# FROM nama_tabel
            # WHERE condition;
            
# Menampilkan seluruh kolom dari tabel city, dengan syarat nilai pada kolom Population harus lebih besar dari 1 juta
USE world;

SELECT * FROM city
WHERE Population > 1000000;

# Filtering 2 kondisi dengan AND (kedua kondisi harus terpenuhi)
SELECT * FROM country
WHERE Population > 100000000 AND GNP > 500000;

# Filtering 2 kondisi dengan OR (hanya salah satu kondisi saja yang harus terpenuhi)
SELECT * FROM country
WHERE Population > 100000000 OR GNP > 500000;

## =======================================================================================================================

## UPDATE & DELETE STATEMENTS

# UPDATE digunakan untuk memodifikasi atau mengedit data yang sudah ada pada tabel tertentu. 
# UPDATE bisa digabungkan dengan WHERE agar data yang di-update bisa lebih spesifik. 

# Syntax --> UPDATE nama_tabel
			# SET nama_kolom1 = value1, nama_kolom2 = value2, ...
            # WHERE condition;
            
# Melakukan update pada tabel person di database seller

USE seller;
SELECT * FROM person;

# Jika terjadi error ketika menjalankan query UPDATE. Tambahkan query berikut:
SET SQL_SAFE_UPDATES = 0;

UPDATE person
SET Address = 'Jl. Sayur'
WHERE PersonID = 3;

UPDATE person
SET Address = 'Jl. Asem'; # Mengubah semua value pada suatu kolom tanpa WHERE condition. Value tiap baris di kolom tersebut akan menjadi sama.

# Mengubah data pada PersonID = 2
UPDATE person
SET FirstName = 'Ratna', Address = 'Jl. Manis'
WHERE PersonID = 2;

## =======================================================================================================================

# DELETE

# DELETE digunakan untuk menghapus bari data di tabel tertentu. 
# Syntax --> DELETE FROM nama_tabel
			# WHERE condition;
            
# Menghapus PersonID = 3 pada tabel person
DELETE FROM person
WHERE PersonID = 3;

## =======================================================================================================================

# Buatlah tabel baru bernama 'pelanggan' yang berisi kolom NomorID, Nama, Usia, Kota, TahunDaftar dengan total 11 baris data.


# SOLUSI

# Membuat tabel 'pelanggan'
CREATE TABLE pelanggan (NomorID int,
						Nama varchar(255),
                        Usia int,
                        Kota varchar(255),
                        TahunDaftar int
                        );

# Cek tabel pada database seller
SHOW TABLES;

# Menambahkan data pada tabel pelanggan
INSERT INTO pelanggan
VALUES (1, 'Andi', 33, 'Bekasi', 2001),
		(2, 'Rudi', 42, 'Bontang', 2001),
        (3, 'Samuel', 41, 'Jakarta', 2002),
        (4, 'Rika', 31, 'Bandung', 2003),
        (5, 'Luis', 29, 'Bandung', 2004),
        (6, 'Marsha', 34, 'Tangerang', 2005),
        (7, 'Noyla', 30, 'Semarang', 2006),
        (8, 'Burhan', 45, 'Surabaya', 2007),
        (9, 'Fahri', 39, 'Jakarta', 2007),
        (10, 'Lena', 35, 'Jakarta', 2008),
        (11, 'Mardi', 43, 'Bekasi', 2009);
        
# Cek data pada tabel pelanggan
SELECT * FROM pelanggan;

