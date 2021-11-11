from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisiterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisiterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisiterForm()
    return render(request, 'users/register.html', {'form': form})
