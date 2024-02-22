from django.urls import path
from jinja import views
urlpatterns=[
    path('',views.home,name='my_home'),
    path('about',views.about,name='my_about'),
    path('contact',views.contact,name='my_contact'),
    path('gallery',views.gallery,name='my_gallery')

]