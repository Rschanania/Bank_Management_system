from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import TemplateView,ListView
from .models import branches as Branch,BranchForm,SearchForm
from django.urls import reverse_lazy
from . filter import BranchFilter,IfscFilter

class show(TemplateView):
    template_name='branch/list_posts.html'
    model=Branch
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
       
        context['object_list']=Branch.objects.all()[:27]
        return context


class edit(UpdateView):
    model=Branch
    fields="__all__"
    success_url="/branch/"


class add(CreateView):
    model=Branch
    fields="__all__"
    success_url="/branch/"

class delete(DeleteView):
    model=Branch
    success_url=reverse_lazy("show")



def branchFilter(request):
    branches1=Branch.objects.prefetch_related()
   
    branches2=Branch.objects.prefetch_related()
    
    
    branchFilter=BranchFilter(request.GET,queryset=branches1)
    ifscFilter=IfscFilter(request.GET,queryset=branches2)
  
    b1=branchFilter.qs
    b2=ifscFilter.qs
    print(len(b1))
    print(len(b2))
    branches=branchFilter.qs

    context={
        'object_list':branches,
        "branchFilter":branchFilter,
        'ifscFilter':ifscFilter,
    }

    return render(request,'branch/filter_bank.html',context)




    


def search(request):
    form=SearchForm()
    
    if request.method=="POST":
        print(request.POST)
        form =SearchForm(request.POST)
        ifsc=form.data['ifsc']
        bank_id=form.data['bank_id'] or None
       
        City = request.POST.get('city', None)
       
        if ifsc:
            branches=Branch.objects.filter(ifsc=ifsc)
            res=render(request,'branch/search_bank.html',{'branches':branches,'form':form})
            return res

        else:
            branches=Branch.objects.filter(bank_id=bank_id,city=City)
            res=render(request,'branch/search_bank.html',{'branches':branches,'form':form})
            return res


       
        
    

    
    res=render(request,'branch/search_bank.html',{'form':form})
    return res




    
