import asyncio
import time
import os
os.system("cls")
def saySomething():
    print("Say something starts...")
    # ! Note asyncio does not create the any other thread works in current thread
    # ! so it's will sleep the current thread for 2 sec. So everything will pause for 2 sec.
    time.sleep(2)
    print("Say Something ended....")


async def customRunner():
    print("Custom runner starts .....")
    saySomething()
    await asyncio.sleep(1)
    print("Custom runner stops.......")

print("Starts : ",time.strftime("%X"))
asyncio.run(customRunner())
print("Ends : ",time.strftime("%X"))