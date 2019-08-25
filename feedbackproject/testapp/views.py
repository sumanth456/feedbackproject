from django.shortcuts import render
from . import forms

# Create your views here.

def feedbackview(request):
    if request.method=='GET':
        form=forms.FeedbackForm()
        return render(request,'testapp/feedback.html',{'form':form})
    if request.method=='POST':
        form=forms.FeedbackForm(request.POST)
        if form.is_valid():
            print('Form Validation sucess and retriving Feedback')
            print('Student Name:',form.cleaned_data['name'])
            print('Student roll no:',form.cleaned_data['EMP_ID'])
            print('Student Email:',form.cleaned_data['Email'])
            print('Student feebdack:',form.cleaned_data['feedback'])
            return render(request,'testapp/thankyou.html',{'name':form.cleaned_data['name']})

    return render(request,'testapp/feedback.html',{'form':form})
