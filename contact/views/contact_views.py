from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'page_obj': page_object,
        'site_title': 'Contatos - ',
    }

    return render(
        request,
        'contact/pages/index.html',
        context
    )


def contact(request, contact_id):
    #single_contact = Contact.objects.get(pk=contact_id )

    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contact/pages/contact.html',
        context
    )


def search(request):
    #single_contact = Contact.objects.get(pk=contact_id )
    search_value = request.GET.get('q','').strip()

    if search_value == '':
        return redirect('contact:index')

    print(search_value)

    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            Q(first_name__contains=search_value) |
            Q(last_name__contains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__contains=search_value))\
        .order_by('-id')
    print(contacts.query)

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'page_obj': page_object,
        'site_title': 'Search - ',
    }
    print(context)

    return render(
        request,
        'contact/pages/index.html',
        context
    )