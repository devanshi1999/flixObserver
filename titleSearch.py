import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def search(title, year):
	with codecs.open('data.tsv','r', encoding='utf-8') as tsvfile:
	  reader = csv.reader(tsvfile, delimiter='\t')
	  for row in reader:
	    if row[2].lower()==title.lower() or row[3].lower()==title.lower():
	    	if row[5]==year:
	    		return row