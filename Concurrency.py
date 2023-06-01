import asyncio


def multiply(x, y):
    return x * y


def squared(n):
    return multiply(n, n)


def printSquare(n):
    return squared(n)


numberSquared = printSquare(5)
print(numberSquared)


async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")


asyncio.run(main())
