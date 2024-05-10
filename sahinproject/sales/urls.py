from django.urls import path
from .views import login_view, customer_form, get_ilceler
from . import views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('customer/', customer_form, name='customer_form'),
    path('get_ilceler/', views.get_ilceler, name='get_ilceler'),
    path('ziyaret-form/', views.visit_form, name='visit_form'),
    path('logout/', views.logout_view, name='logout'),
     path('get_customer_info/<int:customer_id>/', views.get_customer_info, name='get_customer_info'),

    # Diğer URL'ler buraya eklenebilir
]
