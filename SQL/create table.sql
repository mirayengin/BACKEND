SELECT "Track"."TrackId", "Track"."Name","AlbumId" FROM "Track" 
WHERE "AlbumId" = (select "AlbumId" from "Album" where "Title" = 'Faceless');


SELECT "Track"."TrackId", "Track"."Name","Album"."AlbumId" FROM "Track" 
 inner join "Album" on "Track"."AlbumId" = "Album"."AlbumId" WHERE "Album"."Title" ='Faceless';
 
SELECT "Track"."TrackId", "Track"."Name", "Track"."AlbumId"
FROM "Track"
WHERE "Track"."AlbumId" IN (
	SELECT "AlbumId" FROM "Album" WHERE "Title" in ('Faceless', 'Let There Be Rock'));
	
	
SELECT "Track"."TrackId", "Track"."Name", "Track"."AlbumId"
FROM "Track"
INNER JOIN "Album"
ON "Track"."AlbumId"="Album"."AlbumId"
WHERE "Album"."Title" IN ('Faceless' , 'Let There Be Rock');


SELECT "Track"."Name", "Genre"."Name", "Album"."Title" FROM "Track"
INNER JOIN "Genre" ON "Track"."GenreId" = "Genre"."GenreId"
JOIN "Album" ON "Track"."AlbumId" = "Album"."AlbumId";





























