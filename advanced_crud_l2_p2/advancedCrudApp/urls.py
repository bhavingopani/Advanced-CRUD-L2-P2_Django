from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('', views.listUser, name='listUser'),
    path('addUser/', views.addUser, name='addUser'),
    path('editUser/<user_id>', views.editUser, name='editUser'), #check this path after sometime.
]
#have to add this url file in the main url.py to configure the same.
#possible views
 # 1. home page -- listing of all users with all the required data from all tables. - with edit and delete button
 # 2. Add user - Creating User with all the required fields.
 # 3. Edit user - Editing User with all information editable with fields.
