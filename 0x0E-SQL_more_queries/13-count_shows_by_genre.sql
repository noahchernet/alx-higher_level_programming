-- ists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
SELECT name AS genre, COUNT(*) AS number_of_shows from tv_genres LEFT JOIN
    tv_show_genres tsg on tv_genres.id = tsg.genre_id
    GROUP BY name ORDER BY number_of_shows DESC ;
