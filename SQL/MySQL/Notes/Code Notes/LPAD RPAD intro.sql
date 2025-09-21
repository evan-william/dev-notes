SELECT LPAD("SQL Tutorial", 20, "-");

/* THIS TO MARGIN IT TO THE RIGHT */
SELECT h.KodeCIn, lpad(c.Nama,30,' ')
FROM HCheckIn h, customer c
WHERE KodeCust=c.KodeCust