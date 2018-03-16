from django.shortcuts import render

# Create your views here.
# from rosario_form_app import form  # same as from . import forms
# Create your views here.

def index(request):
    # point = { 'message':'Ever Garcia' }
    # return render(request, 'index.html', context=point)
    return render(request, 'index.html')

def strong(request):
    point = { 'message':'STRONG INDEX' }
    return render(request, 'strong/index.html', context=point)

# def form_view(request):
#     formz = form.FormName()
#     if request.method == 'POST':
#         formz = form.FormName(request.POST)
#         if formz.is_valid():
#             print('Name: '+formz.cleaned_data['name'])
#             print('Email: '+formz.cleaned_data['email'])
#             print('Password: '+formz.cleaned_data['password'])
#             print('Text: '+formz.cleaned_data['text'])
            
#     return render(request,'rosario_form_app/form.html',{'form':formz})