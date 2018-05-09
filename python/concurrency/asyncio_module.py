# -*- coding: utf-8 -*-
# asyncio_module.py


import asyncio
import datetime
import time


def function1(end_time, loop):
    print("function1 called")
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, function2, end_time, loop)
    else:
        loop.stop()


def function2(end_time, loop):
    print("function2 called")
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, function3, end_time, loop)
    else:
        loop.stop()


def function3(end_time, loop):
    print("function3 called")
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, function1, end_time, loop)
    else:
        loop.stop()


def function4(end_time, loop):
    print("function4 called")
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, function4, end_time, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()

end_loop = loop.time() + 9.0

loop.call_soon(function1, end_loop, loop)
# loop.call_soom(function4, end_loop, loop)
loop.run_forever()
loop.close()