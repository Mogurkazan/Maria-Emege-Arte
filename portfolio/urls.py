from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portfolio-index'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
