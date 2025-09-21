/* 
We want to create a database in MySQL with this schema! On the terminal, let’s connect to a MySQL server. */

mysql -u root -h 127.0.0.1 -P 3306 -p
/*
In this terminal command, -u indicates the user. We provide the user we want to connect to the database as — root (synonymous with database admin, in this case).
127.0.0.1 is the address of local host on the internet (our own computer).
3306 is the port we want to connect to, and this is the default port where MySQL is hosted. Think of the combination of host and port as the address of the database we are trying to connect to!
-p at the end of the command indicates that we want to be prompted for a password when connecting.
Since this a full database server with potentially many databases inside it. To show all the existing ones, we use the following MySQL command/ */.
SHOW DATABASES;

/*
This returns some default databases already in the server. */

/*
We will perform some operations to set up the MBTA database. We have seen how to do these in SQLite already, so let’s focus on the syntax differences for MySQL!
Creating a new database: */

CREATE DATABASE `mbta`;
/*
Instead of quotation marks, we use backticks to identify the table name and other variables in our SQL statements.

To change the current database to mbta: */

USE `mbta`;