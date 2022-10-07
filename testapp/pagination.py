from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
class Mypagenation(PageNumberPagination):
    page_size=10
    page_query_param='mypage'
    page_query_description='num'
    max_page_size=10
    last_page_strings=('endpage',)
    
class pagination2(LimitOffsetPagination):
    default_limit=15 
    limit_query_param='mylimit'
    offset_query_param='myoffset'
    max_limit=20
    
class Mypagination3(CursorPagination):
    ordering='-esal'
    page_size=5