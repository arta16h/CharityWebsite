from django.shortcuts import render, redirect
from .forms import ContactUsForm
# Create your views here.

def home(request) :
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('home')
    form = ContactUsForm()
    context = {'form' : form}
    return render(request, "home.html", context)