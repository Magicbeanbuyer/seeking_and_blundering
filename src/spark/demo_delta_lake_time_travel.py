# %%
from pyspark.sql import SparkSession
from delta import DeltaTable
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = (
    SparkSession.builder.appName("x")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

# %% create delta table
table_name = "friends_v2"
s3_prefix = "s3a://path-to-s3"
# table_path = f"{s3_prefix}/{table_name}"
table_path = "delta/vacumm"
schema = StructType(
    [StructField("id", IntegerType(), False), StructField("name", StringType(), False)]
)
# delta_table = (
#     DeltaTable.create(spark)
#     .tableName(table_name)
#     .addColumns(schema)
#     .location(table_path)
#     # .property("delta.deletedFileRetentionDuration", "0 hours")
#     .execute()
# )
# write v1
data = [(1, "Monica"), (2, "Rachel")]
df = spark.createDataFrame(data, schema)
df.write.format("delta").mode("append").save(table_path)

# write v2
data = [(1, "Monica"), (2, "Rachel"), (3, "Joey")]
# schema = "age integer, name string"
df = spark.createDataFrame(data, schema)
df.write.format("delta").mode("overwrite").save(table_path)

# %% query v1
df = spark.read.format("delta").option("versionAsOf", "0").load(table_path)
df.show()
# query v2
df = spark.read.format("delta").option("versionAsOf", "1").load(table_path)
df.show()
# query latest
df = spark.read.format("delta").load(table_path)
df.show()
# %% describe history
deltaTable = DeltaTable.forPath(spark, table_path)
fullHistoryDF = deltaTable.history()  # get the full history of the table
fullHistoryDF.show(truncate=False)
# lastOperationDF = deltaTable.history(1) # get the last operation
# %% vacuum
spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", False)
deltaTable = DeltaTable.forPath(spark, table_path)
deltaTable.vacuum(0)

# q = spark.sql(f"VACUUM delta.`/delta/vacumm` DRY RUN")
# Found 3 files and directories in a total of 1 directories that are safe to delete.
