
from django.shortcuts import render
import pickle
from django.views import generic

# Create your views here.
model=pickle.load(open('ml_model.sav', 'rb'))
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
# list1=[]
# for i in range(17):
#     list1.append(random.randint(0,1))
# print(getPredictions(list1))
class Surveyview(generic.TemplateView):
    template_name="Survey.html"
    
def getPredictions(list1):
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

def result(request):
    answer1 = int(request.GET["Ques1"])
    answer2= int(request.GET["Ques2"])
    answer3 = int(request.GET["Ques3"])
    answer4 = int(request.GET["Ques4"])
    answer5 = int(request.GET["Ques5"])
    answer6 = int(request.GET["Ques6"])
    answer7 = int(request.GET["Ques7"])
    answer8 = int(request.GET["Ques8"])
    answer9 = int(request.GET["Ques9"])
    answer10= int(request.GET["Ques10"])
    answer11 = int(request.GET["Ques11"])
    answer12 = int(request.GET["Ques12"])
    answer13 = int(request.GET["Ques13"])
    answer14 = int(request.GET["Ques14"])
    answer15= int(request.GET["Ques15"])
    answer16 = int(request.GET["Ques16"])
    answer17 = int(request.GET["Ques17"])
    list1=[answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8,
            answer9,answer10,answer11,answer12,answer13,answer14,answer15,answer16,answer17]
    result= getPredictions(list1)
    return render(request, 'result.html', {'result': result})
    
class Depressionview(generic.TemplateView):
    template_name="depression.html"
