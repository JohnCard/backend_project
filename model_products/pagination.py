from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class ProductPageNumberPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 5
    last_page_strings = 'end'
    
class ProductLimitOffPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 7
    limit_query_param = 'records'
    offset_query_param = 'start'
    
class ProductCursorPagination(CursorPagination):
    page_size = 3
    cursor_query_param = 'page_index'
    ordering = 'user'
    max_page_size = 5
    cursor_query_description = 'Were listening all items'
    invalid_cursor_message = 'The provided cursor is invalid or does not exist.'
    page_size_query_description = 'Number of results'
    