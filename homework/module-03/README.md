${\color{blue}1.}$<br>
The answer is **20,332,093**

``` sql
SELECT COUNT(*) AS trips FROM data-engineering-zoomcamp-arp.db_zoomcamp.external_yellow_tripdata;
```

${\color{blue}2.}$<br>
The answer is **0 MB for the External Table and 155.12 MB for the Materialized Table**

``` sql
SELECT COUNT(DISTINCT(PULocationID)) AS count_PU_loc FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata;
```
``` sql
SELECT COUNT(DISTINCT(PULocationID)) AS count_PU_loc FROM data-engineering-zoomcamp-arp.db_zoomcamp.external_yellow_tripdata;
```

${\color{blue}3.}$<br>
The answer is **BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.**

The difference in data size estimation occurs because of the way BigQuery processes columns in columnar storage format.

For the first query:
``` sql
SELECT PULocationID FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata;
```
BigQuery only needs to read one column (PULocationID) from the storage.

For the second query:
``` sql
SELECT PULocationID, DOLocationID FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata;
```
BigQuery needs to read two columns (PULocationID and DOLocationID), so the amount of data read is doubled.

This happens because: BigQuery uses columnar storage, where each column is stored separately When you select a specific column, BigQuery only reads the requested column Each additional column you select means additional data that must be read Estimated data size is usually linear with the number of columns selected

${\color{blue}4.}$<br>
The answer is **8,333**

``` sql
SELECT COUNT(*) AS trips FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata WHERE fare_amount = 0;
```

${\color{blue}5.}$<br>
The answer is **Partition by tpep_dropoff_datetime and Cluster on VendorID**

${\color{blue}6.}$<br>
The answer is **310.24 MB for non-partitioned table and 26.84 MB for the partitioned table**

**Non-partitioned table**
``` sql
SELECT DISTINCT(VendorID) FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata WHERE tpep_dropoff_datetime BETWEEN "2024-03-01" AND "2024-03-15";
```

**Partitioned table**
``` sql
SELECT DISTINCT(VendorID) FROM data-engineering-zoomcamp-arp.db_zoomcamp.yellow_tripdata_partitioned_clustered WHERE tpep_dropoff_datetime BETWEEN "2024-03-01" AND "2024-03-15";
```

${\color{blue}7.}$<br>
The answer is **GCP Bucket**

External Table: Data is STILL stored in GCP Bucket. BigQuery only stores metadata and table definitions When the query is executed, BigQuery will "read" directly from the file in GCP Bucket Such as creating a "bridge" between BigQuery and the file in GCP Bucket

${\color{blue}8.}$<br>
The answer is **False**

No, clustering is not always necessary for effective querying in BigQuery.


