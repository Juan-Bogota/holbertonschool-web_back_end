-- SQL script that creates stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users, 
    (SELECT newTable.id, (SUM(score * weight)/SUM(weight)) AS average 
    FROM users AS newTable 
    INNER JOIN corrections ON newTable.id = corrections.user_id 
    INNER JOIN projects ON corrections.project_id = projects.id
    GROUP BY newTable.id)
  AS query
  SET users.average_score = query.average
  WHERE users.id=query.id;
END;
$$