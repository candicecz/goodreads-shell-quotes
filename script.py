import requests
import time
import random
from bs4 import BeautifulSoup
import re
from IPython.core.display import clear_output
from warnings import warn

# Create a text file.
f = open("quotes", "w+")


# For monitoring the loop.
start_time = time.time()
num_of_requests = 0

# Set the number of pages to crawl
min_page = 1
max_page = 20
pages = [str(i) for i in range(min_page, max_page)]

# Loop through every requested page.
for page in pages:
    # Get request
    url = 'https://www.goodreads.com/quotes/tag/'

    # Check goodreads for available genres. My interests would dictate that this field should be one of either "philosophy" or literature.
    genre = "literature"
    response = requests.get(url + genre + "?page=" + page)

    # Pause loop
    time.sleep(random.randint(8, 15))

    # Monitor requests
    num_of_requests += 1
    current_time = time.time()
    elapsed_time = current_time - start_time
    print('Request:{}; Frequency: {} requests/s'.format(num_of_requests,
                                                        num_of_requests/elapsed_time))
    clear_output(wait=True)

    # Throw a warning if request generates a non-200 status code
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(
            num_of_requests, response.status_code))

    # Break the loop if the number of requests is larger than expected
    if num_of_requests > max_page:
        warn("number of requests is greater than expected: {}".format(num_of_requests))
        break

    # Parse the html with Beautiful soup data structure and find all div tags with quoted text.
    page_html = BeautifulSoup(response.text, "html.parser")
    quotes = page_html.find_all("div", "quoteText")

    for quote in quotes:
        # Get the string and remove the quote symbols.
        q = quote.find(text=True, recursive=False).replace(
            '“', "").replace('”', "").strip()
        # Get the author of the quote.
        a = quote.find("span", "authorOrTitle").get_text().strip()
        # Get the title of the work if available
        w = ""
        work_el = quote.find('span', id=re.compile('^quote_book_link'))
        if work_el:
            w = work_el.find("a", "authorOrTitle").get_text()
        f.write(
            q                     # quote string
            + "\n\n"
            + '-- ' + a           # author name
            + " " + w             # title of work
            + "\n" + "%" + "\n")
