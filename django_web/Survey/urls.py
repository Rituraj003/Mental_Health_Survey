from django.urls import path
from . import views

urlpatterns=[
    path('',views.Indexview.as_view(),name='index_view'),
    path('survey/',views.Surveyview.as_view(),name="survey_view"),
    path('depression/',views.Depressionview.as_view(), name="depression_view")
]