from django import forms
from CreateAccount.models import Resident, Organization
from .models import *


class RegistrationForm(forms.Form):
    user_type = forms.ChoiceField(
        choices=[("R", "Resident"), ("O", "Organization")],
        widget=forms.Select,
        initial="R",
    )


class ResidentRegistrationForm(forms.ModelForm):
    user_type = forms.CharField(widget=forms.HiddenInput(), initial='R')
    password = forms.CharField(widget=forms.PasswordInput)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Resident
        fields = ['username', 'password', 'user_type', 'first_name', 'last_name', 'birth_date', 'present_address']


class OrganizationRegistrationForm(forms.ModelForm):
    user_type = forms.CharField(widget=forms.HiddenInput(), initial='O')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Organization
        fields = ['username', 'password', 'user_type', 'organization_name']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class BorrowResourceForm(forms.ModelForm):
    borrow_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                  initial=timezone.now)
    return_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                  initial=timezone.now() + timezone.timedelta(days=7)
                                  )

    class Meta:
        model = BorrowResource
        fields = ['quantity', 'borrow_date', 'return_date']


