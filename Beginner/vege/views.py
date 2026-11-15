from django.shortcuts import render, redirect
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url='/login/')
# Create your views here.
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )

        return redirect('/recipes/')

    queryset =  Recipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}    

    return render(request, 'recipes.html', context)


@login_required(login_url='/login/')
def delete_recipe(request, recipe_id):

    queryset = Recipe.objects.get(id=recipe_id)
    queryset.delete()
    return redirect('/recipes/')    

@login_required(login_url='/login/')
def update_recipe(request, recipe_id):
    queryset = Recipe.objects.get(id=recipe_id)

    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')    

    context = {'recipe': queryset}

    return render(request, 'update_recipe.html', context)    

def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Username does not exist")
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Incorrect password")
            return redirect('/login/')

        else:
            # Creating a session for the user
            login(request, user)
            return redirect('/recipes/')        

    return render(request, 'login.html')    


def logout_page(request):
    logout(request)

    return redirect('/login/')

def register_page(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already exists")
            return redirect('/register/')

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username)

        user.set_password(password)
        user.save()
        messages.info(request, "User created successfully")

        return redirect('/login/')    

    return render(request, 'register.html')    


from django.db.models import Q

def get_students(request):

    students = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')

        students = students.filter(
            Q(student_name__icontains=search) |
            Q(student_email__icontains=search) |
            Q(department__department__icontains=search) |
            Q(student_id__student_id__icontains=search)
        )

    paginator = Paginator(students, 10)  # Show 10 students per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # print(page_obj.object_list) # This will print the list of students on the current page to the console.

    return render(request, 'report/students.html', {'students': page_obj})