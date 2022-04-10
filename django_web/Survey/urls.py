from django.urls import path
from . import views

urlpatterns=[
    # path('',views.indexview.as_view(),name='index_view'),
    path('Survey/',views.survey, name="survey_view"),
    path('Depression/',views.DepressionView.as_view(),name="depression_view"),
    path('', views.home, name='index_view'),
]