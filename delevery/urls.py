from django.urls import path
from . import views

urlpatterns = [

   # path('', views.home, name='home'),
   path('', views.HomeView.as_view(), name='home'),

   path('add/', views.AddDeliveryView.as_view(), name='add_delivery'),

   path('edit/<int:pk>/', views.EditDeliveryView.as_view(), name='edit_delivery'),

   path('delete/<int:pk>/', views.DeleteDeliveryView.as_view(), name='delete_delivery'),

   path('api/', views.delivery_api),

    #path('add/', views.add_delivery, name='add_delivery'),

    #path('edit/<int:id>/', views.edit_delivery, name='edit_delivery'),

    #path('delete/<int:id>/', views.delete_delivery, name='delete_delivery'),
    
]

