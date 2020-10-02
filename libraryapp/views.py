from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .models import Library,User
from . serializers import UserSerializer,LibrarySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from . forms import SignUp,LoginForm

#view for the emp-list


class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    

#view for the activity period list
class LibraryView(viewsets.ModelViewSet):
    queryset=Library.objects.all()
    serializer_class=LibrarySerializer
    



def signupview(request):
    if request.method=='POST':
        form= SignUp(request.POST or None)

        if form.is_valid() and form.passwordLength():
            name= form.cleaned_data['name']
            password= form.cleaned_data['password']
            cpassword= form.cleaned_data['cpassword']
            email= form.cleaned_data['email']
            check=User.objects.filter(email=email)
            if check:
                return HttpResponse("<script>alert('This email is already registered...!');window.location ='';</script>")
            else:
                if password==cpassword:
                    user= User(name=name,password=password,email=email)
                    user.save()
                    return HttpResponse('sucessfully added')
                else:
                    print('hh')
                    return HttpResponse("<script>alert('Confirm password doesn't match with password...!');window.location ='';</script>")


            
        
       
    else:
        form=SignUp()
       
        return render(request,'signup.html',context= {'form':form})


def login(request):

    if request.method=='POST':
        form=LoginForm(request.POST or None)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            
            user=User.objects.get(email=email,password=password)
            
            if  user:
                print(user.name)
                request.session['email']=user.email
                
                
                return render (request,'home.html',{'user':user,'email':email})
            else:
                return HttpResponse('no')
    else:
        form=LoginForm()
        return render(request,'login.html',context={'form':form})