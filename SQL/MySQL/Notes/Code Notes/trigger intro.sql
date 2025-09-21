/* TO AUTOMATICALLY RUN ANOTHER QUERY AFTER A QUERY IS RUNNED 
FOR EX:
CREATE TRIGGER NAME
BEFORE DELETE ON TABLE
FOR EACH ROW
BEGIN

BLA BLA BLA;

END;
*/

CREATE TRIGGER "sell"
BEFORE DELETE ON "collections" 
FOR EACH ROW  /* GIVE STATEMENT TO RUN FOR EACH ROW THAT IS BEING DELETED FROM COLLECTION */
BEGIN 
    INSERT INTO "transactions" ("title", "action")
    VALUES (OLD."title", 'sold');
END;

CREATE TRIGGER "buy"
AFTER INSERT ON "collections"
FOR EACH ROW
BEGIN
    INSERT INTO "transactions" ("title", "action")
    VALUES (NEW."title", 'bought'); /* NEW IS NEW ROW BEING INSERTED */
END;

CREATE TRIGGER "insert_when_exists"
INSTEAD OF INSERT ON "current_collections"
FOR EACH ROW
WHEN NEW."accession_number" IN (
    SELECT "accession_number" FROM "collections"
) BEGIN 
    UPDATE "collections" SET "deleted" = 0
    WHERE "accession_number" = NEW."accession_number"
END;


/* FOR HEIDISQL ADD DELIMITER $$ AND END $$ DELIMITER FOR IT TO RUN */

