from .forms import StudentForm
from .models import StudentModel
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    data = StudentModel.objects.all()
    return render(request, 'students/index.html', {'data':data})


@login_required
def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student record added successfully!')
            return redirect('index_student')
    form = StudentForm()
    return render(request, 'students/create.html', {'form':form})


@login_required
def show(request, pk):
    student = StudentModel.objects.get(id=pk)
    form = StudentForm(instance=student)
    return render(request, 'students/show.html', {'form':form, 'student':student})


@login_required
def edit(request, pk):
    student = StudentModel.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES ,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data updated successfully!')
            return redirect('index_student')
    form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {'form':form})


@login_required
def delete(request, pk):
    StudentModel.objects.get(id=pk).delete()
    messages.success(request, 'Data deleted successfully!')
    return redirect('index_student')
