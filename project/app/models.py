from django.db import models


class Contactus(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    comments = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name


class Feedback(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    comments = models.TextField(max_length=500)

    def __str__(self):
        return self.username


class UrlDatabase(models.Model):
    user = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    status = models.IntegerField()

    def __str__(self):
        return f"{self.user}---{self.link}---{self.status}"
