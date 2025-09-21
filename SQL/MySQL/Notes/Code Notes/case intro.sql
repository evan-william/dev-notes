SELECT KodeCIn as KODECI, nokamar AS NOK,
(case when ISNULL(KodeUseFas) then "Tidak Pakai Fasilitas"
ELSE "Pakai Fasilitas" end)
AS "Status Fasilitas"
FROM DCheckIn

