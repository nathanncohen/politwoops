#!/usr/bin/python3

# Liste des Ministres:
#
# https://fr.wikipedia.org/wiki/France#Le_gouvernement
#
# (requires beautifulsoup4 + urllib)

# Input Parsing
import argparse
parser = argparse.ArgumentParser(description='Construit la liste des ministres')
parser.add_argument('filename', help="the output .csv file", type=argparse.FileType('w'))
args = parser.parse_args()

# Wikipedia parsing
import urllib

from bs4 import BeautifulSoup

page = urllib.request.urlopen('https://fr.wikipedia.org/wiki/France').read()
soup = BeautifulSoup(page, 'html.parser')

def find_table(soup):
    for table in soup.find_all('table'):
        th = table.find_all('tr')[0].find_all('th')
        th = [x.text for x in th]
        if (len(th) == 2 and
            'Les Minist' in th[0] and
            'Les ministres' == th[1]):
            return table

table = find_table(soup)
if table is None:
    raise RuntimeError("Table of ministries and ministers not found")

ministers = []
for row in table.find_all('tr')[1:]:
    ministry  = row.find_all('th')[0].text.replace('\n',' ')
    minister = row.find_all('td')[0].text
    ministers.append([ministry,minister])

# Output
import csv
ministers.sort()
csv.writer(args.filename,delimiter=';').writerows(ministers)
