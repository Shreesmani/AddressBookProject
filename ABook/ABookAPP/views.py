from django.shortcuts import render
from .models import AddressClass




# from django.http import HttpResponse

# Create your views here.

def index(request):
    #    return HttpResponse("<h1>hello world</h1?");
    return render(request, 'index.html', {'name': 'Sree Manikandan'})


def addaddress(request):

    return render(request, 'addaddress.html')

    # def createpost(request):
    #     if request.method == 'POST':
    #         if request.POST.get('title') and request.POST.get('content'):
    #             post = Post()
    #             post.title = request.POST.get('title')
    #             post.content = request.POST.get('content')
    #             post.save()
    #
    #             return render(request, 'posts/create.html')
    #
    #     else:
    #         return render(request, 'posts/create.html')




def viewaddress(request):
    if request.method == 'POST':
        post = AddressClass()
        AddressClass.slno = request.POST.get("slno")
        AddressClass.name = request.POST.get("name")
        AddressClass.phonenumber = request.POST.get("phonenumber")
        AddressClass.extension = request.POST.get("extension")
        AddressClass.email = request.POST.get("email")
        AddressClass.address = request.POST.get("address")

        #post.save()
        #    val1 = request.POST.get('num1')
        #    val2 = request.POST.get('num2')

        # val = val1 + val2
        # return render(request,'addaddress.html', {'result1': val1, 'result2': val2})
    AddressClass.objects.create(slno=AddressClass.slno, name=AddressClass.name, phonenumber=AddressClass.phonenumber, extension=AddressClass.extension, email=AddressClass.email, address=AddressClass.address)







    # val1 = request.POST.get("slno")
    # val2 = request.POST.get("name")
    # val3 = request.POST.get("phonenumber")
    # val4 = request.POST.get("extension")
    # val5 = request.POST.get("email")
    # val6 = request.POST.get("address")

    #return render(request, 'viewaddress.html', {'slno':val1, 'name': val2, 'phonenumber': val3, 'extension': val4, 'email':val5, 'address' :val6})
    #return render(request, 'viewaddress.html', {'slno':AddressClass.slno, 'name': AddressClass.name, 'phonenumber': AddressClass.phonenumber, 'extension': AddressClass.extension, 'email':AddressClass.email, 'address' :AddressClass.address})

    # AddressData = AddressClass.objects.all()
#    Addressdata = AddressClass.objects.all()
    Addressdata = AddressClass.objects.all()
    return render(request, "viewaddress.html", {'AddressData': Addressdata})
    # { %
    # for AddressClass in student_number %}
    # {{student.f_name}}
    # {{student.l_name}}
    # {{student.student_number}}
    # {{student.dob}}


    # { % endfor %}
    #oo_instance = Foo.objects.create(name='test')
    #Student.objects.create(Name=stud_name[i], Age=stud_age[i], Marks=stud_marks[i])
