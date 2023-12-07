from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm
from django.urls import reverse

from contact.models import Contact


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request,
            'contact/pages/create.html',
            context
        )


    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/pages/create.html',
        context
    )

def update(request, contact_id):
    contact = get_object_or_404(
        Contact, id=contact_id, show=True
    )
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request,
            'contact/pages/create.html',
            context
        )


    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/pages/create.html',
        context
    )

def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, id=contact_id, show=True
    )
    #contact.delete()
    #return redirect('contact:index')
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/pages/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )