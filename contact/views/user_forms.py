from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário salvo com sucesso!')
            return redirect('contact:index')


    return render(
        request,
        'contact/pages/register.html',
        {
            'form': form
        }
    )

