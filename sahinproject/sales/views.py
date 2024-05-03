from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from django.http import JsonResponse
from .models import *


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_form')  # Kullanıcı başarılı bir şekilde giriş yaptıktan sonra bilgileri dolduracağı sayfaya yönlendir
    return render(request, 'login.html')

@login_required  # Kullanıcı giriş yapmadan bilgi dolduramaz
def customer_form(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('success_page')  # Bilgileri başarıyla doldurduktan sonra yönlendirilecek sayfa
    return render(request, 'customer_form.html', {'form': form})

def get_ilceler(request):
    il_id = request.GET.get('il_id')
    ilceler = Ilce.objects.filter(il_id=il_id).values('id', 'ad')
    return JsonResponse(list(ilceler), safe=False)
