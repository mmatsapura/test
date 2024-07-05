import asyncio

from asyncio import Semaphore
from aiohttp import ClientSession


async def get_url(url: str, session: ClientSession, sem: Semaphore):
    print('waiting for semaphore')
    async with sem:
        print('Sem accuired ......')
        await asyncio.sleep(1)
        response = await session.get(url)
        print('Finishing requesting')
        return response.status


async def main():
    semaphore = Semaphore(1)
    async with ClientSession() as sess:
        tasks = [asyncio.create_task(get_url("https://www.example.com", sess, semaphore)) for _ in range(1000)]
        await asyncio.gather(*tasks)


asyncio.run(main())
