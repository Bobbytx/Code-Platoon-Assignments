DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS follows;
DROP TABLE IF EXISTS comments;
Drop Table IF EXISTS posts; 
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    EMAIL VARCHAR NOT NULL
);
CREATE TABLE posts (
    id serial PRIMARY KEY,
    user_id bigint REFERENCES users(id),
    picture VARCHAR,
    caption TEXT,
    post_date timestamptz
);

CREATE TABLE comments (
    id serial PRIMARY KEY,
    post_id bigint REFERENCES posts(id), 
    Comment_time timestamptz,
    user_id bigint REFERENCES users (id),
    content TEXT
);

CREATE TABLE follows (
    id SERIAL PRIMARY KEY,
    follower_id bigint REFERENCES users(id),
    following_id bigint REFERENCES users(id),
    following_date timestamptz,
    UNIQUE(follower_id, following_id)
);

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    post_id bigint REFERENCES posts(id),
    user_id bigint REFERENCES users(id)
);