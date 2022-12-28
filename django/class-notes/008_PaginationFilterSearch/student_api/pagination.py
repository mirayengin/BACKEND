from rest_framework.pagination import  ( 
  PageNumberPagination,
  LimitOffsetPagination,
  CursorPagination
  
  )

class CustomPageNumberPagination(PageNumberPagination):
  page_size = 5
  page_query_param = 'sayfa'  # browser adresinda safya yazdı 
class CustomLimitOffsetPagination(LimitOffsetPagination):
  default_limit = 10
  page_query_param = 'adet'  # browser adresinda adet yazdı 
  offset_query_param ='baslangic'
class CustomCursorPagination(CursorPagination):
  cursor_query_param = 'imlec'  # browser adresinda adet yazdı 
  page_size = 5
  ordering ='_id'




