from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-item-detail'),
]
