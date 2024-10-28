from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from storapp.forms import CodeUploadForm
from storapp.models import CodeMemory

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration_page(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))

    context = {'form': form}
    return render(request, 'registration.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def upload_code(request):
    if request.method == 'POST':
        # create form instance and populate it with data from request (binding)
        form = CodeUploadForm(request.POST)

        if form.is_valid():
            codeMemory = CodeMemory()
            codeMemory.name = form.cleaned_data['name']
            codeMemory.code = form.cleaned_data['code']
            codeMemory.owner = request.user
            codeMemory.is_paid = False

            codeMemory.save()

            return HttpResponseRedirect(reverse('profile'))
    else:
        form = CodeUploadForm()

    context = {
        'form': form,
    }

    return render(request, 'storapp/upload_code.html', context)
