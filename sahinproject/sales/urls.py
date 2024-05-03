from django.urls import path
from .views import login_view, customer_form, get_ilceler
from . import views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('customer/', customer_form, name='customer_form'),
    path('get_ilceler/', views.get_ilceler, name='get_ilceler'),

    # Diğer URL'ler buraya eklenebilir
]
