SELECT
  pl.country   AS country,
  COUNT(pe.id) AS people_born
FROM
  places pl
  LEFT JOIN people pe ON pe.place_of_birth = pl.city
GROUP BY 1
;