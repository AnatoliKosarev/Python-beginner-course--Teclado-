import aiohttp
import asyncio
import time


async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:  # stops and gives back control to main thread when waits for session connection and another task can be started
        async with session.get(url) as response:  # stops and gives back control to main thread when waits for url connection and another task can be started / continued
            print(f"Page took {time.time() - page_start}")
            return response.status


loop = asyncio.get_event_loop()

tasks = [fetch_page("http://google.com") for _ in range(10)]

start = time.time()
statuses = loop.run_until_complete(asyncio.gather(*tasks))  # all tasks are unpacked from tasks list into loop and are run one by one
print(f"All took {time.time() - start}")
print(statuses)
