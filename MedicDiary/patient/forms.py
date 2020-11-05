from django import forms
from django.contrib.auth.models import User                    #its a model that defines the parameters of a user
from django.contrib.auth.forms import UserCreationForm
from .models import PatientProfile, PatientVitals



class PatientRegisterForm(UserCreationForm):                         # the form created by us is in a form of a class
    email = forms.EmailField(max_length=64)
    password1 = forms.CharField(help_text='Password must contain atleast 8 characters.<br>Password should not be similar to username.<br>Password should not be entirely numeric.<br>Should not be too common.')
    password2 = forms.CharField(help_text="Enter the same password as above, for verification.")

    class Meta:                                               # a meta class defines/builds upon the current class..
        model = User
        # widgets = {'usertype': forms.HiddenInput()}
        fields = ['username','email','password1','password2']
        # exclude = ['usertype']

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('name','age','gender','address','phone','emergency_contact','profession','profile_pic','Aadhar_Number')


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
