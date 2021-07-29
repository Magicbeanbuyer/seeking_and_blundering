"""Demo unittest Mock class."""
import sys
from unittest.mock import Mock

my_mock = Mock()
assert isinstance(my_mock, Mock)

# a Mock object will return another Mock instance when accessing one of its attributes
assert isinstance(my_mock.foo, Mock)

# different attributes point to different Mock instances
assert my_mock.foo is not my_mock.bar

# assign value to attribute during instantiation
my_mock = Mock(foo="haha")
print(my_mock.foo)

# assign a return value to a Mock object
my_mock.return_value = "my mock returns this string"
print(my_mock)
print(my_mock())

# to raise an exception
my_mock.side_effect = RuntimeError("Baaaam")
try:
    my_mock(a=1)  # called with param a
except Exception as e:
    print(e)
    print("Unexpected error:", sys.exc_info())

try:
    my_mock.assert_called_once()
    # called at both line 21 and 26
except AssertionError as e:
    print(f"call count: {my_mock.call_count}")
    print(f"call args {my_mock.call_args_list}")
    print(e)

# clear out all the calls
my_mock.reset_mock()
print(my_mock.call_args_list)
