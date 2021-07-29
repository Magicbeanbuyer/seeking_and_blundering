"""Demo MagicMock, patch, and mocking class behaviors."""

import os


def get_working_dir():
    path = os.getcwd()
    print(f"cwd: {path}")
    return path


class Helper:
    def __init__(self, path):
        self.path = path

    def get_folder(self):
        base_path = os.getcwd()
        return os.path.join(base_path, self.path)


class Worker:
    def __init__(self):
        self.helper = Helper("db")

    def work(self):
        path = self.helper.get_path()
        print(f"Working on {path}")
        return path


if __name__ == "__main__":
    get_working_dir()
    print(Helper("dodo").get_path())
    Worker().work()
