import pytest
#import tasks
from tasks import Task

tasks_to_try = [
        ([Task('sleep', done=True), Task('wake', 'brian')], 2),
        ([], 0)
]

@pytest.fixture(name='own_fixture', params=tasks_to_try)
def initialized_data_for_count_test(request):
    return request.param
