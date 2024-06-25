from django.shortcuts import render, redirect
from . forms import contact_form, member_form, formsingup
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Members, Hotel,dates
from django.contrib.auth.models import User






# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('mypage')
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    formcontact = contact_form()
    if request.method == 'POST':
        formcontact = contact_form(request.POST)
        if formcontact.is_valid():
            formcontact.save()

    formcontet = {'form':formcontact}
    return render(request,"contact.html", formcontet)



def member_view(request):
    if request.method == 'POST':
        formrecord = member_form(request.POST)
        if formrecord.is_valid():
            formrecord.save()
    formrecord = member_form()
    cont = {"formrecord":formrecord}
    return render(request,"singup.html", cont)

def signuser(request):
    if request.method == 'POST':
        formsign = formsingup(request.POST)
        if formsign.is_valid():
            formsign.save()
            username = formsign.cleaned_data['username']
            password = formsign.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('login_user')       
    formsign = formsingup()
    return render(request,'loguser.html',{'formsign':formsign})




#Login function
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
           login(request,user)
           messages.success(request,'You are loged in successifully')
           return redirect('mypage')
        
        else:
            messages.success(request,'Wrong password or username! Try again.')
            return redirect('login_user')
    else:
        return render(request,"login.html")
    
def logout_user(request):
    logout(request)
    messages.success(request,"You are loged out successifully")
    return redirect('home')
    

def mypage(request):
    if request.user.is_authenticated:
        return redirect('information')
    
    else:
        return redirect('home')
        

#displaying content of user


def information(request):  
    if request.method == 'POST':
        malik_date = request.POST['datee']
        malik_pay = request.POST['payment']
        mal = request.POST['malik']
        hotel_aimi = Hotel.objects.get( hotel_name = mal)
        objMember = Members.objects.get(user_name = request.user)

        malik_dictionary = {
                    "malik_hotel":{
                        "hotel_name":hotel_aimi.hotel_name,
                        "hotel_location":hotel_aimi.location,
                        "payment":malik_pay,
                        "malik_date":malik_date,
                        "maliksataus":"Confirmed",
                        "meminfo":objMember
                    }
                }
        return render(request,"mypage.html",malik_dictionary)
    objMember = Members.objects.get(user_name = request.user)
    meminfo = {'objmember':objMember}
    return render(request,"mypage.html",meminfo)


        
# edit information
    
def edit(request):
    if request.method == 'POST':
        details = Members.objects.get(user_name = request.user)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mail = request.POST['mail']
        

        if firstname:
            details.first_name = firstname
            details.save()

        if lastname:
            details.last_name = lastname
            details.save()

        if mail:
            details.email = mail
            details.save()

        messages.success(request, "You have succeffuly updated your information")     
    return render(request,"infor.html")

def delete(request):
    delobj = Members.objects.get(user_name = request.user)
    objuser = User.objects.get(username = request.user)
    objuser.delete()
    delobj.delete()
    messages.success(request,"Your account is deleted succesifully!")
    logout(request)
    return redirect('home')

# hotel details
def hoteldetail(request):
    if request.method == 'POST':
            datey = request.POST['datee']
            payment = request.POST['payment']

            daty = dates.objects.create( date_booked = datey, payment_type = payment, status = "Confiremed")
            daty.save()
    return redirect('mypage')

def booked(request):
    Hotelobj = Hotel.objects.get(pk = 1)
    Hotelobj.hotel_name
    Hotelobj.location

    dayt = dates.objects.get(pk = 3)
    dayt.date_booked
    dayt.payment_type
    dayt.status
    
    content = { 
                "dict":{
                        "hotelname":Hotelobj.hotel_name,
                        "location":Hotelobj.location,
                        "date":dayt.date_booked,
                        "payment":dayt.payment_type,
                        "status":dayt.status
                      }
             }
    return render(request,"mypage.html", content)


    
        

    
    
       
   
    





    

