object = presidents
all: $(object).csv

$(object).csv:
	./$(object)_to_csv.py $(object).csv

clean:
	rm -f $(object).csv
	rm -f $(object)_tmp.csv

test: $(object).csv
	rm -f $(object)_tmp.csv
	./$(object)_to_csv.py $(object)_tmp.csv
	diff $(object).csv $(object)_tmp.csv
	rm $(object)_tmp.csv
