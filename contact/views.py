from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Contact
from contact.forms import ContactForm
from django.contrib import messages



def index(request):
    context_dict = {'aboutmessage': "Developed my MEBuilds."}

    return render(request, 'contact/index.html', context=context_dict)


def list(request):
    contact_list = Contact.objects.all
    context_dict = {'contacts' : contact_list}

    return render(request, 'contact/list.html', context=context_dict)

def add(request):
    contact_list = Contact.objects.all
    context_dict = {'contacts' : contact_list}
    form = ContactForm()

    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
        messages.success(request, 'Employee details added successfully')
        return render(request, 'contact/list.html', context=context_dict)

    return render(request, 'contact/add.html', {
        'form': form,
    })

