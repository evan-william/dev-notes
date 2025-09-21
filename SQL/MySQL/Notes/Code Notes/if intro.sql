SELECT k.NoKamar AS nok, j.NamaJenis AS jenis,
if (k.'Status' = 0, 'kosong', 'terisi') AS Status
FROM kamar k, JenisKamar j  
WHERE k.KodeJenis = j.KodeJenis
ORDER BY 1 DESC


SELECT k.NoKamar AS nok,
if (j.Harga < 200000, 'murah', if(j.Harga <= 350000, 'sedang', 'mahal')) AS keterangan
FROM kamar k, JenisKamar j               
WHERE k.KodeJenis=j.KodeJenis
ORDER BY 1 ASC

SELECT KodeCin AS KODECI, nokamar AS NoKamar
IF(ISNULL(KodeUseFas)), "Tidak Pakai Fasilitas", "Pakai Fasilitas")
AS "Status Fasilitas"
FROM DCheckIn




