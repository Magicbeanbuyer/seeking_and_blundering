from unittest import TestCase, mock, main

from demo_magicmock import get_working_dir, Worker


class TestStringMethods(TestCase):
    def test_patch_return_value(self):
        with mock.patch("demo_magicmock.os.getcwd", return_value="/mock/patch/dir") as mocked_cwd:
            assert get_working_dir() == "/mock/patch/dir"
            mocked_cwd.assert_called()

    @mock.patch("demo_magicmock.os.getcwd", return_value="/decorator/path", scope="function")
    def test_call_counts(self, mocky_os):
        get_working_dir()
        mocky_os.assert_called_once()
        assert get_working_dir() == "/decorator/path"

    def test_patching_class(self):
        with mock.patch("demo_magicmock.Helper") as MockHelper:
            MockHelper.return_value.get_path.return_value = "testing"
            worker = Worker()
            MockHelper.assert_called_once_with("db")
            self.assertEqual(worker.work(), "testing")


if __name__ == "__main__":
    main()
