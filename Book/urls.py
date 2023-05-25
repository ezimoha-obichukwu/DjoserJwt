from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ApiHomePage.as_view(), name="home-page"),
    path("<uuid:id>/", views.ApiDetailPage.as_view(), name="detail-page")
]