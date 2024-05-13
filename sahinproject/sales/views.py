from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import JsonResponse
from .models import *



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('visit_form')  
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required 
def customer_form(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('success_page')  
    return render(request, 'customer_form.html', {'form': form})

@login_required
def add_customer_popup(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()

            # Satış temsilcisini bul
            user_id = request.POST.get('user_id')
            sales_representative = User.objects.get(id=user_id).salesrepresentative

            # Müşteriyi satış temsilcisine ata
            sales_representative.assigned_customers.add(customer)

            return JsonResponse({'success': True})
    else:
        form = CustomerForm()
    return render(request, 'add_customer_popup.html', {'form': form})


def get_ilceler(request):
    il_id = request.GET.get('il_id')
    ilceler = Ilce.objects.filter(il_id=il_id).values('id', 'ad')
    return JsonResponse(list(ilceler), safe=False)



def get_customer_info(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    il_ad = customer.il.ad if customer.il else None
    ilce_ad = customer.ilce.ad if customer.ilce else None
    return JsonResponse({'il': il_ad, 'ilce': ilce_ad})

@login_required
def visit_form(request):
    form = VisitForm.for_user(request.user, instance=Visit() )
    if request.method == 'POST':
        form = VisitForm.for_user(request.user, request.POST, instance=Visit())
        if form.is_valid():
            # Ziyaret oluşturma işlemi
            form.save()
            # Başka bir şey yapabilirsiniz, örneğin bir yönlendirme
    return render(request, 'visit_form.html', {'form': form})