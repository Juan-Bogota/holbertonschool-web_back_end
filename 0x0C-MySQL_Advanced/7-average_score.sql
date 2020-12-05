-- Triggers - MYSQL
-- Write a SQL script that creates a stored procedure that adds a new correction for a student.
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
DECLARE prom INT;
SET prom = (select AVG(score) from corrections AS newTable GROUP BY user_id HAVING newTable.user_id=user_id;);
UPDATE users SET average_score=prom WHERE id=user_id ;

END;
|