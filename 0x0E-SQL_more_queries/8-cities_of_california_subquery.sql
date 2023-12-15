-- Show all cities of CA in hbtn_0d_usa database.
-- Results in ascending order cities.id.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
 