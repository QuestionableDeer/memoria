from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from storapp.forms import CodeUploadForm, ImageUploadForm
from storapp.models import CodeMemory, ImageMemory

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
            codeMemory.unlock_price = form.cleaned_data['unlock_price']
            codeMemory.is_paid = False

            codeMemory.save()

            return HttpResponseRedirect(reverse('profile'))
    else:
        form = CodeUploadForm()

    context = {
        'form': form,
    }

    return render(request, 'storapp/upload_code.html', context)

@login_required
def upload_image(request):
    if request.method == 'POST':
        # create form instance and populate it with data from request (binding)
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            imageMemory = ImageMemory()
            imageMemory.name = form.cleaned_data['name']
            imageMemory.img = form.cleaned_data['img']
            imageMemory.owner = request.user
            imageMemory.unlock_price = form.cleaned_data['unlock_price']
            imageMemory.is_paid = False

            imageMemory.save()

            return HttpResponseRedirect(reverse('profile'))
    else:
        form = ImageUploadForm()

    context = {
        'form': form,
    }

    return render(request, 'storapp/upload_image.html', context)

class CodeDetailView(LoginRequiredMixin, generic.DetailView):
    model = CodeMemory

class ImageDetailView(LoginRequiredMixin, generic.DetailView):
    model = ImageMemory
