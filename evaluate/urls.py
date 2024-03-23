from django.urls import path
from evaluate import evaluation
from evaluate import views

urlpatterns = [
    path('evaluate/', evaluation.evaluate_content),
    path('optimize/',evaluation.optimize_content),
    path('',views.evl_test)
]