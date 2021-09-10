from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('structure/', views.structure, name='structure'), 
    path('dep1/', views.dep1, name='dep1'),
    path('dep1_1/', views.dep1_1, name='dep1_1'),
    path('dep2_1/', views.dep2_1, name='dep2_1'),
    path('dep3_1/', views.dep3_1, name='dep3_1'),
    path('dep4_1/', views.dep4_1, name='dep4_1'),
    path('dep5_1/', views.dep5_1, name='dep5_1'),
]
