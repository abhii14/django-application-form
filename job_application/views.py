from django.shortcuts import render
from .forms import ApplicationForm
from .models import From
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            From.objects.create(first_name=first_name,
                                last_name=last_name,
                                email=email, date=date,
                                occupation=occupation)
            message_body = f"{first_name} {last_name} \n" \
                           f"Your form has been submitted succesfully!\n" \
                           f"You will recieve an confirmation mail by this week.\n" \
                           f"for more enquiry feel free to contact."
            email_message = EmailMessage("Form Submission Confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, f"{first_name}, Your form was submitted succesfully!")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
