from django.contrib import admin
from django.urls import path
from dog_data import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("pricing",views.pricing,name="pricing"),
    path("contactus",views.contact,name="contactus"),
    path("login",views.loginuser,name="login"),
    path("logout",views.logoutuser,name="contactus"),
    path("showrecords",views.showrecords,name="showrecords"),
    path("edit",views.edit,name="edit"),
    path("editedrecord",views.editedrecord,name="editedrecord"),
    path("delete",views.delete,name="delete"),
    path("signup",views.signup,name="signup"),
    path('paymenthandler', views.paymenthandler, name='paymenthandler'),
    path("userprofile",views.userprofile,name="userprofile"),
    # path("updatedprofile",views.updatedprofile,name="updatedprofile"),
    path("addpet",views.addpet,name="addpet"),
    path("petdetails",views.petdetails,name="petdetails"),
    path("updatedetails",views.updatedetails,name="updatedetails"),
    path("updatedrecord",views.updatedrecord,name="updatederecord"),
    path("deletedetails",views.deletedetails,name="deletedetails")


    


    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





    # path("login",views.loginuser,name="login"),
    # path("logout",views.logoutuser,name="logout")


    

