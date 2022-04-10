from django.contrib import admin
from django.urls import path
from .views import Indexview,Surveyview,Depressionview,result

urlpatterns=[
    path('',Indexview.as_view(),name='index_view'),
    path('survey/',Surveyview.as_view(),name="survey_view"),
    path('depression/',Depressionview.as_view(), name="depression_view"),
    path('survey/result/',result, name='result')
]