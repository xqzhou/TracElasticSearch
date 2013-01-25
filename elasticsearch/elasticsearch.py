from trac.core import *
from trac.util.html import html
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor
from tracadvsearch import IAdvSearchBackend

class ElasticSearchPlugin(Component):
    implements(IAdvSearchBackend)

    def get_name(self):
        return self.__class__.__name__

    def get_sources(self):
        return ('wiki', 'ticket')

    def upsert_document(self, doc):
        pass

    def delete_document(self, identifier):
        pass

    def query_backend(self, criteria):
        return (
            200, 
            [
                {
                    'title': 'TracHelp', 
                    'score': 0.876, 
                    'source': 'wiki', 
                    'summary': '==Trac Help== ....',
                    'date': '2011-02-34 23:34',
                    'author': 'admin',
                }
            ]
        )
