from pprint import pprint
from types import SimpleNamespace
from zipfile import ZipFile

import yaml

base_p = "."


def read_file(base_path):
	file_path = "../resource/sample.yml"

	if base_path.endswith(".zip"):
		with ZipFile(base_path) as archive:  # Open the .zip file
			data = archive.read(file_path)
			conf_list = yaml.load(data, Loader=yaml.FullLoader)

	else:
		with open(f"{base_path}/{file_path}") as data:
			conf_list = yaml.load(data, Loader=yaml.FullLoader)

	return conf_list


def get_schema(base_path) -> str:
	# try:
	if base_path.endswith(".zip"):
		with ZipFile(base_path, 'r') as archive:  # Open the .zip file
			binary_data = archive.read("schema/aaa.sql")  # Read the CSV => binary format
			return binary_data.decode("utf-8").replace('\n', ' ').replace('\t', ' ')
	else:
		with open("schema/aaa.sql", newline='') as input_file:
			binary_data = input_file.read()
			return binary_data.replace('\n', ' ').replace('\t', ' ')


# except (FileNotFoundError, KeyError):  # schema doesn't exist
# 	print("External schema does not exist.")


a = read_file(base_p)
for i in a:
	dedup = SimpleNamespace(**i["deduplication"])
	print(dedup.watermark)

pprint(a)
