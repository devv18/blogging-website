from typing import Any, Dict
from django.shortcuts import render,get_object_or_404
from django import forms
from django.views.generic import ListView , DetailView ,CreateView , UpdateView , DeleteView
from .models import post  ,cat
from .forms import dattaform
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect


class homeview(ListView):
    model = post
    template_name='home.html'
    def get_context_data(self, **kwargs: Any):
        cat_menu = cat.objects.all()
        context = super(homeview,self).get_context_data()
        context['cat_menu']=cat_menu
        return context
class showview(DetailView):
    model =post
    template_name = 'details.html'
    

class postview(CreateView):
    model= post
    form_class = dattaform
    tempplate_name = 'part1/post_form.html'

class updatepostview(UpdateView):
    model = post
    form_class = dattaform
    template_name = 'update.html'
    #fields = '__all__'
    
class deletepostview(DeleteView):
    model = post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
class catview(CreateView):
    model= cat
    
    tempplate_name = 'part1/cat_form.html'
    fields= '__all__'
def categorypost(request,cat):  

    catss= post.objects.filter(cat=cat)


    return render(request,'cat.html',{'catss':catss})
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse



    



