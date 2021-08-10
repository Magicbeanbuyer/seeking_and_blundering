def read_number_from_file(file_path: str):
    with open(file_path, mode="rb") as file:
        number = int(file.read())
    return number


def double_number(number: int):
    return number * 2


def save_number(number: int, file_path: str):
    with open(file_path, mode="w") as file:
        file.write(str(number))


if __name__ == "__main__":
    my_num = read_number_from_file("/Users/zheng/Desktop/number.txt")
    print(my_num)
    doubled_num = double_number(my_num)
    print(doubled_num)
    save_number(doubled_num, "/Users/zheng/Desktop/number.txt")
