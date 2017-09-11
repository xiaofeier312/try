import asyncio
import time
import requests
import aiohttp

urllist = ['https://www.baidu.com', 'https://www.elong.com', 'https://www.sina.com', 'http://www.126.com']
urllist.reverse()


async def aio_req(url):
    print('Starting req_async, url is: {}'.format(url))
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as respsone:
            print('--Current time: {}'.format(time.time() - start))
            # print('Get requests results, r.body: {}'.format(respsone.status))
            await respsone.text()
            print('~~Get result!, Current url: {}'.format(url))
            # print('Current time: {}'.format(time.time() - start))


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(aio_req(i)) for i in (urllist * 25)
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    print('End all at {}'.format(time.time() - start))
