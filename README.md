# Kisscartoon and Kissanime Batch Downloader

Get's and downloads Videos from Kisscartoon and Kissanime

# Changelog

* Fixed Link Decryption
* Rewrote Core


# Usage


```./python kissgrab.py <cartoon page> ```

If you want extra Information add -v or --verbose

```./python kisscartoon.py -v <cartoon page> ```

If you want to handle the downloading yourself use --only-links or -l to just print the links

```./python kisscartoon.py -l <cartoon page> ```

If you want the links written to a File use --save-links or -s to save them to links.txt

```./python kisscartoon.py -s <cartoon page> ```

If you want the links as a HTML List use --html or -d to save them to download.html

```./python kisscartoon.py -s <cartoon page> ```

If you don't want the highest quality ( it's the default setting ) you can add -q or --low-quality to get the lowest available quality

```./python kisscartoon.py -q <cartoon page> ```


Those Operators are freely combinable


```./python kisscartoon.py -q -s http://kisscartoon.me/Cartoon/Aqua-Teen-Hunger-Force-Season-10```

# Requirements

Python :

* [cfscrape](https://github.com/Anorov/cloudflare-scrape/)
  * requests
  * PyExecJS
  * A JavaScript Engine (Like Node or PyV8)
* [BeautifulSoup4 ( bs4 )](https://pypi.python.org/pypi/beautifulsoup4)
* [pySmartDL](https://pypi.python.org/pypi/pySmartDL/)
* [pyCrypto](https://pypi.python.org/pypi/pycrypto)

All of the dependencies are available via pip and easy_install


 


