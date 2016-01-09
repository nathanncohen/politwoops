#!/usr/bin/env python3
from bs4 import BeautifulSoup

def get_entry(soup,txt):
    ans = min((x for x in soup.find_all('div') if txt in x.text),
                key=lambda e:len(e.text))
    return ans.find_all('strong')[0].text

# INSEE code to city name
name = {}
import csv
with open('codes_insee.txt','r') as f:
    name = dict(list(csv.reader(f,delimiter='\t'))[1:])

# Parse the web pages
data = []
import os,re
for filename in os.listdir('website/'):
    #int(filename) # should be an integer

    with open('website/'+filename,'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    if soup.text == '':
        print(filename+" skipped. Web page error"),
        continue

    maire = get_entry(soup, "Nom du Maire :")
    regexp = re.compile('^([^\xa0]*)\xa0(.*[a-zé])\xa0(.*)$',re.UNICODE)
    print(filename)
    try:
        sexe,prenom,nom = re.match(regexp,maire).groups()
    except AttributeError:
        sexe, prenom, nom = 'M.', '?','?'
    if sexe == 'Mme':
        sexe = 'F'
    elif sexe == 'M.':
        sexe = 'M'
    else:
        raise Exception(sexe)

    data.append([filename,
                 name[filename],
                 sexe,
                 nom,
                 prenom,
                 get_entry(soup, "Nombre d'habitants :"),
                 get_entry(soup, "Superficie :")])
data.sort()
data.insert(0,('CODE INSEE','VILLE','MAIRE (H/F)', 'MAIRE (NOM)', 'MAIRE (PRENOM)','NOMBRE HABITANTS','SUPERFICIE'))
#assert len(name) == len(data)

# Output
with open('maires.csv','w') as f:
    csv.writer(f,delimiter=';').writerows(data)
