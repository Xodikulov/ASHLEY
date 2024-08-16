from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "email", "content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customizing the field widget (optional)
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        email = cleaned_data.get('email')
        content = cleaned_data.get('content')

        # Validate first name
        if first_name and len(first_name) < 3:
            self.add_error('first_name', 'First name must be at least 3 characters')

        # Validate email
        if email:
            try:
                forms.EmailField().clean(email)  # Use Django's built-in email validation
            except forms.ValidationError:
                self.add_error('email', 'Enter a valid email address')

        # Validate content
        if not content:
            self.add_error('content', 'Content is required')

        return cleaned_data
