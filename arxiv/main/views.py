from django.shortcuts import render,redirect
from .models import arxivdb
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surename = request.POST.get('surename')
        faculty = request.POST.get('faculty')
        group = request.POST.get('group')
        grade = request.POST.get('grade')

        arxivdb.objects.create(name=name,surename=surename,faculty=faculty,group=group,grade=grade)
        return redirect('home')
    allStudents = arxivdb.objects.all()
    return render(request,'main/home.html',{'students':allStudents})
