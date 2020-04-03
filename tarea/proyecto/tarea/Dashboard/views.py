from django.shortcuts import render, redirect
from django.views.generic import View

class DashboardClass(View):
    templates_oke = 'Dashboard/dashboard.html'
    def get(self, request, *args, **kwargs):
        print("GET")
        return render(request, self.templates_oke,{})