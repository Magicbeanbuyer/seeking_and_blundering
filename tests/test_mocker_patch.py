from src.scratch_skatch import print_env

ENV_DICT = {"a": "a", "b": "b"}


def test_one(mocker):
    mocker.patch.dict("os.environ", {"a": "a", "b": "b"}, clear=True)
    assert print_env() == ENV_DICT
