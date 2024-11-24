from django.shortcuts import render

# Create your views here.
from .models import Projects, Category

def about(request):
    return render(request, 'blog/about.html')

def projects(request):
    projs_1 = Projects.objects.all()[:2]
    projs_2 = Projects.objects.all()[2:4]
    projs_3 = Projects.objects.all()[4:6]
    projs_4 = Projects.objects.all()[6:]
    categories = Category.objects.all()
    return render(request, 'blog/projects.html', {'projs_1' : projs_1, 'projs_2' : projs_2, 'projs_3' : projs_3, 'projs_4' : projs_4, 'categories' : categories})

def projects_by_id(request, cat):
    current_category = Category.objects.get(pk = cat)
    projects = Projects.objects.filter(category = cat)
    categories = Category.objects.all()
    return render(request, 'blog/projects_id.html', {'current_category' : current_category, 'projects' : projects, 'categories' : categories})

def main_page(request):
    return render(request, 'main_page.html')