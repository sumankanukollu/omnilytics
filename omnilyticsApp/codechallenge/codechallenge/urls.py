from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage , name='home_page'),
    path('generate/',views.generate,name='generate_logic'),
    path('download/', views.download_file,name='download_file'),
    path('report/',views.report,name='generateddata_analyze'),
]
