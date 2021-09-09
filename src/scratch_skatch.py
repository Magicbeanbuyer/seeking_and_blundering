from zipfile import ZipFile

with ZipFile(
    "/Users/zheng/PycharmProjects/seeking_and_blundering/resource/sample.zip", "r"
) as archive:  # Open the .zip file
    # Read the CSV => binary format
    binary_data = archive.read("sample/schema/orders.sql")
    print(binary_data)
