from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,View,FormView
from .models import User,questions
from .forms import user_registration_form,UserLoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def Register_view(request):
    form = user_registration_form(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create(username=username, email=email, password=password,is_permission=False)
        user.save()
        login(request,user)
        return redirect('/login')
    return render(request,"userregister.html",{'form': form})
class User_logout_View(View):
    def get(self, request):
        logout(request)
        return redirect("entry")
@csrf_exempt
def User_Login_View(request):
    form = UserLoginForm(request.POST)
    if form.is_valid():
        # get info from login form
        username = request.POST["username"]
        password = request.POST["password"]
        customer = User.objects.get(username=username, password=password)
        if customer is not None and customer.is_permission:
            login(request, customer)
            return redirect('dash')
        else:
            # return to login page with error message
            context = {"message": "You are not a customer please verify or register"}
            return render(request, "userlogin.html",{"context":context}) 
    else:
        return render(request, "userlogin.html",{'form': form})
@csrf_exempt
def User_Login_View(request):
    form = UserLoginForm(request.POST)
    if form.is_valid():
        # get info from login form
        username = request.POST["username"]
        password = request.POST["password"]
        customer = User.objects.get(username=username, password=password)
        if customer is not None and customer.is_permission:
            login(request, customer)
            return redirect('/dash')
        else:
            # return to login page with error message
            context = {"message": "You are not selected now please wait...."}
            return render(request, "userlogin.html",{"context":context}) 
    else:
        return render(request, "userlogin.html",{'form': form})
    
def dash(request):
    if request.method == 'POST':
        print(request.POST)
        ques=questions.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in ques:
            total+=1
            print("hello",request.POST.get(q.question))
            print("asn",q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
                score+=-0.25
                
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        qw=questions.objects.all()
        context = {
            'questions':qw
        }
        return render(request,'dash.html',context)