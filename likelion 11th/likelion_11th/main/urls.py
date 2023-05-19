from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('setting/', setting, name="setting"),
    path('study/', study, name="study"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('tag/', tag_list, name="tag_list"),
    path('tag/<int:tag_id>', tag_posts, name="tag_posts"),
    path('search', search, name="search"),
    path('delete_com/<int:id>', delete_com, name="delete_com"),
]