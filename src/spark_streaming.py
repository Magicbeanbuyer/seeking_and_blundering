#%%
from pyspark.sql.streaming import StreamingQuery
from pyspark.sql.types import StructType
from pyspark.sql import SparkSession
import time

spark = (
    SparkSession.builder.appName("x")
    .config("spark.hadoop.fs.s3a.path.style.access", True)
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .config(
        "spark.hadoop.fs.s3a.aws.credentials.provider",
        "org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider",
    )
    .getOrCreate()
)

#%%
userSchema = StructType().add("name", "string").add("age", "integer")
df = (
    spark.readStream.option("sep", ",").schema(userSchema).csv("spark_application/csv")
)  # Equivalent to format("csv").load("/path/to/directory")

#%%
query = (
    df.writeStream.outputMode("append")
    .option("checkpointLocation", "delta/stream_write/checkpoint")
    .format("console")
    .start()
)

time.sleep(10)
query.stop()

#%%
query = (
    df.writeStream.format("delta")
    .outputMode("append")
    .option("checkpointLocation", "delta/kids/_checkpoints/")
    .toTable("kids")
)

time.sleep(60)

query.stop()

#%%
query = (
    df.writeStream.format("delta")
    .outputMode("append")
    .option("checkpointLocation", "delta/people/_checkpoints/etl-from-csv")
    .partitionBy("name")
    .start("delta/people")
)

time.sleep(30)

query.stop()

#%%
df = spark.table("kids")
df.show()
#%%
spark.read.format("delta").load("delta/people").show()
#%%
df_i = df.select("*").where("age > 5")
df_i = df_i.groupBy("name").count()

print(df_i.isStreaming)

query = df_i.writeStream.outputMode("complete").format("console").start()


time.sleep(20)
query.stop()
#%%
df_i.createOrReplaceTempView("updates")
df_ii = spark.sql("select * from updates")  # returns another streaming DF
print("show =====")
df_ii.show()

time.sleep(30)
query.stop()

#%%
import boto3
from botocore import UNSIGNED
from botocore.config import Config

BUCKET = "deutsche-boerse-xetra-pds"
s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))
files = s3.list_objects_v2(Bucket=BUCKET, Prefix="2022-02-10")
for i in files["Contents"]:
    print(i["Key"])

#%%
df = spark.read.csv("s3a://deutsche-boerse-xetra-pds/2022-02-10/2022-02-10_BINS_XETR00.csv")
df.show()

#%%
schema = (
    StructType()
    .add("isin", "string")
    .add("mnemonic", "string")
    .add("securityDesc", "string")
    .add("securityType", "string")
    .add("currency", "string")
    .add("securityID", "long")
    .add("date", "date")
    .add("time", "string")
    .add("startPrice", "float")
    .add("maxPrice", "float")
    .add("minPrice", "float")
    .add("endPrice", "float")
    .add("tradedVolume", "float")
    .add("numberOfTrades", "integer")
)

df = spark.readStream.schema(schema).csv("s3a://deutsche-boerse-xetra-pds/2022-02-10/", header=True)

#%%
query = (
    df.writeStream.queryName("stock_price")
    .format("delta")
    .trigger(once=True)
    .outputMode("append")
    .option("checkpointLocation", "delta/stock_price/checkpoint")
    .toTable("stock_price")
)


def stop_streaming_query_gracefully(streaming_query: StreamingQuery):
    query_status = streaming_query.status["message"]
    while query_status != "Stopped":
        print(f"{streaming_query.name} status: {query_status}")
        time.sleep(3)
        query_status = streaming_query.status["message"]
        print(f"{streaming_query.name} status: {query_status}")
    streaming_query.stop()


stop_streaming_query_gracefully(query)

#%%
spark.table("stock_price").show()
