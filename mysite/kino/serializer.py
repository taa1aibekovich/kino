from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['nickname', 'email', 'phone', 'status']
#
#     def create(self, validated_data):
#         user = UserProfile.objects.create_user(**validated_data)
#         return user
#


#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'email', 'phone', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")


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
        fields = ['id', 'date', 'country', 'director', 'avg_rating', 'actors', 'genre', 'status', 'movie_time',
                  'description', 'movie_trailer',
                  'movie_image', 'status']

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
        fields = ['id', 'product', 'product_id' ]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_name', 'movie_name']
