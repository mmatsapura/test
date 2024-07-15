import pytest
import tasks
from tasks import Task


@pytest.fixture()
def db_connect(tmpdir):
     tasks.start_tasks_db(str(tmpdir), 'tiny')
     yield
     tasks.stop_tasks_db()

@pytest.mark.skip(reason='want to tests usage of fixture')
@pytest.mark.parametrize('tasks_created, number_of_tasks',
     [
        ([Task('sleep', done=True), Task('wake', 'brian')], 2),
        ([], 0)
     ])

def test_count_api(db_connect, tasks_created, number_of_tasks):
    for i in tasks_created:
        tasks.add(i)
    assert tasks.count() == number_of_tasks


def test_count_api_with_fixture(db_connect, own_fixture):
    for inner_tasks in own_fixture[0]:
        tasks.add(inner_tasks)
    assert tasks.count() == own_fixture[1]
