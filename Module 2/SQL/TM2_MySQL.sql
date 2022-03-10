## DAY 2

## STRING PATTERN

# LIKE digunakan untuk membatasi atau filtering baris yang berisi kolom berupa teks.
# LIKE digunakan setelah WHERE clause. 

# % -->  Menunjukkan bisa diawali atau diakhiri dengan berapapun jumlah karakter.
# _ --> Menunjukkan bisa diawali atau diakhiri dengan 1 karakter per 1 underscore.

USE world;

# Untuk menampilkan seluruh tabel beserta keterangannya
SHOW FULL TABLES;

# Contoh materi hari pertama
SELECT * 
FROM city
WHERE Population > 5000000;


# Filtering dengan menggunakan LIKE pada kolom berisi teks
SELECT * FROM city
WHERE District LIKE 'England';

# Mencari kota yang District-nya diawali huruf 'z' dan diikuti berapapun jumlah hurufnya.
SELECT * FROM city
WHERE District LIKE 'Z%';

# Mencari kota yang District-nya diawali huruf 'z' dan diikuti 4 huruf
SELECT * FROM city
WHERE District LIKE 'Z____';

# Mencari kota yang CountryCode-nya diakhiri dengan huruf 'a' dan diawali berapapun jumlah hurufnya
SELECT * FROM city
WHERE CountryCode LIKE '%a';

# Mencari kota yang nama hurufnya 6 huruf
SELECT * FROM city
WHERE Name LIKE '______';

# Mencari kota yang namanya 6 huruf dan huruf terakhirnya adalah 'o'
SELECT * FROM city
WHERE Name LIKE '_____o';

# Mencari kota yang namanya mengandung huruf 'x', baik di depan, tengah, atau belakang
SELECT * FROM city
WHERE Name LIKE '%x%';

# Mencari kota yang namanya mengandung huruf 'x', diawali 2 huruf dan diikuti 2 huruf setelah 'x'
SELECT * FROM city
WHERE Name LIKE '__x__';

# Mencari kota yang namanya mengandung huruf 'x' di tengah (tidak diawali atau diakhiri 'x')

# Cara 1 tanpa underscore
SELECT * FROM city
WHERE Name LIKE '%x%'
AND Name NOT LIKE 'x%'
AND Name NOT LIKE '%x';


SELECT * FROM city
WHERE Name LIKE '_%x%_'
AND Name NOT LIKE 'x%'
AND Name NOT LIKE '%x';

# NOT untuk negasi
# Mencari kata yang namanya bukan sesuai dengan yang didefinisikan.

# Mencari kota yang namanya bukan diawali huruf 'a'
SELECT * FROM city
WHERE Name NOT LIKE 'a%';

## =========================================================================================================

## RANGE

# BETWEEN AND digunakan untuk membatasi rentang nilai tertentu.
# BETWEEN harus mengandung nilai awal dan nilai akhir (nilai awal dan akhir termasuk).
# NOT BETWEEN --> kita mencari nilai yang bukan dalam rentang yang kita definisikan.

SELECT * FROM city
WHERE Population >= 5000000 AND Population <= 6000000;

# Populasi kota antara 5000000 sampai 6000000 penduduk, termasuk kota yang punya populasi rentang tersebut
SELECT * FROM city
WHERE Population BETWEEN 5000000 AND 6000000;

# Mencari kota yang populasinya di bawah 100 ribu dan di atas 8 juta
SELECT * FROM city
WHERE Population NOT BETWEEN 100000 AND 8000000;


## =========================================================================================================

## SORTING

# ORDER BY digunakan untuk mengurutkan data baik ascending atau descending. 
# Ascending: A --> Z, nilai kecil ke nilai besar (Default pada MySQL).
# Descending: Z --> A, nilai besar ke nilai kecil. 

# Keyword: ASC DESC


# Mengurutukan populasi kota dari yang penduduknya paling sedikit
SELECT * FROM city
ORDER BY Population;

# Mengurutkan populati kota dari yang penduduknya paling terbanyak
SELECT * FROM city
ORDER BY Population DESC;

# Mencari 5 kota dengan populasi terbanyak
SELECT * FROM city
ORDER BY Population DESC
LIMIT 5; # LIMIT didefinisikan paling akhir

# Mengurutkan nama kota dari Z ke A 
SELECT * FROM city
ORDER BY Name DESC;

# Mengurutkan nama kota dari A ke Z
SELECT * FROM city
ORDER BY Name;

# Mengurutkan kota berdasarkan CountryCode dari A ke Z, lalu District dari A ke Z
SELECT * FROM city
ORDER BY CountryCode, District;

# Mengurutkan kota berdasarkan CountryCode dari A ke Z, lalu District dari Z ke A 
SELECT * FROM city
ORDER BY CountryCode, District DESC;

## =========================================================================================================

## GROUP BY

# GROUP BY digunakan untuk mengelompokkan data berdasarkan baris tertentu. 
# Contoh: Total populasi berdasarkan negara. 

# GROUP BY biasanya berpasangan dengan aggregate function (SUM, AVG< COUNT, MIN, MAX, dll).
# Untuk melakukan filtering setelah GROUP BY, tidak bisa menggunakan WHERE clause, tapi harus menggunakan HAVING. 


# Menghitung jumlah kota berdasarkan negara.
SELECT CountryCode, COUNT(Name) AS Jumlah_Kota
FROM city
GROUP BY CountryCode;

# Menghitung jumlah kota berdasarkan negara, kemudian diurutkan dari jumlah kota terbanyak.
SELECT CountryCode, COUNT(Name) AS Jumlah_Kota
FROM city
GROUP BY CountryCode
ORDER BY Jumlah_Kota DESC;

# Rata-rata populasi kota berdasarkan District-nya, kemudian diurutkan dari populasi terbanyak, tapi hanya diambil 5 terbesar saja.
SELECT District, AVG(Population) AS Average_Population	# Memilih kolom yang ingin ditampilkan
FROM city												# Mengambil dari tabel apa
GROUP BY district										# Mengelompokkan berdasarkan kolom yang didefinisikan
ORDER BY Population DESC								# Mengurutkan berdasarkan kolom yang didefinisikan dan diurutkan dari yang terbesar ke terkecil
LIMIT 5;												# Membatasi hanya 5 baris/data teratas saja yang muncul di output


# Menampilkan total populasi dan jumlah kota untuk tiap negara
SELECT CountryCode, SUM(Population) AS Jumlah_Populasi, COUNT(Name) AS Jumlah_Kota
FROM city
GROUP BY CountryCode;

# Rata-rata populasi suatu kota dan jumlah kota untuk tiap negara yang kode negaranya berawalan huruf 'B' dan diurutkan dari populasi terkecil
SELECT CountryCode AS Negara, AVG(Population) AS Rata_rata_Populasi, COUNT(Name) AS Jumlah_Kota
FROM city
GROUP BY CountryCode
HAVING CountryCode LIKE 'B%'
ORDER BY Rata_rata_populasi;

SELECT CountryCode AS Negara, AVG(Population) AS Rata_rata_Populasi, COUNT(Name) AS Jumlah_Kota
FROM city
WHERE CountryCode LIKE 'B%'
GROUP BY CountryCode
ORDER BY Rata_rata_populasi;

# Rata-rata populasi suatu kota dan jumlah kota untuk tiap negara, yang jumlah kotanya lebih dari 100 dan diurutkan dari populasi terbesar.
SELECT CountryCode, AVG(Population) AS Rata_rata_Populasi, COUNT(Name) AS Jumlah_Kota
FROM city
GROUP BY CountryCode
HAVING Jumlah_Kota > 100
ORDER BY Rata_rata_Populasi DESC;

SELECT CountryCode, AVG(Population) AS Rata_rata_Populasi, COUNT(Name) AS Jumlah_Kota
FROM city
WHERE Jumlah_Kota > 100
GROUP BY CountryCode
ORDER BY Rata_rata_Populasi DESC; # Error, filtering dilakukan setelah grouping, sehingga harus menggunakan HAVING. 

## =========================================================================================================

## BUILT-IN DATABASE FUNCTION

# Aggregate function: berlaku untuk kumpulan/kelompok data atau seluruh data dalam sebuah kolom. 
# Contoh: SUM, COUNT, AVG, MIN, MAX, dll.

# Contoh
SELECT CountryCode, SUM(Population) # Kita menjumlahkan semua data di kolom Population
FROM city
GROUP BY CountryCode;

# Scalar function: berlaku pada tiap baris pada suatu kolom. 
# Contoh: ROUND, LENGTH, UCASE, LCASE, dll. 

# Contoh
SELECT District, LENGTH(District) AS Panjang_Kata  # Mencari jumlah karakter dari kolom District untuk tiap baris
FROM city;

SELECT Name, UCASE(Name)
FROM city;


# Menampilkan nama kota dan jumlah karakternya, diambil yang terpanjang
SELECT Name, LENGTH(Name) AS Jumlah_Karakter
FROM city
ORDER BY Jumlah_Karakter DESC
LIMIT 1;

# Menampilkan jumlah karakter nama kota terpanjang
SELECT MAX(LENGTH(Name)) # Aggregate dan scalar function bisa digabung
FROM city;

# Menampilkan nilai LifeExpectancey yang dibulatkan 
SELECT Name, ROUND(LifeExpectancy)
FROM country;

# Menampilkan nilai GNPOld yang dibulatkan 1 digit di belakang koma
SELECT Name, ROUND(GNPOld, 1)
FROM country;

# Menampilkan kepadatan penduduk (2 digit di belakang koma)
SELECT Name, ROUND((Population/SurfaceArea), 2) AS Kepadatan_Penduduk
FROM Country;

SELECT * FROM country;

## =========================================================================================================

## DATE & TIME BUILT-IN FUNCTION

USE sakila;
SHOW FULL TABLES;

# Untuk melihat tipe data tiap kolom pada suatu tabel
SHOW COLUMNS FROM payment;

# Menampilkan tahun dari suatu kolom (YEAR)
SELECT payment_id, payment_date, YEAR(payment_date)
FROM payment; 

# Menampilkan bulan ke berapa (1-12) --> MONTH
SELECT payment_id, payment_date, MONTH(payment_date)
FROM payment;

# Menampilkan nama bulan (Jan-Dec) --> MONTHNAME
SELECT payment_id, payment_date, MONTHNAME(payment_date)
FROM payment;

# Menampilkan tanggal (1-31) --> DAY
SELECT payment_id, payment_date, DAY(payment_date)
FROM payment;

# Menampilkan hari --> DAYNAME
SELECT payment_id, payment_date, DAYNAME(payment_date)
FROM payment;

# Menampilkan pukul berapa (0-23) --> HOUR
SELECT payment_id, payment_date, HOUR(payment_date)
FROM payment;

# Menampilkan menit (0-59) --> MINUTE
SELECT payment_id, payment_date, MINUTE(payment_date)
FROM payment;

# Menampilkan detik (0-59) --> SECOND
SELECT payment_id, payment_date, SECOND(payment_date)
FROM payment;

# Menmapilkan pekan ke berapa (0-53) --> WEEK atau WEEKOFYEAR
SELECT payment_id, payment_date, WEEK(payment_date)
FROM payment;

SELECT payment_id, payment_date, WEEKOFYEAR(payment_date)
FROM payment;

# Menampilkan hari ke berapa dalam 1 minggun (0: Monday, 6: Sunday) --> WEEKDAY
SELECT payment_id, payment_date, WEEKDAY(payment_date), DAYNAME(payment_date)
FROM payment;
