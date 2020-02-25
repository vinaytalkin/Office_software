from django import forms
from .models import basicmod,ContactForms
# class ContactForms(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField(label= 'Email required')
#     category = forms.ChoiceField(choices=[('question','Questionone'),('other','Other')])
#     subject = forms.CharField(required=False)
#     body = forms.CharField(widget=forms.Textarea)

class ContactForms(forms.ModelForm):
    class Meta:
        model = ContactForms
        fields = '__all__'

class basicModForm(forms.ModelForm):
    class Meta:
        model = basicmod
        fields = '__all__'
