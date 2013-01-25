from sqlite3 import connect, Row
from pyelasticsearch import ElasticSearch

es = ElasticSearch('http://localhost:9200/')
# es.search('name:joe')

conn = connect('/Users/xq/Workspace/my-trac-proj/db/trac.db')
conn.row_factory = Row
c = conn.cursor()
c.execute('select * from wiki limit 1')
r = c.fetchone()
conn.close()


# doc = dict(zip(r.keys(), r))
# es.index('trac', 'wiki', doc)

