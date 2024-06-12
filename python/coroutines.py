# Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications.
import asyncio
import time

import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, "hello")
    await say_after(2, "world")

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


# The asyncio.create_task() function to run coroutines concurrently as asyncio
async def main():
    task1 = asyncio.create_task(say_after(1, "hello"))

    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


# The asyncio.TaskGroup class provides a more modern alternative to create_task()
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(1, "hello"))

        task2 = tg.create_task(say_after(2, "world"))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")


# We say that an object is an awaitable object if it can be used in an await expression
import asyncio


async def nested():
    return 42


async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".


asyncio.run(main())

# If result is provided, it is returned to the caller when the coroutine completes.

# sleep() always suspends the current task, allowing other tasks to run.
import asyncio
import datetime


async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


asyncio.run(display_date())

import asyncio
from asyncio import CancelledError


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    task = asyncio.create_task(call_api("Calling API...", result=2000, delay=5))

    if not task.done():
        print("Cancelling the task...")
        task.cancel()

    try:
        await task
    except CancelledError:
        print("Task has been cancelled.")


asyncio.run(main())

# function runs an iterable of awaitables objects and blocks until a specified condition
import asyncio
from asyncio import create_task


class APIError(Exception):
    pass


async def call_api(message, result=100, delay=3, raise_exception=False):
    print(message)
    await asyncio.sleep(delay)
    if raise_exception:
        raise APIError
    else:
        return result


async def main():
    task_1 = create_task(call_api("calling API 1...", result=1, delay=1))
    task_2 = create_task(call_api("calling API 2...", result=2, delay=2))
    task_3 = create_task(call_api("calling API 3...", result=3, delay=3))

    pending = (task_1, task_2, task_3)

    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        result = done.pop().result()
        print(result)


asyncio.run(main())

import asyncio


async def call_api(message, result, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    a, b = await asyncio.gather(
        call_api("Calling API 1 ...", 1), call_api("Calling API 2 ...", 2)
    )
    print(a, b)


asyncio.run(main())
