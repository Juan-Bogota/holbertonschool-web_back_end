-- Triggers - MYSQL
-- Write a SQL script that creates a stored procedure for a student.
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
DECLARE prom INT;
SET prom = (select AVG(score) from corrections GROUP BY user_id HAVING user_id=user_id);
UPDATE users SET average_score=prom WHERE id=user_id;

END;
|