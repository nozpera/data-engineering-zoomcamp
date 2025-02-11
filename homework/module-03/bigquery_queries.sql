-- Creating external table from gcs path
CREATE OR REPLACE EXTERNAL TABLE data-engineering-zoomcamp-arp.db_zoomcamp.external_yellow_tripdata
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://nozpera_bucket/yellow_tripdata_2024-*.parquet']
);

CREATE OR REPLACE TABLE data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata
AS SELECT * FROM data-engineering-zoomcamp-arp.db_zoomcamp.external_yellow_tripdata;

SELECT * FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata;

SELECT COUNT(DISTINCT(PULocationID)) AS count_PU_loc FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata;

SELECT COUNT(DISTINCT(PULocationID)) AS count_PU_loc FROM data-engineering-zoomcamp-arp.db_zoomcamp.external_yellow_tripdata;

SELECT PULocationID FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata;

SELECT PULocationID, DOLocationID FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata;

SELECT COUNT(*) AS trips FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata WHERE fare_amount = 0;

CREATE OR REPLACE TABLE data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata_partitioned_clustered
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS SELECT * FROM data-engineering-zoomcamp-arp.db_zoomcamp.external_yellow_tripdata;

SELECT DISTINCT(VendorID) FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata_partitioned_clustered WHERE tpep_dropoff_datetime BETWEEN "2024-03-01" AND "2024-03-15";

SELECT DISTINCT(VendorID) FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata WHERE tpep_dropoff_datetime BETWEEN "2024-03-01" AND "2024-03-15";
