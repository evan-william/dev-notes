/*
One way to increase security of our database is to use access control and grant only the necessary privileges to each user. However, our applications that use an SQL database could also be exposed to attacks — one of them is an SQL injection attack.
As the name indicates, this involves a malicious user injecting some SQL phrases to complete an existing query within our application in an undesirable way.
For example, a website that asks a user to log in with their username and password may be running a query like this on the database.
*/

SELECT `id` FROM `users`
WHERE `user` = 'Carter' AND `password` = 'password';
/*
In the above example, the user Carter entered their username and password as per usual. However, a malicious user could enter something different, like the string “password’ OR ‘1’ = 1” as their password. In this case, they are trying to gain access to the entire database of users and passwords.
*/

SELECT `id` FROM `users`
WHERE `user` = 'Carter' AND `password` = 'password' OR '1' = '1';

/*
In MySQL, we can use prepared statements to prevent SQL injection attacks. Let’s connect to MySQL with the user we created previously and change to the bank database.
An example of an SQL injection attack that can be run to display all user accounts from the accounts table is this.
*/

SELECT * FROM `accounts`
WHERE `id` = 1 UNION SELECT * FROM `accounts`;
A prepared statement is a statement in SQL that we can later insert values into. For the above query, we can write a prepared statement.


PREPARE `balance_check`
FROM 'SELECT * FROM `accounts`
WHERE `id` = ?';
/*
The question mark in the prepared statement acts as a safeguard against the unintended execution of SQL code.

To actually run this statement now and check someone’s balance, we accept user input as a variable and then plug it into the prepared statement.
*/
SET @id = 1;
EXECUTE `balance_check` USING @id; /*
In the above code, imagine the SET statement to be procuring the user’s ID through the application! The @ is a convention for variables in MySQL.

The prepared statement cleans up input to ensure that no malicious SQL code is injected. Let’s try to run the same statements as above but with a malicious ID.
*/
SET @id = '1 UNION SELECT * FROM `accounts`';
EXECUTE `balance_check` USING @id;

/*
This also gives us the same results as the previous code — it shows us the balance of the user with ID 1 and nothing else! Thus, we have prevented a possible SQL injection attack.*/