/* VIEW THAT ONLY EXIST ONLY ON A DURATION OF A QUERY */
WITH "average_book_ratings" AS (
SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating"
FROM "ratings"
JOIN "books" ON "ratings"."book_id" = "books"."id"
GROUP BY "book_id"
) SELECT "year", ROUND(AVG("rating"), 2) AS "rating" FROM "average_book_ratings" GROUP BY "year";