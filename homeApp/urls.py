from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_func, name="home_func"),
    path('about-us', views.about_us_func, name="about_us_func"),
    path('timeline/', views.timeline_func, name='timeline_func'),
    path('gallery/', views.gallery_func, name='gallery_func'),
    path('videos/', views.videos_func, name='videos_func'),
    path('events/', views.events_func, name='events_func'),
    path('news/', views.news_func, name='news_func'),
    path('shop/', views.shop_func, name='shop_func'),
    path('contact/', views.contact_func, name='contact_func'),
]
