import asyncio
import time

async def say(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def manager():
    print(f"started at {time.strftime('%X')}")
    await say(1, 'hello')
    await say(2, 'world')
    print(f"end at {time.strftime('%X')}")


asyncio.run(manager())