import pytest
import tasks
from tasks import Task


@pytest.fixture()
def db_connect(tmpdir):
     tasks.start_tasks_db(str(tmpdir), 'tiny')
     yield
     tasks.stop_tasks_db()

@pytest.mark.parametrize('tasks_created, number_of_tasks',
     [
        ([Task('sleep', done=True), Task('wake', 'brian')], 2),
        ([], 0)
     ])

def test_count_api(db_connect, tasks_created, number_of_tasks):
    for i in tasks_created:
        tasks.add(i)
    assert tasks.count() == number_of_tasks

