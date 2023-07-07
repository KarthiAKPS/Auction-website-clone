from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.category

class listing(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name="type")
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    posted_user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class bid(models.Model):
    item = models.ForeignKey(listing, related_name="item", on_delete=models.CASCADE, null=True)
    cur = models.IntegerField(default=0)
    buyer = models.ForeignKey(User, related_name="buyer", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.auc_item}: {self.cur} by {self.buyer}"

class comment(models.Model):
    commenter = models.ForeignKey(User, related_name="commenter", on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.commenter} : {self.comment}" 
