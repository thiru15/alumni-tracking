from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Account,colleges
from django.views.generic import TemplateView
from .forms import AccountForm,collegeform
from django.conf import settings

from django.core.mail import send_mail

global l
g=''
l=[]
for acc in Account.objects.all():
    l.append(acc)


coll=''
class IndexView(TemplateView):
    template_name = "base.html"


def index(request):
    account=Account.objects.filter(validity=False)
    return render(request,'admin.html',{'account':account})
    #return HttpResponse("HI WORLD A STAR IS BORN")

def college_login(request):
      
    flag=0
    print(flag)
    if request.method == 'POST':
        form2=collegeform(request.POST)
        collegecode=request.POST['college_code']
        global coll
        coll=collegecode
        print("COLLLLLL ",coll)
        password=request.POST['password']
        user=authenticate(username=collegecode,password=password)
        print(collegecode,password,user)
        a=colleges.objects.filter(college_code=collegecode,password=password)
        print(a)
        if a:
            #return user_valid(collegecode)
            return HttpResponseRedirect('/main/')
            loggedin=True
            
        else:
           return HttpResponse("INVALID")
    elif flag==1:
            if request.method=='POST':
                v=request.POST['accept']
                return HttpResponse(v)
    else:
        form2=collegeform()
        form=AccountForm()
        a=False
    return render(request, 'collegelogin.html',{'form2':form2},{'a':a})



def get_name(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AccountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AccountForm()

    return render(request, 'registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['email'] #this get will grab it from the HTML
        password = request.POST['password']


        #user = authenticate(email=username, password=password) #user is a boolean that tells us if it is authenticated or not
        #print(username,password,user)
        user=Account.objects.filter(email=username, password=password)
        
        if user:
            if user:
                g=Account.objects.filter(email=username)
                print('GG ',g)
                for k in g:
                    valid=k.validity
                    print("BBB ",valid)


                if valid==True:
                    #login(request, user)
                    return HttpResponseRedirect('/index/')
                else:
                    return HttpResponse("You are not verified yet by your college")
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!")
        else:
            print("LOGIN FAILED!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'login.html',{})

def user_valid(request):
        global coll
        global g
        #return HttpResponse(coll)
        if request.method=='POST':
            l1=[]
            for i in range(len(l)):
                  a=l[i]
                  print(a.username)
                  print(a.email)
                  print(a.college)
                  print(a.field)
                  print("\n")
            print("COLUU ",coll)
            print("HEY BABE ",g)
            crrct=Account.objects.filter(college=g,validity=False) 
            print("CORRECT ",crrct)
            

            if request.POST['accept']=='accept':
              for k in crrct:
                print("LUST ",k)
                k.validity=True

                k.save()
                subject="GREETINGS FROM RMK ALUMNI PORTAL"
                message="Your Application has been Verified"
                from_email=settings.EMAIL_HOST_USER
                to_list=['thirumalaisrinivasan7@gmail.com']
                send_mail(subject,message,from_email,to_list,fail_silently=False)

                break
               
              #a1.save()
              print('accepted')
              #print(l)
              
              #print(l[0])
              return HttpResponse("accepted")
            else:
              for k in crrct:
                print("LUST ",k)
                k.delete()
                break
              
              print('rejected')
              return HttpResponse("rejected")
        
        
        #global coll
        #return HttpResponse(coll)
        college=colleges.objects.filter(college_code=coll)
        
        

        for coll in college:
                g=coll.college_name
        
       
        print("G ",g)
        acc=Account.objects.filter(college=g,validity=False)
        print("ACCOUNT ",acc)
        print()
        print(Account.objects.all)
        print()
        for colle in acc:
                print("A ",colle.username)
                flag=1

        
        
        return render(request,'posts.html',{'acc':acc,'college':college})



        


