## TM3 MYSQL

## SUB-QUERY

# Sub-query adalah SQL query di dalam query (seperti nested loop pada Python).
# Sub-query disebut juga sebagai inner query. 
# Jadi, kalau misalnya ada 2 SELECT clause dalam 1 query, SELECT clause yang pertama disebut outer query, sedangkan yang kedua adalah sub-query/inner query.

# Ketika mengeksekusi query, MySQL akan mengeksekusi sub-query (inner query) terlebih dahulu, lalu nanti hasilnya akan digunakan untuk outer query. 
# Gunakan IN atau NOT IN operator pada WHERE clause jika sub-query mengembalikan lebih dari 1 value/data. 


# Contoh syntax

# SELECT nama_kolom1
# FROM nama_tabel
# WHERE nama_kolom2 = (SELECT MAX(nama_kolom2) FROM nama_tabel


# Kita tidak bisa menggunakan aggregate function (AVG, SUM, COUNT, dll) di dalam WHERE clause. 
# Oleh karena itu, kita membutuhkan sub-query agar dapat menggunakan aggregate function tersebut. 

USE employees;
SHOW FULL TABLES;
SELECT * FROM employees;

# Contoh syntax sub-query setelah WHERE clause

# SELECT ID, Name, Salary
# FROM employees
# WHERE Salary < (SELECT AVG(Salary) FROM employees);


# Contoh syntax 2
# SELECT customerName
# FROM customers
# WHERE customerID NOT IN (SELECT DISTINCT customerID FROM orders):


# Sub-query bukan hanya digunakan setelah WHERE clause saja, tetapi bisa juga digunakan setelah SELECT clause.

# Contoh:

USE employees;
SHOW FULL TABLES;
SELECT * FROM salaries;
SELECT * FROM employees;

SELECT emp_no, salary,
(SELECT AVG(salary) FROM salaries) AS average_salary
FROM salaries;


# Mencari emp_no yang memiliki salary di atas rata-rata
SELECT emp_no, salary,										# Kita mau menampilkan 3 kolom. Kolom 1 adalah emp_no, kolom 2 adalah salary, kolom 3 adalah average_salary
(SELECT AVG(salary) FROM salaries) AS average_salary		# Untuk kolom 3, kita menggunakan sub-query untuk bisa mendapatkan nilai average_salary
FROM salaries												# Kita mengambil dari tabel salaries
WHERE salary > (SELECT AVG(salary) FROM salaries)			# Kita memasukkan kondisi filtering di mana hanya ingin menampilkan salary > average_salary. Tapi, kita tidak bisa menggunakan
															# aggregate function setelah WHERE clause. Jadi, kita harus menggunakan sub-query.
ORDER BY salary;											# Mengurutkan data dari nilai salary terendah. 


# Kita hanya bisa menggunakan ALIAS pada GROUP BY, ORDER BY, HAVING clause.
# By system, SQL tidak memperbolehkan kita untuk me-refer ke column ALIAS pada WHERE clause.

# Mengecek apakah gaji seseorang lebih kecil atau lebih besar dari minimum dan maximum salary.
SELECT emp_no, salary,
(SELECT MIN(salary) FROM salaries) Min_Salary,
(SELECT MAX(salary) FROM salaries) Max_Salary
FROM salaries;


# Sub-query juga bisa digunakan di FROM clause untuk mengubah nama tabelnya sesuai yang diinginkan (Table expressions).
# Ketika sub-query digunakan pada FROM clause, set hasil yang dikembalikan oleh sub-query digunakan sebagai tabel sementara (temporary table). 

SELECT * FROM
(SELECT first_name, last_name, gender, birth_date FROM employees)
AS employees_biodata;

## ======================================================================================================================================================

## WORKING WITH MULTIPLE TABLES

# Dapat menggunakan sub-query, implicit join, dan juga join operators.


## SUB-QUERY

# Menampilkan employees pada tabel employees yang emp_no nya ada pada emp_no tabel titles.
SELECT * FROM employees
WHERE emp_no IN (SELECT emp_no FROM titles);

# Menampilkan employees pada tambel employees yang emp_no nya ada pada emp_no tabel titles
	# dengan syarat title-nya adalah 'senior staff'
SELECT * FROM employees
WHERE emp_no IN (SELECT emp_no FROM titles WHERE title = 'Senior Staff');


# Menmapilkan employees yang memiliki salary > US$ 80k pada tabel salaries.
SELECT * FROM employees
WHERE emp_no IN (SELECT emp_no FROM salaries WHERE salary > 80000);

# Contoh syntax menggunakan ALIAS untuk nama tabel
SELECT first_name, last_name, E.emp_no
FROM employees E
JOIN salaries S 
ON E.emp_no;

## ======================================================================================================================================================

## IMPLICIT JOIN

# Implicit join digunakan untuk mengakses beberapa tabel sekaligus dengan menuliskan nama tabelnya setelah FROM clause. 

# Menampilkan seluruh data dari tabel employees dan salaries dengan ditambahkan WHERE clause employees.emp_no = salaries.emp_no

SELECT * FROM employees, salaries
WHERE employees.emp_no = salaries.emp_no;

# Gunakan ALIAS pada tabel yang digunakan agar memudahkan jika ingin kembali menggunakan tabel yang sama. 

SELECT * FROM employees E, salaries S 
WHERE E.emp_no = S.emp_no;

SELECT * FROM employees;

# Menggunakan lebih dari 1 tabel
SELECT E.emp_no, first_name, last_name, salary # Kita gunakan alias pada kolom emp_no karena kolom ini terdapat pada kedua tabel. 
FROM employees E, salaries S 
WHERE E.emp_no = S.emp_no;

# Kita menggunakan nama tabel alias dalam mendefinisikan nama kolom jika kolom tersebut ada pada kedua tabel yang kita gunakan. ALIAS digunakan agar tidak ambigu.

## ======================================================================================================================================================

## RELATIONAL MODEL CONSTRAINTS

# Referencing --> Menghubungkan antar tabel pada RDBMS (Relational Database Management System).

# PRIMARY KEY --> Identitas unik yang dimiliki oleh setiap tabel. Contohnya seperti customerID, employeeID, departmentID.
# Primary key harus memiliki data unuk di setiap barisnya dan tidak boleh ada data kosong. 

# Primary key tabel tertentu bisa ditampilkan di tabel lain. Misalnya primary key tabel A ditempatkan di tabel B juga. 
# Primary key yang ditempatkan di tabel lain disebut FOREIGN KEY.
# Foreign key merupakan key yang digunakan untuk menghubungkan dua tabel atau lebih. 

# DEPENDENT TABLE --> Tabel yang memiliki FOREIGN KEY. 
# PARENT TABLE --> Tabel yang memiliki PRIMARY KEY.

# Untuk mengetahui mana dependent atau parent table, kita bisa melihatnya pada database schema. 

SHOW SCHEMAS;

SHOW FULL TABLES;

# Syntax untuk membuat VIEW (virtual table)
-- CREATE VIEW nama_view AS ...
-- SELECT nama_kolom1, nama_kolom2, ...
-- FROM nama_tabel
-- WHERE condition

## ======================================================================================================================================================

## JOIN TABLE USING JOIN OPERATORS

# JOIN clause digunakan untuk mengombinasikan data dari 2 atau lebih tabel berdasarkan kolom tertentu yang dimiliki oleh tabel-tabel yang digunakan. 


## INNER JOIN 

# INNER JOIN digunakan untuk menghubungkan 2 tabel atau lebih dengan cara hanya menampilkan data yang dimiliki oleh tabel-tabel tersebut (hanya data yang match saja yang ditampilkan). 

# Syntax:

# SELECT nama_kolom1, nama_kolom2, ...
# FROM nama_tabel1 
# INNER JOIN nama_tabel2 
# ON tabel1.nama_kolom = tabel2.nama_kolom;

# Menggunakan INNER JOIN untuk menggabungkan tabel employees dan salaries berdasarkan kolom emp_no 
SELECT E.emp_no, first_name, last_name
FROM employees E
INNER JOIN salaries S
ON E.emp_no = S.emp_no; # Output terdapat nama duplikat karena data emp_no pada tabel salaries terdapat banyak duplikat juga. 

## ======================================================================================================================================================

## LEFT JOIN

# Saat melakukan join, ada tabel yang disebut tabel pertama (setelah FROM clause), lalu setelah JOIN clause disebut sebagai tabel kedua. 
# Untuk LEFT JOIN, data yang akan ditampilkan akan mengikuti data tabel yang disebut pertama. 
# Sehingga, data yang ada pada tabel pertama, tetapi tidak dimiliki oleh tabel kedua, tetap akan ditampilkan. Jadi, nanti di kolom tabel kedua, akan terisi sebagai NULL.

# Syntax:

# SELECT nama_kolom1, nama_kolom2, ...
# FROM nama_tabel1
# LEFT JOIN nama_tabel2
# ON tabel1.nama_kolom = tabel2.nama_kolom;

# Contoh
SELECT A.first_name, A.last_name, B.title
FROM employees A
LEFT Join titles B
ON A.emp_no = B.emp_no;

SELECT * FROM employees;
SELECT * FROM titles;

## ======================================================================================================================================================

## RIGHT JOIN

# Kebalikan dari left join, tabel pertama harus mengikuti tabel kedua.

# Syntax:

# SELECT nama_kolom1, nama_kolom2, ...
# FROM nama_tabel1
# RIGHT JOIN nama_tabel2
# ON tabel1.nama_kolom = tabel2.nama_kolom;

# Contoh
SELECT A.first_name, A.last_name, B.title
FROM employees A
RIGHT Join titles B
ON A.emp_no = B.emp_no
ORDER BY B.title;

## ======================================================================================================================================================

## SELF JOIN

# SELF JOIN sama dengan IMPLICIT JOIN.
# Kita tidak harus menulis secara eksplisit keyword JOIN-nya (INNER JOIN, LEFT JOIN, RIGHT JOIN)

# Syntax:

# SELECT nama_kolom1, nama_kolom2, ...
# FROM nama_tabel1 T1, nama_tabel2 T2
# WHERE condition;

# Contoh
SELECT A.first_name, A.last_name, B.title
FROM employees A, titles B
WHERE A.emp_no = B.emp_no;


## ======================================================================================================================================================

## ACCESS DATABASES USING PYTHON

# Materi bagian ini ada pada file .IPYNB