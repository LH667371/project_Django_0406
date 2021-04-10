from rest_framework.pagination import CursorPagination, PageNumberPagination, LimitOffsetPagination


# 游标分页器 (加密)
class MyCursorPagination(CursorPagination):
    cursor_query_param = "cursor"
    page_size = 3
    max_page_size = 5
    page_size_query_param = "page_size"
    # 使用时需要指定排序规则
    ordering = "id"

# 基础分页器
class MyPageNumberPagination(PageNumberPagination):
    # 指定分页分页的数量
    page_size = 5
    # 指定每页可以展示的最大数量
    max_page_size = 5
    # 指定前端修改每个分页数量的key
    page_size_query_param = "page_size"
    # 指定获取第几页的对象
    page_query_param = 'page'

class MyLimitOffsetPagination(LimitOffsetPagination):
    # 执行获取每页数量
    default_limit = 5
    # 指定前端修改获取每页数量的key
    limit_query_param = "limit"
    # 前端指定偏移的数量的key
    offset_query_param = "offset"
    # 指定每页获取的最大对象个数
    max_limit = 5