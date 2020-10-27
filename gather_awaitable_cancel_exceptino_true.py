import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    try: 
        s = await asyncio.gather(
            factorial("A", 2),
            factorial("B", '3'),
            factorial("C", 4),return_exceptions=True  #the first raised exception is immediately propagated to the task that awaits on gather()
        )
    except Exception as e:
        print(e)
    print(s)

asyncio.run(main())