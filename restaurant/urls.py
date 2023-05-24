from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.bookings)

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu.as_view(), name="menu"),
    path('menu_item/<int:pk>/', views.menu_item.as_view(), name="menu_item"),  
    path('bookings/', include(router.urls)), 
]