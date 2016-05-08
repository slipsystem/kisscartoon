# SlipCartoon

Updates Series from Kisscartoon and Kissanime
all credits goes to wlan22 for 

#Credits

all credits go to wlan22 for making this script

[Kisscartoon](https://github.com/wlan222/kisscartoon)

Without him this would not be possible. I only added the ability to do multiple series.

# Usage

Add Series You Already Have

```./python kissgot.py <cartoon page> ```

Add New Series

``` add the link so series.txt ```

Run Updater

```./python slipcartoon.py ```

or for Windows

```Run Update.exe ```

# Python Requirements

Python :

* [cfscrape](https://github.com/Anorov/cloudflare-scrape/)
  * requests
  * PyExecJS
  * A JavaScript Engine (Like Node or PyV8)
* [BeautifulSoup4 ( bs4 )](https://pypi.python.org/pypi/beautifulsoup4)
* [pySmartDL](https://pypi.python.org/pypi/pySmartDL/)
* [pyCrypto](https://pypi.python.org/pypi/pycrypto)

All of the dependencies are available via pip and easy_install

# Install Guide

Windows :

* Install [Python 2.7](https://www.python.org/downloads/windows/)
	Add python.exe to Path
* Install [C++ Python Compiler](https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266)
* Install [PyV8](https://code.google.com/archive/p/pyv8/downloads)
* Open Command Prompt and type
	* pip install cfscrape
	* pip install BeautifulSoup4
	* pip install pySmartDL
	* pip install pyCrypto
* Edit The config.py
    * SeriesList = Path to series.txt
    * GotList = Path to got.txt
    * DownloadPath = Path to Download Folder
    * Qality =  remove space -q for higher quality
    * InstallDir = Path to this code




