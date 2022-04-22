from django import forms
from django.forms import ModelForm #This is modelform as we will addding this form to our database hence its model.
from advancedCrudApp.models import User


#Create a Add User form
class CreateUserForm(ModelForm):
    class Meta: #just a way of django .. so dont need to think logically .. Just how it is.
        model = User
        # fields = "__all__" #if we want all the fields from the model.
        #if we want certain fields then -- can define exactly as follow.
        fields = ('user_id','first_name', 'last_name', 'email', 'date_of_birth','profile_picture', 'user_address_id')
        #to call it ..we will need different other things as well like new webpage etc.




