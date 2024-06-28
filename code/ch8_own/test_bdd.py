import pytest
from pytest_bdd import given, then

@pytest.fixture
def foo():
    return 'foo'

@given("i have injected one", target_fixture='foo')
def injectin_given():
    return 'injected_foo'

@then('foo should be "injected foo"')
def foo_is_foo(foo):
    assert foo == 'injected_foo'