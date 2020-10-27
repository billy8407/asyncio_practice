import asyncio
import time

async def sayafter(delay, something):
    await asyncio.sleep(delay)
    print(something)

async def main():
    task1 = asyncio.create_task(sayafter(1, 'hello'))
    task2 = asyncio.create_task(sayafter(2, 'world'))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"end at {time.strftime('%X')}")
asyncio.run(main())