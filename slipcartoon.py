import subprocess
for line in open('series.txt'):
    subprocess.call(" python kissgrab.py -q " + line, shell=True)