from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q

from .models import Literature, Gene
from .forms import Literatureform, Geneform

def home(request):
    geneinfos = Gene.objects.all()
    return render(request, 'home.html', {'geneInfo': geneinfos, })

def addGene(request):
    if request.method == 'POST':
        filled_form = Geneform(request.POST)
        if filled_form.is_valid():
            obj = filled_form.save(commit=False)
            obj.submitter = request.user
            created_exp = filled_form.save()
            messages.success(request,'Success!! The new gene has been added!')
            created_exp_pk = created_exp.id
        else:
            messages.error(request,'The new gene was not created, please try again!')
        new_form = Geneform()
        expInfo = Gene.objects.all().order_by('-id')
       # myFilter = ExpFilter(request.GET, queryset=expInfo)
        return render(request, 'home.html', {'expInfo': expInfo, 'created_exp_pk': created_exp_pk,  #'myFilter': myFilter,
                                             })
    else:
        form = Geneform()
        return render(request, 'addGene.html', {'addform': form, })


def addLiterature(request):
    if request.method == 'POST':
        filled_form = Literatureform(request.POST)
        if filled_form.is_valid():
            obj = filled_form.save(commit=False)
            obj.submitter = request.user
            created_exp1 = filled_form.save()
            messages.success(request,'Success!! The new literature has been added!')
            created_exp_pk1 = created_exp1.id
        else:
            messages.error(request,'The new gene was not created, please try again!')
        new_form = Literatureform()
        litInfo = Literature.objects.all().order_by('-id')
       # myFilter = ExpFilter(request.GET, queryset=expInfo)
        return render(request, 'home.html', {'litInfo': litInfo, 'created_exp_pk1': created_exp_pk1,  #'myFilter': myFilter,
                                             })
    else:
        form = Literatureform()
        return render(request, 'addLiterature.html', {'addform': form, })

def showAuthor(request):
    dispAuthor = request.GET.get('q')
    if dispAuthor:
        displayAuthor = Literature.objects.filter(Q(author__icontains=dispAuthor))
        return render(request, 'showAuthor.html', {'displayAuthor':displayAuthor})
    else:
        displayAuthor = Literature.objects.all()
        return render(request,'showAuthor.html', {'displayAuthor':displayAuthor})


