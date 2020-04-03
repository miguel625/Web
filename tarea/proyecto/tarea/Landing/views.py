from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django import template

# Importar metodo de auntenticacion
from django.contrib.auth import authenticate

class LandingClass(View):
    templates_ok = 'Landing/landing.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_ok,{})
