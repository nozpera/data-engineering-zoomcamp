import csv
import os
import json
import requests
import gzip
import time
import shutil
from kafka import KafkaProducer

def main():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    t0 = time.time()
    
    file_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/"
    filename = "green_tripdata_2019-10.csv.gz"
    csv_filename = filename.replace(".gz", "")
    request_url = f"{file_url}{'green'}/{filename}"
    
    print(f"filename: {filename}")
    print(f"request_url: {request_url}")
    
    with requests.get(request_url, stream=True) as response:
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            with gzip.open(filename, 'rb') as gz_file:
                with open(csv_filename, 'wb') as out_file:
                    shutil.copyfileobj(gz_file, out_file)
            
            with open(csv_filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    selected_data = {key: row[key] for key in ['lpep_pickup_datetime', 'lpep_dropoff_datetime', 'PULocationID', 'DOLocationID', 'passenger_count', 'trip_distance', 'tip_amount']}
                    producer.send('green_trips', value=selected_data)
                    print(f"sent: {selected_data}")
                producer.flush()
                
                t1 = time.time()
                print(f'took {(t1 - t0):.2f} seconds')
    
    os.remove(filename)
    os.remove(csv_filename)
                
if __name__ == "__main__":
    main()