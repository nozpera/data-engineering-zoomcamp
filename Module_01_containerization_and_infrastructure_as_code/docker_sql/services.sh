docker run -it \
    -e POSTGRES_USER="Postgres" \
    -e POSTGRES_PASSWORD="Postgres" \
    -e POSTGRES_DB="ny_taxi" \
    -v c:/Users/gamers/data-engineering-zoomcamp/Module_01_containerization_and_infrastructure_as_code/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5431:5432 \
    postgres:13 