from Tools.scripts.make_ctype import method
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from . models import register
from . forms import Registerforms

# class list(ListView):
#     model = register
#     template_name = 'home.html'
#     context_object_name = 'obj'
#
# class detail(DetailView):
#     model = register
#     template_name = 'detail.html'
#     context_object_name = 'i'

def list(request):
    obj=register.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        dob = request.POST['dob']
        mob = request.POST['mob']
        qual = request.POST['qual']
        email = request.POST['email']
        pname = request.POST['pname']
        pmob = request.POST['pmob']
        course = request.POST['course']
        img = request.FILES['img']
        i=register(name=name,address=address,dob=dob,mob=mob,qual=qual,email=email,pname=pname,pmob=pmob,course=course,img=img)
        i.save()
        return render(request,'detail.html',{'i':i})
    return render(request,'home.html',{'obj':obj})

def preview(request,id):
    i=register.objects.get(id=id)
    return render(request,'detail.html',{'i':i})

def update(request,id):
    d=register.objects.get(id=id)
    form=Registerforms(request.POST or None, instance=d)
    if form.is_valid():
        form.save()
        i=register.objects.get(id=id)
        return render(request,'detail.html',{'i':i})
    return render(request,'update.html',{'d':d,'form':form})

def submit(request):
    return render(request,'submit.html')