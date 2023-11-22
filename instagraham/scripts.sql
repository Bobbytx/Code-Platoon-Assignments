
--finding posts where username is grahamcrkr
-- SELECT * from posts WHERE user_id IN (
--     SELECT user_id
--     FROM users
--     WHERE username = GrahamCrkr
-- );

-- SELECT * FROM follows;

/*query to list:
 -all posts that user 1 is following
    -should include username of poster, post(img), caption, date posted
    -should include comments (content) on each post w/ username of commenter, content, date
 */

--SHOW ALL POSTS WITH COMMENTS , line 18 through 28
-- SELECT 
--     users.username AS poster, 
--     posts.picture,
--     posts.caption, 
--     posts.post_date, 
--     comments.content AS comment, 
--     commenter.username AS commenter
-- FROM users 
-- JOIN posts on users.id = posts.user_id
-- JOIN comments on comments.post_id = posts.id
-- JOIN users AS commenter on comments.user_id = commenter.id
-- ORDER BY posts.post_date DESC;

--WHERE THE USER ID 1 FOLLLOWS USERID OF OTHER POSTERS
 --need to create 2 diff alias for users, AS poster, AS commenter
 --one will join w/ posts table, other with commentse table to get user comments
 --modify 


--LETS SHOW ALL THE COMMMENTS

-- SELECT 
--    users.username AS poster, 
--    posts.picture,
--    posts.caption, 
--    posts.post_date,
--    JSON_AGG(comments.content) as comments
-- FROM 
--    users 
-- JOIN posts on users.id = posts.user_id
-- JOIN comments on comments.post_id = posts.id
-- JOIN users AS commenter on comments.user_id = commenter.id
-- GROUP BY 
--    poster, 
--    posts.picture, 
--    posts.caption, 
--    posts.post_date;

--select comments.content FROM comments JOIN posts ON posts.id = comments.post_id WHERE posts.id=1;

-- SELECT users.username, comments.content 
-- FROM users 
-- INNER JOIN comments  ON users.id = comments.user_id;
