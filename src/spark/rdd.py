# %%
# Parallelized Collections
from pyspark.sql import SparkSession
from operator import add

spark = SparkSession.builder.appName("x").getOrCreate()
sc = spark.sparkContext
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8], 3)
rdd.glom().collect()
# %%
rdd = rdd.coalesce(1)
rdd.collect()

# %%
# External Datasets
# number of partitions must be greater than the number of files
rdd = sc.textFile("src/spark/data.txt", 1)
# rdd.glom().collect()
rdd.map(lambda s: len(s)).reduce(add)

# %%
# SequenceFile
rdd = sc.parallelize(range(1, 4)).map(lambda x: (x, "a" * x))
rdd.saveAsSequenceFile("src/spark/sf")
sorted(sc.sequenceFile("src/spark/sf").collect())
