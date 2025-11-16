from django import forms
from .models import Feedback


class SubmitFeedback(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
