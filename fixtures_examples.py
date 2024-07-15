import pytest


@pytest.fixture(params=[(0,1),(1,3),2,pytest.param(6,marks=pytest.mark.skip)])
def fixt_to_use(request):
    if isinstance(request.param, tuple):
        return request.param[0]
    return request.param


def test_my_own(fixt_to_use):
    print(fixt_to_use)


# content of test_fixture_marks.py
