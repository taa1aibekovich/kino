from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField


class UserProfile(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()
    STATUS_CHOICES = (
        ('Pro', 'Pro'),
        ('Simple', 'Simple'),
    )

    def __str__(self):
        return self.nickname


class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    director_image = models.ImageField(upload_to='directors/', null=True, blank=True)

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    actor_image = models.ImageField(upload_to='actors/', null=True, blank=True)

    def __str__(self):
        return self.actor_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('144', '144'),
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080', '1080'),
        ('1080 Ultra', '1080 Ultra'),
    )
    movie_time = models.IntegerField()
    description = models.TextField()
    movie_trailer = models.URLField(null=True, blank=True)
    movie_image = models.ImageField(upload_to='movies/', null=True, blank=True)
    STATUS_CHOICES = (
        ('pro', 'pro'),
        ('Simple', 'Simple'),
    )

    def __str__(self):
        return self.movie_name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])

    def __str__(self):
        return f'{self.user} - {self.movie} - {self.stars}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.user} - {self.movie}'


class Cart(models. Model):
    user = models. OneToOneField(UserProfile, on_delete=models. CASCADE, related_name='cart')
    created_date = models. DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class CarItem(models. Model):
    cart = models. ForeignKey(Cart, related_name='items', on_delete=models. CASCADE)
    product = models. ForeignKey(Movie, on_delete=models. CASCADE)

    def __str__(self):
        return f'{self.product} -{self.cart}'

