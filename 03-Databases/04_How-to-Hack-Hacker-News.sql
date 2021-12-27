SELECT *
FROM hacker_news
LIMIT 3;

-- 1. What are the top five stories with the highest scores?
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5; 

-- 2. Find the total score of all the stories.
SELECT SUM(score)
FROM hacker_news; 

-- 3. Find the individual users who have gotten combined scores of more than 200, and their combined scores.
SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC;

-- 4. Then, we want to add these users’ scores together and divide by the total to get the percentage.
SELECT (517 + 309 + 304 + 282) / 6366.0;

-- 5. While we are looking at the power users, some users are rickrolling — tricking readers into clicking on a link to a funny video. 
-- How many times has each offending user posted this link?
SELECT user, COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY 1
ORDER BY 2;

-- 6. Which of these sites feed Hacker News the most: GitHub, Medium, or New York Times?
SELECT CASE 
   WHEN url LIKE '%github.com%' THEN 'Github'
   WHEN url LIKE '%medium.com%%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source',
  COUNT(*)
FROM hacker_news
GROUP BY 1; 

-- 7. What’s the best time of the day to post a story on Hacker News?
SELECT strftime('%H', timestamp) AS 'Hour',
   ROUND(AVG(score), 1) AS 'Average Score',
   COUNT(*) AS 'Number of Stories'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 1;
