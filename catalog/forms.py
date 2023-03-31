from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator

from catalog.models import Redactor, Newspaper


class RedactorCreateForm(UserCreationForm):
    MIN_YEARS_OF_EXPERIENCE = 0

    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(MIN_YEARS_OF_EXPERIENCE)])
    
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
         "first_name", "last_name", "years_of_experience"
        )


class NewspaperForm(forms.ModelForm):
    redactors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Newspaper
        fields = "__all__"
