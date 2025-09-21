/* WHEN THERE IS SAME Per Pupil Expenditure, SORT BY ALPHABETICALLY */
SELECT "name", "per_pupil_expenditure" AS "Per Pupil Expenditure", "graduated" FROM "schools"
    JOIN "expenditures" ON "schools"."district_id" = "expenditures"."district_id"
        JOIN "graduation_rates" ON "schools"."id" = "graduation_rates"."school_id" ORDER BY "Per Pupil Expenditure" DESC "name" ASC;