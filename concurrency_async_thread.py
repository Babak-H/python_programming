# we use this library instead of Requests, since that one is not optimized for asynchronous operations.
import aiohttp
import asyncio
import threading
import concurrent.futures
import requests
import time


# https://realpython.com/python-concurrency/


##### Synchronous version #####


def download_site(url, session):
    with session.get(url) as response:
        print(f"read {len(response.content)} from url")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == '__main__':
    sites = [
        "https://jython.org",
        "https://olympus.realpython.org/dice",
    ] * 10

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f" download {len(sites)} in {duration}  in synchronous mode")


##### Threading version #####

'''
local() method is the one that prevents data being shared between threads to be interrupted and 
 makes the Requests module thread-safe '''
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site_thr(url):
    '''
    each thread needs to create its own requests.Session() object
    '''
    session = get_session()
    with session.get(url) as response:
        print(f"read {len(response.content)} from url")


def download_all_sites_thr(sites):
    '''
    ThreadPoolExecutor = Thread + Pool + Executor
    Thread => the main part of multithreading, each thread is like a train of thought, working separate from others but have shared memory.
    pool => This object is going to create a pool of threads, each of which can run concurrently.
    executer => the part that’s going to control how and when each of the threads in the pool will run.

    number of threads to create is not fixed, play with it to find the best number.
    '''
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site_thr, sites)


if __name__ == '__main__':
    sites = [
        "https://jython.org",
        "https://olympus.realpython.org/dice",
    ] * 10

    start_time = time.time()
    download_all_sites_thr(sites)
    duration = time.time() - start_time
    print(f" download {len(sites)} in {duration} in threaded mode")


##### AsyncIO version #####


async def download_site_io(session, url):
    '''
    When your code awaits a function call, it’s a signal that the call is likely to be something that takes a while and that the task should give up control.
    when  using 'async' as context manager, await can be omitted
    '''
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites_io(sites):
    async with aiohttp.ClientSession() as session:
        # tasks never give up control without intentionally doing so. They never get interrupted in the middle of an operation.  => code is thread-safe by default
        tasks = []
        for url in sites:
            # 'ensure_future' takes care of starting the tasks
            task = asyncio.ensure_future(download_site_io(session, url))
            tasks.append(task)
        # 'await' is the magic that allows the task to hand control back to the event loop.
        # 'gather' keep the session context alive until all of the tasks have completed.
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    sites = [
        "https://jython.org",
        "https://olympus.realpython.org/dice",
    ] * 10

    start_time = time.time()
    '''
    The general concept of asyncio is that a single Python object, called the event loop, controls how and when each task gets run. The event loop is aware of each task and knows what state it’s in
    '''
    asyncio.get_event_loop().run_until_complete(download_all_sites_io(sites))
    duration = time.time() - start_time
    print(f" download {len(sites)} in {duration} in threaded mode")
