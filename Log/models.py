from django.db import models
from django.utils import timezone


# Create your models here.

def image_PATH(instance, filename):
    file_name = 'Database/Art/{0}'.format(filename)

class Post(models.Model):
    post_author = models.CharField(max_length=100)
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_date = models.DateField()
    post_label = models.CharField(max_length=100)

class Arts(models.Model):
    arts_author = models.CharField(max_length=100)
    arts_title = models.CharField(max_length=50)
    arts_description = models.TextField()
    arts_date = models.DateField()
    arts_image = models.ImageField(upload_to=image_PATH)

class Novels(models.Model):
    novel_title = models.CharField(max_length=100)
    novel_sinopsis = models.TextField()
    novel_date = models.DateField()
    novel_chapter = models.ForeignKey()

class Novel_Chapter(models.Model):
    chapter_number = models.IntegerField()
    chapter_title = models.CharField(max_length=100)
    chapter_of_novel = models.ForeignKey(Novels)
    chapter_content = models.TextField()
    chapter_date_create = models.DateField()

class Books (models.Model):
    books_number = models.CharField(max_length=3)
    books_sinopsis = models.TextField()
    books_author = models.CharField(max_length=100)
    books_review_characterization = models.TextField()
    books_review_setting = models.TextField()
    books_review_plot = models.TextField()
    books_review_interface = models.TextField()
    books_review_conflict = models.TextField()
    books_rate = models.IntegerField(max(10))