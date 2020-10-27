import asyncio

async def nested():
    return 42

async def main():
    task1 = asyncio.create_task(nested())
    print(await task1)
asyncio.run(main())