from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate

# Create your views here.
# class Landing_Class(View):
#     def get(self,request,*arg,**kwargs):
#         return render(request,self.template,{})
class Landing_Class(View):
    template='Landing/Landing.html'
    def get(self,request,*arg,**kwargs):
        return render(request,self.template,{})

class Dashboard_Class(View):
    template='Dashboard/dashboard.html'
    def get(self,request,*arg,**kwargs):
        return render(request,self.template,{})


class Login_Class(View):
    template='Login/Login.html'
    template_ok='Dashboard/dashboard.html'
    def get(self,request,*arg,**kwargs):
        return render(request,self.template,{})

    def post(self,request,*arg,**kwargs):
        user_post = request.POST['user']
        password_post = request.POST['password']

        user_session= authenticate(username=user_post,password=password_post)

        if user_session is not None:
            return render(request,self.template_ok,{})
        else:
            self.message='usurio o contraseña incorrecto'

        return render(request,self.template,self.get_context())

    def get_context(self):
        return{
            'error':self.message,
        }
# def Index(request):
#     return render(request, 'Index.html'),

# def Landing(request):
#     return render(request, 'Landing.html'),
