from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from contact.forms import ContactForm
from django.contrib import messages


def index(request):
    return render(request, 'contact/index.html')


def list(request):
    contact_list = Contact.objects.all
    context_dict = {'contacts': contact_list}

    return render(request, 'contact/list.html', context=context_dict)


def add(request):
    contact_list = Contact.objects.all
    context_dict = {'contacts' : contact_list}
    form = ContactForm()

    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee details added successfully')
            return render(request, 'contact/list.html', context=context_dict)
        else:
            messages.error(request, 'Oops Check form again')
            return render(request, 'contact/add.html', {'form': form})

    return render(request, 'contact/add.html', {
        'form': form,
    })


def delete(request, id):
    deleted_contact = Contact.objects.get(pk=id)
    name = deleted_contact.name
    Contact.objects.get(pk=id).delete()
    messages.success(request, name + "'s" + ' contact was deleted successfully')
    return list(request)

