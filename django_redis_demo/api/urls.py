from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_items, manage_item

urlpatterns = [
    path('items', manage_items, name="items"),
    path('item/<slug:key>', manage_item, name="single_item")
]
