from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator

def create(request):

    context = {
    }

    return render(
        request,
        'contact/pages/create.html',
        context
    )