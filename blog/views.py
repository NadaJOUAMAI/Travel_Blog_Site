from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm
def home_view(request):
    #return HttpResponse('Hello world!')
    return render(request,'home.html')

def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            titre = f'Blog | {nom} {prenom} {email}'
            
            # Set the sender email to the user's provided email address
            sender_email = email
            
            # Use the user's email as the sender
            send_mail(titre, message, sender_email, ['nonejerk1@gmail.com'])
            
            return HttpResponseRedirect(reverse('remerciements'))
    
    return render(request, 'contact.html', {"form": form})


def remerciements_view(request):
    return HttpResponse("Merci de nous avoir contacté")
