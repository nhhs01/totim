from django.shortcuts import render
from hello_subproject.models import Student, SHobby, Mentor
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

# Create your views here.
def index(request):
    displayMen=Mentor.objects.all().values()
    context = {
        'firstname1':'Lee Jong Suk',
        'displayMen':displayMen,
        'message': 'You successfully save new Mentor'
    }
    return render(request,'index.html', context)

def desc(request):
    return render(request, 'desc.html')

def newmentor(request):
    displayMen=Mentor.objects.all().values()

    if request.method=='POST':
        menid1=request.POST['menid']
        menname1=request.POST['menname']
        menroomno1=request.POST['menroomno']

        data=Mentor(menid=menid1, menname=menname1, menroomno=menroomno1)
        data.save()

        context = {
        'displaydata':displayMen,
        'message':"NEW MENTOR HAS BEEN SAVED" 
        }

        return render(request, 'newmentor.html', context)

    else:
        dict = {
            'message':'',
            'displaydata':displayMen 
        }

    return render(request, 'newmentor.html', dict)

def newstudent(request):
    displayStu=Student.objects.all().values()
    displayMen=Mentor.objects.all().values()

    if request.method=='POST':
        stuid1=request.POST['stuid']
        stuname1=request.POST['stuname']
        stuemail1=request.POST['stuemail']
        stuage1=request.POST['stuage']
        menid2=request.POST['selectmenid']

        mentornew=Mentor.objects.get(menid=menid2)
        data=Student(stuid=stuid1, stuname=stuname1, stuemail=stuemail1, stuage=stuage1, stumentor=mentornew)
        data.save()

        context = {
        'displayStu':displayStu,
        'displayMen':displayMen,
        'message':"NEW STUDENT HAS BEEN SAVED" 
        }

        return redirect('displaystudent')


    else:
        dict = {
        'displayStu':displayStu,
        'displayMen':displayMen,
        'message':"" 
        }

    return render(request, 'newstudent.html', dict)

def displaystudent(request):
    displayStu=Student.objects.all().values()

    context = {
        'displayStu': displayStu
    }
    return render(request,'displaystudent.html', context)

def update(request, stuid):
    updateid=Student.objects.get(stuid=stuid)

    dict = {
        'updateid': updateid
    }
    return render(request,"updatestudent.html", dict)

def updatestudent(request, stuid):
    data=Student.objects.get(stuid=stuid)
    stuname=request.POST['stuname']
    stuemail=request.POST['stuemail']
    stuage=request.POST['stuage']

    data.stuname=stuname
    data.stuemail=stuemail
    data.stuage=stuage
    data.save()

    return HttpResponseRedirect(reverse("displaystudent"))

def delete(request, stuid):
    deleteid=Student.objects.get(stuid=stuid)

    dict = {
        'deleteid': deleteid
    }
    return render(request,"deletestudent.html", dict)

def deletestudent(request, stuid):
    deletedata=Student.objects.get(stuid=stuid)
    deletedata.delete()

    return HttpResponseRedirect(reverse("displaystudent"))