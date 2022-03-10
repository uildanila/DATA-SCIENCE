USE world;
SHOW FULL TABLES;
SELECT * FROM city;
SELECT * FROM country;
SELECT * FROM countrylanguage;

#1
SELECT city.Name AS Kota, country.Name AS Negara, city.Population 
FROM city, country  
WHERE city.CountryCode = country.Code 
ORDER BY city.population DESC 
LIMIT 10;

SELECT * FROM city;

#2
SELECT country.Name AS Negara, country.GNP, city.Name AS Kota, city.population
FROM country 
JOIN city
ON country.Code = city.CountryCode
WHERE country.Name = 'Netherlands' AND country.Capital = city.ID;


#3
SELECT c.Name AS Negara, cl.Percentage AS Persentase
FROM country c 
INNER JOIN countrylanguage cl
ON c.Code = cl.CountryCode
WHERE cl.language = 'Spanish'
ORDER BY cl.percentage DESC
LIMIT 10;



#4
SELECT country.Name AS Negara, country.GNP,
		city.Name AS 'Ibu Kota', city.Population AS Populasi, countrylanguage.Language
FROM country 
JOIN city 
ON country.Code = city.CountryCode
JOIN countrylanguage 
ON country.Code = countrylanguage.CountryCode
WHERE country.Name = 'Indonesia'
AND countrylanguage.IsOfficial = 'T'
AND country.capital = city.ID;



#5
# Mengecek jumlah negara di North America
SELECT count(Name) 
FROM country 
WHERE continent = 'North America';

SELECT continent, count(Name) AS 'Jumlah Negara' 
FROM country
GROUP BY continent
HAVING count(Name) > (SELECT count(Name) FROM country WHERE continent = 'North America');



#6
# Mengecek rata-rata GNP Europe
SELECT AVG(GNP) 
FROM country
WHERE continent = 'Europe';

SELECT name AS Negara, GNP 
FROM country
WHERE continent = 'Asia'
AND GNP > (SELECT AVG(GNP) FROM country WHERE continent = 'Europe')
ORDER BY GNP DESC;



#7
# Mengecek jumlah region unik di Asia
SELECT count(DISTINCT(region)) 
FROM country 
GROUP BY continent 
HAVING continent='Asia';

SELECT COUNT(DISTINCT(region)) AS 'Jumlah Region Unik', continent 
FROM country
WHERE continent LIKE '%a'
GROUP BY continent 
HAVING COUNT(DISTINCT(region)) > (SELECT COUNT(DISTINCT(region)) 
								  FROM country 
								  GROUP BY continent 
								  HAVING continent = 'Asia');



