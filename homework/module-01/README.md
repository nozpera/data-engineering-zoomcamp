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

${\color{blue}4.}$<br>
``` sql
SELECT 
	to_char(lpep_pickup_datetime::timestamp, 'yyyy-MM-DD') 
		AS date 
	FROM 
		taxi_trips 
	WHERE 
		trip_distance IN (SELECT MAX(trip_distance) FROM taxi_trips);
```

${\color{blue}5.}$<br>
``` sql
SELECT * 
	FROM 
	(SELECT z."Zone", ROUND(SUM(t.total_amount)::numeric, 2) AS total_amount 
		FROM 
			(SELECT * FROM taxi_trips WHERE to_char(lpep_pickup_datetime::timestamp, 'yyyy-MM-DD') = '2019-10-18') AS t
		JOIN zones AS z ON (z."LocationID" = t."PULocationID")
			GROUP BY z."Zone"
				ORDER BY total_amount DESC) 
	WHERE total_amount > 13000;
```

${\color{blue}6.}$<br>
``` sql
SELECT zDO."Zone" AS DO_Zone
	FROM taxi_trips AS t
JOIN zones AS zPU ON (zPU."LocationID" = t."PULocationID")
JOIN zones AS zDO ON (zDO."LocationID" = t."DOLocationID")
	WHERE (to_char(t.lpep_pickup_datetime::timestamp, 'yyyy-MM') = '2019-10') AND (zPU."Zone" = 'East Harlem North')
		ORDER BY tip_amount DESC LIMIT 1;
```

${\color{blue}7.}$<br>
```shell
terraform init
```
```shell
terraform apply -auto-approve
```
```shell
terraform destroy
```
- **terraform init** This command is used to download the provider plugins and set up the backend. This is the first step in any Terraform workflow.
- **terraform apply -auto-approve** This command is used to generate the proposed changes (plan) and execute immediately without requiring manual confirmation.
- **terraform destroy** This command is used to delete all resources managed by Terraform.
