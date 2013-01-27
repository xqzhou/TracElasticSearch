from trac.core import *
from trac.util.html import html
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor
from tracadvsearch import IAdvSearchBackend
from pyelasticsearch import ElasticSearch

class ElasticSearchPlugin(Component):
    implements(IAdvSearchBackend)


    def __init__(self):
        self.es = ElasticSearch('http://localhost:9200/')

    def get_name(self):
        return self.__class__.__name__

    def get_sources(self):
        return ('wiki', 'ticket')

    def upsert_document(self, doc):
        pass

    def delete_document(self, identifier):
        pass

    def query_backend(self, criteria):
        q_parts = []
        if criteria['q']:
            q_parts.append(criteria['q']) 

        q_author = ' OR '.join([f for f in criteria['author'] if f])
        if q_author:
            q_parts.append('author:(%s)' % q_author)

        q = ' AND '.join(q_parts)
        print('==================================')
        print(q)
        print('==================================')

        result = self.es.search(q)

        hits = result['hits']
        docs = []
        for hit in hits['hits']:
            doc = {
                'title': hit['_source']['name'],
                'summary': hit['_source']['text'],
                'score': hit['_score'],
                'source': 'wiki'
            }
            docs.append(doc)

        return (hits['total'], docs)
