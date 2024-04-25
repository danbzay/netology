--Полуавтоматически сделаны с помощью таблицы https://docs.google.com/spreadsheets/d/14T_7ydW5bKNKDDeWAhPSTaSLdR95MGBQBZAo_E21C_s/edit?usp=sharing



INSERT INTO collections (collection_title, year_of_release) VALUES 
('BBC Radio 1''s Live Lounge 2017', 2017),
('The Ghost Note Symphonies, Vol. 1', 2018),
('All Time Best', 2020),
('Music of Friends', 2019),
('The Bootleg Series Vol. 16: Springtime in New York 1980–1985', 2021);

INSERT INTO genres(genre_name) VALUES 
('pop'), ('EDM'), ('hip hop'), ('Melodic hardcore'), ('Hardcore melodic'), ('surf'), ('Folk rock'), ('Rock');

INSERT INTO artists(artist_name) VALUES 
('Ed Sheeran'), ('P!nk'), ('Justin Timberlake'), (' Rise Against'), ('Miho Nakayama'), ('Beach Boys'), ('Joni Mitchell'), ('Bob Dylan');

INSERT INTO albums(album_title, year_of_release) VALUES ('÷', 2017), ('Beautiful Trauma', 2017), ('FutureSex/LoveSounds', 2006), ('Appeal to Reason', 2020), ('Endgame', 2011), ('Catch the Nite', 1988), ('Ballads', 1989), ('Surfer Girl', 1963), ('Ladies of the Canyon', 1970), ('The Bootleg Series Volumes 1–3 (Rare & Unreleased) 1961–1991', 1991);



INSERT INTO songs (song_title, song_duration, album_id) 
SELECT 'Castle on the Hill', '225', album_id FROM albums 
WHERE album_title = '÷';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'What About Us', '269', album_id FROM albums WHERE album_title = 'Beautiful Trauma';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'My Love (originally by Justin Timberlake)', '222', album_id FROM albums WHERE album_title = 'FutureSex/LoveSounds';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Savior', '294', album_id FROM albums WHERE album_title = 'Appeal to Reason';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Wait for Me', '236', album_id FROM albums WHERE album_title = 'Endgame';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Catch Me', '256', album_id FROM albums WHERE album_title = 'Catch the Nite';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'You''re My Only Shinin'' Star', '279', album_id FROM albums WHERE album_title = 'Ballads';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'In My Room', '161', album_id FROM albums WHERE album_title = 'Surfer Girl';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Big Yellow Taxi (Traffic Jam Mix)', '289', album_id FROM albums WHERE album_title = 'Ladies of the Canyon';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Lord Protect My Child (Infidels outtake)', '257', album_id FROM albums WHERE album_title = 'The Bootleg Series Volumes 1–3 (Rare & Unreleased) 1961–1991';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Blind Willie McTell (take 5 – Infidels outtake)', '266', album_id FROM albums WHERE album_title = 'The Bootleg Series Volumes 1–3 (Rare & Unreleased) 1961–1991';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Eraser', '233', album_id FROM albums WHERE album_title = '÷';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Dive', '238', album_id FROM albums WHERE album_title = '÷';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Beautiful Trauma', '248', album_id FROM albums WHERE album_title = 'Beautiful Trauma';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Revenge (featuring Eminem)', '226', album_id FROM albums WHERE album_title = 'Beautiful Trauma';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Whatever You Want', '242', album_id FROM albums WHERE album_title = 'Beautiful Trauma';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'FutureSex/LoveSound', '241', album_id FROM albums WHERE album_title = 'FutureSex/LoveSounds';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'SexyBack', '242', album_id FROM albums WHERE album_title = 'FutureSex/LoveSounds';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Sexy Ladies / Let Me Talk to You (Prelude)', '332', album_id FROM albums WHERE album_title = 'FutureSex/LoveSounds';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Hero of War', '253', album_id FROM albums WHERE album_title = 'Appeal to Reason';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'A Gentlemen''s Coup', '226', album_id FROM albums WHERE album_title = 'Endgame';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Hawaii', '119', album_id FROM albums WHERE album_title = 'Surfer Girl';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Woodstock', '329', album_id FROM albums WHERE album_title = 'Ladies of the Canyon';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Just My Lover', '296', album_id FROM albums WHERE album_title = 'Catch the Nite';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Sherry', '279', album_id FROM albums WHERE album_title = 'Ballads';
INSERT INTO songs (song_title, song_duration, album_id) SELECT 'Foot of Pride (April 25, 1983)', '357', album_id FROM albums WHERE album_title = 'The Bootleg Series Volumes 1–3 (Rare & Unreleased) 1961–1991';

INSERT INTO genres_artists (genre_id, artist_id) 
SELECT genres.genre_id, artists.artist_id 
FROM genres, artists 
WHERE genre_name = 'pop' AND artist_name = 'Ed Sheeran';
INSERT INTO genres_artists (genre_id, artist_id) SELECT genres.genre_id, artists.artist_id FROM genres, artists WHERE genre_name = 'EDM' AND artist_name = 'P!nk';INSERT INTO genres_artists (genre_id, artist_id) SELECT genres.genre_id, artists.artist_id FROM genres, artists WHERE genre_name = 'hip hop' AND artist_name = 'Justin Timberlake';INSERT INTO genres_artists (genre_id, artist_id) SELECT genres.genre_id, artists.artist_id FROM genres, artists WHERE genre_name = 'Melodic hardcore' AND artist_name = ' Rise Against';INSERT INTO genres_artists (genre_id, artist_id) SELECT genres.genre_id, artists.artist_id FROM genres, artists WHERE genre_name = 'pop' AND artist_name = 'Miho Nakayama';INSERT INTO genres_artists (genre_id, artist_id) SELECT genres.genre_id, artists.artist_id FROM genres, artists WHERE genre_name = 'surf' AND artist_name = 'Beach Boys';INSERT INTO genres_artists (genre_id, artist_id) SELECT genres.genre_id, artists.artist_id FROM genres, artists WHERE genre_name = 'Folk rock' AND artist_name = 'Joni Mitchell';INSERT INTO genres_artists (genre_id, artist_id) SELECT genres.genre_id, artists.artist_id FROM genres, artists WHERE genre_name = 'Rock' AND artist_name = 'Bob Dylan';
INSERT INTO genres_artists (genre_id, artist_id) SELECT genres.genre_id, artists.artist_id FROM genres, artists WHERE genre_name = 'Hardcore melodic' AND artist_name = ' Rise Against';
INSERT INTO genres_artists (genre_id, artist_id) SELECT genres.genre_id, artists.artist_id FROM genres, artists WHERE genre_name = 'pop' AND artist_name = 'P!nk';


INSERT INTO artists_albums (artist_id, album_id) 
SELECT artists.artist_id, albums.album_id 
FROM artists, albums 
WHERE artist_name = 'Ed Sheeran' AND album_title = '÷';
INSERT INTO artists_albums (artist_id, album_id) SELECT artists.artist_id, albums.album_id FROM artists, albums WHERE artist_name = 'P!nk' AND album_title = 'Beautiful Trauma';INSERT INTO artists_albums (artist_id, album_id) SELECT artists.artist_id, albums.album_id FROM artists, albums WHERE artist_name = 'Justin Timberlake' AND album_title = 'FutureSex/LoveSounds';INSERT INTO artists_albums (artist_id, album_id) SELECT artists.artist_id, albums.album_id FROM artists, albums WHERE artist_name = ' Rise Against' AND album_title = 'Appeal to Reason';INSERT INTO artists_albums (artist_id, album_id) SELECT artists.artist_id, albums.album_id FROM artists, albums WHERE artist_name = ' Rise Against' AND album_title = 'Endgame';INSERT INTO artists_albums (artist_id, album_id) SELECT artists.artist_id, albums.album_id FROM artists, albums WHERE artist_name = 'Miho Nakayama' AND album_title = 'Catch the Nite';INSERT INTO artists_albums (artist_id, album_id) SELECT artists.artist_id, albums.album_id FROM artists, albums WHERE artist_name = 'Miho Nakayama' AND album_title = 'Ballads';INSERT INTO artists_albums (artist_id, album_id) SELECT artists.artist_id, albums.album_id FROM artists, albums WHERE artist_name = 'Beach Boys' AND album_title = 'Surfer Girl';INSERT INTO artists_albums (artist_id, album_id) SELECT artists.artist_id, albums.album_id FROM artists, albums WHERE artist_name = 'Joni Mitchell' AND album_title = 'Ladies of the Canyon';INSERT INTO artists_albums (artist_id, album_id) SELECT artists.artist_id, albums.album_id FROM artists, albums WHERE artist_name = 'Bob Dylan' AND album_title = 'The Bootleg Series Volumes 1–3 (Rare & Unreleased) 1961–1991';

INSERT INTO collections_songs (collection_id, song_id) 
SELECT collections.collection_id, songs.song_id 
FROM collections, songs WHERE collection_title = 'BBC Radio 1''s Live Lounge 2017' AND song_title = 'Castle on the Hill';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'BBC Radio 1''s Live Lounge 2017' AND song_title = 'What About Us';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'BBC Radio 1''s Live Lounge 2017' AND song_title = 'My Love (originally by Justin Timberlake)';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'The Ghost Note Symphonies, Vol. 1' AND song_title = 'Savior';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'The Ghost Note Symphonies, Vol. 1' AND song_title = 'Wait for Me';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'All Time Best' AND song_title = 'Catch Me';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'All Time Best' AND song_title = 'You''re My Only Shinin'' Star';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'Music of Friends' AND song_title = 'In My Room';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'Music of Friends' AND song_title = 'Big Yellow Taxi (Traffic Jam Mix)';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'The Bootleg Series Vol. 16: Springtime in New York 1980–1985' AND song_title = 'Lord Protect My Child (Infidels outtake)';
INSERT INTO collections_songs (collection_id, song_id) SELECT collections.collection_id, songs.song_id FROM collections, songs WHERE collection_title = 'The Bootleg Series Vol. 16: Springtime in New York 1980–1985' AND song_title = 'Blind Willie McTell (take 5 – Infidels outtake)';


