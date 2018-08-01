# supreme court decision scraper

Scrape all the tables from a Wikipedia article into a folder of CSV files (only
tested on Supreme Court ones)

## Status of this Repo

### Components

- [x] write a test scraper to see if possible
- [ ] scrape all the [term
  opinions](https://en.wikipedia.org/wiki/Lists_of_United_States_Supreme_Court_cases)
- [ ] limit the justices votes
- [ ] scrape individual cases
- [ ] scrape page information from each case (this will vary)
- [ ] Convert this repo into a [Jupyter Notebook](http://jupyter.org)

## Installation

This will be a [Python 3.7][python] module that depends on the [Beautiful Soup][beautiful-soup] and [requests][requests] packages.

1. Clone and `cd` into this repo.
2. Install [Python 3.7][python].
3. Install requirements from pip with `pip install -r requirements.txt`.
4. If on Windows, download the  `.whl` for the [`lxml`][lxml] parser and install it locally.

## Usage

Just import the module and call the `scrape` function. Pass it the full URL of a Wikipedia article, and a simple string (no special characters or filetypes) for the output name. The output will all be written to the `output_name` folder, with files named `output_name.csv`, `output_name_1.csv`, etc.

```python
import test_scrape

test_scrape.scrape(
    url="https://en.wikipedia.org/wiki/2000_term_opinions_of_the_Supreme_Court_of_the_United_States"
    output_name="2000_term"
)
```

Inspecting the output with Bash gives the following results:

```text
$ ls 2000_term/
2000_term.csv   2000_term1.csv

$ cat 2000_term/2000_term.csv
"#","Case name and citation","Argued","Decided","Rehnquist","Stevens","O'Connor","Scalia","Kennedy","Souter","Thomas","Ginsburg","Breyer"
"1","Artuz v. Bennett, 531 U.S. 4","October 10, 2000","November 7, 2000","","","","","","","","","","","","","","","","","",""
"","","","","","","","","","","","",""
"","","","","","","","","","","","",""
"","","","","","","","","","","","",""
"","","","","","","","","","","","",""
"","","","","","","","","","","","",""
"","","","","","","","","","","","",""
"","","","","","","","","","","","",""
"","","","","","","","","","","","",""
"","","","","","","","","","","","",""
"2","Cleveland v. United States, 531 U.S. 12","October 10, 2000","November 7, 2000","","","","","","","","","","","","","","","","","",""
```

## Disclaimer

This can always be cleaner. This can easily be generalized but will be very
utilitarian (by design) 

[beautiful-soup]: https://www.crummy.com/software/BeautifulSoup/
[blog-post]: https://roche.io/2016/05/08/scrape-wikipedia-with-python
[lxml]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
[python]: https://www.python.org/downloads/
[requests]: http://docs.python-requests.org/en/master/
