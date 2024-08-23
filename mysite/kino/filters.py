from django_filters.rest_framework import FilterSet
from .models import Movie, Rating


class Moviefilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'country': ['exact'],
            'genre': ['exact'],
            'date': ['gt', 'lt'],

        }


class Ratingfilter(FilterSet):
    class Meta:
        model = Rating
        fields = {
             'stars': ['gt', 'lt']
        }


# class Ratingfilter:
#     pass