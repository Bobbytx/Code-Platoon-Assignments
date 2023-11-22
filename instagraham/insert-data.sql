\COPY users FROM 'users.csv' DELIMITER ',' CSV HEADER;
\COPY posts FROM 'posts.csv' DELIMITER ',' CSV HEADER;
\COPY comments FROM 'comments.csv' DELIMITER ',' CSV HEADER;
\COPY follows FROM 'follows.csv' DELIMITER ',' CSV HEADER;
\COPY likes FROM 'likes.csv' DELIMITER ',' CSV HEADER;