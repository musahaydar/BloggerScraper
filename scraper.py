#! /usr/bin/env python3
import re
import asyncio
from requests_html import HTMLSession
from pyppeteer import launch
from pathlib import Path

def scrapePage(url):
    session = HTMLSession()
    res = session.get(url)
    while res:
        filename = re.match(".+(\/[^.]+).html$", url)
        asyncio.get_event_loop().run_until_complete(generatePDF(url, "output/" + filename.group(1) + ".pdf"))
        print(url)
        # get the next post
        next = res.html.find('.blog-pager-older-link', first=True)
        if next:
            url = next.attrs["href"]
            res = session.get(url)
        else:
            res = None

async def generatePDF(url, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    await browser.close()

def main():
    url = input("Enter the URL of the latest post: ")

    # create output dir
    Path("output").mkdir(exist_ok=True)

    scrapePage(url)

main()
