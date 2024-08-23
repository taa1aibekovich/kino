from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    genre = GenreSerializer()
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'movie_image', 'avg_rating', 'date', 'country', 'genre']

    def get_avg_rating(self, obj):
        ratings = Rating.objects.filter(movie=obj)
        if ratings.exists():
            return ratings.aggregate(avg_rating=models.Avg('stars'))['avg_rating']
        return None


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    movie = MovieSerializer()

    class Meta:
        model = Rating
        fields = ['id', 'user', 'movie', 'stars']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    movie = MovieSerializer()
    parent = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = MovieSerializer(read_only=True)
    product_id = serializers. PrimaryKeyRelatedField(queryset=Movie. objects.all(), write_only=True, source='product')

    class Meta:
        model = CarItem
        fields = ['id', 'product', 'product_id',]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']

