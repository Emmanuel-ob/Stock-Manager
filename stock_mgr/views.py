
from django.shortcuts import render, redirect
from django.http import HttpResponse
from stock_mgr.forms import RegistrationForm, LoginForm, UserAccountForm, AddItemForm
from stock_mgr.models import UserAccount, StoreItem
from salesman_mgr.models import SalesStock
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
from django.views.generic import RedirectView

# Create your views here.
def index(request):
    #return HttpResponse('welcome to user_mgr')
    context = {
        
    }
    return render(request, 'stock_mgr/index.html', context)

def home(request):
    context = {
        
    }
    return render(request, 'stock_mgr/home1.html', context)


@login_required()
def addStock(request, username):
    add_form = AddItemForm()
    context = {
	    'add_form':add_form,
	    'time':datetime.now(),
	    'username':username
	}
    if request.method == 'POST':
        add_form = AddItemForm(data = request.POST)
        rp = request.POST
        if add_form.is_valid():
            if StoreItem.objects.filter(itemName =  rp['itemName'], ).exists():
                update_item = StoreItem.objects.get(itemName = rp['itemName'],)
                if rp['quantity'] > 0:
                    update_item.description = rp['description'] 
                    update_item.quantity = rp['quantity']
                    update_item.save()
                    if update_item:
                        messages.success(request, 'The item have been updated')
                    else:
                        messages.warning(request, 'something went wrong item not updated!! please try again!')
                else:
                    messages.warning(request, 'Quantity selected is invalid!')
            else:
                if rp['quantity'] > 0:
                    add_item = StoreItem.objects.create(itemName = rp['itemName'], itemCode = rp['itemCode'], description = rp['description'], quantity = rp['quantity'], added_by = request.user, )
                    add_item .save()
                    if add_item :
                        messages.success(request, 'The item have been saved')
                    else:
                        messages.warning(request, 'something went wrong item not saved!! please try again!')
                else:
                    messages.warning(request, 'Quantity selected is invalid!')
        else: 
            context['add_form'] = AddItemForm(data = request.POST)
    return render(request, 'stock_mgr/addStock.html', context)
    #return redirect(reverse('stock_mgr:index'))
    #return HttpResponse('welcome to the Stock manager app, this service is currently unavailable')

@login_required()
def transferStock(request, username):
    context = {}

    if request.method == 'POST':
        rp = request.POST
        item_check = StoreItem.objects.filter(itemName = rp['itemName'],).exists()
        user_check = User.objects.filter(username = rp['salesman']).exists()
        
        if item_check and user_check:
            item = StoreItem.objects.get(itemName = rp['itemName'],)
            user = User.objects.get(username = rp['salesman'])
            if item.quantity >= int(rp['quantity']):
                if  int(rp['quantity']) >0:
                    item.quantity -= int(rp['quantity'])
                    if SalesStock.objects.filter(itemName = rp['itemName'], user = user,).exists():
                        sales_item = SalesStock.objects.get(itemName = rp['itemName'], user=user,) 
                        sales_item.quantity +=  int(rp['quantity'])
                        if not rp['price'] =='':
                            sales_item.unit_price = int(rp['price'])
                        sales_item.save()
                        item.save()
                        messages.success(request, 'Item tansfer successful!')
                    else:
                        salesman_stock = SalesStock.objects.create(user = user, itemName = rp['itemName'], quantity = int(rp['quantity']), unit_price = rp['price'],)
                        item.save()
                        salesman_stock.save()
                        messages.success(request, 'Item tansfer successful!')
                else:
                    messages.warning(request, 'Quantity selected is invalid!')
            else:
                messages.warning(request, 'Quantity selected is greater than stock available!')
        else:
            messages.warning(request, 'something went wrong item not saved!! please try again!')
    # else:
    #     messages.warning(request, 'Welcome!')
    view_stock = StoreItem.objects.all()
    user_list = User.objects.filter(is_staff = False,)
    context.update({'view_stock':view_stock, 'username':username, 'time':datetime.now(), 'user_list':user_list}) 
    return render(request, 'stock_mgr/transferStock.html', context)
    

@login_required()
def updateStock(request, username):
    if request.method == 'POST':
        
        rp = request.POST
        update_item = StoreItem.objects.get(pk = rp['itemId'], )
        if rp['quantity'] >0:
            update_item.description = rp['description'] 
            update_item.quantity = rp['quantity']
            update_item.save()
            if update_item:
                messages.success(request, 'The item have been updated')
            else:
                messages.warning(request, 'something went wrong item not saved!! please try again!')
        else:
            messages.warning(request, 'Quantity selected is invalid!')
    #return render(request, 'stock_mgr/addStock.html', context)
    return redirect(reverse('stock_mgr:view_stock', kwargs = {'username':username}))
    

@login_required()
def viewAgentStock(request, username):

    user_list = User.objects.filter(is_staff = False,) 
    context = {
    'username':username,
    'time':datetime.now(),
    'user_list': user_list,
    }
    if request.method == 'POST':
        rp = request.POST
        if User.objects.filter(username = rp['salesman'],).exists():
            user = User.objects.get(username = rp['salesman'],)
            view_stock = SalesStock.objects.filter(user = user,)
            context.update({'view_stock':view_stock, 'username':username, 'user_list': user_list, 'time':datetime.now()})

    return render(request, 'stock_mgr/viewAgentStock.html', context)
    


@login_required()
def renderAdmin(request, username):
    #return HttpResponse('welcome to user_mgr')
    context = {
        'username':username, 'time':datetime.now()
    }
    return render(request, 'stock_mgr/dashBoard.html', context)

def create_account(request):
    reg_form = RegistrationForm()
    context = {
        'reg_form': reg_form
    }
    if request.method == 'POST':
        user = None
        user_reg_form = RegistrationForm(data = request.POST)
        rp = request.POST
        if User.objects.filter(email = rp['email']).exists():
            context['reg_form'] = RegistrationForm(data = request.POST)
            messages.info(request, 'Sorry this email has been taken')
            return redirect(reverse('stock_mgr:register'))
        else:
            if user_reg_form.is_valid():
                #user_reg_form.save()
                user = User.objects.create(username = rp['username'], first_name = rp['first_name'], last_name = rp['last_name'], email = rp['email'], is_staff = True, )
                user.set_password(rp['password'])
                user.save()
                if user:
                   messages.success(request, 'Your details have been saved')
                else:
                    messages.warning(request, 'something went wrong acount not created!! please try again!')
            else: 
                context['reg_form'] = RegistrationForm(data = request.POST)
    return render(request, 'stock_mgr/index.html', context)

@login_required()
def create_user(request, username):
    reg_form = RegistrationForm()
    context = {
        'reg_form': reg_form
    }
    if request.method == 'POST':
        user = None
        user_reg_form = RegistrationForm(data = request.POST)
        rp = request.POST
        if User.objects.filter(email = rp['email']).exists():
            context['reg_form'] = RegistrationForm(data = request.POST)
            messages.info(request, 'Sorry this email has been taken')
            return redirect(reverse('stock_mgr:register'))
        else:
            if user_reg_form.is_valid():
                #user_reg_form.save()
                user = User.objects.create(username = rp['username'], first_name = rp['first_name'], last_name = rp['last_name'], email = rp['email'], )
                user.set_password(rp['password'])
                user.save()
                if user:
                   messages.success(request, 'Salesman details have been saved')
                else:
                    messages.warning(request, 'something went wrong acount not created!! please try again!')
            else: 
                context['reg_form'] = RegistrationForm(data = request.POST)
    return render(request, 'stock_mgr/index.html', context)

def log_in(request):
    login_form = LoginForm()
    context = { 'login_form' : login_form }
    if request.method == 'POST':
        rp = request.POST
        login_form = LoginForm(data = request.POST)
        #check if user exists
        if User.objects.filter(email = rp['email']).exists():
            username = User.objects.get(email = rp['email']).username
            status = User.objects.get(email = rp['email']).is_staff
            auth_user = authenticate(username= username, password = rp['password'])
            if auth_user:
                login(request, auth_user)
                if status == True:
            	
                   return redirect(reverse('stock_mgr:dashboard', kwargs = {'username':request.user.username}))
                else:
                    return redirect(reverse('salesman_mgr:dashboard', kwargs = {'username':request.user.username}))
            else: 
                context['login_form'] = login_form
                messages.error(request, 'Sorry your email or password is incorrect!!')
        else: 
            context['login_form'] = login_form
            messages.error(request, 'Sorry this email adddress doest not exist!!')
            
    context['login_form'] = login_form
    return render(request, 'stock_mgr/index.html', context)
    

def log_out(request):
    logout(request)
    return redirect(reverse('stock_mgr:home'))


@login_required()
def viewStock(request, username):
	context = {}
	view_stock = StoreItem.objects.all()
	context.update({'view_stock':view_stock, 'username':username, 'time':datetime.now()}) 
	return render(request, 'stock_mgr/stockView.html', context)


@login_required()
def deleteStock(request, username):
    if request.method == 'POST':
        
        rp = request.POST
        delete_item = StoreItem.objects.get(pk = rp['itemId'], )
        delete_item.delete()
        if delete_item:
            messages.success(request, 'The item have been deleted!')
        else:
            messages.warning(request, 'something went wrong item not deleted!! please try again!')
        
    return redirect(reverse('stock_mgr:view_stock', kwargs = {'username':username}))
    #return HttpResponse('welcome to the Stock manager app, this service is currently unavailable')

def searchProduct(request):
    if request.method =="POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    products = StoreItem.objects.filter(itemName__icontains=search_text)
    return render(request, 'stock_mgr/ajax_search.html', {'products': products})


class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        print(slug)
        obj = get_object_or_404(Post, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions

# class PostLikeAPIToggle(APIView):
#     authentication_classes = (authentication.SessionAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)

#     def get(self, request, slug=None, format=None):
#         # slug = self.kwargs.get("slug")
#         obj = get_object_or_404(Post, slug=slug)
#         url_ = obj.get_absolute_url()
#         user = self.request.user
#         updated = False
#         liked = False
#         if user.is_authenticated():
#             if user in obj.likes.all():
#                 liked = False
#                 obj.likes.remove(user)
#             else:
#                 liked = True
#                 obj.likes.add(user)
#             updated = True
#         data = {
#             "updated": updated,
#             "liked": liked
#         }
#         return Response(data)


