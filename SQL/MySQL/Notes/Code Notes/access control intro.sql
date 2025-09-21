/*
Previously, we logged into MySQL using the root user. However, we can also create more users and give them some kind of access to the database.
Let’s create a new user called Carter (feel free to try with your own name here)!
*/

CREATE USER 'carter' IDENTIFIED BY 'password';

/*
We can log into MySQL now using the new user and password, in the same way we did with the root user previously.
When we create this new user, by default it has very few privileges. Try the following query.*/

SHOW DATABASES;
/*
This only displays some of the default databases in the server.

If we log in again with the root user and run the above query, many more databases show up! This is because the root user has access to most everything in the server.
Let us look at how we can grant access to users by discussing an example from previous weeks. We had a rideshare database with a rides table. In this table, we stored the names of riders, which is personally identifiable information (PII). We created a view called analysis which anonymized the names of the riders, intending to share only this view with an analyst or other user.
If we wanted to share the analysis view with the user we just created, we would do the following while logged in as the root user.
*/
GRANT SELECT ON `rideshare`.`analysis` TO 'carter';
/*
Now, let’s log in as the new user and verify that we can access the view. We are now able to run
*/
USE `rideshare`; /*
The only part of the database, however, that this user can access is the analysis view. We can now see the data in this view, but not from the original rides table! We just demonstrated the benefit of MySQL’s access control: we can have multiple users accessing the database but only allow some to access confidential data.
*/