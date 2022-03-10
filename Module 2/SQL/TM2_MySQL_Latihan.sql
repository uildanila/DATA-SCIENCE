# Latihan SQL DAY 2

# World

#1. Ada berapa negara di database world?
#2. Ada berapa negara di Africa?
#3. Tampilkan 5 negara dengan populasi terbesar!
#4. Tampilkan rata-rata harapan hidup tiap benua dan urutkan dari yang terendah!
#5. Tampilkan jumlah region tiap benua dengan jumlah region lebih dari 3!
#6. Tampilkan rata-rata GNP di Afrika berdasarkan regionnya dan urutkan dari GNP terbesar
#7. Tampilkan negara di Eropa yang memiliki nama dimulai dengan huruf I!
#8. Ada berapa bahasa berbeda di dunia?
#9. Tampilkan nama negara yang panjang hurufnya 6 huruf dan berakhiran 'O'!
#10. Tampilkan 7 bahasa terbesar di Indonesia (secara persentase, dengan persentase dibulatkan)!

USE world;
SHOW FULL TABLES;

#1. Ada berapa negara di database world?
SELECT COUNT(name) AS Jumlah_Negara 
FROM country;


#2. Ada berapa negara di Africa?
SELECT COUNT(name) AS Jumlah_Negara_Afrika
FROM country 
WHERE continent = 'Africa';


#3. Tampilkan 5 negara dengan populasi terbesar!
SELECT name, population 
FROM country
ORDER BY population DESC
LIMIT 5;


#4. Tampilkan rata-rata harapan hidup tiap benua dan urutkan dari yang terendah!
SELECT Continent, AVG(LifeExpectancy) AS Average_Life_Expectancy 
from country
GROUP BY continent
ORDER BY Average_Life_Expectancy;


#5. Tampilkan jumlah region tiap benua dengan jumlah region lebih dari 3
SELECT continent, COUNT(region) AS Jumlah_Region
FROM country
GROUP BY continent
HAVING Jumlah_Region > 3;


#6. Tampilkan rata-rata GNP di Afrika berdasarkan regionnya dan urutkan dari GNP terbesar
SELECT region, AVG(GNP) as Average_GNP 
FROM country
WHERE continent='Africa'
GROUP BY region
ORDER BY Average_GNP DESC;


#7. Tampilkan negara di Eropa yang memiliki nama dimulai dengan huruf I
SELECT name AS Negara, continent 
FROM country
WHERE name LIKE 'I%' AND continent='Europe';


#8. Ada berapa bahasa berbeda di dunia?
SELECT COUNT(DISTINCT(language)) AS Jumlah_Bahasa 
FROM countrylanguage;


#9. Tampilkan nama negara yang panjang hurufnya 6 huruf dan berakhiran 'O'
SELECT name 
FROM country
WHERE name LIKE '_____o';

SELECT name, LENGTH(name) 
FROM country
WHERE name LIKE '_____o';


#10. Tampilkan 7 bahasa terbesar di Indonesia (secara persentase, dengan persentase dibulatkan)
SELECT Language, ROUND(Percentage) AS Persentase
FROM countrylanguage 
WHERE countrycode = 'IDN' 
ORDER BY Percentage DESC
LIMIT 7;

## =========================================================================================================================

# SAKILA

#1. Tampilkan aktor yang memiliki nama depan ‘Scarlett’! 
#2. Tampilkan aktor yang memiliki nama belakang ‘Johansson’!
#3. Berapa banyak nama belakang aktor yang unik?
#4. Tampilkan 5 nama belakang aktor yang keluar hanya satu kali!
#5. Tampilkan 5 nama depan aktor yang keluar lebih dari satu kali!
#6. Berapa rata-rata durasi film di database Sakila?
#7. Tahun berapa film ‘Airport Pollock’ dirilis?
#8. Tampilkan judul film dengan rating R dan berdurasi antara 50 sampai 100
#9. Nomor customer_id berapakah yang paling sering melakukan transaksi?
#10. Adakah customer yang nama depan dan belakangnya hanya terdiri dari 3 karakter?


SELECT COUNT(district) AS Jumlah
FROM address
WHERE district = 'Oriental';



# SOLUSI

USE sakila;
SHOW FULL TABLES;
SELECT * FROM rental;


#1. 
SELECT first_name AS Nama_Depan, last_name AS Nama_Belakang
FROM actor
WHERE first_name = 'Scarlett'; 


#2.
SELECT first_name AS Nama_Depan, last_name AS Nama_Belakang
FROM actor
WHERE last_name = 'Johansson'; 


#3. 
SELECT COUNT(DISTINCT(last_name)) AS Jumlah_Nama_Terakhir
FROM actor;


#4.
SELECT last_name AS Nama_Belakang
FROM actor
GROUP BY last_name
HAVING COUNT(last_name) = 1
limit 5;


#5. 
SELECT first_name AS Nama_Depan
FROM actor
GROUP BY first_name
HAVING COUNT(first_name) > 1
limit 5;


#6.
SELECT AVG(length) AS Rata_Durasi
FROM film;


#7. 
SELECT title AS Judul, release_year AS Tahun_Release
FROM film
where title = 'Airport Pollock';


#8.
SELECT title AS Judul_Film, rating AS Rating, length AS Durasi
FROM film
WHERE rating = 'R' AND length BETWEEN 50 AND 100;

SHOW FULL TABLES;

#9.
SELECT customer_id, COUNT(customer_id) AS Loyal_Customer
FROM rental
GROUP BY customer_id
ORDER BY Loyal_Customer DESC
LIMIT 1;


#10.
SELECT first_name, last_name
FROM customer
WHERE LENGTH(first_name) = 3 AND LENGTH(last_name) = 3;