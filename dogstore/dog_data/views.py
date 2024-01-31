from django.shortcuts import render, HttpResponse, redirect
from dog_data.models import inquiry,addnewpet
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from .forms import ImageUploadForm
import git

def get_git_root(path):

        git_repo = git.Repo(path, search_parent_directories=True)
        git_root = git_repo.git.rev_parse("--show-toplevel")
        print git_root

if __name__ == "__main__":
    get_git_root('C:\Users\admin\Desktop\Dj-Dogstore\dogstore\dog_data\templates\index.html')


# import pkg_resources


def home(request):
    # return render(request, "login.html")
    if request.user.is_authenticated:
        return render(request,"index.html")
#   Do something for authenticated users.
    #  ...
    else:
     return render(request,"login.html")
#  Do something for anonymous users.
    # ...
#  context = {
#      "firstname": "omkar",
#      "lastname": "shete"
#  }

# # return HttpResponse("We are at the homepage")


def about(request):
    return render(request, "aboutus.html")
    # return HttpResponse("we are at the about page")


def pricing(request):

    currency = 'INR'
    amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'pricing.html', context=context)

    # return HttpResponse("we are at the pricing page.")
    
    
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.

@csrf_exempt
def paymenthandler(request):

    # only accept POST request.
    if request.method == "POST":
        try:

            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:

                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)

                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:

                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()



def contact(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        values = inquiry(name=name, email=email,
                         subject=subject, message=message)
        values.save()
        messages.success(request, "Your form has been submitted succesfully.")

    return render(request, "contactus.html")

# def home(request):


def loginuser(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in succesfully.")
            return render(request, "index.html")
        # A backend authenticated the credentials
        else:
            #    messages.warning(request, "please enter the correct credentials and try again...")
            return render(request, "login.html")

    # return render(request,"login.html")

    # return HttpResponse("please enter the correct credentials")
    # No backend authenticated the credentials

    #  print(email)
    #  print(password)


def logoutuser(request):
    logout(request)
    return redirect("/login")


def signup(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        surname = request.POST.get("surname")
        mobileno = request.POST.get("mobileno")
        address = request.POST.get("address")
        state = request.POST.get("state")
        password = request.POST.get("password")



        client1 = User.objects.create_user(
            username=name, password=password, email=email)
        client1 = authenticate(
            username=name, password=password, email=email)
        if client1 is not None:

            login(request, client1)
            subject = 'welcome to Dogstore Family'
            message = f'Hi {client1.username}, thank you for registering in dogstore.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [client1.email]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=True)
            return render(request, "index.html")
        else:
            return render(request, "signup.html")

    return render(request, "signup.html")

    # if request.method == "POST":

    #     username = request.POST.get("username")
    #     email = request.POST.get("email")
    #     password = request.POST.get("password")

    #     client = User.objects.create_user(
    #         username=username, password=password, email=email)
    #     client = authenticate(
    #         username=username, password=password, email=email)
    #     if client is not None:

    #         login(request, client)
    #         subject = 'welcome to Dogstore Family'
    #         message = f'Hi {
    #             client.username}, thank you for registering in dogstore.'
    #         email_from = settings.EMAIL_HOST_USER
    #         recipient_list = [client.email]
    #         send_mail(subject, message, email_from,
    #                   recipient_list, fail_silently=True)
    #         return render(request, "index.html")
    #     else:
    #         return render(request, "signup.html")

    # return render(request, "signup.html")


# Create your views here.


# def showrecords(request):
#    n1=request.post.get


def showrecords(request):  # crud operation
    #    n1=request.POST.get("name")
    #    n2=request.POST.get("email")
    #    n3=request.POST.get("subject")
    #    n4=request.POST.get("message")
#     showvalues = inquiry.objects.all()
# #    n5=n1 +" " + n2 + " " + n3 + " " +n4
#     return render(request, "showrecords.html", {"showvalues": showvalues})

        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
        
            User.objects.filter(username=username).update(username=username, email=email,password=password)
            User.save()
        # n1=request.POST.get("name")
        

        n1 = request.GET["username"]
        
        for data in User.objects.filter(username=n1):
            username = data.username
            email = data.email
            password=data.password
            
            
        return render(request, "userprofile.html", {"username": username, "email": email,"password":password})

        


def edit(request):

    n1 = request.GET["name"]
    # name = email = "Not Available"

    for data in inquiry.objects.filter(name=n1):
        name = data.name
        email = data.email
    return render(request, "edit.html", {"Name": name, "Email": email})


def editedrecord(request):

    if request.method == "POST":
        # n1=request.POST.get("name")
        name = request.POST.get("name")
        email = request.POST.get("email")
        inquiry.objects.filter(name=name).update(name=name, email=email)
        # showvalues.save()
    return redirect("/showrecords")


def delete(request):

    #    if request.method=="POST":
    n1 = request.GET["name"]
    inquiry.objects.filter(name=n1).delete()
    return redirect("/showrecords")

 #   return HttpResponseRedirect("show")
 
 
def userprofile(request):
    
    # n2 = request.GET["username"]
    
    

    # for  data in User.objects.values():
        
    #     p1=data.username
    data=User.objects.all()
    # new=data.username
        
        
        
    
    return render(request,"userprofile.html",{'data':data})

#     return render(request,"userprofile.html") 



# def updatedprofile(request):
#     if request.method == "POST":
#         # n1=request.POST.get("name")
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
        
#         User.objects.filter(username=username).update(username=username, email=email,password=password)
#         # User.save()
#         # showvalues.save()
        
#     return redirect("/userprofile")

    
def petdetails(request):
    details=addnewpet.objects.all()
    return render(request,"petdetails.html",{"pets":details})



def addpet(request):
    if request.method == "POST":

        pet_id = request.POST.get("pet_id")
        name = request.POST.get("name")
        breed = request.POST.get("breed")
        sex = request.POST.get("sex")
        color = request.POST.get("color")
        image=request.FILES.get("image")

        details1 = addnewpet(pet_id=pet_id,name=name, breed=breed,sex=sex, color=color,image=image)
        details1.save()

    return render(request, "addpet.html")

def updatedetails(request):
    n1 = request.GET.get("name")
    requiredpet=addnewpet.objects.filter(name=n1)
    return render(request,"updatedetails.html",{"pets":requiredpet})


def updatedrecord(request):

    if request.method == "POST":
        

        pet_id1= request.POST.get("pet_id")
        name = request.POST.get("name")
        breed = request.POST.get("breed")
        sex = request.POST.get("sex")
        color = request.POST.get("color")
        # image=request.FILES.get("image")
        addnewpet.objects.filter(pet_id=pet_id1).update(pet_id=pet_id1,name=name,breed=breed,sex=sex, color=color )
    return redirect("/petdetails")

def deletedetails(request):

    #    if request.method=="POST":
    n1 = request.GET["name"]
    addnewpet.objects.filter(name=n1).delete()
    return redirect("/petdetails")
