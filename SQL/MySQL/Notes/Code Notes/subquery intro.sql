/* USE TO WRITE A QUERY INSIDE A QUERY */
SELECT "title" FROM "books" WHERE "publisher_id" = (
    SELECT "id" FROM "publishers" WHERE "publisher" = 'Fitzcarraldo Editions';
)

/* USAGE of "( )" means the code inside the paranthesis will be runned first */ 

/* THIS CAN BE DONE FOR 3 TABLE RELATION */
SELECT "name" FROM "authors" WHERE "id" = (
    SELECT "author_id" FROM "authored" WHERE "book_id" = (
        SELECT "id" FROM "books" WHERE "title" = 'Flights'
    )
);

/* THIS CAN BE DONE FOR MULTIPLE AND USAGE OF IN  (IN IS TO CHECK IF SOMETHING IS IN MORE THAN 1 ITEM) */
SELECT "title" FROM "books" WHERE "id" IN (
    SELECT "book_id" FROM "authored" WHERE "author_id" = (
        SELECT "id" FROM "authors" WHERE "name" = 'Fernanda Melchor'
    )
)

/* USAGE OF IN OR = 
IN IF U KNOW THE RESULT IS MULTIPLE
= IF U KNOW U ONLY HAVE 1 RESULT
*/