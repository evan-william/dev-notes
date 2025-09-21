/* Transactions have some properties, which can be remembered using the acronym ACID:

atomicity: can’t be broken down into smaller pieces,
consistency: should not violate a database constraint,
isolation: if multiple users access a database, their transactions cannot interfere with each other,
durability: in case of any failure within the database, all data changed by transactions will remain.

Let’s open up bank.db in our terminal so we can implement a transaction for transferring money from Alice to Bob!
First, we want to see the data already in the accounts table. */

SELECT * FROM "accounts";
/* We note here that Bob’s ID is 2 and Alice’s ID is 1, which will be useful for our query. 
To move $10 from Alice’s account to Bob’s, we can write the following transaction.*/

BEGIN TRANSACTION;
UPDATE "accounts" SET "balance" = "balance" + 10 WHERE "id" = 2;
UPDATE "accounts" SET "balance" = "balance" - 10 WHERE "id" = 1;
COMMIT;
/* Notice the UPDATE statements are written in between the commands to begin the transaction and to commit it. If we execute the query after writing the UPDATE statements, but without committing, neither of the two UPDATE statements will be run! This helps keep the transaction atomic. By updating our table in this way, we are unable to see the intermediate steps.

If we tried to run the above transaction again — Alice tries to pay Bob another $10 — it should fail to run because Alice’s account balance is at 0. (The "balance" column in accounts has a check constraint to ensure that it has a non-negative value. We can run .schema to check this.)
The way we implement reverting the transaction is using ROLLBACK. Once we begin a transaction and write some SQL statements, if any of them fail, we can end it with a ROLLBACK to revert all values to their pre-transaction state. This helps keep transactions consistent. */

BEGIN TRANSACTION;
UPDATE "accounts" SET "balance" = "balance" + 10 WHERE "id" = 2;
UPDATE "accounts" SET "balance" = "balance" - 10 WHERE "id" = 1; -- Invokes constraint error
ROLLBACK;

/*
Race Conditions
Transactions can help guard against race conditions.
A race condition occurs when multiple entities simultaneously access and make decisions based on a shared value, potentially causing inconsistencies in the database. Unresolved race conditions can be exploited by hackers to manipulate the database.
In the lecture, an example of a race condition is discussed wherein two users working together can exploit momentary inconsistencies in the database to rob the bank.
However, transactions are processed in isolation to avoid the inconsistencies in the first place. Each transaction dealing with similar data from our database will be processed sequentially. This helps prevent the inconsistencies that an adversarial attack can exploit.
To make transactions sequential, SQLite and other database management systems use locks on databases. A table in a database could be in a few different states:
UNLOCKED: this is the default state when no user is accessing the database,
SHARED: when a transaction is reading data from the database, it obtains shared lock that allows other transactions to read simultaneously from the database,
EXCLUSIVE: if a transaction needs to write or update data, it obtains an exclusive lock on the database that does not allow other transactions to occur at the same time (not even a read)
Questions
How do we decide when a transaction can get an exclusive lock? How do we prioritize different kinds of transactions?

Different algorithms could be used to make these decisions. For example, we could always choose the transaction that came first. If an exclusive transaction is needed, no other transaction can run at the same time, which is a necessary downside to ensure consistency of the table.
What is the granularity of locking? Do we lock a database, a table or a row of a table?

This depends on the DBMS. In SQLite, we can actually do this by running an exclusive transaction as below:
*/

BEGIN EXCLUSIVE TRANSACTION;
/*
If we do not complete this transaction now, and try to connect to the database through a different terminal to read from the table, we will get an error that the database is locked! This, of course, is a very coarse way of locking because it locks the entire database. Because SQLite is coarse in this manner, it has a module for prioritizing transactions and making sure an exclusive lock is obtained only for the shortest necessary duration.