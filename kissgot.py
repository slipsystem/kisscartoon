import argparse
import logging
import os
import time
import config

import cfscrape
from pySmartDL import SmartDL
import urllib2

from shows import *

logging.basicConfig(level=logging.ERROR, format='[%(levelname)s] : %(message)s')

SeriesList = config.SeriesList
GotList = config.GotList
DownloadPath = config.DownloadPath

if os.path.exists(SeriesList):
    f = file(SeriesList, "r+")
else:
    f = file(SeriesList, "w")
	
if os.path.exists(GotList):
    f = file(GotList, "r+")
else:
    f = file(GotList, "w")


parser = argparse.ArgumentParser()
parser.add_argument("show")
parser.add_argument("-l", "--only-links", help="only print's the links. doesn't download the files.",
                    action="store_true")
parser.add_argument("-s", "--save-links", help="saves the links to links.txt", action="store_true")
parser.add_argument("-q", "--low-quality", help="reduces the quality", action="store_true")
parser.add_argument("-d", "--html", help="outputs a link list to download.html", action="store_true")
parser.add_argument("-v", "--verbose", help="make kissgrab tell you what it's doing", action="store_true")
args = parser.parse_args()

if args.verbose:
    logging.getLogger().setLevel(logging.INFO)

sfileopen = open(SeriesList,'r+' )
splines = sfileopen.read()
sfile = open(SeriesList,'w' )
sfile.write(splines + args.show + '\n')
	
scraper = cfscrape.create_scraper()
for show in Show.__subclasses__():
    showinstance = show(None, args.show)
    if showinstance.is_valid():
        showinstance.get_episodes(scraper)
        logging.info('Show : {show}'.format(show=showinstance.show))
        for episode in showinstance.episodes:
            linksopen = open(GotList,'r+' )
            linksread = linksopen.read()
            if episode.source not in linksread:
                fileopen = open(GotList,'r+' )
                plines = fileopen.read()
                file = open(GotList,'w' )
                file.write(plines + episode.source + '\n')
