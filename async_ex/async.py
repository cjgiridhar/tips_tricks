__author__ = 'cgiridhar'
import asyncio
# Asyncio is async, non blocking module introduced in python 3.2 for optimizing non blocking I/O operations
# asyncio runs on philosophy of single threaded event loop
# User requests are handled by the event loop
# event loop create tasks

def operation():
    future = asyncio.Future()
    print("Going to sleep now")
    yield from asyncio.sleep(4)
    future.set_result("Done!")
    print(future.result())


def two():
    future = asyncio.Future()
    print("Going to sleep now (2)")
    yield from asyncio.sleep(1)
    future.set_result("Done!(2)")
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop() # event loop started
asyncio.async(operation()) # creates task
asyncio.async(two()) # another task created

try:
    loop.run_forever()
finally:
    loop.close()