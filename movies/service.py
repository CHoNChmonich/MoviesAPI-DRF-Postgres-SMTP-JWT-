from django_filters import rest_framework
from .models import Movie
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginationMovies(PageNumberPagination):
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

def get_client_ip(self, request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class CharFilterInFilter(rest_framework.BaseInFilter, rest_framework.CharFilter):
    pass

class MovieFilter(rest_framework.FilterSet):

    genres = CharFilterInFilter(field_name='genres__name', lookup_expr='in')
    year = rest_framework.RangeFilter()

    class Meta:
        model = Movie
        fields = ("genres", "year")


