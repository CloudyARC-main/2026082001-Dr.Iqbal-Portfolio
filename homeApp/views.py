from django.shortcuts import render

# Create your views here.



def home_func(request):
    return render(request, "home.html")

def about_us_func(request):
    return render(request, "about_us.html")

def timeline_func(request):
    return render(request, "timeline.html")

def gallery_func(request):
    return render(request, "gallery.html")

def videos_func(request):
    return render(request, "videos.html")

def events_func(request):
    return render(request, "events.html")

def news_func(request):
    return render(request, "news.html")

def shop_func(request):
    return render(request, "shop.html")

def contact_func(request):
    return render(request, "contact.html")

def shop_func(request):
    return render(request, "shop.html")

def shop_func(request):
    return render(request, "shop.html")