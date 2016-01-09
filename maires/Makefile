all: maires.csv

clean:
	rm -f codes_insee.txt
	rm -rf website
	rm -rf website.log

codes_insee.txt:
	wget "http://www.insee.fr/fr/methodes/nomenclatures/cog/telechargement/2015/txt/comsimp2015.zip"
	#cp /tmp/comsimp2015.zip .
	unzip comsimp2015.zip
	rm comsimp2015.zip
	cat comsimp2015.txt | iconv -f ISO8859-1 -t utf8 | cut -f 4,5,12 | sed 's/\t//' > codes_insee.txt
	rm comsimp2015.txt

website.log: codes_insee.txt
	mkdir website
	./1-wget_data.sh | tee website.log

maires.csv: | website.log
	./2-scraping.py

test:
	echo "No test is implemented for this database"
	exit 1
