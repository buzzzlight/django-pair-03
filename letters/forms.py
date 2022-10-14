from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import CustomLetters
from django import forms


class CustomLettersForm(forms.ModelForm):
    class Meta:
        model = CustomLetters
        fields = ("to_email", "title", "content")

    def clean_to_email(self):
        to_email = self.cleaned_data["to_email"]
        if not len(get_user_model().objects.filter(email=self.cleaned_data["to_email"])):
            raise ValidationError("이메일이 유효하지 않습니다.")
        return to_email
