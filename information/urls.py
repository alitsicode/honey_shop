from django.urls import path
from . import views 
urlpatterns = [
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.ContactUsCreateView.as_view(),name='contactus'),
]