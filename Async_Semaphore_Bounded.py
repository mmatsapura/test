import asyncio
from asyncio import Semaphore


async def acquire(semaphore: Semaphore):
    print("acquire: Ожидание возможности захвата")
    async with semaphore:
        print("acquire: Захвачен...")
        await asyncio.sleep(5)
    print("acquire: Освобождается...")


async def release(semaphore: Semaphore):
    print("release: Одиночное освобождение...")
    semaphore.release()
    print("release: Одиночное освобождение - готово!")


async def main():
    semaphore = Semaphore(2)
    print("Два захвата, три освобождения...")
    await asyncio.gather(asyncio.create_task(acquire(semaphore)),
                         asyncio.create_task(acquire(semaphore)),
                         asyncio.create_task(release(semaphore)))
    print("Три захвата...")
    await asyncio.gather(asyncio.create_task(acquire(semaphore)),
                         asyncio.create_task(acquire(semaphore)),
                         asyncio.create_task(acquire(semaphore)))


if __name__ == "__main__":
    asyncio.run(main())
