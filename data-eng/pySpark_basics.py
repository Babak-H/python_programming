import SparkContext as sc
import pyspark.sql.functions as F

# Verify SparkContext
print(sc)
# Print Spark version
print(sc.version)


# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession
# Create my_spark
# This returns an existing SparkSession if there's already one in the environment, or creates a new one if necessary!
my_spark = SparkSession.builder.getOrCreate()
# Print my_spark
print(my_spark)
# Print the tables in the catalog
# catalog lists all the data inside the cluster. 
print(spark.catalog.listTables())


# One of the advantages of the DataFrame interface is that you can run SQL queries on the tables in your Spark cluster.
query = "FROM flights SELECT * LIMIT 10"
# Get the first 10 rows of flights
# spark : SparkSession object
flights10 = spark.sql(query)
# Show the results
flights10.show()


# Spark DataFrames make it easy with the .toPandas() method. Calling this method on a Spark DataFrame returns the corresponding pandas DataFrame
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"
# Run the query
flight_counts = spark.sql(query)
# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()
# Print the head of pd_counts
print(pd_counts.head())


# Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))
# Create spark_temp from pd_temp
spark_temp = spark.createDataFrame(pd_temp)
# Examine the tables in the catalog
print(spark.catalog.listTables())
# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView("temp")
# Examine the tables in the catalog again
print(spark.catalog.listTables())


file_path = "/usr/local/share/datasets/airports.csv"
# Read in the airports data
airports = spark.read.csv(file_path)
# Show the data
airports.show()


file_path = "/usr/local/share/datasets/airports.csv"
# Read in the airports data
airports = spark.read.csv(file_path, header=True)
# Show the data
airports.show()


# Create the DataFrame flights
flights = spark.table("flights")
# Show the head
flights.show()
# Add duration_hrs
# withColumn(name, value)
flights = flights.withColumn("duration_hrs", flights.air_time/60)


# Filter flights by passing a string
long_flights1 = flights.filter("distance > 1000")
# Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)
# # Print the data to check they're equal
long_flights1.show()
long_flights2.show()


# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")
# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)
# Define first filter
filterA = flights.origin == "SEA"
# Define second filter
filterB = flights.dest == "PDX"
# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)


# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")
# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)
# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")
speed1.show()


# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()
# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()


# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()
# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()


# groupby and use aggregate methods with pySpark
flights.groupBy("tailnum").count().show()
flights.groupBy("origin").avg("air_time").show()


# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")
# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()
# Standard deviation of departure delay
by_month_dest.agg(F.stddev("dep_delay")).show()


# Examine the data
print(airports.show())
# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")
# Join the DataFrames
flights_with_airports = flights.join(airports, "dest", "leftouter")
# Examine the new DataFrame
print(flights_with_airports.show())
