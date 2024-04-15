from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', upload_document, name='upload_document'),
    path('documents/', document_list, name='document_list'),
    path('download-pdf/<int:document_id>/', download_pdf, name='download_pdf'),
    path('home',home,name='home')
]
