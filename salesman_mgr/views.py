from django.shortcuts import render, redirect
from django.http import HttpResponse
from stock_mgr.forms import UserAccountForm
from stock_mgr.models import UserAccount
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from salesman_mgr.models import SalesStock
#from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime


@login_required()
def renderSalesman(request, username):
    #return HttpResponse('welcome to user_mgr')
    context = {
        'username':username, 'time':datetime.now(),
        'attr': UserAccount.objects.get_or_none(user=request.user)
    }
    return render(request, 'salesman_mgr/dashBoard.html', context)


@login_required()
def viewStock(request, username):
	context = {}
	view_stock = SalesStock.objects.filter(user = request.user)
	context.update({'view_stock':view_stock, 'username':username, 'time':datetime.now(),'attr': UserAccount.objects.get_or_none(user=request.user)}) 
	return render(request, 'salesman_mgr/stockView.html', context)
   
@login_required()
def transactionHistory(request, username):
    return HttpResponse('welcome to the Stock manager app, this service is currently unavailable')

@login_required()
def updateStock(request, username, messages=None):
    context = {}
    view_stock = SalesStock.objects.filter(user = request.user)
    context.update({'view_stock':view_stock, 'username':username, 'time':datetime.now(), 'attr': UserAccount.objects.get_or_none(user=request.user)}) 
    return render(request, 'salesman_mgr/makeSale.html', context)
    #return HttpResponse('welcome to the Stock manager app, this service is currently unavailable')



@login_required()
def updateInfo(request, username):
    info_form = UserAccountForm()
    context = {
        'info_form':info_form,
        'time':datetime.now(),
        'username':username,
        'attr': UserAccount.objects.get_or_none(user=request.user)
    }
    if request.method == 'POST':
        info_form = UserAccountForm(request.POST, request.FILES)
        rp = request.POST
        if info_form.is_valid():
            #user = request.user
            user = User.objects.get(username = username)
            if UserAccount.objects.filter(user = user, ).exists():
                update_info = UserAccount.objects.get(user = user,)
                update_info.gender = rp['gender'] 
                update_info.phoneNumber = rp['phone_number']
                update_info.dob = rp['date_of_birth']
                update_info.address = rp['address']
                update_info.state = rp['state']
                update_info.country = rp['country']
                if request.FILES['image']:
                    update_info.thumbnail = request.FILES['image']
                update_info.save()
                if update_info:
                    messages.success(request, 'Your details have been updated')
                else:
                    messages.warning(request, 'something went wrong item not updated!! please try again!')
            else:
                add_info = UserAccount.objects.create(user = user, gender = rp['gender'], phoneNumber = rp['phone_number'], dob = rp['date_of_birth'], address = rp['address'], state = rp['state'], country = rp['country'], )
                if request.FILES['image']:
                    add_info.thumbnail = request.FILES['image']
                add_info.save()
                if add_info:
                    messages.success(request, 'Your details have been saved')
                else:
                    messages.warning(request, 'something went wrong item not saved!! please try again!')
        else: 
            context['info_form'] = UserAccountForm(request.POST, request.FILES)
    return render(request, 'salesman_mgr/addInfo.html', context)

@login_required()
def sellStock(request, username):
    context = {}
    if request.method == 'POST':
        rp = request.POST
        stock_check = SalesStock.objects.filter(user = request.user, itemName = rp['itemName'], ).exists()
        
        if stock_check:
            item = SalesStock.objects.get(user = request.user, itemName = rp['itemName'],)
            if item.quantity >= int(rp['quantity']):
                if int(rp['quantity']) > 0:
                    item.quantity -= int(rp['quantity'])
                    item.save()
                    if item.quantity ==0:
                        item.delete()
                else:
                    messages.warning(request, 'Quantity selected is invalid!')
            else:
                messages.warning(request, 'Quantity selected is greater than stock available!')
        else:
            messages.warning(request, 'This stock is not in your warehouse') 
    #context = {'messages':messages}         
    return redirect(reverse('salesman_mgr:update_stock', kwargs = {'username':username}))


 