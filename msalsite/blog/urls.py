from django.urls import path
from . import views

# app_name = 'polls'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_inhoud'),
    path('post/nieuw/', views.post_nieuw, name='post_nieuw'),
    path('delete/<post_id>',views.delete_post,name='delete'),
    path('polls/', views.poll_view, name='poll_view'),
]



# app_name = 'polls'

