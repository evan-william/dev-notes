/* TO CAPITALIZE ALL */
UPDATE "votes" SET "title" = upper("title");

/* TO NOT CAPITALIZE ALL */
UPDATE "votes" SET "title" = lower("title");