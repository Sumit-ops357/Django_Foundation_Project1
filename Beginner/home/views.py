from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    peoples = [
        {'name': 'Sumit', 'age': 22},
        {'name': 'Sneha', 'age': 21},
        {'name': 'Swateja', 'age': 20},
        {'name': 'Shashank', 'age': 19},
    ]

    vegetables = ['Tomato', 'Potato', 'Cabbage', 'Carrot']

    text = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Neque nihil sapiente voluptatibus possimus minus incidunt hic animi culpa, quo, dolorem labore ipsum. Doloribus reiciendis quo commodi soluta sit impedit eum."

    return render(request, 'home/index.html', context={'peoples': peoples, 'text': text, 'vegetables': vegetables})

def success_page(request):
    return HttpResponse("Welcome to the Success Page")    

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')        