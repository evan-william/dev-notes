/* SELECT IS TO SELECT A ROW IN THE TABLE TO GET BACK  ROWS  */
SELECT * FROM "Anything"; /* This will select everything in the table called "Anything" cuz of the "*" */
SELECT "Title (Or Anything)" FROM "Anything"; /* This will get back all row called "Title (Or Anything)" */
SELECT "Title", "Author" FROM "Anything"; /* THis allows to select multiple row */

SELECT "Title" FROM "Anything" LIMIT 5; /* LIMIT ALLOWS TO LIMIT THE OUTPUT */
SELECT "Title" FROM "Anything" WHERE "Year" = 2023; /* Will now only show wanted rows based on specific wants */

SELECT "Title", "Format" FROM "Anything" WHERE "Format" != "Hardcover"; /* More advanced Search */
/* OR CAN DO THE SAME THING WITH */
SELECT "Title", "Format" FROM "Anything" WHERE NOT "Format" = "Hardcover";


/* USAGE OF OPERATIONS */
SELECT "Title", "Author" FROM "Anything" WHERE " Year" = 2022 OR "Year" = 2023 AND "Format" != "Hardcover";
SELECT "TItle", "Translator" FROM "Anything" WHERE "Translatpr" IS NULL;

/* USAGE OF ">" ETC ETC */
SELECT "Title" FROM "Anything" WHERE "Year" >= 2019 AND "Year" <= 2022;

/* CAN USE BETWEEN AS WELL */
SELECT "Title" FROM "Anything" WHERE "Year" BETWEEN 2019 AND 2022;

/* ANOTHER USAGE OF AND */
SELECT "Title" FROM "Anything" WHERE "Rating" > 4.0 AND "Votes" > 10000;

/* TO DODGE DUPLICATES USE DISTINCT */
SELECT DISTINCT "Publisher" FROM "Anything";
SELECT COUNT(DISTINCT "Publisher") FROM "Anything";
