CREATE TABLE genres (
genre_id serial primary key,            
genre_name varchar(80)
);

CREATE TABLE artists (
artist_id serial primary key,            
artist_name varchar(80) 
);

CREATE TABLE albums (
album_id serial primary key,            
album_title varchar(80),
year_of_release smallint
);

CREATE TABLE songs (
song_id serial primary key,            
song_title varchar(255),
song_duration interval,
album_id serial references albums(album_id));

CREATE TABLE collections (
collection_id serial primary key,
collection_title varchar(80),
year_of_release smallint
);


CREATE TABLE genres_artists (
genre_id serial references genres(genre_id),            
artist_id serial references artists(artist_id)
);

CREATE TABLE artists_albums (
artist_id serial references artists(artist_id),            
album_id serial references albums(album_id)
);

CREATE TABLE collections_songs ( 
collection_id serial references collections(collection_id),
song_id serial references songs(song_id)
);


