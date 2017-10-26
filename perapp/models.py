from django.db import models

# Create your models here.


class OlineNote(models.Model):
    headline = models.CharField(max_length=200)
    textdata = models.DateTimeField()
    author = models.CharField(max_length=50)
    mainbody = models.TextField()

    def __str__(self):
        return self.headline


class OlineProject(models.Model):
    headline = models.CharField(max_length=200)
    textdata = models.DateTimeField()
    author = models.CharField(max_length=50)
    projectabstract = models.TextField()
    projectweb = models.TextField()


class PersonalAbstract(models.Model):
    Pername = models.CharField(max_length=50)
    Perabstract = models.TextField()

    def __str__(self):
        return self.Pername
