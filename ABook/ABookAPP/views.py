from django.shortcuts import render

#from django.http import HttpResponse

# Create your views here.

def index(request):
#    return HttpResponse("<h1>hello world</h1?");
    return render(request, 'index.html', {'name': 'Sree Manikandan'})

def addaddress(request):
#    val1 = request.POST.get('num1')
#    val2 = request.POST.get('num2')

   # val = val1 + val2
    #return render(request,'addaddress.html', {'result1': val1, 'result2': val2})
    return render(request, 'addaddress.html')

def viewaddress(request):
    val1 = request.POST.get("slno")
    val2 = request.POST.get("name")
    val3 = request.POST.get("phonenumber")
    val4 = request.POST.get("extension")
    val5 = request.POST.get("email")
    val6 = request.POST.get("address")

    return render(request, 'viewaddress.html', {'slno':val1, 'name': val2, 'phonenumber': val3, 'extension': val4, 'email':val5, 'address' :val6})