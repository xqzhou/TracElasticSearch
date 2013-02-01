from datetime import datetime
from sqlite3 import connect, Row
from pyelasticsearch import ElasticSearch

es = ElasticSearch('http://localhost:9200/')
# es.search('name:joe')

conn = connect('/Users/xq/Workspace/my-trac-proj/db/trac.db')
conn.row_factory = Row

def index_wiki(r): 
	doc = {}
	doc['name'] = r['name']
	doc['comment'] = r['comment']
	doc['author'] = r['author']
	doc['text'] = r['text']
	doc['version'] = r['version']
	doc['time'] = datetime.fromtimestamp(r['time'] / 1000000)
	doc['ipnr'] = r['ipnr']
	es.index('trac', 'wiki', doc, doc['name'])

c = conn.cursor()
c.execute('select * from wiki')

rows = c.fetchmany(50)
while rows:
	for r in rows:
		index_wiki(r)
	rows = c.fetchmany(50)

c.close()
conn.close()
