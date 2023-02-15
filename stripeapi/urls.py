from django.contrib import admin
from django.urls import path, include
from myitems.views import buy_item, item_detail, buy_item_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
    path('buyr/<int:item_id>/', buy_item_redirect, name='buy_item_redirect'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
]