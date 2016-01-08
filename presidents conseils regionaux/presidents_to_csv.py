#!/usr/bin/python3

# Liste des presidents de conseils regionaux:
#
# http://fr.wikipedia.org/wiki/Liste_des_pr%C3%A9sidents_des_conseils_r%C3%A9gionaux_en_France
#
# (requires beautifulsoup4 + urllib)

# Input Parsing
import argparse
parser = argparse.ArgumentParser(description='Construit la liste des presidents de conseils regionaux')
parser.add_argument('filename', help="the output .csv file", type=argparse.FileType('w'))
args = parser.parse_args()

# Wikipedia parsing
import urllib
from bs4 import BeautifulSoup

page = urllib.request.urlopen('http://fr.wikipedia.org/wiki/Liste_des_pr%C3%A9sidents_des_conseils_r%C3%A9gionaux_en_France').read()
soup = BeautifulSoup(page, 'html.parser')

table = soup.find_all('table')[1]

presidents = []
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    for i in range(len(cells)-1):
        if cells[i+1].find_all('img'): # The cell right before the picture
            if i>0:
                region = cells[0].text
            presidents.append((region,cells[i].find_all('a')[0].text))

# Output
import csv
presidents.sort()
csv.writer(args.filename,delimiter=';').writerows(presidents)
