docker run -it \
    -e POSTGRES_USER="Postgres" \
    -e POSTGRES_PASSWORD="Postgres" \
    -e POSTGRES_DB="ny_taxi" \
    -v c:/Users/gamers/data-engineering-zoomcamp/Module_01_containerization_and_infrastructure_as_code/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5431:5432 \
    postgres:13 

ls -l ingest-data.py

chmod +x ingest-data.py

python ingest_data.py \
    --user=Postgres \
    --password=Postgres \
    --host=localhost \
    --port=5431 \
    --database=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"