from unittest import TestCase, mock, main

from demo_magicmock import get_working_dir, Worker


class TestStringMethods(TestCase):
    def test_patch_return_value(self):
        with mock.patch(
            "demo_magicmock.os.getcwd", return_value="/one/mock/patch/dir"
        ) as mocked_cwd:
            assert get_working_dir() == "/one/mock/patch/dir"
            mocked_cwd.assert_called()

    def test_patching_class(self):
        with mock.patch("demo_magicmock.Helper", autospec=True) as MockHelper:
            # failed because the Helper class has method get_folder
            # however Worker classed call get_path instead
            MockHelper.return_value.get_path.return_value = "/three/testing"
            worker = Worker()
            MockHelper.assert_called_once_with("db")
            self.assertEqual(worker.work(), "/three/testing")

    @mock.patch("demo_magicmock.os")
    def test_call_counts(self, mocky_os):
        get_working_dir()
        mocky_os.getcwd.assert_called_once()


# https://yeraydiazdiaz.medium.com/what-the-mock-cheatsheet-mocking-in-python-6a71db997832


if __name__ == "__main__":
    main()
