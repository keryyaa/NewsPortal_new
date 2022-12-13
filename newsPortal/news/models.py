from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posRat = self.post_set.aggregate(posRat=Sum('rating'))
        pRat = 0
        pRat += posRat.get('rating')

        comRat = self.comment_set.aggregate(comRat=Sum('rating'))
        comR = 0
        comR += comRat.get('comRat')

        self.rating = pRat + comR
        self.save()

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.name}'



class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    ]
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=NEWS)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.title} {self.text}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
