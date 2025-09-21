/* TO ALTER A TABLE */
ALTER TABLE "visits" RENAME TO "swipes";
ALTER TABLE "swipes" ADD COLUMN "type" TEXT; /* ADDING AFFINITY AS WELL */
ALTER TABLE "swipes" DROP COLUMN "type"; 
ALTER TABLE "collections" ADD COLUMN "deleted" INTEGER DEFAULT 0;

/*
MySQL allows us to alter tables more fundamentally than SQLite did.
If we wanted to add a silver line to the possible lines a station could be on, we can do the following.
*/

ALTER TABLE `stations` 
MODIFY `line` ENUM('blue', 'green', 'orange', 'red', 'silver') NOT NULL;

/*
This allows us to modify the line column and change its type, such that the ENUM now includes silver as an option.
Note also that we use the keyword MODIFY in addition to the ALTER TABLE construct we are familiar with from SQLite.
*/