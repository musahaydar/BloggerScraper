# Blogger Scraper

- Install Python libraries with `pip install -r requirements.txt`
- Install [wkhtmltopdf](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf)
- Run with `./scraper.py`

## How it Works

- Provide the URL to the latest post page when prompted
- The script scrapes the webpage to find the next URL, a link in an HTML element with the class `.blog-pager-older-link`. If your target blog has the link to the next blog post in a different HTML class, make the necessary change in the `scrapePage` function.
- The `pyppeteer` library is used to download the webpage via a headless browser (credit for the `generate_pdf` function to [Manoj Ahirwar](https://apitemplate.io/blog/how-to-convert-html-to-pdf-using-python/))
- The script will loop, downloading each page until no more previous posts are found
