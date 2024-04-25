--Задание 2

--Название и продолжительность самого длительного трека.
    
SELECT song_title, song_duration FROM songs
WHERE song_duration = (SELECT max(song_duration) FROM songs);
    
--Название треков, продолжительность которых не менее 3,5 минут.

SELECT song_title FROM songs
WHERE song_duration >= '210'::interval;

--Названия сборников, вышедших в период с 2018 по 2020 год включительно.

SELECT collection_title FROM collections 
WHERE year_of_release BETWEEN 2018 AND 2020;

--Исполнители, чьё имя состоит из одного слова.

SELECT artist_name FROM artists
WHERE artist_name NOT LIKE '% %';

--Название треков, которые содержат слово «мой» или «my».

SELECT song_title FROM songs 
WHERE LOWER(song_title) LIKE '%my%';

--Задание 3

--Количество исполнителей в каждом жанре.

SELECT genres.genre_name, count(genres_artists.artist_id) 
FROM genres INNER JOIN genres_artists ON genres.genre_id = genres_artists.genre_id
GROUP BY genres.genre_name;

--Количество треков, вошедших в альбомы 2019–2020 годов.

SELECT album_title, count(song_id) 
FROM albums INNER JOIN songs USING(album_id)
WHERE year_of_release BETWEEN 2019 AND 2020
GROUP BY album_title;

--Средняя продолжительность треков по каждому альбому.

SELECT albums.album_title, avg(songs.song_duration) 
FROM songs INNER JOIN albums USING(album_id)
GROUP BY albums.album_title;

--Все исполнители, которые не выпустили альбомы в 2020 году.

SELECT DISTINCT artist_name 
FROM artists JOIN artists_albums USING(artist_id) 
WHERE artist_id NOT IN (
    SELECT artist_id 
    FROM artists_albums JOIN albums USING(album_id) 
    WHERE albums.year_of_release = 2020);

--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).

SELECT DISTINCT collection_title
FROM collections
JOIN collections_songs USING(collection_id)
JOIN songs USING(song_id)
JOIN artists_albums USING(album_id)
JOIN artists USING(artist_id)
WHERE artist_name = ' Rise Against';
       
--Задание 4(необязательное)

--Названия альбомов, в которых присутствуют исполнители более чем одного жанра.

SELECT album_title 
FROM albums 
JOIN artists_albums USING(album_id)
WHERE artist_id IN (SELECT artist_id 
    FROM genres_artists 
    GROUP BY artist_id HAVING count(genre_id) > 1);

--Наименования треков, которые не входят в сборники.

-- Вот чем это лучше?
SELECT song_title FROM songs LEFT JOIN collections_songs USING(song_id)
WHERE collection_id IS NULL;

-- Чем это
SELECT song_title FROM songs 
WHERE song_id NOT IN (SELECT song_id FROM collections_songs);

--Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.

SELECT artist_name 
FROM artists JOIN artists_albums USING(artist_id) JOIN songs USING(album_id)
WHERE song_duration = (SELECT min(song_duration) FROM songs);

--Названия альбомов, содержащих наименьшее количество треков.

SELECT album_title
FROM albums JOIN songs USING(album_id) 
GROUP BY album_id 
HAVING count(song_id) = (
    SELECT min(c) FROM (
        SELECT count(song_id) c FROM songs GROUP BY album_id));




