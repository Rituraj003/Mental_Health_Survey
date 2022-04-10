from re import template
from django.views import generic
from django.shortcuts import render
import pickle

# Create your views here.

# class indexview(generic.DetailView):
#     template_name="index.html"
def home(request):
    return render(request, 'index.html')

def getPredictions(list1):
    model = pickle.load(open('ml_model.sav', 'rb'))

    prediction = model.predict(list1)
    
    if prediction == 1:
        return 'Lonely'
    elif prediction == 2:
        return 'Anxiety'
    elif prediction == 3:
        return 'Stress'
    elif prediction == 4:
        return 'Depression'
    else:
        return 'Normal'

# class SurveyView(generic.DetailView):
#     template_name="Survey.html"

def survey(request):
    return render(request,'survey.html')

class DepressionView(generic.TemplateView):
    template_name="depression.html"

