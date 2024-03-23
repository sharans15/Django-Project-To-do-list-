from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import *

#juststud15
#sdsd

# Create your views here.






from django.contrib import messages
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q



def home(request):


    users = Todo.objects.all().order_by('-created_date')
    query = request.GET.get('q')
    if query:
        print('here in search')
        users = Todo.objects.filter(
            Q(title__icontains=query) | Q(task_content__icontains=query) |
            Q(employee__name__icontains=query)
        ).distinct()
 
    page = request.GET.get('page',1 )

    paginator = Paginator(users, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'users': users}



    return render(request, 'task/home.html', context)

def create_todo(request):
    if request.method == 'POST':
        print("in postt")
        empobj =  Employee.objects.get(id=2)
        print(request.FILES.get('title2'))


        Todo.objects.create(title=request.POST['title'],task_content=request.POST['task_content'],employee=empobj,image2 = request.FILES.get('title2'))
        messages.success(request,'Your Todo is created!')

        return redirect('home')
    
    return render(request, 'task/create.html')

def edit_todo(request, pk):
    if request.method == 'POST':
        print(pk)
        todo = Todo.objects.get(id=pk)
        print("---------8888888")
        print((request.FILES))

        print(len(request.FILES))
        

        todo.title = request.POST['title']
        empobj =  Employee.objects.get(id=todo.employee.id)

        (todo.employee) = empobj
        
        todo.task_content = request.POST['task_content']
        print(request.FILES)
        if len(request.FILES)>0:
            print("found")
            todo.image2 = request.FILES.get('title2')
        else:
            print("none")

        todo.save()
       
        messages.success(request,'Your Todo is Updated Successfully!')
        return redirect('home')
   
    todoob = Todo.objects.all().filter(id=pk)

    for x in todoob:
        print(x.title)

    return render(request, 'task/edit.html', {'todo':todoob})

def complete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    context = {'todos' : Todo.objects.all()}
    return render(request, 'task/home.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    context = {'todos' : Todo.objects.all()}
    return render(request, 'task/home.html', context)

def completed(request):
    todo = Todo.objects.all().filter(complete=True)
    context = {'todos' : todo}
    return render(request, 'task/completed.html', context)


def to_display(request):
    data="my name is sharan"
    context = {'data' : data}
    return render(request, 'task/to_display.html', context)



def createstud(request):
    if request.method == 'POST':

        print(request.POST)

        students.objects.create(name=request.POST['name'],age=request.POST['age'])
        messages.success(request,'Your Student is created!')

        return redirect('homestudent')
    
    return render(request, 'task/student_create.html')


def homestudent(request):
    todos = students.objects.all().order_by('-created_date')
    page = request.GET.get('page',1 )

    paginator = Paginator(todos, 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'users': users}
    return render(request, 'task/homestudent.html', context)




def editsutd(request, pk):
    if request.method == 'POST':
        print(pk)
        todo = students.objects.get(id=pk)

        print(request.POST)
        todo.name = request.POST['name']

        
        todo.age = request.POST['age']
        todo.save()
       
        messages.success(request,'Your Student is Updated Successfully!')
        return redirect('homestudent')
   
    todoob = students.objects.all().filter(id=pk)

  

    return render(request, 'task/editsutd.html', {'todo':todoob})



def deletestud(request, pk):
    todo = students.objects.get(id=pk)
    todo.delete()
    context = {'todos' : students.objects.all()}
    return render(request, 'task/homestudent.html', context)














def register(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        createuser.objects.create(username=Username,password=password)
        messages.info(request,'Account created!')
        return redirect('/register/')
    else:
        return render(request, 'task/register.html', {})




def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
   
        if createuser.objects.filter(username=Username, password=password).exists():
                user = createuser.objects.get(username=Username, password=password)
                request.session['type_id'] = 'User'
                request.session['username'] = Username
                request.session['login'] = 'Yes'
                return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'task/user_login.html', {})



def logout(request):
    Session.objects.all().delete()
    return redirect('/')
















def paginate(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'task/user_list.html', { 'users': users })




def post_list(request):
    posts_list = Todo.objects.all()
    query = request.GET.get('q')
    if query:
        posts_list = Todo.objects.filter(
            Q(title__icontains=query) | Q(task_content__icontains=query) |
            Q(employee__name__icontains=query)
        ).distinct()
    
    context = {
        'posts': posts_list
    }
    return render(request, "task/post-list.html", context)



    ################################blogs###################################################



def Bloghome(request):


    users = blog.objects.all()
    query = request.GET.get('q')
    if query:
        print('here in search')
        users = blog.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) |
            Q(blogger_name__username__icontains=query)
        ).distinct()

    page = request.GET.get('page',1 )

    paginator = Paginator(users, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'users': users}



    return render(request, 'task/blog_home.html', context)


def Blogcreate(request):
    if request.method == 'POST':


        Username = request.session['username']
        print(request.session['username'])
        bloggerobject = Blogger.objects.get(username=Username)

        blog.objects.create(title=request.POST['title'],description=request.POST['description'],blogger_name=bloggerobject)
        messages.success(request,'Your Blog is created!')

        return redirect('Bloghome')
    
    return render(request, 'task/blog_create.html')

def blogedit(request, pk):
    if request.method == 'POST':
        print(pk)
        blogobject = blog.objects.get(id=pk)

        print(request.POST)
        blogobject.title = request.POST['title']

        
        blogobject.description = request.POST['description']
        blogobject.save()
       
        messages.success(request,'Your blog is Updated Successfully!')
        return redirect('Bloghome')
   
    blogobject = blog.objects.all().filter(id=pk)


    return render(request, 'task/blog_edit.html', {'todo':blogobject})


def blogdelete(request, pk):
    print(pk)
    blogobject = blog.objects.get(id=pk)
    blogobject.delete()
    messages.success(request,'Your blog is deleted Successfully!')

    return redirect('Bloghome')



def Blogregister(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        Blogger.objects.create(username=Username,password=password)
        messages.info(request,'Account created!')
        return redirect('/Bloglogin/')
    else:
        return render(request, 'task/blog_register.html', {})




def Bloglogin(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
   
        if Blogger.objects.filter(username=Username, password=password).exists():
                user = Blogger.objects.get(username=Username, password=password)
                request.session['type_id'] = 'BlogUser'
                request.session['username'] = Username
                request.session['login'] = 'Yes'
                return redirect('/Bloglogin/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'task/blog_login.html', {})


def bloglogout(request):
    Session.objects.all().delete()
    return redirect('/Bloglogin/')