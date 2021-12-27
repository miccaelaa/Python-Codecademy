-- 1. Let’s examine the three tables.   
SELECT * FROM trips;
 
SELECT * FROM riders;
 
SELECT * FROM cars;

-- 2. Try out a simple cross join between riders and cars.
SELECT riders.first,
   riders.last,
   cars.model
FROM riders, cars;

-- 3. Find the columns to join between trips and riders and combine the two tables using a LEFT JOIN.
SELECT *
FROM trips
 LEFT JOIN riders
  ON trips.rider_id = riders.id;

-- 4. Find the columns to join on and combine the trips and cars table using an INNER JOIN.
SELECT * 
FROM trips
 JOIN cars
  ON trips.car_id = cars.id;

-- 5. Find the columns to join on and combine the trips and cars table using an INNER JOIN.
SELECT *
FROM riders
UNION 
SELECT *
FROM riders2;

-- 6. What is the average cost for a trip?
SELECT ROUND(AVG(cost), 2)
FROM trips;

-- 7. Find all the riders who have used Lyft less than 500 times!
SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;

-- 8. Calculate the number of cars that are active
SELECT COUNT(*)
FROM cars
WHERE status = 'active';

-- 9. Write a query that finds the two cars that have the highest trips_completed.
SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;
