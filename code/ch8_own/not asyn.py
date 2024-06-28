import asyncio
import time


def fn():
    print("one")
    time.sleep(1)
    fn2()
    print('four')
    time.sleep(1)
    print('five')
    time.sleep(1)


def fn2():
    time.sleep(1)
    print("two")
    time.sleep(1)
    print("three")


fn()
