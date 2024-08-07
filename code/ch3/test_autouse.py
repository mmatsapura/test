"""Demonstrate autouse fixtures."""

import time

import pytest


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session."""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report tests durations after each function."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntests duration : {:0.3} seconds'.format(delta))


def test_1():
    """Simulate long-ish running tests."""
    time.sleep(1)


def test_2():
    """Simulate slightly longer tests."""
    time.sleep(1.23)
