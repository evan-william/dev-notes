/* TO INSTANTLY QUERY A TABLE INSTANLTY */
CREATE VIEW "longlist" AS 
SELECT "name", "title" FROM "authors"
JOIN "authored" ON "authors"."id" = "authored"."author_id"
JOIN "books" ON "books"."id" = "authored"."book_id";

/* AFTER CREATING VIEW CAN CHECK IT AT SCHEMA , LOOK LIKE THIS: */
SELECT * FROM "longlist";


/* THIS IS A VIRTUAL TABLE AND WORKS LIKE NORMAL, CAN ORDER , ETC ETC */

CREATE VIEW "average_book_ratings" AS
SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating"
FROM "ratings"
JOIN "books" ON "ratings"."book_id" = "books"."id"
GROUP BY "book_id";

/* AFTER CREATING SUCH, CAN DO : */
SELECT * FROM "average_book_ratings";


/* ALSO AVAILABLE CREATE TEMPORARY VIEW THAT WILL BE GONE IF WE LOST CONNECTION WITH THE DB, SLIKE SQLITE3.quit */
CREATE TEMPORARY VIEW -etc etc

/* A VIEW CANNOT BE UPDATED */

CREATE VIEW "current_collections" AS
SELECT "id", "title", "accesion_number", "acquired"
FROM "collections" WHERE "deleted" = 0;