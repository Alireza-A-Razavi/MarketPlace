from allauth.account.forms import SignupForm
from .models import ROLE_CHOICES
from django import forms

from .models import ProducerProfile, Profile

class CustomSignUpForm(SignupForm):
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=ROLE_CHOICES)

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.role = self.cleaned_data['role']
        user.save()
        return user

class ProducerProfileForm(forms.ModelForm):

    class Meta:
        model = ProducerProfile
        fields = (
            'gender',
            'profile_picture',
            'province',
            'city',
            'company_name',
            'phone_number',
            'company_address',
            'office_address',
            'office_phone_num',
            'introduce_yourself',
            'description',
            'web_site',
            'categoty',
            'department',
            'job_title',
            'postal_code',
            'alternative_phone',
            'fax_number',
            'business_type',
        )


class CustomerProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'gender',
            'profile_picture',
            'province',
            'city',
            'company_name',
            'phone_number',
            'company_address',
            'office_address',
            'office_phone_num',
            'introduce_yourself',
            'description',
            'web_site',
        )