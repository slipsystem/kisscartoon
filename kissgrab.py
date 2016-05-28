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

def download(url, name, quiet=False):
    SeriesName = showinstance.show
    path = "%s%s" % (os.sep, name)
    pathc = path.replace("?", "")
    patha = pathc.replace(":", "")
    pathb = DownloadPath + os.sep + SeriesName.replace("-", " ") + patha.replace("!", "")
    EpisodeName = "%s%s" % (os.sep, name)
    linksopen = open(GotList,'r+' )
    linksread = linksopen.read()
    time.sleep(5)
    if EpisodeName not in linksread: 
        obj = SmartDL(url, pathb)
        try:
            obj.start()
            fileopen = open(GotList,'r+' )
            plines = fileopen.read()
            file = open(GotList,'w' )
            file.write(plines + episode.source + '\n')
        except KeyboardInterrupt:
            obj.stop()

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
                episode.get_links(scraper)
                if args.only_links:
                    if args.low_quality:
                        print episode.links[-1].link
                    else:
                        print episode.links[0].link
                elif not args.save_links and not args.html:
                    logging.info('Downloading : {file}'.format(file=episode.title))
                    if args.low_quality:
                        download(episode.links[-1].link, '{title}.mp4'.format(title=episode.title))
                    else:
                        download(episode.links[0].link, '{title}.mp4'.format(title=episode.title))
            if args.save_links:
                with open('links.txt', 'w') as linkfile:
                    for episode in showinstance.episodes:
                        if args.low_quality:
                            linkfile.write(episode.links[-1].link)
                        else:
                            linkfile.write(episode.links[0].link)
                        linkfile.write('\n')
                logging.info('Saved links to links.txt')
            if args.html:
                with open('download.html', 'w') as linkfile:
                    linkfile.write('<html><head><title>{show}</title></head><body>'.format(show=showinstance.show))
                    for episode in showinstance.episodes:
                        if args.low_quality:
                            link = episode.links[-1].link
                        else:
                            link = episode.links[0].link
                            req = urllib2.Request(link)
                        res = urllib2.urlopen(req)
                        finalurl = res.geturl()
                        linkfile.write(
                            '<a href="{link}" download="{file}">{title}</a>'.format(link=finalurl,
                                                                                file=episode.title.replace(" ", ""),
                                                                                title=episode.title))
                        linkfile.write('<br>')
                    linkfile.write('</body></html>')
                logging.info('Saved links to download.html')
