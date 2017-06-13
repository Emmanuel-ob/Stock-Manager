from django.conf.urls import url
from . import views

app_name = 'salesman_mgr'
urlpatterns = [
    
    url(r'^view/(?P<username>[\w.@+-]+)/$', views.viewStock, name='view_stock'),
    url(r'^dashboard/(?P<username>[\w.@+-]+)/$', views.renderSalesman, name='dashboard'),
    url(r'^history/(?P<username>[\w.@+-]+)/$', views.transactionHistory, name='viewTransactions'),
    url(r'^update/(?P<username>[\w.@+-]+)/$', views.updateStock, name='update_stock'),
    url(r'^update/(?P<username>[\w.@+-]+)/(?P<messages>[\w.@+-]+)/$', views.updateStock, name='update_stock'),
    url(r'^updateInfo/(?P<username>[\w.@+-]+)/$', views.updateInfo, name='update_contact_detail'),
    url(r'^sell/(?P<username>[\w.@+-]+)/$', views.sellStock, name='sell_stock'),
    
]
