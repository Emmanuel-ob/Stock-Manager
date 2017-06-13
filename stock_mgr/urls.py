from django.conf.urls import url
from . import views

app_name = 'stock_mgr'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.create_account, name = 'register'),
    url(r'^registerUser/(?P<username>[\w.@+-]+)/$', views.create_user, name = 'registerUser'),
    url(r'^login/$', views.log_in, name ='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^view/(?P<username>[\w.@+-]+)/$', views.viewStock, name='view_stock'),
    url(r'^dashboard/(?P<username>[\w.@+-]+)/$', views.renderAdmin, name='dashboard'),
    url(r'^add/(?P<username>[\w.@+-]+)/$', views.addStock, name='add_stock'),
    url(r'^transfer/(?P<username>[\w.@+-]+)/$', views.transferStock, name='transfer_stock'),
    url(r'^update(?P<username>[\w.@+-]+)/$', views.updateStock, name='update_stock'),
    url(r'^viewAgent(?P<username>[\w.@+-]+)/$', views.viewAgentStock, name='viewAgent_stock'),
    url(r'^delete(?P<username>[\w.@+-]+)/$', views.deleteStock, name='delete'),
    
]
