# Every async_IO function is called co-routine and it's object is called coroutine-object

import asyncio
import os
os.system("cls")

async def main():
    print("Start of main....")
    await  asyncio.sleep(1)
    print("End of main....")


asyncio.run(main())
