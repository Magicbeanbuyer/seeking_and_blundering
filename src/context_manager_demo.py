"""Demonstrate context manager."""

from zipfile import ZipFile

import yaml


def read_file(base_path):
    """Read a file in a given path.

    Args:
        base_path: file path

    Returns:
        list: a list of files
    """
    file_path = "sample.yml"

    if base_path.endswith(".zip"):
        with ZipFile(base_path) as archive:  # Open the .zip file
            data = archive.read(file_path)
            print(data)
            conf_list = yaml.load(data, Loader=yaml.FullLoader)

    else:
        with open(f"{base_path}/{file_path}") as data:
            conf_list = yaml.load(data, Loader=yaml.FullLoader)

    return conf_list


def get_schema(base_path):
    """Read schema from file path.

    Args:
        base_path: the folder that contains a schema folder

    Returns:
        the schema string
    """
    if base_path.endswith(".zip"):
        with ZipFile(base_path, "r") as archive:  # Open the .zip file
            binary_data = archive.read("schema/aaa.sql")  # Read the CSV => binary format
            return binary_data.decode("utf-8").replace("\n", " ").replace("\t", " ")
    else:
        with open("schema/aaa.sql", newline="") as input_file:
            binary_data = input_file.read()
            return binary_data.replace("\n", " ").replace("\t", " ")


base_p = "/Users/zheng/PycharmProjects/seeking_and_blundering/resource/sample.zip"
a = read_file(base_p)
CONFIG_BYTES = (
    b"aws:\n  region_name: eu-central-1\n\nkafka:\n  cluster_name: dataeng-msk\n\ndelta_lake:\n  "
    b"s3_bucket: mop-dataeng-deltalake\n\nspark:\n  metadata_bucket: mop-dataeng-emrmetadata\n  "
    b"kafka_package: org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1\n  "
    b"delta_lake_package: io.delta:delta-core_2.12:1.0.0"
)
b = yaml.load(CONFIG_BYTES, Loader=yaml.FullLoader)
print(b)
# for i in a:
#     dedup = SimpleNamespace(**i["deduplication"])
#     print(dedup.watermark)
#
# pprint(a)
