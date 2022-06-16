from django.core.paginator import Paginator, Page
from django.db.models import QuerySet


def get_paginator_if_page_correct(items_: QuerySet, per_page: int, page: int) -> Page | None:
    paginator = Paginator(items_, per_page)
    if paginator.num_pages >= page > 0:
        paginator_obj = paginator.get_page(page)
        return paginator_obj


def get_paginator(items_: QuerySet, per_page: int, page: int) -> Page:
    paginator = Paginator(items_, per_page)
    paginator_obj = paginator.get_page(page)
    return paginator_obj
