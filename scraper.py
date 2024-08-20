#! /usr/bin/env python3
import re
import asyncio
from requests_html import HTMLSession
from pyppeteer import launch
from pathlib import Path

async def scrapePage(url):
    session = HTMLSession()
    browser = await launch()
    page = await browser.newPage()

    res = session.get(url)
    while res:
        filename = re.match(".+(\/[^.]+).html$", url)
        print(url)

        # get page as html
        await page.goto(url)
        await page.pdf({'path': "output/" + filename.group(1) + ".pdf", 'format': 'A4'})

        # get the next post
        next = res.html.find('.blog-pager-older-link', first=True)
        if next:
            url = next.attrs["href"]
            res = session.get(url)
        else:
            res = None
    
    await browser.close()    


def main():
    url = input("Enter the URL of the latest post: ")
    # create output dir
    Path("output").mkdir(exist_ok=True)
    asyncio.get_event_loop().run_until_complete(scrapePage(url))

main()
