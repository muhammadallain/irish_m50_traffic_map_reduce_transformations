# Big Data Management
## Hadoop Map Reduce | Ubuntu Server | Data Transformations
This project performs map reduce data transformation operations on Irish Traffic Counter 
data. Irish Road Network has installed sensors on specific location that collect vehicle data 
including location, type, speed, weight and more. This data is stored in atomic form.

**Dataset:**  [Traffic Dataset Ireland](https://data.tii.ie/Datasets/TrafficCountData/2021/01/15/per-vehicle-records-2021-01-15.csv)


**Watch the video instead:** https://youtu.be/3IhpsT_cOTw

Downloading Data Set using ‘wget’ followed by the download link.

![Picture1](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/ec29d923-e27e-4743-930b-bcdfa0f801d2)

Create directory for project’s assignment

![Picture2](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/48e3d28e-8f9b-4ba3-a087-d42a82dc839a)

Create directory for input. This is where the input data comes and gets stored.

![Picture3](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/c9cf984f-b911-4f0a-a88a-d2af6182ecd2)

Upload data on Hadoop DFS

![Picture4](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/436ebf5a-d58e-4331-9243-4b309dc0a109)

**Query 1:** Lets develop custom mapper and reducer to calculate the usage of Irish road network in terms of percentage grouped by vehicle type.

**Mapper:** Lines are read from standard input and stored in the variable called lines. The class 
name from line is printed with each iteration through the loop with a ‘1’ delimited by tab.

![Picture5](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/b223d83d-a240-4b0d-aa1f-72ba749a1706)

**Reducer:** reduce the key value pairs to single unique key. Instead of counting the 
occurrences, we divide the occurrences with total rows and multiply with hundred to get 
the percentage for each individual key. This calculation is performed directly in the print 
statements.

![Picture6](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/dff5e6fa-991f-4dc9-b2d7-4334873ef16f)

Output: The output is as follows. We also have 0.01% missing values for class name column that are empty has represented as “ “ empty string.

![Picture7](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/ae2ca781-0f69-442f-b318-2a94646b8bf6)

**Query 2:** Lets calculate the highest and lowest hourly flows for Cars on M50 (use the counters installed between junction 03 - junction 17).

**Mapper:**

![Picture8](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/5b7c936a-6273-43b6-bfd8-b357d0297601)

**Reducer:**

![Picture9](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/5baa39cd-b0db-4820-a1f6-9c78fa4e007b)
![Picture10](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/1c1c1df3-3455-4f75-aacc-8910ed9adee9)

**Output: **

![Picture11](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/a4c911f1-61b5-44af-a918-d932188f94b7)
![Picture12](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/4913b572-ede6-4da0-95e9-7d31cb2368e9)

**Query 3:** Lets calculate average speed of Motorbikes.

**Mapper:**

![Picture13](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/2d1d0c03-4a00-4a5f-a277-72e0c2e43fb3)

**Reducer:**

![Picture14](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/bbabbce5-8447-40fd-8bfa-0c3b35ca448e)

**Output:**

![Picture15](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/b2b8a622-6678-4f7f-806d-4e37dc423668)

**Query 4:** Lets calculate the top 10 locations with highest number of counts of HGVs (consider both RIGID + ART).

**Mapper:**

![Picture16](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/ae4f5d5d-0b50-4f04-95eb-fa5ac19051c9)

**Reducer:**

![Picture17](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/ea0e1d6e-92dc-48c8-86b2-05831ada0e99)

**Output:**

![Picture18](https://github.com/muhammadallain/irish_m50_traffic_map_reduce_transformations/assets/96694357/b541f242-d2f9-4c12-b880-508ea97733ef)
