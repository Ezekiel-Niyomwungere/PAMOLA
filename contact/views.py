from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for reaching out to PAMOLA. We have received your message "
                "and will get back to you as soon as possible.",
            )
            return redirect("contact:contact")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
