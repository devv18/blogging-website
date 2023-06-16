
from django import forms
from .models import post, cat
cats = cat.objects.all().values_list('cat','cat')
cat_list= [

]

for i in cats:
    cat_list.append(i)
class dattaform(forms.ModelForm):

    class Meta:
        model = post
        
        fields= '__all__'
        widgets ={
    
        'title' : forms.TextInput(attrs={'class':'form-control'}),
        'author' : forms.Select(attrs={'class':'form-control','id':'devp','value':'','type':'hidden'}),
        'cat':forms.Select(  choices=cat_list , attrs={'class':'form-control'}),
        'body' : forms.Textarea(attrs={'class':'form-control'}),
        }