CREATE INDEX "person_index" ON "stars" ("person_id");
CREATE INDEX "name_index" ON "people" ("name");

/* We can use the following command to create an index for the "title" column in the movies table. */
CREATE INDEX "title_index" ON "movies" ("title");

/* To remove the index we just created, run: */
DROP INDEX "title_index";

/* After dropping the index, running EXPLAIN
 QUERY PLAN again with the SELECT query will demonstrate that the plan would revert to scanning the entire database. */

/* First, let us drop the existing implementation of our index on the stars table. */

DROP INDEX "person_index";
/* Next, we create the new index. */

CREATE INDEX "person_index" ON "stars" ("person_id", "movie_id");
/* Running the following will demonstrate that we now have two covering indexes, which should result in a much faster search! */

EXPLAIN QUERY PLAN
SELECT "title" FROM "movies" WHERE "id" IN (
    SELECT "movie_id" FROM "stars" WHERE "person_id" = (
        SELECT "id" FROM "people" WHERE "name" = 'Tom Hanks'
    )
);

/* This is an index that includes only a subset of rows from a table, allowing us to save some space that a full index would occupy.
This is especially useful when we know that users query only a subset of rows from the table. 
In the case of IMDb, it may be that the users are more likely to query a movie
 that was just released as opposed to a movie that is 15 years old. 
 Let’s try to create a partial index that stores the titles of movies released in 2023.*/

CREATE INDEX "recents" ON "movies" ("titles")
WHERE "year" = 2023;
/* We can check that searching for movies released in 2023 uses the new index. */

EXPLAIN QUERY PLAN
SELECT "title" FROM "movies"
WHERE "year" = 2023;
/* This shows us that the movies table is scanned using the partial index.*/