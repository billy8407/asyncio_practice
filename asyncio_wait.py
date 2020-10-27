import asyncio

async def a():
    print('in')
    await asyncio.sleep(1)
    print('out')

asyncio.run(a())