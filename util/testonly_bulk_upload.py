import csv
from elasticsearch import helpers, Elasticsearch

def csv_reader(file_name, index_name):
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    with open(file_name, 'r') as outfile:
        reader = csv.DictReader(outfile)
        helpers.bulk(es, reader, index=index_name, doc_type="type")

csv_reader('crashes.csv', 'nypd_crashes')