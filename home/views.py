from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'index.html')
def loginpage(request):
    return render(request,'login.html')
def signuppage(request):
    return render(request,'signup.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def report(request):
    return render(request,'report.html')