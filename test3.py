import asyncio
import time
import os
os.system("cls")

async def say_after(time,msg):
    await asyncio.sleep(time)
    print(msg)


# ! create_task start execution as soon as it's created , we just have to wait to finish them
async def main():
    task1 = asyncio.create_task(
        say_after(1,"Hello")
    )

    task2 = asyncio.create_task(
        say_after(2,"World")
    )

    print("Started at time : ",time.strftime('%X'))

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print("Finished after : ",time.strftime('%X'))

asyncio.run(main=main())

