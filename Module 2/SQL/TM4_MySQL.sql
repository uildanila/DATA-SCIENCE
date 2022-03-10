## SQL DAY 4

## COMMON TABLE EXPRESSION (CTE)

# CTE adalah sebuah query dalam SQL yang berupa sub-query yang ditulis secara terpisah, sehingga dapat dipergunakan kembali

# CTE ditulis sebelum melakukan operasi SELECT ... FROM ... 

# Syntax: 
# WITH nama_tabel_CTE AS (isi sub-query nya)

# Cara kerjanya, SQL akan menjalankan CTE terlebih dahulu, kemudian hasilnya disimpan dalam sebuah tabel sementara sesuai dengan nama CTE-nya.
# Kemudian, tabel CTE ini bisa digunakan berulang kali untuk keperluan pengambilan data atau join table. 

# Kelebihan:
	# - Cara penulisannya lebih rapi dan mudah dibaca.
	# - Dapat digunakan kembali. 
    
# Kekurangan:
	# - Running lebih lambat dari metode lainnya. 
    
USE sakila;
SHOW FULL TABLES;

SELECT * FROM film;

## Contoh
# Menampilkan film dengan rental duration yang lebih besar dari rata-rata rental duration secara keseluruhan.

# Pertama, cari dulu rata-rata rental duration secara keseluruhan
SELECT AVG(rental_duration)
FROM film;

# Kemudian, query di atas dijadikan sebagai sub-query untuk filtering
SELECT * FROM film
WHERE rental_duration > (SELECT AVG(rental_duration) FROM film);

## ==============================================================================================================

## Cara menggunakan CTE

## Membuat tabel CTE berisi average rental duration

# Cara 1
WITH avg_rental_duration AS 
							(SELECT AVG(rental_duration) AS avg_rental FROM film)	# CTE

SELECT * FROM film
WHERE rental_duration > (SELECT avg_rental FROM avg_rental_duration);


# Cara 2
WITH avg_rental_duration AS
							(SELECT AVG(rental_duration) AS avg_rental FROM film)

SELECT * 
FROM film F, avg_rental_duration T 
WHERE F.rental_duration > T.avg_rental;


## Latihan

USE WORLD; 

# Gunakan CTE untuk menampilkan benua dengan jumlah negara lebih dari jumlah negara di benua North America.

# Pertama, kita cari dulu jumlah negara di continent North America
SELECT COUNT(name) AS jumlah_negara
FROM country
WHERE continent = 'North America';

# Query di atas, kita gunakan sebagai CTE
WITH tabel_jumlah_negara AS
							(SELECT COUNT(name) AS jumlah_negara_cte FROM country WHERE continent = 'North America')
                            
SELECT continent, COUNT(name) AS jumlah_negara
FROM country
GROUP BY continent
HAVING jumlah_negara > (SELECT jumlah_negara_cte FROM tabel_jumlah_negara);


## ==============================================================================================================

## WINDOW FUNCTION

# Kalau menggunakan GROUP BY, terdapat key column yang isinya adalah distinct value (nilai unik), dan kolom lainnya adalah agregasi.
# GROUP BY menyebabkan berkurangnya jumlah baris.
# Baris yang ditampilkan sesuai dengan jumlah distinct value pada key column. 

# Tapi, dengan WINDOW FUNCTION, kita dapat melakukan agregasi dengan tetap mempertahankan jumlah baris sebagaimana adanya. 
# Semua value tetap pada row-nya. 

USE sakila;

# Contoh dengan menggunakan GROUP BY

# Menampilkan rata-rata rental duration berdasarkan rating
SELECT rating, AVG(rental_duration)
FROM film
GROUP BY rating;

## ==============================================================================================================

## OVER PARTITION

# Cara kerja mirip dengan GROUP BY. Yang membedakan adalah jumlah baris yang dikembalikan pada output (mengembalikan sesuai dengan jumlah baris yang ada).

SELECT * FROM film;

SELECT film_id, title, rating, rental_rate,
	AVG(rental_rate) OVER () AS avg_rental_rate,								# Ini rata-rata rental_rate secara keseluruhan
    AVG(rental_rate) OVER () - rental_rate AS selisih_avg_dikurang_rental_rate	# Ini selisih rata-rata rental_rate keseluruhan dengan rental_rate tiap baris
FROM film;


# Menggunakan OVER PARTITION
SELECT film_id, title, rating, rental_rate,
	AVG(rental_rate) OVER (PARTITION BY rating) AS avg_rental_rate_by_rating,
	AVG(rental_rate) OVER (PARTITION BY rating) - rental_rate AS selisih
FROM film;


## Latihan

# Gunakan OVER PARTITION untuk menampilkan nama film, category, length, dan rata-rata durasi film berdasarkan category.

SHOW FULL TABLES;

# Mengambil data dari base table

SELECT A.film_id, A.title, C.name, A.length, 
	AVG(A.length) OVER (PARTITION BY B.category_id) AS avg_durasi
FROM film A
JOIN film_category B
ON A.film_id = B.film_id
JOIN category C
ON B.category_id= C.category_id;

# Mengambil data dari VIEW
SELECT * FROM film_list;

SELECT title, category, length,
	AVG(length) OVER (PARTITION BY category) AS avg_length_by_category
FROM film_list;


## ==============================================================================================================

## NON-AGGREGATE FUNCTION

## ROW_NUMBER

# Membuat kolom baru berisikan nomor baris.
# Mirip dengan index baris, tapi ROW_NUMBER ini disimpan dalam kolom. 

# Contoh

# Menampilkan ROW NUMBER secara keseluruhan
SELECT ROW_NUMBER () OVER () AS Nomor,
	title, rating, rental_duration
FROM film;

# Menampilkan ROW NUMBER berdasarkan rating-nya
SELECT ROW_NUMBER () OVER (PARTITION BY rating) AS Nomor_by_rating,
	title, rating, rental_duration
FROM film;

## ==============================================================================================================

## RANK DAN DENSE_RANK

# ROW_NUMBER menghitung baris data dalam angka 1 sampai n dari urutan terkecil.
# RANK dan DENSE_RANK menghitung urutan berdasarkan value yang ingin kita ukur dan bisa dari tertinggi ke terendah.


# Contoh

# Tampilkan ranking untuk category rating dengan total film paling banyak 

SELECT rating, COUNT(film_id) AS Jumlah_Film,
	RANK () OVER (ORDER BY COUNT(film_id) DESC) AS Ranking
FROM film
GROUP BY rating;

# ORDER BY seperti biasa, tanpa diketahui urutan atau ranking ke berapanya
SELECT rating, COUNT(film_id) AS Jumlah_Film
FROM film
GROUP BY rating
ORDER BY Jumlah_Film DESC;

# RANK --> dari peringkat 1 langsung lanjut ke peringkat 204 (karena ada 203 film yang berdurasi sewa 3 hari) --> WITH GAPS
SELECT film_id, title, rental_duration, 
	RANK () OVER (ORDER BY rental_duration) AS Ranking
FROM film;

# DENSE_RANK --> dari peringkat 1 lanjut ke peringkat 2, meskipun ada 203 film berdurasi 3 hari --> WITHOUT GAPS
SELECT film_id, title, rental_duration, 
	DENSE_RANK () OVER (ORDER BY rental_duration) AS Ranking
FROM film;


## ==============================================================================================================

## NTILE ()

# Mengelompokka data dari terkecil ke terbesar. Jumlah kelompoknya disesuaikan dengan persentase pembagian yang kita input-kan. 
# NTILE(4) --> Artinya data akan dibagi menjadi 4 bagian/kelompok dengan tiap kelompoknya memiliki jumlah data yang sama. 

# Contoh

SELECT title, rating,
	NTILE(4) OVER () AS Quartile,
    NTILE(10) OVER () AS Percentile,
    ROW_NUMBER() OVER () AS Nomor
FROM film;

## ==============================================================================================================

## SLIDING WINDOWS

# Digunakan untuk menghitung angka agregat yang bersifat bergerak atau kumulatif. 
# Bisa digunakan untuk menghitung moving avera, cumulative sum, dll. 

# Syntax:
# OVER (ROWS BETWEEN tipe_sliding1 AND tipe_sliding2)

# TIPE SLIDING:
	# - CURRENT ROW --> Row yang aktif
    # - FOLLOWING --> Row setelah
    # - PRECEDING --> Row sebelum
    # - UNBOUNDED PRECEDING --> Row pertama
    # - UNBOUNDED FOLLOWING --> Row terakhir

# Contoh

# Menghitung cummulative sum dari total film berdasarkan rating

WITH tabel_jumlah_film_per_rating AS
	(SELECT rating, COUNT(film_id) AS jumlah_film
    FROM film
    GROUP BY rating)
    
SELECT rating, jumlah_film, 
	SUM(jumlah_film) OVER (ORDER BY jumlah_film ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_sum_jumlah_film,
    AVG(jumlah_film) OVER (ORDER BY jumlah_film ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS moving_avg_jumlah_film
FROM tabel_jumlah_film_per_rating;
