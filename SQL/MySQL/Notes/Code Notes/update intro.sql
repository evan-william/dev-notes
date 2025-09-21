UPDATE "created" SET "artist_id" = (
    SELECT "id" FROM "artists"
    WHERE "name" = 'Li Yin'
) WHERE "collection_id" = (    
    SELECT "id" FROM "collections"
    WHERE "title" = 'Farmers working at dawn'
);


/* FORMULA 
UPDATE TABLE
SET column0 = value0, ...
WHERE condition;
*/

