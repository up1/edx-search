""" Abstract SearchEngine with factory method """
# pylint: disable=R0921
from django.conf import settings


class SearchEngine(object):
    """ Base abstract SearchEngine object """

    index_name = "courseware"

    def __init__(self, index=None):
        if index:
            self.index_name = index

    def index(self, doc_type, body, **kwargs):
        """ This operation is called to add a document of given type to the search index """
        raise NotImplementedError

    def remove(self, doc_type, doc_id, **kwargs):
        """ This operation is called to remove a document of given type from the search index """
        raise NotImplementedError

    def search(self, query_string=None, field_dictionary=None, filter_dictionary=None, **kwargs):
        """ This operation is called to search for matching documents within the search index """
        raise NotImplementedError

    def search_string(self, query_string, **kwargs):
        """ Helper function when primary search is for a query string """
        return self.search(query_string=query_string, **kwargs)

    def search_fields(self, field_dictionary, **kwargs):
        """ Helper function when primary search is for a set of matching fields """
        return self.search(field_dictionary=field_dictionary, **kwargs)

    @staticmethod
    def get_search_engine(index=None):
        """
        Returns the desired implementor (defined in settings)
        """
        search_engine_class = getattr(settings, "SEARCH_ENGINE", None)
        return search_engine_class(index=index) if search_engine_class else None
