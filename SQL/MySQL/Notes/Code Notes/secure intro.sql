/* TO SHOW ONLY THE DATA U WANT TO SOMEONE */
/* CAN USE VIEW TO DO THIS AND ONLY SET VIEW TO THE ONE U WANNA SHOW */

/* FOR EX A TABLE WITH: id origin destination rider , can do: */
SELECT "id", "origin", "destination" FROM "rides";
/* THIS DOESNT SHOW THE RIDER */

/* TO SHOW PEOPLE THAT DATA HAS BEEN ANONIMYZED AND PEOPLE KNOW THERE IS "rider" , use */
SELECT "id", "origin", "destination", 'Anonymous' AS "rider"
FROM "riders";

/* VIEW VERSION */
CREATE VIEW "analysis" AS 
SELECT "id", "origin", "destination", 'Anonymous' AS "rider"
FROM "riders";