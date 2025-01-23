ls -l ingest-data.py

chmod +x ingest-data.py

./ingest-data.py --user Postgres --password Postgres --host localhost --port 5431 --db ny_taxi --table-name yellow_taxi_trips --url "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

docker container create --name database-server --network postgresql-ingest_taxi --env POSTGRES_USER=Postgres --env POSTGRES_PASSWORD=Postgres --env POSTGRES_DB=ny_taxi --volume c:/Users/gamers/data-engineering-zoomcamp/Module_01_containerization_and_infrastructure_as_code/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data -p 5431:5432 postgres:13
bf4b9c6b75f5d0a2981fb17aa6f6cde15382e916bd1e6aff2bc71b35d1d41911

docker build -t taxi_ingest:v01 .

docker run -it --name docker-ingest --network postgresql-ingest_taxi taxi_ingest:v01 --user Postgres --password Postgres --host database-server --port 5432 --db ny_taxi --table-name yellow_taxi_trips --url "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"