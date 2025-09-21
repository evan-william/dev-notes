/* TO GROUP TOGETHER SAME ID OR NAME OR WHATEVER THAN WE CAN DO SOMEHTING TO IT LIKE AVG IT */
SELECT "book_id", AVG("rating") AS "average rating" FROM "ratings" GROUP BY "book_id";

/* WILL BE MORE LIKE book id 1: avg 3.0 book id 2: avg 3.1 , etc etc */

SELECT "book_id", ROUND(AVG("rating"), 2) AS "average rating" FROM "ratings" GROUP BY "book_id" HAVING "average_rating" > 4.0;
/* THIS WILL GROUP AND ONLY SHOW RATHING WITH >4.0  , SAME LIKE WHERE BUT FOR GROUP */ 

/* AS IS SAME LIKE CREATING A COLUMN */

/* TO SEE HOW MANY RATING , BUT NOT THE RATING HIGHNESS */
SELECT "book_id", COUNT("rating")  FROM "ratings" GROUP BY "book_id";

/* USAGE WITH ORDER BY */
SELECT "book_id", ROUND(AVG("rating") ,2) AS "average rating" FROM "ratings" GROUP BY "book_id" HAVING "average rating" > 4.0 ORDER BY "average rating" DESC;