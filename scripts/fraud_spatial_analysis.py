import pyspark.sql.functions as F
from pyspark.sql import Window
import math

@F.udf("double")
def haversine(lat1, lon1, lat2, lon2):
    if None in (lat1, lon1, lat2, lon2):
        return None

    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2

    return 2 * R * math.asin(math.sqrt(a))

df = spark.read.csv(
    "wasbs://transactions@<ACCOUNT>.blob.core.windows.net/transactions.csv",
    header=True,
    inferSchema=True
)

window = Window.partitionBy("UserID").orderBy("Timestamp")

df = df.withColumn("PrevLat", F.lag("Latitude").over(window)) \
       .withColumn("PrevLon", F.lag("Longitude").over(window)) \
       .withColumn("PrevTime", F.lag("Timestamp").over(window))

df = df.withColumn(
    "DistanceKM",
    haversine("Latitude", "Longitude", "PrevLat", "PrevLon")
)

df = df.withColumn(
    "MinutesSincePrev",
    (F.col("Timestamp").cast("long") - F.col("PrevTime").cast("long")) / 60
)

df = df.withColumn(
    "SpatialAnomaly",
    (F.col("DistanceKM") > 1000) & (F.col("MinutesSincePrev") < 30)
)

df.createOrReplaceTempView("transactions")

print("✅ Spatial anomaly feature added")
