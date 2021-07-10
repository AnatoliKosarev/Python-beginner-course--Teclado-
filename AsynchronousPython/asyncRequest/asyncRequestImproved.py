import aiohttp
import asyncio
import async_timeout
import time

"""
Earlier we where creating session pool with aiohttp.ClientSession() fro each task
Now will change it so that on session pool will be used for all tasks
"""


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):  # in case server takes more than 10 seconds to respond - terminate the program and treat it as an error
        async with session.get(url) as response:  # stops and gives back control to main thread when waits for url connection and another task can be started / continued
            print(f"Page took {time.time() - page_start}")
            return response.status


async def get_multiple_pages(loop, urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:  # stops and gives back control to main thread when waits for session connection and another task can be started
        for url in urls:
            tasks.append(fetch_page(session, url))  # adding created coroutines to task list
        grouped_tasks = asyncio.gather(*tasks)  # groups the tasks together into one, but it doesn't wait for it to finish
        return await grouped_tasks  # awaits until all tasks are complete

loop = asyncio.get_event_loop()

urls = ["http://google.com" for _ in range(50)]

start = time.time()
loop.run_until_complete(get_multiple_pages(loop, urls))
print(f"All took {time.time() - start}")