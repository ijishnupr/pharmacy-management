from django.shortcuts import render,HttpResponse,redirect
from store.models import medicine
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView,DetailView
from django.db.models import Q
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,UpdateView,DeleteView
def signup(request):
    if request.method=="POST":
        uname=request.POST.get('fname')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("your password and conform password are not same")
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('loginpage')
    return render(request,'signup.html')
def loginpage(request):
    if request.method=="POST":
        use=request.POST.get('username')
        pas=request.POST.get('password')
        
        user=authenticate(request,username=use,password=pas)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("username or password in incorrect")
    return render(request,'login.html')
def Logoutpage(request):
    logout(request)
    return render(request,'logout.html')
def index(request):
    if request.user.is_authenticated:
        n=request.user.username
        d=datetime.now().strftime("%I:%M-%p")
        t=datetime.now().strftime("%d/%m/%y")
        context={
            'h':n,
            'd':d,
            't':t
        }
        return render(request,'index.html',context)
    else:
        return redirect('loginpage')
class medlist(LoginRequiredMixin,ListView):
    model=medicine
    paginate_by=4
class midupdate(LoginRequiredMixin,UpdateView):
    model=medicine
    fields=['title','price','no_of_pack','status','exp']
    success_url=reverse_lazy('listview')
class middelete(LoginRequiredMixin,DeleteView):
    model=medicine
    fields=['title','price','no_of_pack','status','exp']
    success_url=reverse_lazy('listview')
@login_required
def search(request):
    result=[]
    if request.method=="GET":
        query=request.GET.get('search')
        if query=='':
            query='@#$'
        result=medicine.objects.filter(title__icontains=query)
        arg={
            'query':query,
            'result':result,
        }
        return render(request,'search.html',arg)
@login_required 
def about(request):

    return render(request,'about.html')
@login_required
def midcreate(request):
    if request.method=='POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        no_of_pack=request.POST.get('no_of_pack')
        exp=request.POST.get('exp')
        status=request.POST.get('status')
        med=medicine(title=title,price=price,no_of_pack=no_of_pack,exp=exp,status=status)
        med.save()
        return redirect('listview')
    return render(request,'add.html')
@login_required
def meddetail(request,pk):
    item=medicine.objects.get(pk=pk)
    title=item.title
    price=item.price
    status=item.status
    no_of_stock=item.no_of_pack
    red=item.exp
    exp=item.exp
    rexpiry=red.strftime("%m%y")
    t=datetime.now().strftime("%m%y")
    context={
        'title':title,
        'price':price,
        'status':status,
        'no_of_stock':no_of_stock,
        'expiry':rexpiry,
        'exp':exp,
        't':t
    }
    return render(request,'det.html',context)