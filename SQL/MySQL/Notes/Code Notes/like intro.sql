/* LIKE USED TO FIND SPECIFIC WORD */
SELECT "Title" FROM "Anything" WHERE "Title" LIKE '%Love%'; /* % means liek "love" can be somewhere in the title , as long as it has Love */
SELECT "Title" FROM "Anything" WHERE "Title" LIKE 'The%'; /* THis means that the title will only the first word MUST BE THE, rest is anything */

/* THIS LINE ABOVE CAN RESULT IN STUFF LIKE "THEY" AND "THERE" TO APPEAR AS WELL AND NOT JUST "THE" */
SELECT "Title" FROM "Anything" WHERE "Title" LIKE 'The %'; /* CAN BE FIXED BY ADDING A SPACE */

SELECT "Title" FROM "Anything" WHERE "Title" LIKE 'The %Love%'; /* THIS ALSO CAN BE DONE TO FIND EVEN MORE SPECIFIC */

/* USAGE OF "_"  CAN BE USED MORE THAN JUST 1 INSIDE*/
SELECT "Title" FROM "Anything" WHERE "Title" LIKE 'P_re'; /* "_" means that i can be any character , a single char */

/* CASE SENSITIVITY!!!! */
/* LIKE IS NOT CASE SENSITIVE , UNLIKE "=" , FOR EXAMPLE: */
SELECT "Title" FROM "Anything" WHERE "Title" = 'pyre';
SELECT "Title" FROM "Anything" WHERE "Title" LIKE 'pyre';