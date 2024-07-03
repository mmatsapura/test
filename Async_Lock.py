import asyncio

import aiohttp

cache = dict()


async def request_remote():
    print("Will request the website to get status.")
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://www.example.com")
        return response.status


async def get_value(key: str, locker: asyncio.Lock):
    async with locker:
        if key not in cache:
            print(f"The value of key {key} is not in cache.")
            value = await request_remote()
            cache[key] = value
        else:
            print(f"The value of key {key} is already in cache.")
            value = cache[key]
        print(f"The value of {key} is {value}")
        return value


async def main():
    locker = asyncio.Lock()
    task_one = asyncio.create_task(get_value("status", locker))
    task_two = asyncio.create_task(get_value("status", locker))

    await asyncio.gather(task_one, task_two)


asyncio.run(main())
