"""
URL configuration for dogstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# manually added
admin.site.site_header  =  "Dog store Admin panel"  
admin.site.site_title  =  "Welcome To Dog store"
admin.site.index_title  =  "Dog store Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("dog_data.urls")),
    path("about",include("dog_data.urls")),
    path("pricing",include("dog_data.urls")),
    path("contactus",include("dog_data.urls")),
    path("showrecords",include("dog_data.urls")),
    path("edit",include("dog_data.urls")),
    path("editedrecord",include("dog_data.urls")),
    path("delete",include("dog_data.urls")),
    path("signup",include("dog_data.urls")),
    path("paymenthandler",include("dog_data.urls")),
    path("userprofile",include("dog_data.urls")),
    path("addpet",include("dog_data.urls")),
    path("petdetails",include("dog_data.urls")),
    path("updatedetails",include("dog_data.urls")),
    path("updatedrecord",include("dog_data.urls")),
    path("deletedetails",include("dog_data.urls"))


 
    


    # path("updatedprofile",include("dog_data.urls"))






    # path("login",include("dog_data.urls"))


]

# 
