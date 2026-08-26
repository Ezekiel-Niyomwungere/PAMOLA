from django import forms

from .models import ContactInquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = [
            "full_name",
            "email",
            "phone_number",
            "organization",
            "inquiry_type",
            "message",
        ]
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name",
                    "autocomplete": "name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "you@example.com",
                    "autocomplete": "email",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "placeholder": "+254 700 000 000",
                    "autocomplete": "tel",
                }
            ),
            "organization": forms.TextInput(
                attrs={
                    "placeholder": "Company or organization (optional)",
                    "autocomplete": "organization",
                }
            ),
            "inquiry_type": forms.Select(),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Tell us how we can help you…",
                    "rows": 5,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].required = True
        self.fields["email"].required = True
        self.fields["inquiry_type"].required = True
        self.fields["message"].required = True
        self.fields["phone_number"].required = False
        self.fields["organization"].required = False

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.setdefault("class", "form-control")
