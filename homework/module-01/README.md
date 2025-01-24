${\color{blue}1.}$<br>
```shell
docker run -it --name docker_hw1 python:3.12.8 bash
```
```shell
pip --version
```

${\color{blue}2.}$<br> 
#### Connect to pgadmin (localhost:8080)
- Hostname : postgres
- Port : 5432 
- Maintenance database : ny_taxi
- Username : postgres
- Password : postgres

${\color{blue}3.}$<br>
``` sql
SELECT
	CASE
		WHEN trip_distance <= 1 THEN '1'
		WHEN trip_distance > 1 AND trip_distance <= 3 THEN '2'
		WHEN trip_distance > 3 AND trip_distance <= 7 THEN '3'
		WHEN trip_distance > 7 AND trip_distance <= 10 THEN '4'
		WHEN trip_distance > 10 THEN '5'
	END
		AS number,
	COUNT(*) AS answer
FROM (SELECT * FROM taxi_trips WHERE to_char(lpep_dropoff_datetime::timestamp, 'yyyy-MM') = '2019-10')
GROUP BY number;
```


