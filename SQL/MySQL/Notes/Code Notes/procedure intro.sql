/* Stored procedures are a way to automate SQL statements and run them repeatedly.
To demonstrate stored procedures, we will again use a database from previous lectures — the Boston MFA database.
Recall that we used views in SQLite to implement a soft-delete feature for collections in the MFA database. A view current_collections displayed all the collections not marked as deleted. We will now use a stored procedure in MySQL to do something similar.
Let’s navigate to the MFA database already created on our MySQL server. */

USE `mfa`;

/*
On describing the collections table, we see that the deleted column is not present and needs to be added to the table.
*/

ALTER TABLE `collections` 
ADD COLUMN `deleted` TINYINT DEFAULT 0;

/*
Given that the deleted column only has values of 0 or 1, it is safe to use a TINYINT. We also assign the default as 0 because we want to keep all the collections already in the table.

Before we create a stored procedure, we need to change the delimited from ; to something else. Unlike SQLite, where we could type in multiple statements between a BEGIN and END (which we need for a stored procedure here) and end them with a ;, MySQL prematurely ends the statement when it encounters a ;.

delimiter //
Now, we write the stored procedure. */

CREATE PROCEDURE `current_collection`()
BEGIN
    SELECT `title`, `accession_number`, `acquired` 
    FROM `collections` 
    WHERE `deleted` = 0;
END//

/*
Notice how we use empty parantheses next to the name of the procedure, perhaps reminiscent of functions in other programming languages. Similar to functions, we can also call stored procedures to run them.

After creating this, we must reset the delimited to ;. */

delimiter ;

/*
Let us try calling this procedure to see the current collections. At this point, the query should output all the rows in the collections table because we haven’t soft-deleted anything yet.
*/
CALL current_collection();

/*
If we soft-delete “Farmers working at dawn” and call the procedure again, we will find that the deleted row is not included in the output.
*/

UPDATE `collections` 
SET `deleted` = 1 
WHERE `title` = 'Farmers working at dawn';



/* WITH PARAMETER
When we previously worked with the MFA database, we had a table called transactions to log artwork being bought or sold, which we can create here as well.
*/

CREATE TABLE `transactions` (
    `id` INT AUTO_INCREMENT,
    `title` VARCHAR(64) NOT NULL,
    `action` ENUM('bought', 'sold') NOT NULL,
    PRIMARY KEY(`id`)
);
/*
Now, if a piece of artwork is deleted from collections because it is being sold, we would also like to update this in the transactions table. Usually, this would be two different queries but with a stored procedure, we can give this sequence one name.
*/
delimiter //
CREATE PROCEDURE `sell`(IN `sold_id` INT)
BEGIN
    UPDATE `collections` SET `deleted` = 1 
    WHERE `id` = `sold_id`;
    INSERT INTO `transactions` (`title`, `action`)
    VALUES ((SELECT `title` FROM `collections` WHERE `id` = `sold_id`), 'sold');
END//
delimiter ;
/*
The choice of the parameter for this procedure is the ID of the painting or artwork because it is a unique identifier.

We can now call the procedure to sell a particular item. Suppose we want to sell “Imaginative landscape”.
*/
CALL `sell`(2);
/*
We can display data from the collections and transactions tables to verify that the changes were made.

What happens if I call sell on the same ID more than once? There is a danger of it being added multiple times to the transactions table. Stored procedures can be considerably improved in logic and complexity by using some regular old programming constructs. The following list contains some popular constructs available in MySQL.

"Programming constructs in MySQL"
*/