${\color{blue}1.}$<br>
The answer is **128.3 MB**

Explanation: That the task purge files are removed whose task configuration is like this
```shell
- id: purge_files
type: io.kestra.plugin.core.storage.PurgeCurrentExecutionFiles
description: This will remove output files. If you'd like to explore Kestra outputs, disable it.
```
so, we can see the size of output in extract task.

${\color{blue}2.}$<br>
The answer is **green_tripdata_2020-04.csv**

```shell
variables:
  file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"
  staging_table: "public.{{inputs.taxi}}_tripdata_staging"
  table: "public.{{inputs.taxi}}_tripdata"
  data: "{{outputs.extract.outputFiles[inputs.taxi ~ '_tripdata_' ~ inputs.year ~ '-' ~ inputs.month ~ '.csv']}}"
```
Explanation : The result is green_tripdata_2020-04.csv because each placeholder in vars.file is replaced with the values inputs.taxi = 'green', inputs.year = '2020', and inputs.month = '04', forming the final string.

${\color{blue}3.}$<br>
The answer is **24,648,499**

Explanation: After make scheduling with backfill execution set to **true**. So, i can queries on the **yellow_tripdata** table like this
``` sql
SELECT COUNT(*) AS count FROM yellow_tripdata;
```
${\color{blue}4.}$<br>
The answer is **1,734,051**

Explanation: After make scheduling with backfill execution set to **true**. So, i can queries on the **green_tripdata** table like this
``` sql
SELECT COUNT(*) AS count FROM green_tripdata;
```

${\color{blue}5.}$<br>
The answer is **1,925,152**

Explanation: After load the dataset into pgAdmin (yellow_tripdata_2021-03.csv) and we can type queries like this:
``` sql
SELECT COUNT(*) AS count FROM yellow_tripdata_staging;
```
why use staging table? because every each of the dataset will load into staging table at first and then every dataset have loaded will be accumulate in main table.

${\color{blue}6.}$<br>
The answer is **Add a timezone property set to America/New_York in the Schedule trigger configuration**

Explanation:
```shell
triggers:
  - id: daily
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "@daily"
    timezone: America/New_York
```




