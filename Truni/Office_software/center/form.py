from datetime import timezone

import material
from django import forms
from django.http import HttpResponseRedirect

from material import Layout, Row, Fieldset
from formtools.preview import FormPreview

from center.models import Registration, UserImagesUpload
from datetime import date

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

from django.forms.widgets import SelectDateWidget

class Registration_model(forms.ModelForm):
    # photoimage = models.FileField(blank=True, null=True)
    user_id = forms.CharField(max_length=100,required=False)
    password = forms.CharField(widget=forms.PasswordInput,required=False)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password",required=False)
    first_name = forms.CharField(max_length=100,required=False)
    last_name = forms.CharField(max_length=100,required=False)
    CHOICES_Gender = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'))
    gender = forms.ChoiceField(choices=CHOICES_Gender)
    email_id = forms.EmailField(max_length=250,required=False)
    father_name = forms.CharField(max_length=100,required=False)
    joining_date  = forms.DateField( required=False,initial=date.today(),disabled=True)
    dob = forms.DateField(required=False)
    spouse_name  = forms.CharField(max_length=100,required=False)
    current_residency_address  = forms.CharField(max_length=100,required=False)
    current_zip_code  = forms.CharField(max_length=20,required=False)
    current_state  = forms.CharField(max_length=100,required=False)
    current_country  = forms.CharField(max_length=100,required=False)
    permanent_address  = forms.CharField(max_length=100,required=False)
    permanent_zip_code  = forms.CharField(max_length=20,required=False)
    permanent_state  = forms.CharField(max_length=100,required=False)
    permanent_country  = forms.CharField(max_length=100,required=False)
    personal_contact_no  = forms.IntegerField(required=False)
    emergency_contact_no  = forms.IntegerField(required=False)
    highest_education  = forms.CharField(max_length=250,required=False)
    educational_institute_name  = forms.CharField(max_length=250,required=False)
    year_of_passing  = forms.DateField(required=False)
    previous_employee_name  = forms.CharField(max_length=250,required=False)
    previous_empoyee_from  = forms.DateField(required=False)
    previous_empoyee_to  = forms.DateField(required=False)
    # photoidproofimage = forms.FileField(blank=True, null=True)
    pan_no  = forms.CharField(max_length=250,required=False)
    bank_details_for_salary  = forms.Textarea()
    active_user  = forms.BooleanField(required=False)
    employee_info  = forms.ChoiceField(choices=(('F', 'Full Time'), ('P', 'Part Time'), ('O', 'Other')),required=False)
    agreeterms = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    layout = Layout(
                    Row('user_id', 'email_id',),
                    Row('password', 'password_confirm'),
                    Fieldset('Personal details',
                             Row('first_name', 'last_name'),
                             Row('father_name','spouse_name'),
                             Row('joining_date', 'dob'),
                             Row('personal_contact_no', 'emergency_contact_no'),
                             Row('current_residency_address', 'current_zip_code','current_state','current_country'),
                             Row('permanent_address', 'permanent_zip_code', 'permanent_state', 'permanent_country'),
                             Row('highest_education', 'educational_institute_name','year_of_passing'),
                             Row('previous_employee_name', 'previous_empoyee_from','previous_empoyee_to'),
                             Row('gender','employee_info'),
                             Row('pan_no','bank_details_for_salary'),
                             'active_user', 'agreeterms'))
    class Meta:
        model = Registration
        fields = '__all__'


class Registration_Preview(FormPreview):
    # photoimage = models.FileField(blank=True, null=True)
    user_id = forms.CharField(max_length=100,required=False,disabled=True)
    password = forms.CharField(widget=forms.PasswordInput,required=False,disabled=True)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password",required=False,disabled=True)
    first_name = forms.CharField(max_length=100,required=False,disabled=True)
    last_name = forms.CharField(max_length=100,required=False,disabled=True)
    CHOICES_Gender = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'))
    gender = forms.ChoiceField(choices=CHOICES_Gender,disabled=True)
    email_id = forms.EmailField(max_length=250,required=False,disabled=True)
    father_name = forms.CharField(max_length=100,required=False,disabled=True)
    joining_date  = forms.DateField( required=False,initial=date.today(),disabled=True,)
    dob = forms.DateField(required=False,disabled=True)
    spouse_name  = forms.CharField(max_length=100,required=False,disabled=True)
    current_residency_address  = forms.CharField(max_length=100,required=False,disabled=True)
    current_zip_code  = forms.CharField(max_length=20,required=False,disabled=True)
    current_state  = forms.CharField(max_length=100,required=False,disabled=True)
    current_country  = forms.CharField(max_length=100,required=False,disabled=True)
    permanent_address  = forms.CharField(max_length=100,required=False,disabled=True)
    permanent_zip_code  = forms.CharField(max_length=20,required=False,disabled=True)
    permanent_state  = forms.CharField(max_length=100,required=False,disabled=True)
    permanent_country  = forms.CharField(max_length=100,required=False,disabled=True)
    personal_contact_no  = forms.IntegerField(required=False,disabled=True)
    emergency_contact_no  = forms.IntegerField(required=False,disabled=True)
    highest_education  = forms.CharField(max_length=250,required=False,disabled=True)
    educational_institute_name  = forms.CharField(max_length=250,required=False,disabled=True)
    year_of_passing  = forms.DateField(required=False,disabled=True)
    previous_employee_name  = forms.CharField(max_length=250,required=False,disabled=True)
    previous_empoyee_from  = forms.DateField(required=False,disabled=True)
    previous_empoyee_to  = forms.DateField(required=False,disabled=True)
    # photoidproofimage = forms.FileField(blank=True, null=True)
    pan_no  = forms.CharField(max_length=250,required=False,disabled=True)
    bank_details_for_salary  = forms.Textarea()
    active_user  = forms.BooleanField(required=False,disabled=True)
    employee_info  = forms.ChoiceField(choices=(('F', 'Full Time'), ('P', 'Part Time'), ('O', 'Other')),required=False,disabled=True)
    agreeterms = forms.BooleanField(required=True, label='I agree with the Terms and Conditions',disabled=True)

    layout = Layout(
        Row('user_id', 'email_id',),
        Row('password', 'password_confirm'),
        Fieldset('Personal details',
                 Row('first_name', 'last_name'),
                 Row('father_name','spouse_name'),
                 Row('joining_date', 'dob'),
                 Row('personal_contact_no', 'emergency_contact_no'),
                 Row('current_residency_address', 'current_zip_code','current_state','current_country'),
                 Row('permanent_address', 'permanent_zip_code', 'permanent_state', 'permanent_country'),
                 Row('highest_education', 'educational_institute_name','year_of_passing'),
                 Row('previous_employee_name', 'previous_empoyee_from','previous_empoyee_to'),
                 Row('gender','employee_info'),
                 Row('pan_no','bank_details_for_salary'),
                 'active_user', 'agreeterms'))
    class Meta:
        model = Registration
        fields = '__all__'


import django_tables2 as tables
class MyGrid(tables.Table):
    class Meta:
        model = Registration
    # user_id = forms.CharField(max_length=100,required=False,disabled=True)
    # password = forms.CharField(widget=forms.PasswordInput,required=False,disabled=True)
    # password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password",required=False,disabled=True)
    # first_name = forms.CharField(max_length=100,required=False,disabled=True)
    # last_name = forms.CharField(max_length=100,required=False,disabled=True)
    # CHOICES_Gender = (
    #     ('F', 'Female'),
    #     ('M', 'Male'),
    #     ('O', 'Other'))
    # gender = forms.ChoiceField(choices=CHOICES_Gender,disabled=True)
    # email_id = forms.EmailField(max_length=250,required=False,disabled=True)
    # father_name = forms.CharField(max_length=100,required=False,disabled=True)
    # joining_date  = forms.DateField( required=False,initial=date.today(),disabled=True,)
    # dob = forms.DateField(required=False,disabled=True)
    # spouse_name  = forms.CharField(max_length=100,required=False,disabled=True)
    # current_residency_address  = forms.CharField(max_length=100,required=False,disabled=True)
    # current_zip_code  = forms.CharField(max_length=20,required=False,disabled=True)
    # current_state  = forms.CharField(max_length=100,required=False,disabled=True)
    # current_country  = forms.CharField(max_length=100,required=False,disabled=True)
    # permanent_address  = forms.CharField(max_length=100,required=False,disabled=True)
    # permanent_zip_code  = forms.CharField(max_length=20,required=False,disabled=True)
    # permanent_state  = forms.CharField(max_length=100,required=False,disabled=True)
    # permanent_country  = forms.CharField(max_length=100,required=False,disabled=True)
    # personal_contact_no  = forms.IntegerField(required=False,disabled=True)
    # emergency_contact_no  = forms.IntegerField(required=False,disabled=True)
    # highest_education  = forms.CharField(max_length=250,required=False,disabled=True)
    # educational_institute_name  = forms.CharField(max_length=250,required=False,disabled=True)
    # year_of_passing  = forms.DateField(required=False,disabled=True)
    # previous_employee_name  = forms.CharField(max_length=250,required=False,disabled=True)
    # previous_empoyee_from  = forms.DateField(required=False,disabled=True)
    # previous_empoyee_to  = forms.DateField(required=False,disabled=True)
    # # photoidproofimage = forms.FileField(blank=True, null=True)
    # pan_no  = forms.CharField(max_length=250,required=False,disabled=True)
    # bank_details_for_salary  = forms.Textarea()
    # active_user  = forms.BooleanField(required=False,disabled=True)
    # employee_info  = forms.ChoiceField(choices=(('F', 'Full Time'), ('P', 'Part Time'), ('O', 'Other')),required=False,disabled=True)
    # agreeterms = forms.BooleanField(required=True, label='I agree with the Terms and Conditions',disabled=True)



class UserImages_Form(forms.ModelForm):

    class Meta:
        model = UserImagesUpload
        fields = '__all__'









# class ChoiceFieldForm_preview(FormPreview):
#     description = "ChoiceField options"
#     CHOICES_Gender = (
#         ('F', 'Female'),
#         ('M', 'Male'),
#         ('O', 'Other'))
#     FLOAT_CHOICES = (
#         (1.1, 'Perfect'),
#         (1.0, 'Good'),
#         (0.8, 'Bad'),
#     )
#     GROUPED_CHOICES = (
#         (None, [(7, 'Mikhail')]),
#         ('Team 1', [(1, 'Joe'), (2, 'Bob'), (3, 'Marie')]),
#         ('Team 2', [(4, 'Anatoliy'), (5, 'Svetlana'), (6, 'Olga')]),
#     )
#     LONG_CHOICES = ((n, n) for n in range(100))
#     status_code =''
#     field1 = forms.ChoiceField(help_text='default', choices=CHOICES_Gender)
#     field2 = forms.ChoiceField(help_text='initial value', choices=CHOICES_Gender, initial=2)
#     field3 = forms.ChoiceField(help_text='float choices', choices=FLOAT_CHOICES)
#     field4 = forms.ChoiceField(help_text='groups', choices=GROUPED_CHOICES)
#     field5 = forms.ChoiceField(help_text='long choices list', choices=LONG_CHOICES)
#     field6 = forms.TypedChoiceField(help_text='cource to int', coerce=int, choices=CHOICES_Gender)
#     field7 = forms.ChoiceField(help_text='prefix', choices=CHOICES_Gender)
#     field8 = forms.ChoiceField(help_text='disabled', choices=CHOICES_Gender, initial=3, disabled=True, required=False)
#
