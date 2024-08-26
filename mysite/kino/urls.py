from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_detail'),

    path('country', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country_list'),
    path('country<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_detail'),

    path('director/', DirectorViewSet.as_view({'get': 'list', 'post': 'create'}), name='director_list'),
    path('director/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='director_detail'),

    path('actor/', ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
    path('actor/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='actor_detail'),

    path('genre/', GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='genre_list'),
    path('genre/<int:pk>/', GenreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='genre_detail'),

    path('', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='movie_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),

    path('comment/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment_detail'),

    path('cart/', CartViewSet.as_view({'get': 'retrieve'}), name='cart_detail'),

    path('cart_items/', CarItemViewSet.as_view({'get': 'List', 'post': 'create'}), name='car_item_list'),
    path('cart_items/<int:pk>/', CarItemViewSet.as_view({'put': 'update', 'delete': 'destroy'}))

]
