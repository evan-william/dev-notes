/* UNION BOTH TABLE ( COMBINE 2 SETS ) */
SELECT "name" FROM "translators" UNION SELECT "name" FROM "authors";

/* INTERSECT, WILL SHOW WHO IS AUTHOR AND TRANSLATOR AT THE SAME TIME*/
SELECT "name" FROM "authors" INTERSECT SELECT "name" FROM "translators";

/* WILL ONLY SHOW AUTHORS AND REMOVE AUTHORS THAT IS ALSO A TRANSLATOR */
SELECT "name" FROM "authors" EXCEPT SELECT "name" FROM "translators";

/* TO FIND BOOK THAT Translator HAVE COLLABED ON */
SELECT "book_id" FROM "translated" WHERE "translator_id" = (
    SELECT "id" FROM "translator" WHERE "name" = 'Sophie Hughes' /* THIS TO SEE WHAT BOOK SOPHIE HUGHES TRANSLATE */
);

SELECT "book_id" FROM "translated" WHERE "translator_id" = (
    SELECT "id" FROM "translator" WHERE "name" = 'Sophie Hughes' /* THIS TO SEE WHAT BOOK SOPHIE HUGHES AND MARGAET TRANSLATE TOGETHER */
) INTERSECT SELECT "book_id" FROM "translated" WHERE "translator_id" = (
    SELECT "id" FROM "translator" WHERE "name" = 'Margaret Jull Costa'
);




 
