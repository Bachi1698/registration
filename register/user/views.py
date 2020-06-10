from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    message = "",
    us = authenticate(username=name, password=passe)
    if us.is_active:
        login(request,us)
        message = "bienvenue"
    else:
        message = "identifiant incorrecte"
    datas = {

    }
    return render(request,'pages/index.html',datas)
def login(request):
    datas = {

    }
    return render(request,'pages/login.html',datas)

def inscription(request):
    message = "",
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        passe = request.POST.get('pass')
        re_pass = request.POST.get('re_pass')
        #  traitement des données 
        validate_email(email)
        isemail = True
        if passe != re_pass:
            message = "erreur lors de l'enregistrement"
            print("le mot de passe est différent ")
        else:
            print("mot de passe correct")
            if name is not None and not name.isspace() and isemail and email is not None and passe is not None and not passe.isspace() and re_pass is not None and not re_pass.isspace():
                # enregistrement des données 
                user = User(
                    username = name,
                    first_name = name,
                    last_name = name,
                    email = email
                
                )
                user.save()
                user.password = passe
                user.set_password(user.password) #permet à django de cacher le mot de passe 
                user.save()
                message = " l'enregistrement a été effectué avec succes"
                try:
                    us = authenticate(username=name, password=passe)
                    if us.is_active:
                        login(request,us)
                except:
                    pass
            
            else:
                message = "l'inscription a échoué"
                print("inscription echoué")


    datas = {
        "message" : message,
    }
    return render(request,'pages/inscription.html',datas)

