from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponseRedirect #this will allow us to redirect the page of what we want
#importing that form
from advanced_crud_l2_p2.forms import CreateUserForm #have to import here 
# Create your views here.
#now decide what all views we will be needing.

 
# def home(request):
#     return render(request, 'templates/home.html/')
#     # return HttpResponse("Hello there")


def listUser(request):




    return render(request, 'listUser.html')
    # return HttpResponse("Hello there")



def addUser(request):
    #To create the logic that.. somebody has submitted the form or its first time.. -- to create this logic we are taking this variable.
    submitted = False  #if the user is the coming first time -- this will be false. - we will make it true later
    #if the fillout the form
    if request.method == "POST":
        form = CreateUserForm(request.POST) #request.POST means.. if they posted it.. will get all the data meaning.. whatever they have posted . and PASS THAT INTO THE CreateUserForm
        #now check whatever they POSTED or submitted is valid or not. like typing or validaiton stuff
        if form.is_valid():  
            form.save() #if its valid then save it to the database.
            #if saved successfully
            return HttpResponseRedirect('/addUser?submitted=True') #redirecting and sending a variable with it.
                                                                    #with it we are making the submitted to True for the same.
    

    form = CreateUserForm

    return render(request, 'addUser.html', {'form':form})






def editUser(request):


    return render(request, 'editUser.html')