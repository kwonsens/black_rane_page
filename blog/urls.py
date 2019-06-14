from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accelerating', views.accelerating, name='accelerating'),
    path('contact', views.contact, name='contact'),
    path('listing', views.listing, name='listing'),
    path('lp', views.lp, name='lp'),
    path('partner', views.partner, name='partner'),
    path('portfolio', views.portfolio, name='portfolio'),    

    path('post', views.post, name='post'),
]
