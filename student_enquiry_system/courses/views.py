from .forms import *
from .models import CourseModel
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    data = CourseModel.objects.all()
    return render(request, 'courses/index.html', {'data':data})


@login_required
def create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data added successfully!')
            return redirect('index_course')
        return redirect('create_course')
    form = CourseForm()
    return render(request, 'courses/create.html', {'form':form})


@login_required
def edit(request, pk):
    course = CourseModel.objects.get(id=pk)
    if request.method == 'POST':
        data = CourseForm(data=request.POST, instance=course)
        if data.is_valid():
            data.save()
            messages.success(request, 'Data updated successfully!')
            return redirect('index_course')
        return redirect('index_course')
    return render(request, 'courses/edit.html', {'course':course})


@login_required
def delete(request, pk):
    CourseModel.objects.get(id=pk).delete()
    messages.success(request, 'Data deleted successfully!')
    return redirect('index_course')

