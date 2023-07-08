from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, listing, bid, comment, Category
from .forms import ListingForm, BidsForm, CategoryForm


def index(request):
    if request.method == "POST":
        cat = request.POST["category"]
        c = Category.objects.get(category=cat)
        all_cat = Category.objects.all()
        items = listing.objects.filter(isActive=True, category=c)
        return render(request, 'auctions/index.html', {
            "items" : items,
            "cat" : all_cat
            })
    else:
        items = listing.objects.filter(isActive=True)
        cat = Category.objects.all()
        return render(request, "auctions/index.html", {
            "items" : items,
            "cat" : cat
        })

@login_required
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
    o = listing.objects.get(title=t)
    inWatchlist = request.user in o.watchlist.all()
    form = BidsForm()
    u = request.user
    owner = o.posted_user
    try: 
        cur_item = bid.objects.get(item = o.id)
        curr = cur_item.cur
        by = cur_item.buyer
    except:
        curr = 0
        by = "None"
    comms = comment.objects.filter(commented = o)
    return render(request, "auctions/listings.html", {
        "cur" : curr,
        "listings" : o,
        "watching" : inWatchlist,
        "form" : form,
        "comms" : comms,
        "by" : by,
        "u" : u,
        "owner" : owner,
    })

@login_required
def watch(request):
    u = request.user
    items = u.Watch_items.all()
    return render(request, "auctions/mywatchlist.html", {
        "items" : items,
        })

@login_required
def current(request, id):
    if request.method=='POST':
        cur_bid = request.POST['cur']
        form = BidsForm()
        u = request.user
        o = listing.objects.get(pk=id)
        try:
           bid_object = bid.objects.get(item = o.id)
           c =  bid_object.cur
        except:
            c = 0
            bid_object = bid(item = o, cur = c, buyer = request.user)
            bid_object.save()
        inWatchlist = request.user in o.watchlist.all()
        comms = comment.objects.filter(commented = o)
        if float(cur_bid) > float(c):
            bid_object.cur = cur_bid
            bid_object.item = listing.objects.get(pk = id)
            bid_object.buyer = request.user
            bid_object.save()
        else:
            return render(request, "auctions/listings.html", {
            "cur" : c,
            "listings" : o,
            "watching" : inWatchlist,
            "form" : form,
            "comms" : comms,
            "by" : bid_object.buyer,
            "u" : u,
            "pass" : False,
            "message" : "Your bid should be higher than the current bid"
                })
        return render(request, "auctions/listings.html", {
            "cur" : bid_object.cur,
            "listings" : o,
            "watching" : inWatchlist,
            "form" : form,
            "comms" : comms,
            "by" : bid_object.buyer,
            "u" : u,
            "pass" : True,
            "message" : "Bid Placed"
                })

@login_required
def mypage(request):
    if request.method=="POST":
        obj = request.POST['obj_id']
        o = listing.objects.get(id=obj)
        cat = Category.objects.all()
        return render(request, "auctions/edit.html", {
            "id" : o.id,
            "title" : o.title,
            "description" : o.description,
            "price" : o.price,
            "categories" : cat,
            "image" : o.image,
        })

    else:
        user = request.user
        if user.is_authenticated:
            items = listing.objects.filter(posted_user=user)
            return render(request, "auctions/mypage.html", {
                "items" : items
            })

@login_required
def edit(request, id):
    if request.method=='POST':
       title = request.POST['title']
       description = request.POST['description']
       price = request.POST['price']
       category = request.POST['category']
       img = request.POST['image']
       o = listing.objects.get(pk = id)
       o.title = title
       o.description = description
       o.price = price
       o.category = Category.objects.get(category=category)
       o.image = img
       o.save()
       return HttpResponseRedirect(reverse('mypage'))

@login_required
def delete(request, id):
    listing.objects.filter(pk = id).delete()
    return HttpResponseRedirect(reverse('mypage'))

@login_required
def comm(request, id):
    if request.method == "POST":
        comments = request.POST['comment']
        u = request.user
        i = listing.objects.get(pk = id)
        o = comment(commented=i, commenter=u, comment=comments)
        o.save()
        return HttpResponseRedirect(reverse("list", args=(i.title, )))

@login_required
def add(request, id):
    if request.method=='POST':
        user = request.user
        o = listing.objects.get(pk = id)
        o.watchlist.add(user)
        o.save()
        return HttpResponseRedirect(reverse("list", args=(o.title, )))

@login_required
def remove(request, id):
    if request.method=='POST':
        user = request.user
        o = listing.objects.get(pk = id)
        o.watchlist.remove(user)
        o.save()
        return HttpResponseRedirect(reverse("list", args=(o.title, )))

def sell(request, id):
    o = listing.objects.get(pk = id)
    o.isActive = False
    o.save()
    comms = comment.objects.filter(commented = o)
    try: 
        cur_item = bid.objects.get(item = o.id)
        curr = cur_item.cur
        by = cur_item.buyer
    except:
        curr = 0
        by = "None"
    return render(request, "auctions/listings.html", {
        "comms" : comms,
        "listings" : o,
        "cur" : curr,
        "by" : by,
        })



