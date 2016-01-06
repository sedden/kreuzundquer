SELECT 'cp "' || p.photo || '" "uploads/' || to_char(p.uploaded, 'YYYY') || '/' || to_char(p.uploaded, 'MM') || '/' || 10000 + p.id || '.jpg"' AS cmd
FROM media_photos p
ORDER BY p.id;