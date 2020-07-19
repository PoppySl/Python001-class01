SELECT * FROM data;

SELECT * FROM data LIMIT(10);

SELECT id FROM data; //id 是 data 表的特定一列

SELECT COUNT(id) FROM data;

SELECT * FROM data WHERE id<1000 AND age>30;

SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;

SELECT FROM table1 UNION SELECT FROM table2;

DELETE FROM table1 WHERE id=10;

ALTER TABLE table1 DROP COLUMN column_name;