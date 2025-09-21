/* There are ways to delete unused space in our database. SQLite allows us to “vacuum” data — this cleans up previously deleted data (that is actually not deleted, but just marked as space being available for the next INSERT).
To find the size of movies.db on the terminal, we can use a Unix command */

du -b movies.db
/* In lecture, this command showed us that the size of the database is something like 158 million bytes, or 158 megabytes.
We can now connect to our database and drop an index we previously created. */

DROP INDEX "person_index";
/* Now, if we run the Unix command again, we see that the size of the database has not decreased! To actually clean up the deleted space, we need to vacuum it. We can run the following command in SQLite.*/

VACUUM;
/* This might take a second or two to run. On running the Unix command to check the size of the database again, we can should see a smaller size. Once we drop all the indexes and vacuum again, the database will be considerably smaller than 158 MB (in lecture, around 100 MB).*/