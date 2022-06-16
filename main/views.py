from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm
#from .service import send
from .tasks import send_beat_email, send_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact.html'

    def form_valid(self, form):
        form.save()
        # send_mail(form.instance.email)
        print(form.instance.email, form.instance.body)

        send_email.delay(form.instance.email, form.instance.body)
        return super().form_valid(form)

