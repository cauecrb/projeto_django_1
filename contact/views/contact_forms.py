from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/pages/create.html',
            context
        )


    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/pages/create.html',
        context
    )