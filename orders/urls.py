from django.urls import path,include
# from store import urls
# from zEcom.settings import MEDIA_ROOT
from . import  views
urlpatterns = [
     path('place_order/',views.place_order,name="place_order"),
    path('payments/', views.payments, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),
     
] 
