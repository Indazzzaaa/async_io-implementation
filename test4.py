import asyncio
import os
import time

os.system("cls")

async def say_after(time,msg):
    await asyncio.sleep(time)
    print(msg)

#  ! TaskGroup is new in the pthon 3.11
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())