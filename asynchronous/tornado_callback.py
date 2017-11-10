'''
Callback Style Async
While many asynchronous libraries exist in Python, the most popular ones are probably Tornado and gevent. 
As we have already talked about gevent, lets focus a little on how Tornado works. Tornado is an asynchronous 
web framework that uses the callback style to do asynchronous network I/O. A callback is a function, and it means 
“Once this is done, execute this function”. It’s basically a “when done” hook for your code. In other words a callback 
is like when you call a customer service line, and immediately leave your number and hang up, so they can call you back 
when they are available, rather than having to wait on hold forever.

Let’s take a look at how to do the same thing as above using tornado.
'''

import tornado.ioloop

from tornado.httpclient import AsyncHTTPClient

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']


def handle_response(response):
    if response.error:

        print("Error:", response.error)

    else:

        url = response.request.url

        data = response.body

        print('{}: {} bytes: {}'.format(url, len(data), data))


http_client = AsyncHTTPClient()

for url in urls:
    http_client.fetch(url, handle_response)

tornado.ioloop.IOLoop.instance().start()

'''
To explain the code a little, the very last line is calling a tornado method called AsyncHTTPClient.fetch which fetches 
a url in a non-blocking way. This method essentially executes and returns immediately allowing the program to do other 
things, while waiting on the network call. Because the next line is reached before the url has been hit, it is not 
possible to get a return object from the method. The solution to this problem is that instead of the fetch method 
returning an object, it calls a function with the result, or a callback. 
The callback in this example is handle_response.

'''