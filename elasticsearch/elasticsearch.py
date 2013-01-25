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
        result = self.es.search(criteria['q'])
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
