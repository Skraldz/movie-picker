DROP TABLE movies;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    how_long INT,
    added_by VARCHAR(255),
    tmdb_id VARCHAR(255),
    date_added DATE,
    seen BOOLEAN,
    released INT,
    country VARCHAR(255),
    languages VARCHAR(255)
);

CREATE TABLE actors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    actor_name VARCHAR(255)
);

CREATE TABLE genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    genre VARCHAR(255)
);

CREATE TABLE movie_actors (
    movie_id INT,
    FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
    actor_id INT,
    FOREIGN KEY (actor_id) REFERENCES actors(id) ON DELETE CASCADE
);

CREATE TABLE movie_genres (
    movie_id INT,
    FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
    genre_id INT,
    FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);