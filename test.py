import asyncio
import time

async def test(delay, reply):
    await asyncio.sleep(delay)
    print(reply)


async def main():
    task1 = asyncio.create_task(test(1, 'hello'))
    task2 = asyncio.create_task(test(2, "world"))
    print(f"startd time {time.strftime('%X')}")
    await task1
    await task2
    print(f"end time {time.strftime('%X')}")

asyncio.run(main())