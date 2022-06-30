-- List of bands with Glam rock

SELECT band_name AS band_name,
    IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
