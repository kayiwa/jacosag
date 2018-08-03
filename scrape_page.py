"""Create CSVs from all tables on a Wikipedia article."""

import csv
import os
import platform

from bs4 import BeautifulSoup
import requests

def scrape(url, output_name):
    """Create CSVs from all tables in a Wikipedia article.

    ARGS:
        url (str): The full URL of the Wikipedia article to scrape tables from.
        output_name (str): The base file name (without filepath) to write to.
    """

    # Read pages from Wikipedia article into list of HTML strings
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data)
    title_tag = soup.find('h1')
    title_box = head_tag.text.strip()
    summary_tag = soup.find('p').[0]
    summary_box = summary_tag.text.strip()
    opinion_tag = opinion_tag = soup.find_all('p')[1]
    opinion_box = opinion_tag.text.strip()
    seealso_tag = opinion_tag = soup.find_all('li')[0]
    seealso_box = seealso_tag.text.strip()

    # Create a directory for output if it doesn't exist
    try:
        os.mkdir(output_name)
    except Exception:
        pass

    for index, table in enumerate(wikitables):
        # Make a unique file name for each CSV
        if index == 0:
            filename = output_name
        else:
            filename = output_name + '_' + str(index)

        filepath = os.path.join(output_name, filename) + '.csv'

        with open(filepath, mode='w', newline='', encoding='utf-8') as output:
            # Deal with Microsoft Windows inserting an extra '\r' in line terminators
            if platform.system() == 'Windows':
                kwargs = {'lineterminator': '\n'}

                csv_writer = csv.writer(output,
                                        quoting=csv.QUOTE_ALL,
                                        **kwargs)
            else:
                csv_writer = csv.writer(output,
                                        quoting=csv.QUOTE_ALL)

            write_html_table_to_csv(table, csv_writer)


def write_html_table_to_csv(table, writer):
    """Write HTML table from Wikipedia to a CSV file.

    ARGS:
        table (bs4.Tag): The bs4 Tag object being analyzed.
        writer (csv.writer): The csv Writer object creating the output.
    """

    # Hold elements that span multiple rows in a list of
    # dictionaries that track 'rows_left' and 'value'
