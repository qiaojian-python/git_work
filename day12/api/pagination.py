from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    # 指定每页分页的数量
    page_size = 2
    # 指定每页分页的最大数量
    max_page_size = 5
    # 指定前端修改每页分页数量的key
    page_size_query_param = "page_size"
    # 指定获取第几页
    page_query_param = "page"
    print()


# 偏移分页器
class MyLimitOffsetPagination(LimitOffsetPagination):
    # 默认获取每页的数量
    default_limit = 3
    max_limit = 5
    # 指定偏移开始的位置
    offset_query_param = "offset"
    limit_query_param = 'limit'



# 游标分页器
class MyCursorPagination(CursorPagination):
    cursor_query_param = "course"
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5
    ordering = "-price"





