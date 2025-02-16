${\color{blue}1.}$<br>
The answer is **1.6.1**

``` python
import dlt
print("dlt version:", dlt.__version__)
```

${\color{blue}2.}$<br>
The answer is **4**

``` python
import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import PageNumberPaginator
pipeline = dlt.pipeline(
    pipeline_name = "ny_taxi_pipeline",
    destination = dlt.destinations.postgres("postgresql://kestra:k3str4@localhost:5431/postgres-zoomcamp"),
    dataset_name = "homework"
)
def paginated_getter():
    client = RESTClient(
        base_url = "https://us-central1-dlthub-analytics.cloudfunctions.net",
        paginator = PageNumberPaginator(base_page=1, total_path=None)
    )
    for page in client.paginate("data_engineering_zoomcamp_api"):
        yield page
load_info = pipeline.run(paginated_getter(), table_name="ny_taxi_data", write_disposition="replace")
print(load_info)
```

${\color{blue}3.}$<br>
The answer is **10000**

``` python
df = pipeline.dataset(dataset_type="default").ny_taxi_data.df()
df
```

${\color{blue}4.}$<br>
The answer is **12.3049**

``` SQL
SELECT
  ROUND(AVG(EXTRACT(EPOCH FROM (trip_dropoff_date_time - trip_pickup_date_time)) / 60), 4)
    AS Average_trip
FROM homework.ny_taxi_data;
```
