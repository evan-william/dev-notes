/* TO GIVE LIKE STRING FORMAT */
SELECT c.Nama AS "Nama Customer",
concat(COUNT(d.NoKamar), " kamar") AS "Pemakaian Kamar"
FROM customer c
LEFT JOIN HCheckIn h                                    
ON c.KodeCust = h.KodeCust
LEFT JOIN DCheckIn d
ON d.KodeCIn = h.KodeCIn
GROUP BY c.Nama

