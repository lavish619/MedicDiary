from django import forms
from django.contrib.auth.models import User                    #its a model that defines the parameters of a user
from django.contrib.auth.forms import UserCreationForm
from .models import PatientProfile,PatientVitals



class PatientRegisterForm(UserCreationForm):                         # the form created by us is in a form of a class
    email = forms.EmailField()
    # usertype = forms.IntegerField()

    class Meta:                                               # a meta class defines/builds upon the current class..
        model = User
        # widgets = {'usertype': forms.HiddenInput()}
        fields = ['username','email','password1','password2']
        # exclude = ['usertype']

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('name','age','address','phone','emergency_contact','profession','gender','profile_pic','Aadhar_Number')


class PatientVitalsForm(forms.ModelForm):
    class Meta:
        model = PatientVitals
        fields = ('Height_in_Centimeters','Weight_in_kilograms','Allergies','Smoker_or_not','Chronic_conditions')
























# =================================================================================================
# =================================================================================================
#

# from django.contrib.auth.forms import UserCreationForm
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
# # from .models import Profile
#
#
# class RegisterForm(UserCreationForm):                         # the form created by us is in a form of a class
#     email = forms.EmailField()
#
#     class Meta:                                               # a meta class defines/builds upon the current class..
#         model = User
#         fields = ['username','email','password1','password2']
#
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.helper = FormHelper()
#     #     self.helper.layout = Layout(
#     #     Div('username', 'email', 'password1', 'password2')
#     #         ButtonHolder(Submit('submit', 'Submit', css_class=''))
#     #     )
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name','last_name','age', 'address')
