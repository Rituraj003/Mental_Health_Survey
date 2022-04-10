from django.shortcuts import render
import pickle
from django.views import generic

# Create your views here.

class Indexview(generic.TemplateView):
    template_name="index.html"

def getPredictions(list1):
    model = pickle.load(open('../ml_model.sav', 'rb'))
    prediction =model.predict([list1])
    
    if prediction == 1:
        return 'Lonely'
    elif prediction==2:
        return "Anxiety"
    elif prediction==3:
        return "Stress"
    elif prediction==4:
        return "Depression"
    else:
        return 'Normal'

class Surveyview(generic.TemplateView):
    template_name="Survey.html"

class Depressionview(generic.TemplateView):
    template_name="depression.html"
