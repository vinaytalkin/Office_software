import material
from django import forms
from material import Layout, Row, Fieldset

from center.models import Registration, UserImagesUpload


# class RegistrationForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField(label="Email Address")
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
#     first_name = forms.CharField(required=False)
#     last_name = forms.CharField(required=False)
#     gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')),required=False)
#     receive_news = forms.BooleanField(required=False, label='I want to receive news and special offers')
#     agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')
#
#     layout = Layout('username', 'email',
#                         Row('password', 'password_confirm'),
#                         Fieldset('Personal details',
#                                  Row('first_name', 'last_name'),
#                                  'gender',
#                                  'receive_news', 'agree_toc'))


class Registration_model(forms.Form):
    # photoimage = models.FileField(blank=True, null=True)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    sex = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')),required=False)
    email = forms.EmailField(max_length=250)
    fathername = forms.CharField(max_length=100)
    joiningdate = forms.DateField()
    dob = forms.DateField()
    spousename = forms.CharField(max_length=100)
    currentresidencyaddress = forms.CharField(max_length=100)
    czip_code = forms.CharField(max_length=20)
    cstate = forms.CharField(max_length=100)
    ccountry = forms.CharField(max_length=100)
    permanentaddress = forms.CharField(max_length=100)
    pzip_code = forms.CharField(max_length=20)
    pstate = forms.CharField(max_length=100)
    pcountry = forms.CharField(max_length=100)
    personalcontactno = forms.IntegerField()
    emergencycontactno = forms.IntegerField()
    highesteducation = forms.CharField(max_length=250)
    educationalinstitutename = forms.CharField(max_length=250)
    yearofpassing = forms.DateField()
    previousemployeename = forms.CharField(max_length=250)
    previousempoyeefrom = forms.DateField()
    previousempoyeeto = forms.DateField()
    # photoidproofimage = forms.FileField(blank=True, null=True)
    panno = forms.CharField(max_length=250)
    bankedtailsforsalary = forms.CharField(max_length=100)
    activeuser = forms.BooleanField()
    employeeinfo = forms.ChoiceField(choices=((None, ''), ('F', 'Full Time'), ('P', 'Part Time'), ('O', 'Other')),required=False)
    agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    layout = Layout('username', 'email',
                    Row('password', 'password_confirm'),
                    Fieldset('Personal details',
                             Row('firstname', 'lastname'),
                             Row('joiningdate', 'dob'),
                             Row('personalcontactno', 'emergencycontactno'),
                             Row('currentresidencyaddress', 'czip_code','cstate','ccountry'),
                             Row('permanentaddress', 'pzip_code', 'pstate', 'pcountry'),
                             Row('highesteducation', 'educationalinstitutename','yearofpassing'),
                             Row('previousemployeename', 'previousempoyeefrom','previousempoyeeto'),
                             'spousename',
                             'sex','panno','bankedtailsforsalary','bankedtailsforsalary',
                             'activeuser', 'agree_toc'))


# class Registration_model(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = Registration
#         fields = '__all__'


class UserImages_Form(forms.ModelForm):
    class Meta:
        model = UserImagesUpload
        fields = '__all__'
