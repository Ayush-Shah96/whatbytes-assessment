"""
Custom pagination classes for Django REST Framework.
"""

from rest_framework.pagination import PageNumberPagination


class StandardPagination(PageNumberPagination):
    """Standard pagination class."""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class LargePagination(PageNumberPagination):
    """Large pagination for bulk operations."""
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500


class SmallPagination(PageNumberPagination):
    """Small pagination for quick browsing."""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20
