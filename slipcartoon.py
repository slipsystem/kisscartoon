import subprocess
import time

for line in open('series.txt'):
    subprocess.call(" python kissgrab.py -q " + line, shell=True)
    time.sleep(10)