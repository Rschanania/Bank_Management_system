from django.db import models
from django import forms

class banks(models.Model):
    name=models.CharField(max_length=200)
    id=models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.name}"
   






class branches(models.Model):
    id=models.IntegerField(null=True,blank=True)
    ifsc=models.CharField(max_length=20,null=False,blank=False,primary_key=True)
    bank_id=models.ForeignKey(banks,on_delete=models.CASCADE)
    branch=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    state=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.ifsc} Branch name   {self.branch}"


class BranchForm(forms.ModelForm):
    class Meta:
        model=branches
        fields="__all__"


class SearchForm(forms.Form):
    ifsc=forms.CharField(max_length=100, label='Bank Ifsc code',required=False)
    city=forms.CharField(max_length=100, label='Bank City',required=False)
    bank_id=forms.ModelChoiceField(queryset=banks.objects.all(),required=False,label='Bank Name')
    
    
    

   
    