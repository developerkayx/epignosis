from django.urls import path

from . import views

# Write your URL Configuration here
urlpatterns = [
    # path('collections/', views.CollectionList.as_view(), name="collection_list"),
    # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name="collection_detail"),
    # path('collections/<int:pk>/parts/', views.PartList.as_view(), name="part_list"),
    path('messages/<int:pk>', views.MessageDetail.as_view(), name="message_detail"),
    path('messages/', views.MessageList.as_view(), name="message_detail"),
    path('tags', views.tagged_messages, name='tags'),
]
