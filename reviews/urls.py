from django.urls import path

from . import views

urlpatterns = [
        path('', views.search, name='search'),
        path('review/<str:company>/', views.review, name='review')
]
