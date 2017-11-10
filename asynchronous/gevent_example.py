'''
Green Threads
Green threads are a primitive level of asynchronous programming. 
A green thread looks and feels exactly like a normal thread, except that the threads are scheduled by application code 
rather than by hardware. Gevent is a well known python library for using green threads. 
Gevent is basically green threads + eventlet, a non-blocking I/O networking library. 
Gevent monkey patches common python libraries to have non-blocking I/O. 
Here is an example using gevents to make requests to multiple urls at once:

'''
import gevent.monkey

from urllib.request import urlopen

gevent.monkey.patch_all()

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']


def print_head(url):

    print('Starting {}'.format(url))

    data = urlopen(url).read()

    print('{}: {} bytes: {}'.format(url, len(data), data))

jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.wait(jobs)

'''
As you can see, the gevent API looks and feels just like threading. However under the hood, it’s using coroutine’s 
rather than actual threads, and running them on an event loop for scheduling. This means you get the benefits of 
light-weight threading without needing to understand coroutines, but you still have all the other issues that threading 
brings. Gevent is a good library for those who already understand threading and want lighter weight threads.


Event Loop? Coroutines? Woah, slow down, I’m lost…
Lets clear up some things about how asynchronous programming works. One way to do asynchronous programming is with an 
event loop. The event loop is exactly what it sounds like, there is a queue of events/jobs and a loop that just 
constantly pulls jobs off the queue and runs them. These jobs are called coroutines. They are a small set of 
instructions, including which events to put back on to the queue, if any.
'''