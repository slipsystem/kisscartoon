import subprocess
import time
import os
import config

SeriesList = config.SeriesList
Qality = config.Qality

if os.path.exists(SeriesList):
    f = file(SeriesList, "r+")
else:
    f = file(SeriesList, "w")

for line in open(SeriesList):
    print 'checking for updates on ' + line
    subprocess.call(" python kissgrab.py" + Qality + line, shell=True)
    time.sleep(5)