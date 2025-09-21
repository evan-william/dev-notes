/* FORMULA =  INSERT INTO table (column0, ...) VALUES (value0, ...); */

/*
CREATE TABLE "collections" (
    "id" INTEGER,
    "title" TEXT NOT NULL,
    "accession_number" TEXT NOT NULL UNIQUE,
    "acquired" NUMERIC,
    PRIMARY KEY ("id")
)
*/


INSERT INTO "collections" ("id", "title", "accession_number", "acquired")
VALUES (1, 'Profusion of flowers', '56.257', '1956-04-12');


INSERT INTO "collections" ("id", "title", "accession_number", "acquired")
VALUES (2, 'Farmers Working at Dawn', '11.6152', '1911-08-03');

/* CAN ALSO NOT ADD ID, SQLITE CAN INCREMENT IT AUTOMATICALLY CUZ ID IS PRIMARY KEY*/ 
INSERT INTO "collections" ("title", "accession_number", "acquired")
VALUES ('Spring Outing', '14.76', '1914-01-08');

/* THIS CAN ADD MULTIPLE ROW AT THE SAME TIME BY STACKING VALUES */
INSERT INTO "collections" ("title", "accession_number", "acquired")
VALUES 
('Imaginative Landscape', '56.496', NULL),
('Peonies and butterfly', '06.1899', '1906-01-01');




