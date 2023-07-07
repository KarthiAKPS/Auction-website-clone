from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, listing, bid, comment, Category
from .forms import ListingForm, BidsForm, CategoryForm, CommentForm


def index(request):
    items = listing.objects.all()
    return render(request, "auctions/index.html", {
        "items" : items,
    })

def create(request):
    if request.method=="POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.posted_user = request.user.id
            form.save()
        else:
            return render(request, "auctions/create.html", {
                "form": form,
                "message": "Enter valid details"
                })
        return HttpResponseRedirect( reverse("index"))
    else:
        form = ListingForm()
        return render(request, "auctions/create.html", {
            "form" : form
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def list(request, t):
    for i in listing.objects.all():
        if i.title == t:
            name = i.title
            description = i.description
            price = i.price
            category = i.category
            image = i.image
            form = BidsForm()
            return render(request, "auctions/listing.html", {
                "name" : name,
                "description" : description,
                "price" : price,
                "category" : category,
                "image" : image,
                "form" : form
            })

def current(request, name, price):
    if request.method=='POST':
        o = listing.objects.get(title=name)
        if float(price) > o.price:
            bid_object = bid.objects.get(id = o.id)
            bid_object.cur = price
            bid_object.item = o.id
            bid_object.buyer = request.user.id
            bid_object.save()
        else:
            return render(request, "auctions/listing.html", {
                "message" : "Your bid should be higher than the current bid!"
                })
        return render(request, "auctions/listing.html", {})


