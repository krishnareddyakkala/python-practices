'''
Up until python 3.3 this really was the best you could do. In order to do better you need more language support. 
In order to do better, Python would need some way to execute a method partially, halting execution, and maintain stack 
objects and exceptions throughout. If you’re familiar with Python concepts, you might realize I am hinting at 
Generators. Generators allow a functions to return a list, one item at a time, halting execution until the next item is 
needed. The problem with generators is that they must be completely consumed by the function calling it. In other words,
 a generator can not call a generator, halting execution of both. That is however until PEP 380 added the yield from 
 syntax that allows a generator to yield the result of another generator. While async isn’t really the intention of 
 generators, it provides all the features needed to make async great. Generators maintain a stack and can raise 
 exceptions. If you were to write an event loop that ran generators, you could have a great async library. 
 And thus, the asyncio library was born. All you have to do is add a @coroutine decorator and asyncio will patch your 
 generator into a coroutine. Here is an example of us calling the same three urls as before.
'''
import asyncio

import aiohttp



urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']



@asyncio.coroutine

def call_url(url):

    print('Starting {}'.format(url))

    response = yield from aiohttp.get(url)

    data = yield from response.text()

    print('{}: {} bytes: {}'.format(url, len(data), data))

    return data



futures = [call_url(url) for url in urls]



loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(futures))


'''
Async and Await
The asyncio library was gaining a lot of traction, so Python decided to make it a core library. 
With the introduction of the core library, they also added the keywords async and await in Python 3.5. 
The keywords are designed to make it more clear your code is asynchronous; so your methods are not confused with 
generators. The async keyword goes before def to show that a method is asynchronous. 
The await keyword replaces yield from and makes it more clear that you are waiting for a coroutine to finish. 
Here is our example again but with the async/await keywords.

'''

import asyncio

import aiohttp



urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']



async def call_url(url):

    print('Starting {}'.format(url))

    response = await aiohttp.get(url)

    data = await response.text()

    print('{}: {} bytes: {}'.format(url, len(data), data))

    return data



futures = [call_url(url) for url in urls]



loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(futures))

'''
Basically what is happening here is an async method, when executed, returns a coroutine which can then be awaited.
'''