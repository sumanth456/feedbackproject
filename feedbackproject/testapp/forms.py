from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(4)])
    EMP_ID=forms.IntegerField()
    Email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    Re_Enter_password=forms.CharField(label='password(Again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data=super().clean()
        inpwd=cleaned_data['password']
        inpwd_again=cleaned_data['Re_Enter_password']
        inp_Email=cleaned_data['Email']
        if inpwd != inpwd_again:
            raise forms.ValidationError('Password does not match in both field')
        if inp_Email[len(inp_Email)-12:] !='deloitte.com':
            raise forms.ValidationError('Deloitte Maild ID should be provided')
