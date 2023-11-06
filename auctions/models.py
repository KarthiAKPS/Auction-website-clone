from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.posted_user, filename)

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
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name="item_type")
    image = models.ImageField(null=True, blank=True, upload_to=user_directory_path, max_length=100)
    posted_user = models.ForeignKey(User, related_name="posted_item", on_delete=models.CASCADE, null=True)
    isActive = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, null=True, related_name="Watch_items", blank=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class bid(models.Model):
    item = models.ForeignKey(listing, related_name="item", on_delete=models.CASCADE, null=True)
    cur = models.IntegerField(default=0)
    buyer = models.ForeignKey(User, related_name="buyer", on_delete=models.CASCADE, null=True)
    prevbuyer = models.ForeignKey(User, related_name="prevbuyer", on_delete=models.CASCADE, null=True)
    prevbid = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item}: {self.cur} by {self.buyer}"

class comment(models.Model):
    commented = models.ForeignKey(listing,on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    commenter = models.ForeignKey(User, related_name="user_name", on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.commenter} : {self.comment}" 
