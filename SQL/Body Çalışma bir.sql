--Write a query that returns track name and its composer using tracks table. 
SELECT "Name", "Composer" FROM "Track";

--Write a query that returns all columns of albums table.

SELECT * FROM "Album";

--Write a query that returns columns of tracks table.
SELECT * FROM "Track";

--Find the name of composers of each track using tracks table.

SELECT "Composer" FROM "Track";

--Write a query that return distinct AlbumId, MediaTypeId pair

SELECT DISTINCT("AlbumId", "MediaTypeId") FROM "Track";


--Find the track names of Jimi Hendrix.

SELECT "Name" FROM "Track"  WHERE "Name" LIKE 'Jimi H%';


--Find all the info of the invoices of which total amount is greater than $10.

SELECT * FROM "Invoice" WHERE "Total" > 10;


--Find all the info of the invoices of which total amount is greater than $10. Just return the first 4 

SELECT * FROM "Invoice" WHERE "Total" > 10 ORDER BY "Total" asc LIMIT 4;


--Find all the info of the invoices of which total amount is greater than $10. Then sort them by the total amount in descending order.

SELECT * FROM "Invoice" WHERE "Total" > 10 ORDER BY "Total" desc ;


--Find all the info of the invoices of which billing country is not USA. Then sort them by the total 
--amount in ascending order.

SELECT * FROM "Invoice" WHERE "BillingCountry"  NOT IN ('USA') ORDER BY "BillingCountry" ;


--Find the newest invoice date among the invoice dates between 2009 and 2011
SELECT * FROM "Invoice" WHERE "InvoiceDate"  BETWEEN '2009-01-01' AND '2011-01-01' ORDER BY "InvoiceDate" DESC ;
 
--Find the first and last name of the customers who gave an order from Belgium, Norway, Canada and USA.

SELECT "FirstName", "LastName", "Country" FROM "Customer" WHERE "Country" IN ('Belgium','Norway','Canada','USA') ;


--Find the track names of Bach
SELECT "Name" FROM "Track" WHERE "Composer" LIKE ('%Bach%');


--How many invoices are in the digital music store?
SELECT COUNT("InvoiceId") FROM "Invoice";

--How many composers are there in the digital music store?
SELECT COUNT("Composer") FROM "Track";


--Find the track name having the minimum duration.

SELECT "Milliseconds", "Name" FROM "Track" ORDER BY "Milliseconds" LIMIT 1;


--How much money did our store earn?
SELECT SUM("Total") FROM "Invoice";


--Find the total number of each composer’s track. Your result will include name of the composer and number.
SELECT COUNT("Name"),"Composer" FROM "Track" GROUP BY "Composer";



--Find the minimum duration of track for each album. Your result will include album id and min duration.
SELECT MIN("Milliseconds"),"AlbumId" FROM "Track" GROUP BY "AlbumId";





---------------JOINLER------------------


SELECT "Album"."Title", "Artist"."Name" FROM "Album" LEFT JOIN "Artist" ON "Album"."ArtistId" = "Artist"."ArtistId";

--Find the genre of each track.
SELECT "Track"."Name","Genre"."Name" FROM "Genre" INNER JOIN "Track" ON "Genre"."GenreId" = "Track"."GenreId";

--Find the customer name of each invoice.Your result will include Invoice id and customer name.
SELECT "Customer"."FirstName", "Invoice"."InvoiceId" FROM "Customer" INNER JOIN "Invoice" ON "Customer"."CustomerId" = "Invoice"."CustomerId";








