""" 
We say that an object is an awaitable object if it can be used in an await expression. Many asyncio APIs are designed to accept awaitables.

There are three main types of awaitable objects: coroutines, Tasks, and Futures.

! Python coroutines are awaitables and therefore can be awaited from other coroutines:

"""


import asyncio
import os
os.system("cls")

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested() # ! even this will throw the warning 

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())


""" 
Important In this documentation the term “coroutine” can be used for two closely related concepts:
a coroutine function: an async def function;

a coroutine object: an object returned by calling a coroutine function.


 """