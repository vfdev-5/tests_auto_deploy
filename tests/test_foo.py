
from check_auto_deploy import Foo


def test_foo():

    foo = Foo()
    assert foo.a == 10
    assert foo.b == "test"
